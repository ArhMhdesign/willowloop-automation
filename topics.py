# WillowLoop – Nature ambient loop topics
# Each topic produces one 2-hour loop video + one 60s Short per day
# Topic is selected by: day_of_year % len(TOPICS)

TOPICS = [
    {
        "id": 0,
        "name": "Cozy Fireplace",
        "slug": "fireplace",
        "emoji": "🔥",
        "video_queries": ["fireplace burning fire", "fireplace crackling logs", "cozy fireplace"],
        "duration": 7200,
        "title": "🔥 Cozy Fireplace – 2 Hours of Crackling Fire | Relaxing Ambience for Sleep & Study",
        "short_title": "🔥 Crackling Fireplace Sounds – 1 Minute of Pure Relaxation #shorts #fireplace",
        "description": (
            "🔥 Let the warmth of a cozy fireplace fill your space.\n\n"
            "2 hours of uninterrupted crackling fire — perfect for sleep, study, "
            "meditation, or just relaxing after a long day.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#fireplace #fireplaceambience #relaxingsounds #sleepsounds #cozysounds"
        ),
        "short_description": "🔥 Pure crackling fireplace bliss. Subscribe for 2-hour loops! 🌿 #fireplace #relaxing",
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
        "emoji": "🌧️",
        "video_queries": ["rain forest tropical", "jungle rain", "rainforest rainfall"],
        "duration": 7200,
        "title": "🌧️ Rain in the Forest – 2 Hours of Soothing Rainfall | Sleep & Relaxation",
        "short_title": "🌧️ Rain Forest Sounds – Pure Relaxation #shorts #rainsounds",
        "description": (
            "🌧️ Escape to a lush rainforest with gentle rainfall.\n\n"
            "2 hours of soothing forest rain sounds — perfect for deep sleep, stress relief, "
            "focus, or meditation.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#rainsounds #forestrain #relaxingsounds #sleepsounds #naturalsounds"
        ),
        "short_description": "🌧️ Rainforest sounds in 60 seconds. Subscribe for full 2-hour loops! 🌿",
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
        "emoji": "🌊",
        "video_queries": ["ocean waves beach", "sea waves calm", "gentle ocean waves"],
        "duration": 7200,
        "title": "🌊 Ocean Waves – 2 Hours of Calming Sea Sounds | Sleep & Meditation",
        "short_title": "🌊 Calming Ocean Waves – Pure Relaxation #shorts #oceansounds",
        "description": (
            "🌊 Let the rhythm of the ocean calm your mind.\n\n"
            "2 hours of gentle ocean waves — perfect for sleep, meditation, yoga, "
            "or unwinding after a stressful day.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#oceansounds #wavessounds #beachsounds #relaxingsounds #sleepsounds"
        ),
        "short_description": "🌊 Calming ocean waves in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "emoji": "💧",
        "video_queries": ["waterfall nature", "waterfall river forest", "forest waterfall flowing"],
        "duration": 7200,
        "title": "💧 Waterfall Sounds – 2 Hours of Flowing Water | Focus & Deep Sleep",
        "short_title": "💧 Beautiful Waterfall Sounds – Pure Relaxation #shorts #watersounds",
        "description": (
            "💧 Immerse yourself in the peaceful flow of a waterfall.\n\n"
            "2 hours of pure waterfall sounds — ideal for sleep, focus, ASMR, "
            "or stress relief.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#waterfallsounds #watersounds #relaxingsounds #sleepsounds #naturalsounds"
        ),
        "short_description": "💧 Beautiful waterfall in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "duration": 7200,
        "title": "⛈️ Thunderstorm – 2 Hours of Rain & Thunder | Deep Sleep & Relaxation",
        "short_title": "⛈️ Thunderstorm Rain & Thunder – Pure Relaxation #shorts #thunderstorm",
        "description": (
            "⛈️ Experience the power and peace of a thunderstorm.\n\n"
            "2 hours of rain and thunder — perfect for deep sleep, stress relief, "
            "focus, or cozy indoor moments.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#thunderstorm #thundersounds #rainsounds #sleepsounds #stormsounds"
        ),
        "short_description": "⛈️ Thunderstorm sounds in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "duration": 7200,
        "title": "❄️ Snowy Forest – 2 Hours of Falling Snow | Peaceful Winter Ambience",
        "short_title": "❄️ Beautiful Snowy Forest – Pure Relaxation #shorts #snowsounds",
        "description": (
            "❄️ Step into a serene winter wonderland.\n\n"
            "2 hours of peaceful snowy forest ambience — ideal for sleep, reading, "
            "meditation, or embracing the quiet of winter.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#snowysounds #wintersounds #relaxingsounds #sleepsounds #snowambience"
        ),
        "short_description": "❄️ Peaceful snowy forest in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "emoji": "🏔️",
        "video_queries": ["mountain stream flowing", "creek stream nature", "river stream rocks"],
        "duration": 7200,
        "title": "🏔️ Mountain Stream – 2 Hours of Flowing Creek Sounds | Relax & Focus",
        "short_title": "🏔️ Peaceful Mountain Stream – Pure Relaxation #shorts #streamsounds",
        "description": (
            "🏔️ Find peace beside a gentle mountain stream.\n\n"
            "2 hours of flowing creek sounds — perfect for focus, sleep, yoga, "
            "or peaceful mornings.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#streamsounds #mountainstream #watersounds #relaxingsounds #naturalsounds"
        ),
        "short_description": "🏔️ Mountain stream sounds in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "emoji": "🌙",
        "video_queries": ["night forest trees", "forest night stars", "moonlit forest"],
        "duration": 7200,
        "title": "🌙 Night Forest – 2 Hours of Crickets & Owl Sounds | Sleep Ambience",
        "short_title": "🌙 Night Forest Sounds – Pure Relaxation #shorts #nightsounds",
        "description": (
            "🌙 Drift away under the stars of a peaceful night forest.\n\n"
            "2 hours of night nature sounds — crickets, owls, and gentle forest whispers — "
            "perfect for deep sleep, relaxation, or meditation.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#nightsounds #forestnight #crickets #sleepsounds #naturalsounds"
        ),
        "short_description": "🌙 Night forest sounds in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "emoji": "🏖️",
        "video_queries": ["tropical beach waves", "paradise beach ocean", "beach sunset tropical"],
        "duration": 7200,
        "title": "🏖️ Tropical Beach – 2 Hours of Paradise Waves | Relaxation & Sleep",
        "short_title": "🏖️ Tropical Beach Sounds – Pure Relaxation #shorts #beachsounds",
        "description": (
            "🏖️ Escape to a tropical paradise.\n\n"
            "2 hours of crystal-clear beach waves — perfect for sleep, vacation vibes, "
            "stress relief, or daydreaming.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#tropicalbeach #beachsounds #oceansounds #relaxingsounds #sleepsounds"
        ),
        "short_description": "🏖️ Tropical beach sounds in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "emoji": "🎋",
        "video_queries": ["bamboo forest wind", "bamboo grove peaceful", "bamboo nature green"],
        "duration": 7200,
        "title": "🎋 Bamboo Forest – 2 Hours of Peaceful Zen Sounds | Meditation & Sleep",
        "short_title": "🎋 Bamboo Forest Sounds – Pure Relaxation #shorts #zen",
        "description": (
            "🎋 Find your inner peace in a serene bamboo forest.\n\n"
            "2 hours of gentle bamboo and wind sounds — perfect for meditation, "
            "yoga, sleep, or a moment of zen calm.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#bambooforest #zensounds #meditationsounds #relaxingsounds #naturalsounds"
        ),
        "short_description": "🎋 Bamboo forest sounds in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "emoji": "🏜️",
        "video_queries": ["desert landscape sunset", "sand dunes desert", "desert nature scenery"],
        "duration": 7200,
        "title": "🏜️ Desert Wind – 2 Hours of Peaceful Desert Ambience | Meditation & Sleep",
        "short_title": "🏜️ Desert Wind Sounds – Pure Relaxation #shorts #desertsounds",
        "description": (
            "🏜️ Lose yourself in the vast silence of the desert.\n\n"
            "2 hours of gentle desert wind and sand sounds — perfect for meditation, "
            "focus, or escaping into a world of peaceful solitude.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#desertsounds #desertambience #windsounds #relaxingsounds #meditationsounds"
        ),
        "short_description": "🏜️ Desert wind sounds in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "emoji": "🌅",
        "video_queries": ["lake sunrise morning", "lakeside calm water", "peaceful lake nature"],
        "duration": 7200,
        "title": "🌅 Lakeside Sunrise – 2 Hours of Morning Nature Sounds | Peaceful Ambience",
        "short_title": "🌅 Lakeside Sunrise Sounds – Pure Relaxation #shorts #lakesounds",
        "description": (
            "🌅 Welcome the day with the peaceful sounds of a lakeside sunrise.\n\n"
            "2 hours of gentle water and birdsong — perfect for morning meditation, "
            "focus, or a calm start to your day.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#lakesounds #sunrisesounds #morningsounds #relaxingsounds #birdsounds"
        ),
        "short_description": "🌅 Lakeside sunrise sounds in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "emoji": "🌨️",
        "video_queries": ["blizzard snow storm", "arctic snowstorm", "heavy snowfall winter"],
        "duration": 7200,
        "title": "🌨️ Arctic Snowstorm – 2 Hours of Blizzard Sounds | Sleep & Relaxation",
        "short_title": "🌨️ Arctic Blizzard Sounds – Pure Relaxation #shorts #blizzard",
        "description": (
            "🌨️ Experience the raw power of an arctic snowstorm.\n\n"
            "2 hours of howling wind and snowstorm sounds — perfect for deep sleep, "
            "cozy indoor moments, or focus work.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#blizzardsounds #snowstorm #wintersounds #sleepsounds #relaxingsounds"
        ),
        "short_description": "🌨️ Arctic blizzard sounds in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "emoji": "🏞️",
        "video_queries": ["river rapids flowing", "rushing river water", "fast river stream"],
        "duration": 7200,
        "title": "🏞️ River Rapids – 2 Hours of Rushing Water | Focus & Deep Sleep",
        "short_title": "🏞️ River Rapids Sounds – Pure Relaxation #shorts #watersounds",
        "description": (
            "🏞️ Be swept away by the energy of rushing river rapids.\n\n"
            "2 hours of powerful flowing water sounds — perfect for focus, deep sleep, "
            "masking noise, or pure relaxation.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#riverrapids #watersounds #rushingwater #relaxingsounds #whitenoise"
        ),
        "short_description": "🏞️ River rapids sounds in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "emoji": "🍂",
        "video_queries": ["autumn leaves falling forest", "fall foliage nature", "autumn forest path"],
        "duration": 7200,
        "title": "🍂 Autumn Leaves – 2 Hours of Fall Forest Ambience | Relaxing Nature Sounds",
        "short_title": "🍂 Autumn Forest Sounds – Pure Relaxation #shorts #autumnsounds",
        "description": (
            "🍂 Stroll through a golden autumn forest.\n\n"
            "2 hours of falling leaves and autumn wind — perfect for relaxation, "
            "sleep, reading, or embracing the beauty of the season.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#autumnsounds #fallambience #leavessounds #relaxingsounds #naturalsounds"
        ),
        "short_description": "🍂 Autumn forest sounds in 60 seconds. Subscribe for 2-hour loops! 🌿",
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
        "emoji": "🌴",
        "video_queries": ["tropical jungle rain", "amazon rainforest rain", "dense jungle waterfall"],
        "duration": 7200,
        "title": "🌴 Jungle Rain – 2 Hours of Tropical Downpour | Deep Sleep & Relaxation",
        "short_title": "🌴 Jungle Rain Sounds – Pure Relaxation #shorts #junglesounds",
        "description": (
            "🌴 Immerse yourself in the sounds of a tropical jungle downpour.\n\n"
            "2 hours of intense tropical rain — perfect for deep sleep, stress relief, "
            "focus, or escaping to a lush paradise.\n\n"
            "🌿 Subscribe to WillowLoop for daily nature ambience videos.\n\n"
            "#junglesounds #tropicalrain #rainsounds #sleepsounds #relaxingsounds"
        ),
        "short_description": "🌴 Jungle rain sounds in 60 seconds. Subscribe for 2-hour loops! 🌿",
        "tags": [
            "jungle sounds", "tropical rain", "rain sounds", "jungle rain", "amazon sounds",
            "sleep sounds", "relaxing sounds", "nature sounds", "tropical sounds", "rainforest rain",
            "ASMR rain", "heavy rain", "jungle ambience", "tropical downpour", "jungle birds rain"
        ],
        "category_id": "22",
    },
]
