# WillowLoop – Nature ambient loop topics
# Each topic produces one 1-hour loop video + one 59s Short per day
# Topic is selected by: day_of_year % len(TOPICS)

TOPICS = [
    {
        "id": 0,
        "name": "Cozy Fireplace",
        "slug": "fireplace",
        "emoji": "U0001f525",
        "video_queries": ["fireplace burning fire", "fireplace crackling logs", "cozy fireplace"],
        "music_queries": ["relaxing piano ambient", "cozy instrumental music", "soft jazz piano"],
        "duration": 3600,
        "title": "U0001f525 Cozy Fireplace – 1 Hour of Crackling Fire | Relaxing Ambience for Sleep & Study",
        "short_title": "U0001f525 Crackling Fireplace – Pure Relaxation #shorts #fireplace",
        "description": (
            "U0001f525 Let the warmth of a cozy fireplace fill your space.\n\n"
            "1 hour of uninterrupted crackling fire with soothing background music — "
            "perfect for sleep, study, meditation, or relaxing after a long day.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#fireplace #fireplaceambience #relaxingsounds #sleepsounds #cozysounds"
        ),
        "short_description": "U0001f525 Cozy fireplace bliss. Subscribe for 1-hour loops! U0001f33f #fireplace #relaxing",
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
        "emoji": "U0001f327️",
        "video_queries": ["rain forest tropical", "jungle rain", "rainforest rainfall"],
        "music_queries": ["rain ambient music relaxing", "forest meditation piano", "peaceful rain instrumental"],
        "duration": 3600,
        "title": "U0001f327️ Rain in the Forest – 1 Hour of Soothing Rainfall | Sleep & Relaxation",
        "short_title": "U0001f327️ Rain Forest Sounds – Pure Relaxation #shorts #rainsounds",
        "description": (
            "U0001f327️ Escape to a lush rainforest with gentle rainfall.\n\n"
            "1 hour of soothing forest rain sounds with soft ambient music — "
            "perfect for deep sleep, stress relief, focus, or meditation.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#rainsounds #forestrain #relaxingsounds #sleepsounds #naturalsounds"
        ),
        "short_description": "U0001f327️ Rainforest sounds. Subscribe for 1-hour loops! U0001f33f",
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
        "emoji": "U0001f30a",
        "video_queries": ["ocean waves beach", "sea waves calm", "gentle ocean waves"],
        "music_queries": ["ocean ambient piano music", "sea meditation music", "relaxing beach instrumental"],
        "duration": 3600,
        "title": "U0001f30a Ocean Waves – 1 Hour of Calming Sea Sounds | Sleep & Meditation",
        "short_title": "U0001f30a Calming Ocean Waves – Pure Relaxation #shorts #oceansounds",
        "description": (
            "U0001f30a Let the rhythm of the ocean calm your mind.\n\n"
            "1 hour of gentle ocean waves with peaceful ambient music — "
            "perfect for sleep, meditation, yoga, or unwinding after a stressful day.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#oceansounds #wavessounds #beachsounds #relaxingsounds #sleepsounds"
        ),
        "short_description": "U0001f30a Calming ocean waves. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "ocean sounds", "wave sounds", "beach sounds", "ocean waves", "sea sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "ocean ambience", "meditation",
            "waves for sleep", "ASMR ocean", "calming waves", "beach ambience", "water sounds"
        ],
        "category_id": "22",
    },
    {
        "id": 3,
        "name": "Waterfall",
        "slug": "waterfall",
        "emoji": "U0001f4a7",
        "video_queries": ["waterfall nature", "waterfall river forest", "forest waterfall flowing"],
        "music_queries": ["waterfall ambient music", "nature meditation instrumental", "peaceful water piano"],
        "duration": 3600,
        "title": "U0001f4a7 Waterfall Sounds – 1 Hour of Flowing Water | Focus & Deep Sleep",
        "short_title": "U0001f4a7 Beautiful Waterfall – Pure Relaxation #shorts #watersounds",
        "description": (
            "U0001f4a7 Immerse yourself in the peaceful flow of a waterfall.\n\n"
            "1 hour of pure waterfall sounds with gentle ambient music — "
            "ideal for sleep, focus, ASMR, or stress relief.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#waterfallsounds #watersounds #relaxingsounds #sleepsounds #naturalsounds"
        ),
        "short_description": "U0001f4a7 Beautiful waterfall sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "waterfall sounds", "water sounds", "flowing water", "waterfall ambience", "river sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "ASMR water", "meditation sounds",
            "focus sounds", "white noise water", "calming water", "stream sounds", "nature ambience"
        ],
        "category_id": "22",
    },
    {
        "id": 4,
        "name": "Thunderstorm",
        "slug": "thunderstorm",
        "emoji": "⛈️",
        "video_queries": ["thunderstorm rain window", "storm rain thunder", "thunder lightning storm"],
        "music_queries": ["storm ambient music", "dramatic orchestral rain", "dark ambient instrumental"],
        "duration": 3600,
        "title": "⛈️ Thunderstorm – 1 Hour of Rain & Thunder | Deep Sleep & Relaxation",
        "short_title": "⛈️ Thunderstorm Rain & Thunder – Pure Relaxation #shorts #thunderstorm",
        "description": (
            "⛈️ Experience the power and peace of a thunderstorm.\n\n"
            "1 hour of rain and thunder with atmospheric ambient music — "
            "perfect for deep sleep, stress relief, focus, or cozy indoor moments.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#thunderstorm #thundersounds #rainsounds #sleepsounds #stormsounds"
        ),
        "short_description": "⛈️ Thunderstorm sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "thunderstorm sounds", "thunder sounds", "rain and thunder", "storm sounds", "heavy rain",
            "sleep sounds", "relaxing storm", "nature sounds", "thunder ambience", "ASMR thunder",
            "storm for sleep", "rainy night", "cozy storm", "thunder rain", "ambient storm"
        ],
        "category_id": "22",
    },
    {
        "id": 5,
        "name": "Snowy Forest",
        "slug": "snowy_forest",
        "emoji": "❄️",
        "video_queries": ["snowy forest winter", "snow falling forest", "winter forest snow"],
        "music_queries": ["winter ambient piano", "peaceful snow music", "soft christmas instrumental"],
        "duration": 3600,
        "title": "❄️ Snowy Forest – 1 Hour of Falling Snow | Peaceful Winter Ambience",
        "short_title": "❄️ Beautiful Snowy Forest – Pure Relaxation #shorts #snowsounds",
        "description": (
            "❄️ Step into a serene winter wonderland.\n\n"
            "1 hour of peaceful snowy forest ambience with soft winter music — "
            "ideal for sleep, reading, meditation, or embracing the quiet of winter.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#snowysounds #wintersounds #relaxingsounds #sleepsounds #snowambience"
        ),
        "short_description": "❄️ Peaceful snowy forest. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "snow sounds", "winter sounds", "snowy forest", "winter ambience", "falling snow",
            "sleep sounds", "relaxing sounds", "nature sounds", "winter relaxation", "snow ambience",
            "cozy winter", "blizzard sounds", "peaceful winter", "ASMR snow", "winter forest"
        ],
        "category_id": "22",
    },
    {
        "id": 6,
        "name": "Mountain Stream",
        "slug": "mountain_stream",
        "emoji": "U0001f3d4️",
        "video_queries": ["mountain stream flowing", "creek stream nature", "river stream rocks"],
        "music_queries": ["mountain ambient music", "peaceful creek instrumental", "nature flute relaxing"],
        "duration": 3600,
        "title": "U0001f3d4️ Mountain Stream – 1 Hour of Flowing Creek Sounds | Relax & Focus",
        "short_title": "U0001f3d4️ Peaceful Mountain Stream – Pure Relaxation #shorts #streamsounds",
        "description": (
            "U0001f3d4️ Find peace beside a gentle mountain stream.\n\n"
            "1 hour of flowing creek sounds with soothing ambient music — "
            "perfect for focus, sleep, yoga, or peaceful mornings.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#streamsounds #mountainstream #watersounds #relaxingsounds #naturalsounds"
        ),
        "short_description": "U0001f3d4️ Mountain stream sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "mountain stream", "stream sounds", "creek sounds", "babbling brook", "water sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "flowing water", "river sounds",
            "focus sounds", "meditation sounds", "ASMR water", "nature ambience", "peaceful stream"
        ],
        "category_id": "22",
    },
    {
        "id": 7,
        "name": "Night Forest",
        "slug": "night_forest",
        "emoji": "U0001f319",
        "video_queries": ["night forest trees", "forest night stars", "moonlit forest"],
        "music_queries": ["night ambient music", "moonlight piano relaxing", "peaceful night instrumental"],
        "duration": 3600,
        "title": "U0001f319 Night Forest – 1 Hour of Crickets & Owl Sounds | Sleep Ambience",
        "short_title": "U0001f319 Night Forest Sounds – Pure Relaxation #shorts #nightsounds",
        "description": (
            "U0001f319 Drift away under the stars of a peaceful night forest.\n\n"
            "1 hour of night nature sounds with soft ambient music — crickets, owls, "
            "and gentle forest whispers — perfect for deep sleep or meditation.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#nightsounds #forestnight #crickets #sleepsounds #naturalsounds"
        ),
        "short_description": "U0001f319 Night forest sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "night sounds", "night forest", "cricket sounds", "owl sounds", "forest night",
            "sleep sounds", "relaxing sounds", "nature sounds", "night ambience", "ASMR nature",
            "peaceful night", "night birds", "nocturnal sounds", "forest ambience", "sleeping sounds"
        ],
        "category_id": "22",
    },
    {
        "id": 8,
        "name": "Tropical Beach",
        "slug": "tropical_beach",
        "emoji": "U0001f3d6️",
        "video_queries": ["tropical beach waves", "paradise beach ocean", "beach sunset tropical"],
        "music_queries": ["tropical ambient music", "beach lounge instrumental", "island relaxing music"],
        "duration": 3600,
        "title": "U0001f3d6️ Tropical Beach – 1 Hour of Paradise Waves | Relaxation & Sleep",
        "short_title": "U0001f3d6️ Tropical Beach Sounds – Pure Relaxation #shorts #beachsounds",
        "description": (
            "U0001f3d6️ Escape to a tropical paradise.\n\n"
            "1 hour of crystal-clear beach waves with chill ambient music — "
            "perfect for sleep, vacation vibes, stress relief, or daydreaming.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#tropicalbeach #beachsounds #oceansounds #relaxingsounds #sleepsounds"
        ),
        "short_description": "U0001f3d6️ Tropical beach sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "tropical beach", "beach sounds", "ocean waves", "paradise sounds", "summer beach",
            "sleep sounds", "relaxing sounds", "nature sounds", "beach ambience", "island sounds",
            "vacation sounds", "ASMR beach", "peaceful beach", "wave sounds", "seaside sounds"
        ],
        "category_id": "22",
    },
    {
        "id": 9,
        "name": "Bamboo Forest",
        "slug": "bamboo_forest",
        "emoji": "U0001f38b",
        "video_queries": ["bamboo forest wind", "bamboo grove peaceful", "bamboo nature green"],
        "music_queries": ["zen ambient music", "japanese flute relaxing", "bamboo meditation music"],
        "duration": 3600,
        "title": "U0001f38b Bamboo Forest – 1 Hour of Peaceful Zen Sounds | Meditation & Sleep",
        "short_title": "U0001f38b Bamboo Forest Sounds – Pure Relaxation #shorts #zen",
        "description": (
            "U0001f38b Find your inner peace in a serene bamboo forest.\n\n"
            "1 hour of gentle bamboo and wind sounds with calming zen music — "
            "perfect for meditation, yoga, sleep, or a moment of zen calm.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#bambooforest #zensounds #meditationsounds #relaxingsounds #naturalsounds"
        ),
        "short_description": "U0001f38b Bamboo forest zen sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "bamboo forest", "zen sounds", "bamboo sounds", "meditation sounds", "peaceful forest",
            "sleep sounds", "relaxing sounds", "nature sounds", "asian garden", "zen garden",
            "yoga sounds", "ASMR nature", "bamboo wind", "forest ambience", "calm nature"
        ],
        "category_id": "22",
    },
    {
        "id": 10,
        "name": "Desert Wind",
        "slug": "desert_wind",
        "emoji": "U0001f3dc️",
        "video_queries": ["desert landscape sunset", "sand dunes desert", "desert nature scenery"],
        "music_queries": ["desert ambient music", "middle eastern relaxing instrumental", "ethnic ambient meditation"],
        "duration": 3600,
        "title": "U0001f3dc️ Desert Wind – 1 Hour of Peaceful Desert Ambience | Meditation & Sleep",
        "short_title": "U0001f3dc️ Desert Wind Sounds – Pure Relaxation #shorts #desertsounds",
        "description": (
            "U0001f3dc️ Lose yourself in the vast silence of the desert.\n\n"
            "1 hour of gentle desert wind with beautiful ethnic ambient music — "
            "perfect for meditation, focus, or escaping into peaceful solitude.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#desertsounds #desertambience #windsounds #relaxingsounds #meditationsounds"
        ),
        "short_description": "U0001f3dc️ Desert wind sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "desert sounds", "wind sounds", "desert ambience", "sand sounds", "desert wind",
            "sleep sounds", "relaxing sounds", "nature sounds", "meditation sounds", "desert night",
            "ASMR wind", "peaceful desert", "open space sounds", "arid landscape", "calm wind"
        ],
        "category_id": "22",
    },
    {
        "id": 11,
        "name": "Lakeside Sunrise",
        "slug": "lakeside_sunrise",
        "emoji": "U0001f305",
        "video_queries": ["lake sunrise morning", "lakeside calm water", "peaceful lake nature"],
        "music_queries": ["morning ambient piano", "sunrise instrumental music", "peaceful birdsong music"],
        "duration": 3600,
        "title": "U0001f305 Lakeside Sunrise – 1 Hour of Morning Nature Sounds | Peaceful Ambience",
        "short_title": "U0001f305 Lakeside Sunrise Sounds – Pure Relaxation #shorts #lakesounds",
        "description": (
            "U0001f305 Welcome the day with the peaceful sounds of a lakeside sunrise.\n\n"
            "1 hour of gentle water and birdsong with soft morning music — "
            "perfect for morning meditation, focus, or a calm start to your day.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#lakesounds #sunrisesounds #morningsounds #relaxingsounds #birdsounds"
        ),
        "short_description": "U0001f305 Lakeside sunrise sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "lake sounds", "sunrise sounds", "morning sounds", "bird sounds", "water sounds",
            "relaxing sounds", "nature sounds", "peaceful morning", "lakeside ambience", "birdsong",
            "meditation morning", "ASMR nature", "lake birds", "calm water", "morning ambience"
        ],
        "category_id": "22",
    },
    {
        "id": 12,
        "name": "Arctic Snowstorm",
        "slug": "arctic_snowstorm",
        "emoji": "U0001f328️",
        "video_queries": ["blizzard snow storm", "arctic snowstorm", "heavy snowfall winter"],
        "music_queries": ["blizzard ambient music", "arctic drone ambient", "cold wind instrumental dark"],
        "duration": 3600,
        "title": "U0001f328️ Arctic Snowstorm – 1 Hour of Blizzard Sounds | Sleep & Relaxation",
        "short_title": "U0001f328️ Arctic Blizzard Sounds – Pure Relaxation #shorts #blizzard",
        "description": (
            "U0001f328️ Experience the raw power of an arctic snowstorm.\n\n"
            "1 hour of howling wind and snowstorm sounds with atmospheric music — "
            "perfect for deep sleep, cozy indoor moments, or focus work.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#blizzardsounds #snowstorm #wintersounds #sleepsounds #relaxingsounds"
        ),
        "short_description": "U0001f328️ Arctic blizzard sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "blizzard sounds", "snowstorm sounds", "arctic sounds", "winter storm", "wind sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "heavy snow", "winter ambience",
            "ASMR wind", "cozy winter storm", "storm for sleep", "howling wind", "cold sounds"
        ],
        "category_id": "22",
    },
    {
        "id": 13,
        "name": "River Rapids",
        "slug": "river_rapids",
        "emoji": "U0001f3de️",
        "video_queries": ["river rapids flowing", "rushing river water", "fast river stream"],
        "music_queries": ["river ambient music energetic", "flowing water instrumental", "nature energy music"],
        "duration": 3600,
        "title": "U0001f3de️ River Rapids – 1 Hour of Rushing Water | Focus & Deep Sleep",
        "short_title": "U0001f3de️ River Rapids Sounds – Pure Relaxation #shorts #watersounds",
        "description": (
            "U0001f3de️ Be swept away by the energy of rushing river rapids.\n\n"
            "1 hour of powerful flowing water sounds with ambient music — "
            "perfect for focus, deep sleep, masking noise, or pure relaxation.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#riverrapids #watersounds #rushingwater #relaxingsounds #whitenoise"
        ),
        "short_description": "U0001f3de️ River rapids sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "river rapids", "rushing water", "water sounds", "river sounds", "white water",
            "sleep sounds", "relaxing sounds", "nature sounds", "white noise water", "focus sounds",
            "ASMR water", "powerful water", "waterfall sounds", "stream sounds", "water ambience"
        ],
        "category_id": "22",
    },
    {
        "id": 14,
        "name": "Autumn Leaves",
        "slug": "autumn_leaves",
        "emoji": "U0001f342",
        "video_queries": ["autumn leaves falling forest", "fall foliage nature", "autumn forest path"],
        "music_queries": ["autumn ambient piano", "fall season instrumental", "melancholic relaxing music"],
        "duration": 3600,
        "title": "U0001f342 Autumn Leaves – 1 Hour of Fall Forest Ambience | Relaxing Nature Sounds",
        "short_title": "U0001f342 Autumn Forest Sounds – Pure Relaxation #shorts #autumnsounds",
        "description": (
            "U0001f342 Stroll through a golden autumn forest.\n\n"
            "1 hour of falling leaves and autumn wind with beautiful piano music — "
            "perfect for relaxation, sleep, reading, or embracing the beauty of the season.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#autumnsounds #fallambience #leavessounds #relaxingsounds #naturalsounds"
        ),
        "short_description": "U0001f342 Autumn forest sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "autumn sounds", "fall sounds", "leaves sounds", "autumn forest", "fall ambience",
            "sleep sounds", "relaxing sounds", "nature sounds", "autumn leaves", "seasonal sounds",
            "ASMR nature", "cozy autumn", "windy leaves", "forest fall", "fall colors"
        ],
        "category_id": "22",
    },
    {
        "id": 15,
        "name": "Jungle Rain",
        "slug": "jungle_rain",
        "emoji": "U0001f334",
        "video_queries": ["tropical jungle rain", "amazon rainforest rain", "dense jungle waterfall"],
        "music_queries": ["jungle ambient music", "tropical rain instrumental", "rainforest meditation music"],
        "duration": 3600,
        "title": "U0001f334 Jungle Rain – 1 Hour of Tropical Downpour | Deep Sleep & Relaxation",
        "short_title": "U0001f334 Jungle Rain Sounds – Pure Relaxation #shorts #junglesounds",
        "description": (
            "U0001f334 Immerse yourself in the sounds of a tropical jungle downpour.\n\n"
            "1 hour of intense tropical rain with exotic ambient music — "
            "perfect for deep sleep, stress relief, focus, or escaping to a lush paradise.\n\n"
            "U0001f33f Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#junglesounds #tropicalrain #rainsounds #sleepsounds #relaxingsounds"
        ),
        "short_description": "U0001f334 Jungle rain sounds. Subscribe for 1-hour loops! U0001f33f",
        "tags": [
            "jungle sounds", "tropical rain", "rain sounds", "jungle rain", "amazon sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "tropical sounds", "rainforest rain",
            "ASMR rain", "heavy rain", "jungle ambience", "tropical downpour", "jungle birds rain"
        ],
        "category_id": "22",
    },
]
