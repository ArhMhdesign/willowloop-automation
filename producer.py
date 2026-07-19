"""
WillowLoop producer.py
Downloads a nature video clip from Pixabay/Pexels (min 2 min),
loops it to 30 minutes via FFmpeg concat+copy,
adds beautiful ambient background music from Pixabay (music only -- no natural audio),
and cuts a 59-second Short (also with music only).
"""
import os
import json
import math
import logging
import subprocess
import requests
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

PIXABAY_KEY = os.environ.get("PIXABAY_KEY", "")
PEXELS_KEY  = os.environ.get("PEXELS_KEY", "")
WORK_DIR    = "/tmp/willowloop"

LOOP_DURATION    = 1800   # 30 minutes
MIN_CLIP_SECONDS = 120    # require clips >= 2 min so loops are not boring
SHORT_DURATION   = 59     # YouTube Shorts limit

# --- Helpers ------------------------------------------------------------------

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
    return path

def get_duration(path):
    cmd = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", path]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(json.loads(result.stdout)["format"]["duration"])

def download_file(url, dest, label="file"):
    logger.info(f"Downloading {label} ...")
    headers = {}
    if "pexels.com" in url and PEXELS_KEY:
        headers["Authorization"] = PEXELS_KEY
    try:
        with requests.get(url, headers=headers, stream=True, timeout=180) as r:
            r.raise_for_status()
            size = 0
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size=2 * 1024 * 1024):
                    if chunk:
                        f.write(chunk)
                        size += len(chunk)
            logger.info(f"  -> {size / 1024 / 1024:.1f} MB saved to {dest}")
            return True
    except Exception as e:
        logger.warning(f"Download failed ({label}): {e}")
        if os.path.exists(dest):
            os.remove(dest)
        return False
# --- Video search --------------------------------------------------------------

def search_pixabay_video(queries, min_duration=MIN_CLIP_SECONDS, min_width=1280):
    results = []
    seen = set()
    for query in queries:
        try:
            r = requests.get(
                "https://pixabay.com/api/videos/",
                params={
                    "key": PIXABAY_KEY, "q": query,
                    "video_type": "film", "per_page": 20,
                    "safesearch": "true", "min_width": min_width,
                },
                timeout=30,
            )
            r.raise_for_status()
            for hit in r.json().get("hits", []):
                if hit["id"] in seen:
                    continue
                dur = hit.get("duration", 0)
                if dur < min_duration:
                    continue
                videos = hit.get("videos", {})
                url = width = None
                for q in ("large", "medium", "small"):
                    v = videos.get(q, {})
                    if v.get("url"):
                        url = v["url"]
                        width = v.get("width", 0)
                        break
                if not url:
                    continue
                results.append({"id": hit["id"], "url": url, "duration": dur,
                                 "width": width, "source": "pixabay"})
                seen.add(hit["id"])
        except Exception as e:
            logger.warning(f"Pixabay video search '{query}': {e}")
    results.sort(key=lambda x: x["duration"], reverse=True)
    return results

def search_pexels_video(queries, min_duration=MIN_CLIP_SECONDS):
    if not PEXELS_KEY:
        return []
    results = []
    seen = set()
    headers = {"Authorization": PEXELS_KEY}
    for query in queries:
        try:
            r = requests.get(
                "https://api.pexels.com/videos/search",
                headers=headers,
                params={"query": query, "per_page": 10, "min_duration": min_duration},
                timeout=30,
            )
            r.raise_for_status()
            for vid in r.json().get("videos", []):
                if vid["id"] in seen:
                    continue
                dur = vid.get("duration", 0)
                if dur < min_duration:
                    continue
                files = sorted(vid.get("video_files", []),
                               key=lambda f: f.get("width", 0), reverse=True)
                if not files:
                    continue
                f = files[0]
                results.append({"id": vid["id"], "url": f["link"], "duration": dur,
                                 "width": f.get("width", 0), "source": "pexels"})
                seen.add(vid["id"])
        except Exception as e:
            logger.warning(f"Pexels search '{query}': {e}")
    results.sort(key=lambda x: x["duration"], reverse=True)
    return results

# --- Music download (direct CDN URLs -- same mechanism as RoarRhythm) ---------

