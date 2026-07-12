# WillowLoop – Nature ambient loop topics
# Each topic produces one 30-min loop video + one 59s Short per day
# Topic is selected by: day_of_year % len(TOPICS)

TOPICS = [
    {
        "id": 0,
        "name": "Cozy Fireplace",
        "slug": "fireplace",
        "emoji": "\U0001f525",
        "video_queries": ["fireplace burning fire", "fireplace crackling logs", "cozy fireplace"],
        "music_url": "https://cdn.pixabay.com/audio/2026/03/28/audio_4acb1675b5.mp3",
        "music_queries": ["relaxing piano ambient", "cozy instrumental music", "soft jazz piano"],
        "duration": 1800,
        "title": "\U0001f525 Cozy Fireplace – 30 Minutes of Crackling Fire | Relaxing Ambience for Sleep & Study",
        "short_title": "\U0001f525 Crackling Fireplace – Pure Relaxation #shorts #fireplace",
        "description": (
            "\U0001f525 Let the warmth of a cozy fireplace fill your space.\n\n"
            "30 minutes of uninterrupted crackling fire with soothing background music — "
            "perfect for sleep, study, meditation, or relaxing after a long day.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#fireplace #fireplaceambience #relaxingsounds #sleepsounds #cozysounds"
        ),
        "short_description": "\U0001f525 Cozy fireplace bliss. Subscribe for daily ambience! \U0001f33f #fireplace #relaxing",
        "tags": [
            "fireplace", "fireplace sounds", "crackling fire", "fire sounds", "cozy fire",
            "sleep sounds", "relaxing sounds", "ambient sounds", "study sounds", "white noise",
            "fireplace ambience", "cozy ambience", "ASMR fire", "relaxing fire", "nature sounds"
        ],
        "category_id": "22",
    },
    {
        "id": 1,
        "name": "Rain Forest",
        "slug": "rain_forest",
        "emoji": "\U0001f327️",
        "video_queries": ["rain forest tropical", "jungle rain", "rainforest rainfall"],
        "music_url": "https://cdn.pixabay.com/audio/2026/05/05/audio_bedae80d67.mp3",
        "music_queries": ["rain ambient music relaxing", "forest meditation piano", "peaceful rain instrumental"],
        "duration": 1800,
        "title": "\U0001f327️ Rain in the Forest – 30 Minutes of Soothing Rainfall | Sleep & Relaxation",
        "short_title": "\U0001f327️ Rain Forest Sounds – Pure Relaxation #shorts #rainsounds",
        "description": (
            "\U0001f327️ Escape to a lush rainforest with gentle rainfall.\n\n"
            "30 minutes of soothing forest rain sounds with soft ambient music — "
            "perfect for deep sleep, stress relief, focus, or meditation.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#rainsounds #forestrain #relaxingsounds #sleepsounds #naturalsounds"
        ),
        "short_description": "\U0001f327️ Rainforest sounds. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "rain sounds", "forest rain", "rainforest", "rain for sleeping", "rain ambience",
            "sleep sounds", "relaxing rain", "nature sounds", "rainfall sounds", "rainy day",
            "study sounds", "white noise rain", "ASMR rain", "tropical rain", "jungle sounds"
        ],
        "category_id": "22",
    },
    {
        "id": 2,
        "name": "Ocean Waves",
        "slug": "ocean_waves",
        "emoji": "\U0001f30a",
        "video_queries": ["ocean waves beach", "sea waves relaxing", "waves crashing shore"],
        "music_url": "https://cdn.pixabay.com/audio/2026/06/09/audio_4968a13b9d.mp3",
        "music_queries": ["ocean ambient music", "beach meditation music", "sea waves instrumental"],
        "duration": 1800,
        "title": "\U0001f30a Ocean Waves – 30 Minutes of Gentle Sea Sounds | Sleep, Study & Relaxation",
        "short_title": "\U0001f30a Ocean Waves – Pure Relaxation #shorts #oceansounds",
        "description": (
            "\U0001f30a Drift away with the gentle sound of ocean waves.\n\n"
            "30 minutes of peaceful ocean waves with soft ambient music — "
            "ideal for sleep, meditation, focus, or unwinding by the sea.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#oceansounds #wavesounds #relaxingsounds #sleepsounds #beachsounds"
        ),
        "short_description": "\U0001f30a Calming ocean waves. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "ocean sounds", "wave sounds", "beach sounds", "sea sounds", "ocean waves",
            "sleep sounds", "relaxing sounds", "nature sounds", "meditation sounds", "white noise",
            "ocean ambience", "coastal sounds", "ASMR ocean", "calming waves", "beach ambience"
        ],
        "category_id": "22",
    },
    {
        "id": 3,
        "name": "Waterfall",
        "slug": "waterfall",
        "emoji": "\U0001f4a7",
        "video_queries": ["waterfall nature", "forest waterfall", "cascading waterfall"],
        "music_url": "https://cdn.pixabay.com/audio/2023/01/29/audio_580d2c877d.mp3",
        "music_queries": ["waterfall ambient music", "nature meditation piano", "flowing water instrumental"],
        "duration": 1800,
        "title": "\U0001f4a7 Waterfall Sounds – 30 Minutes of Flowing Water | Relaxation & Focus",
        "short_title": "\U0001f4a7 Waterfall Sounds – Pure Relaxation #shorts #waterfall",
        "description": (
            "\U0001f4a7 Find tranquility beside a beautiful flowing waterfall.\n\n"
            "30 minutes of serene waterfall sounds with gentle ambient music — "
            "perfect for meditation, deep focus, stress relief, or restful sleep.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#waterfallsounds #flowingwater #relaxingsounds #sleepsounds #naturalsounds"
        ),
        "short_description": "\U0001f4a7 Serene waterfall sounds. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "waterfall sounds", "flowing water", "nature sounds", "water sounds", "waterfall",
            "sleep sounds", "relaxing sounds", "meditation sounds", "white noise", "study sounds",
            "waterfall ambience", "forest waterfall", "ASMR water", "calming water", "stream sounds"
        ],
        "category_id": "22",
    },
    {
        "id": 4,
        "name": "Thunderstorm",
        "slug": "thunderstorm",
        "emoji": "⚡",
        "video_queries": ["thunderstorm rain window", "storm rain nature", "lightning storm"],
        "music_url": "https://cdn.pixabay.com/audio/2026/02/10/audio_f3639f946e.mp3",
        "music_queries": ["thunderstorm ambient music", "rain storm instrumental", "stormy night piano"],
        "duration": 1800,
        "title": "⚡ Thunderstorm – 30 Minutes of Rain & Thunder | Sleep, Study & Relaxation",
        "short_title": "⚡ Thunderstorm Sounds – Pure Relaxation #shorts #thunderstorm",
        "description": (
            "⚡ Experience the raw beauty of a calming thunderstorm.\n\n"
            "30 minutes of rain and rolling thunder with soft ambient music — "
            "perfect for deep sleep, white noise focus, stress relief, or cozy evenings.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#thunderstorm #stormsounds #relaxingsounds #sleepsounds #rainsounds"
        ),
        "short_description": "⚡ Dramatic thunderstorm. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "thunderstorm sounds", "storm sounds", "rain and thunder", "thunder sounds", "storm ambience",
            "sleep sounds", "relaxing sounds", "nature sounds", "white noise", "study sounds",
            "thunderstorm ambience", "rainstorm", "ASMR storm", "cozy storm", "lightning sounds"
        ],
        "category_id": "22",
    },
    {
        "id": 5,
        "name": "Snowy Forest",
        "slug": "snowy_forest",
        "emoji": "❄️",
        "video_queries": ["snowy forest winter", "snow falling trees", "winter forest snow"],
        "music_url": "https://cdn.pixabay.com/audio/2026/06/18/audio_f639ce6f4d.mp3",
        "music_queries": ["winter ambient music", "snowy piano relaxing", "cold forest instrumental"],
        "duration": 1800,
        "title": "❄️ Snowy Forest – 30 Minutes of Winter Ambience | Sleep & Relaxation",
        "short_title": "❄️ Snowy Forest – Pure Relaxation #shorts #snowyforest",
        "description": (
            "❄️ Step into a peaceful snow-covered forest.\n\n"
            "30 minutes of gentle winter ambience with soft ambient music — "
            "perfect for relaxation, meditation, cozy evenings, or restful sleep.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#snowyforest #wintersounds #relaxingsounds #sleepsounds #cozysounds"
        ),
        "short_description": "❄️ Peaceful snowy forest. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "snowy forest", "winter sounds", "snow sounds", "winter ambience", "forest sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "cozy sounds", "white noise",
            "winter forest", "snow ambience", "ASMR snow", "calming winter", "cold forest"
        ],
        "category_id": "22",
    },
    {
        "id": 6,
        "name": "Mountain Stream",
        "slug": "mountain_stream",
        "emoji": "\U0001f3d4️",
        "video_queries": ["mountain stream flowing", "creek mountain nature", "alpine stream water"],
        "music_url": "https://cdn.pixabay.com/audio/2026/03/28/audio_4903e5bcab.mp3",
        "music_queries": ["mountain ambient music", "stream meditation piano", "alpine nature instrumental"],
        "duration": 1800,
        "title": "\U0001f3d4️ Mountain Stream – 30 Minutes of Flowing Creek | Relaxation & Focus",
        "short_title": "\U0001f3d4️ Mountain Stream – Pure Relaxation #shorts #mountainstream",
        "description": (
            "\U0001f3d4️ Relax beside a crystal-clear mountain stream.\n\n"
            "30 minutes of flowing creek sounds with soft ambient music — "
            "ideal for focus, meditation, stress relief, or peaceful sleep.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#mountainstream #creeksounds #relaxingsounds #sleepsounds #naturalsounds"
        ),
        "short_description": "\U0001f3d4️ Calming mountain stream. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "mountain stream", "creek sounds", "stream sounds", "flowing water", "mountain sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "meditation sounds", "white noise",
            "stream ambience", "alpine sounds", "ASMR stream", "river sounds", "nature relaxation"
        ],
        "category_id": "22",
    },
    {
        "id": 7,
        "name": "Night Forest",
        "slug": "night_forest",
        "emoji": "\U0001f319",
        "video_queries": ["night forest crickets", "forest night stars", "dark forest night"],
        "music_url": "https://cdn.pixabay.com/audio/2026/06/27/audio_6430e27d08.mp3",
        "music_queries": ["night ambient music", "forest night piano", "nocturnal nature instrumental"],
        "duration": 1800,
        "title": "\U0001f319 Night Forest – 30 Minutes of Crickets & Night Sounds | Sleep & Relaxation",
        "short_title": "\U0001f319 Night Forest – Pure Relaxation #shorts #nightforest",
        "description": (
            "\U0001f319 Experience the peaceful magic of a forest at night.\n\n"
            "30 minutes of crickets and gentle night sounds with soft ambient music — "
            "perfect for deep sleep, meditation, or unwinding under the stars.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#nightforest #cricketsounds #relaxingsounds #sleepsounds #nightsounds"
        ),
        "short_description": "\U0001f319 Magical night forest. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "night forest", "cricket sounds", "night sounds", "forest night", "nocturnal sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "meditation sounds", "white noise",
            "night ambience", "forest ambience", "ASMR night", "calming night", "starry night"
        ],
        "category_id": "22",
    },
    {
        "id": 8,
        "name": "Tropical Beach",
        "slug": "tropical_beach",
        "emoji": "\U0001f3d6️",
        "video_queries": ["tropical beach paradise", "tropical ocean waves", "palm beach waves"],
        "music_url": "https://cdn.pixabay.com/audio/2026/02/18/audio_53434c9bdd.mp3",
        "music_queries": ["tropical ambient music", "beach relaxation piano", "island instrumental music"],
        "duration": 1800,
        "title": "\U0001f3d6️ Tropical Beach – 30 Minutes of Paradise Sounds | Relaxation & Sleep",
        "short_title": "\U0001f3d6️ Tropical Beach – Pure Relaxation #shorts #tropicalbeach",
        "description": (
            "\U0001f3d6️ Escape to a stunning tropical paradise.\n\n"
            "30 minutes of warm beach waves and tropical ambience with soft music — "
            "perfect for relaxation, visualization, stress relief, or restful sleep.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#tropicalbeach #beachsounds #relaxingsounds #sleepsounds #paradisesounds"
        ),
        "short_description": "\U0001f3d6️ Tropical beach paradise. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "tropical beach", "beach sounds", "ocean waves", "paradise sounds", "tropical sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "meditation sounds", "island sounds",
            "beach ambience", "tropical ambience", "ASMR beach", "calming waves", "vacation sounds"
        ],
        "category_id": "22",
    },
    {
        "id": 9,
        "name": "Bamboo Forest",
        "slug": "bamboo_forest",
        "emoji": "\U0001f38d",
        "video_queries": ["bamboo forest wind", "bamboo grove nature", "bamboo swaying"],
        "music_url": "https://cdn.pixabay.com/audio/2026/06/19/audio_f144de729b.mp3",
        "music_queries": ["zen bamboo music", "japanese meditation music", "bamboo flute ambient"],
        "duration": 1800,
        "title": "\U0001f38d Bamboo Forest – 30 Minutes of Zen Nature Sounds | Meditation & Relaxation",
        "short_title": "\U0001f38d Bamboo Forest – Pure Relaxation #shorts #bambooforest",
        "description": (
            "\U0001f38d Find your inner peace in a serene bamboo forest.\n\n"
            "30 minutes of gentle bamboo and wind sounds with zen ambient music — "
            "perfect for meditation, yoga, study focus, or peaceful sleep.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#bambooforest #zensounds #relaxingsounds #sleepsounds #meditationsounds"
        ),
        "short_description": "\U0001f38d Peaceful bamboo forest. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "bamboo forest", "zen sounds", "bamboo sounds", "asian nature sounds", "wind sounds",
            "sleep sounds", "relaxing sounds", "meditation sounds", "nature sounds", "white noise",
            "bamboo ambience", "zen ambience", "ASMR bamboo", "japanese nature", "calming forest"
        ],
        "category_id": "22",
    },
    {
        "id": 10,
        "name": "Desert Wind",
        "slug": "desert_wind",
        "emoji": "\U0001f3dc️",
        "video_queries": ["desert landscape wind", "sand dunes desert", "desert sunset"],
        "music_url": "https://cdn.pixabay.com/audio/2026/04/21/audio_076e2f430b.mp3",
        "music_queries": ["desert ambient music", "desert meditation music", "vast landscape instrumental"],
        "duration": 1800,
        "title": "\U0001f3dc️ Desert Wind – 30 Minutes of Vast Desert Ambience | Relaxation & Focus",
        "short_title": "\U0001f3dc️ Desert Wind – Pure Relaxation #shorts #desertwind",
        "description": (
            "\U0001f3dc️ Lose yourself in the vast beauty of the desert.\n\n"
            "30 minutes of gentle desert wind and dune ambience with soft music — "
            "ideal for meditation, visualization, creative focus, or relaxation.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#desertsounds #windambience #relaxingsounds #sleepsounds #naturalsounds"
        ),
        "short_description": "\U0001f3dc️ Vast desert ambience. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "desert sounds", "wind sounds", "desert ambience", "sand dunes", "desert wind",
            "sleep sounds", "relaxing sounds", "nature sounds", "meditation sounds", "white noise",
            "desert landscape", "vast sounds", "ASMR desert", "arid sounds", "calm wind"
        ],
        "category_id": "22",
    },
    {
        "id": 11,
        "name": "Lakeside Sunrise",
        "slug": "lakeside_sunrise",
        "emoji": "\U0001f305",
        "video_queries": ["lakeside sunrise morning", "lake morning mist", "sunrise lake nature"],
        "music_url": "https://cdn.pixabay.com/audio/2025/11/05/audio_8eea27848e.mp3",
        "music_queries": ["sunrise ambient music", "morning meditation piano", "peaceful dawn instrumental"],
        "duration": 1800,
        "title": "\U0001f305 Lakeside Sunrise – 30 Minutes of Peaceful Morning | Sleep & Meditation",
        "short_title": "\U0001f305 Lakeside Sunrise – Pure Relaxation #shorts #lakesidesunrise",
        "description": (
            "\U0001f305 Welcome a new day with a tranquil lakeside sunrise.\n\n"
            "30 minutes of peaceful morning lake sounds with gentle ambient music — "
            "perfect for morning meditation, gentle waking, study, or restful sleep.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#lakesunrise #morningsounds #relaxingsounds #sleepsounds #naturalsounds"
        ),
        "short_description": "\U0001f305 Beautiful lakeside sunrise. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "lakeside sunrise", "morning sounds", "lake sounds", "sunrise sounds", "dawn sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "meditation sounds", "bird sounds",
            "lake ambience", "sunrise ambience", "ASMR lake", "peaceful morning", "calm lake"
        ],
        "category_id": "22",
    },
    {
        "id": 12,
        "name": "Arctic Snowstorm",
        "slug": "arctic_snowstorm",
        "emoji": "\U0001f9ca",
        "video_queries": ["arctic blizzard snowstorm", "snow blizzard wind", "winter storm snow"],
        "music_url": "https://cdn.pixabay.com/audio/2026/03/29/audio_72a9ff54fb.mp3",
        "music_queries": ["arctic ambient music", "blizzard instrumental music", "cold winter piano"],
        "duration": 1800,
        "title": "\U0001f9ca Arctic Snowstorm – 30 Minutes of Blizzard White Noise | Sleep & Focus",
        "short_title": "\U0001f9ca Arctic Snowstorm – Pure Relaxation #shorts #arcticstorm",
        "description": (
            "\U0001f9ca Cozy up with the dramatic sounds of an arctic snowstorm.\n\n"
            "30 minutes of powerful blizzard wind and snow with atmospheric music — "
            "perfect for deep sleep, white noise focus, or dramatic background ambience.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#arcticstorm #blizzardsounds #relaxingsounds #sleepsounds #winternoise"
        ),
        "short_description": "\U0001f9ca Dramatic arctic blizzard. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "arctic storm", "blizzard sounds", "snowstorm sounds", "winter storm", "wind sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "white noise", "study sounds",
            "arctic ambience", "storm ambience", "ASMR blizzard", "powerful wind", "cold sounds"
        ],
        "category_id": "22",
    },
    {
        "id": 13,
        "name": "River Rapids",
        "slug": "river_rapids",
        "emoji": "\U0001f30a",
        "video_queries": ["river rapids rushing water", "fast river water", "whitewater rapids"],
        "music_url": "https://cdn.pixabay.com/audio/2026/03/31/audio_31e6dddbb2.mp3",
        "music_queries": ["river ambient music", "rushing water instrumental", "energetic nature music"],
        "duration": 1800,
        "title": "\U0001f30a River Rapids – 30 Minutes of Rushing Water | Energy, Focus & Relaxation",
        "short_title": "\U0001f30a River Rapids – Pure Relaxation #shorts #riverrapids",
        "description": (
            "\U0001f30a Feel the invigorating energy of rushing river rapids.\n\n"
            "30 minutes of powerful flowing water sounds with ambient music — "
            "ideal for energizing focus, blocking distractions, or refreshing the mind.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#riverrapids #rushingwater #relaxingsounds #focussounds #naturalsounds"
        ),
        "short_description": "\U0001f30a Energizing river rapids. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "river rapids", "rushing water", "river sounds", "water sounds", "whitewater",
            "focus sounds", "relaxing sounds", "nature sounds", "energy sounds", "white noise",
            "river ambience", "water ambience", "ASMR river", "flowing water", "powerful water"
        ],
        "category_id": "22",
    },
    {
        "id": 14,
        "name": "Autumn Leaves",
        "slug": "autumn_leaves",
        "emoji": "\U0001f342",
        "video_queries": ["autumn leaves falling", "fall foliage forest", "autumn forest wind"],
        "music_url": "https://cdn.pixabay.com/audio/2026/07/06/audio_2ff9ba1a1d.mp3",
        "music_queries": ["autumn ambient music", "fall piano relaxing", "harvest season instrumental"],
        "duration": 1800,
        "title": "\U0001f342 Autumn Leaves – 30 Minutes of Fall Forest Ambience | Relaxation & Study",
        "short_title": "\U0001f342 Autumn Leaves – Pure Relaxation #shorts #autumnleaves",
        "description": (
            "\U0001f342 Immerse yourself in the golden beauty of autumn.\n\n"
            "30 minutes of rustling leaves and crisp fall sounds with ambient music — "
            "perfect for cozy studying, relaxation, or peaceful sleep on a cool autumn day.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#autumnleaves #fallsounds #relaxingsounds #sleepsounds #cozyfall"
        ),
        "short_description": "\U0001f342 Beautiful autumn forest. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "autumn leaves", "fall sounds", "autumn forest", "leaves rustling", "fall ambience",
            "sleep sounds", "relaxing sounds", "nature sounds", "cozy sounds", "study sounds",
            "autumn ambience", "seasonal sounds", "ASMR leaves", "fall foliage", "harvest sounds"
        ],
        "category_id": "22",
    },
    {
        "id": 15,
        "name": "Jungle Rain",
        "slug": "jungle_rain",
        "emoji": "\U0001f98a",
        "video_queries": ["jungle rain tropical", "rainforest heavy rain", "tropical jungle downpour"],
        "music_url": "https://cdn.pixabay.com/audio/2026/04/24/audio_fdf2509563.mp3",
        "music_queries": ["jungle ambient music", "tropical rain piano", "exotic nature instrumental"],
        "duration": 1800,
        "title": "\U0001f98a Jungle Rain – 30 Minutes of Tropical Downpour | Sleep & Deep Relaxation",
        "short_title": "\U0001f98a Jungle Rain – Pure Relaxation #shorts #junglerain",
        "description": (
            "\U0001f98a Sink into the primal beauty of a jungle rainstorm.\n\n"
            "30 minutes of heavy tropical rain and jungle sounds with ambient music — "
            "perfect for deep sleep, stress relief, or immersive relaxation.\n\n"
            "\U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#junglerain #tropicalrain #relaxingsounds #sleepsounds #junglesounds"
        ),
        "short_description": "\U0001f98a Immersive jungle rain. Subscribe for daily ambience! \U0001f33f",
        "tags": [
            "jungle rain", "tropical rain", "jungle sounds", "rain sounds", "rainforest sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "exotic sounds", "white noise",
            "jungle ambience", "tropical ambience", "ASMR rain", "heavy rain", "wild nature"
        ],
        "category_id": "22",
    },
]

MUSIC_FALLBACK_URLS = [
    "https://cdn.pixabay.com/audio/2024/08/19/audio_53fd9f6bc0.mp3",   # tested, working
    "https://cdn.pixabay.com/audio/2022/10/30/audio_0c1e3cb9fb.mp3",   # tested, working
    "https://cdn.pixabay.com/audio/2022/08/02/audio_884fe92c21.mp3",   # tested, working
    "https://cdn.pixabay.com/audio/2026/06/10/audio_46281ca3ee.mp3",
    "https://cdn.pixabay.com/audio/2026/07/08/audio_9bdff140b9.mp3",
    "https://cdn.pixabay.com/audio/2026/06/27/audio_7aff4b16ad.mp3",
    "https://cdn.pixabay.com/audio/2025/03/10/audio_5e8a58ec04.mp3",
]