def download_music(url, dest):
    """Download music track from a direct Pixabay CDN URL. No API needed."""
    try:
        logger.info(f"Downloading music: ...{url[-35:]} ...")
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        with requests.get(url, stream=True, timeout=120, headers=headers) as r:
            r.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size=65536):
                    if chunk:
                        f.write(chunk)
        dur = get_duration(dest)
        if dur < 10:
            logger.warning(f"Music too short ({dur:.0f}s) -- skipping.")
            return False
        logger.info(f"Music downloaded OK: {dur:.0f}s")
        return True
    except Exception as e:
        logger.warning(f"Music download failed ({url[-30:]}): {e}")
        return False

# --- FFmpeg helpers ------------------------------------------------------------

def _run_ffmpeg(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg failed:\n{result.stderr[-800:]}")
    return result

def normalize_clip(src, dest):
    logger.info("Normalizing clip for clean looping ...")
    _run_ffmpeg([
        "ffmpeg", "-y", "-i", src,
        "-vf", "scale='min(1280,iw)':'min(720,ih)':force_original_aspect_ratio=decrease,pad=ceil(iw/2)*2:ceil(ih/2)*2",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "26",
        "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart",
        dest,
    ])
    logger.info(f"Normalized clip: {dest}")

def create_loop_video(clip_path, output_path, duration=LOOP_DURATION):
    clip_dur = get_duration(clip_path)
    n_reps = math.ceil(duration / clip_dur) + 3
    concat_file = clip_path + ".concat.txt"
    abs_clip = os.path.abspath(clip_path)
    with open(concat_file, "w") as f:
        for _ in range(n_reps):
            f.write(f"file '{abs_clip}'\n")
    logger.info(f"Looping {clip_dur:.0f}s clip x{n_reps} -> {duration // 60}min video ...")
    try:
        _run_ffmpeg([
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0", "-i", concat_file,
            "-t", str(duration),
            "-c:v", "copy", "-c:a", "copy",
            output_path,
        ])
    except RuntimeError:
        logger.warning("Copy-mode failed, re-encoding ...")
        _run_ffmpeg([
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0", "-i", concat_file,
            "-t", str(duration),
            "-c:v", "libx264", "-preset", "ultrafast", "-crf", "28",
            "-c:a", "aac", "-b:a", "128k",
            output_path,
        ])
    finally:
        if os.path.exists(concat_file):
            os.remove(concat_file)
    logger.info(f"Loop video ready: {output_path}")
def apply_music_only(video_path, music_path, output_path, music_vol=1.0):
    """
    Replace ALL audio with looping background music.
    Original video audio is completely discarded -- music only.
    """
    logger.info("Adding music-only audio track ...")
    try:
        _run_ffmpeg([
            "ffmpeg", "-y",
            "-i", video_path,
            "-stream_loop", "-1", "-i", music_path,
            "-t", str(LOOP_DURATION),
            "-filter_complex", f"[1:a]volume={music_vol}[mus]",
            "-map", "0:v",
            "-map", "[mus]",
            "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k",
            output_path,
        ])
        logger.info(f"Music applied successfully: {output_path}")
        return True
    except RuntimeError as e:
        logger.warning(f"Music application failed: {e}")
        return False

def add_silent_audio(video_path, output_path):
    """Fallback: strip original audio and add silence (no natural sounds)."""
    logger.info("Adding silent audio track (no natural audio) ...")
    _run_ffmpeg([
        "ffmpeg", "-y",
        "-i", video_path,
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-t", str(LOOP_DURATION),
        "-map", "0:v",
        "-map", "1:a",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "128k",
        output_path,
    ])
    logger.info(f"Silent audio applied: {output_path}")

def create_short(main_video_path, output_path, duration=SHORT_DURATION):
    """Cut first duration seconds and crop to 9:16 for YouTube Shorts."""
    logger.info(f"Creating {duration}s Short ...")
    try:
        _run_ffmpeg([
            "ffmpeg", "-y",
            "-i", main_video_path,
            "-t", str(duration),
            "-vf", "crop=ih*9/16:ih,scale=1080:1920",
            "-c:v", "libx264", "-preset", "fast", "-crf", "23",
            "-c:a", "aac", "-b:a", "128k",
            output_path,
        ])
    except RuntimeError:
        logger.warning("Vertical crop failed; plain cut fallback.")
        _run_ffmpeg([
            "ffmpeg", "-y",
            "-i", main_video_path,
            "-t", str(duration),
            "-c:v", "copy", "-c:a", "copy",
            output_path,
        ])
    logger.info(f"Short ready: {output_path}")

# --- Main produce function -----------------------------------------------------

def produce(topic):
    """
    Download a long clip (>=2 min), normalize, loop to 30min,
    replace audio with ambient music only (no natural sounds), cut a 59s Short.
    Returns (main_video_path, short_path, metadata_dict).
    """
    ensure_dir(WORK_DIR)
    slug  = topic["slug"]
    today = datetime.now(timezone.utc).strftime("%Y%m%d")

    # 1. Find video clips (prefer long clips >= 2 min, fallback to >= 30s)
    logger.info(f"[{topic['name']}] Searching Pixabay for video ...")
    clips = search_pixabay_video(topic["video_queries"])
    if not clips:
        logger.info("No long clips found; retrying with min 30s ...")
        clips = search_pixabay_video(topic["video_queries"], min_duration=30)
    if not clips:
        logger.info("Pixabay empty -> trying Pexels ...")
        clips = search_pexels_video(topic["video_queries"])
    if not clips:
        clips = search_pexels_video(topic["video_queries"], min_duration=30)
    if not clips:
        raise RuntimeError(f"No video clips found for topic: {topic['name']}")

    # 2. Download best clip (try up to 3)
    raw_clip = os.path.join(WORK_DIR, f"{slug}_raw_{today}.mp4")
    downloaded = False
    for clip_info in clips[:3]:
        logger.info(f"Trying clip {clip_info['id']} ({clip_info['duration']}s, {clip_info['source']}) ...")
        if download_file(clip_info["url"], raw_clip, f"{topic['name']} clip"):
            downloaded = True
            break
    if not downloaded:
        raise RuntimeError("Could not download any video clip.")

    # 3. Normalize clip
    norm_clip = os.path.join(WORK_DIR, f"{slug}_norm_{today}.mp4")
    normalize_clip(raw_clip, norm_clip)
    os.remove(raw_clip)

    # 4. Create 30-min loop
    loop_path = os.path.join(WORK_DIR, f"{slug}_loop_{today}.mp4")
    create_loop_video(norm_clip, loop_path, LOOP_DURATION)
    os.remove(norm_clip)

    # 5. Replace audio with background music only (no natural sounds)
    main_path  = os.path.join(WORK_DIR, f"{slug}_main_{today}.mp4")
    music_path = os.path.join(WORK_DIR, f"{slug}_music_{today}.mp3")
    music_added = False

    # Use direct CDN URLs -- same mechanism as RoarRhythm (Pixabay API has no music support)
    from topics import MUSIC_FALLBACK_URLS
    primary_url = topic.get("music_url")
    music_urls  = ([primary_url] if primary_url else []) + MUSIC_FALLBACK_URLS

    for music_url in music_urls:
        if download_music(music_url, music_path):
            if apply_music_only(loop_path, music_path, main_path):
                music_added = True
                break
        # Clean up failed partial download
        if os.path.exists(music_path):
            try:
                os.remove(music_path)
            except OSError:
                pass

    # Clean up music file if still around
    if os.path.exists(music_path):
        try:
            os.remove(music_path)
        except OSError:
            pass

    if not music_added:
        # All CDN URLs failed -- strip natural audio and add silence
        logger.warning("All music URLs failed -- adding silent audio track.")
        add_silent_audio(loop_path, main_path)

    if os.path.exists(loop_path):
        os.remove(loop_path)

    # 6. Create Short from final video (includes music)
    short_path = os.path.join(WORK_DIR, f"{slug}_short_{today}.mp4")
    create_short(main_path, short_path, duration=SHORT_DURATION)

    # 7. Build metadata
    metadata = {
        "main": {
            "title":       topic["title"],
            "description": topic["description"],
            "tags":        topic["tags"],
            "category_id": topic["category_id"],
            "privacy":     "public",
        },
        "short": {
            "title":       topic["short_title"],
            "description": topic["short_description"],
            "tags":        topic["tags"],
            "category_id": topic["category_id"],
            "privacy":     "public",
        },
    }
    return main_path, short_path, metadata
