import random

# Growth-oriented quotes
quotes = [
    "🌟 *Small steps every day lead to big changes.*",
    "💪 *You’re not behind. You’re just building your story.*",
    "🧠 *Sharpen your mind, and the world becomes your tool.*",
    "✨ *Believe in your ability to learn, unlearn, and grow.*",
    "📘 *Every time you try, you’re one step ahead of who you were.*",
    "🔥 *Discipline is choosing between what you want now and what you want most.*",
    "🌱 *Growth happens when you’re uncomfortable, but still keep going.*",
    "🎯 *Your future is created by what you do today, not tomorrow.*"
]

# City-specific ideas
city_suggestions = {
    "mumbai": [
        "🎧 Create a Bollywood-themed playlist and analyze lyrics.",
        "📸 Try monsoon street photography from your window.",
        "✍️ Write a blog post titled 'Life between trains and tides'.",
        "🎥 Record a 60-sec video about Mumbai’s fast life from your POV.",
    ],
    "delhi": [
        "🗣️ Practice spoken Hindi or English with voice recording.",
        "📖 Learn something about Mughal architecture and sketch it.",
        "💬 Write a tweet thread on your favorite Delhi historical spot.",
        "📱 Build a simple app that shows weather + pollution index!",
    ],
    "bengaluru": [
        "👨‍💻 Join a live tech webinar or AI workshop today.",
        "📊 Analyze Bangalore traffic data (open source) and visualize it.",
        "☕ Try documenting your café visit and rate productivity.",
        "🧘 Try a morning yoga stretch + journaling challenge.",
    ],
    "chennai": [
        "🎨 Try drawing Marina Beach or Mylapore temples.",
        "🎙️ Record a voice note reciting a Tamil thirukkural.",
        "🍛 Cook something local and learn the science behind ingredients.",
        "📖 Read a Tamil short story and summarize it visually.",
    ],
    "kolkata": [
        "📷 Capture shadows and textures indoors inspired by Satyajit Ray.",
        "🖊️ Try Bengali calligraphy with pen and ink.",
        "🎭 Watch a Bengali classic film and review it in 5 lines.",
        "📚 Learn about Rabindranath Tagore’s influence on education.",
    ],
    "pune": [
        "👓 Read a Marathi newspaper or blog and translate a section.",
        "🧠 Build a flashcard deck for Marathi or coding terms.",
        "🎨 Start a digital art project around hills and fort ruins.",
        "📈 Use Excel to track your week’s learning habits.",
    ],
    "hyderabad": [
        "🍲 Try a Hyderabadi biryani recipe and make a cooking video.",
        "📚 Read an Urdu couplet and try rewriting it as a modern poem.",
        "👨‍💻 Code a local-food-finder UI mockup in Figma.",
        "🎤 Record a podcast explaining a simple science concept in Telugu.",
    ],
    "jaipur": [
        "🎨 Create mandala art using Rajasthani patterns.",
        "📜 Study Indian textile designs and sketch 3 new ones.",
        "📸 Capture royal colors at home or in a collage.",
        "💡 Learn about Jaipur’s stepwells and their engineering value.",
    ]
}

def get_mood_suggestion(condition, city):
    condition = condition.lower()
    city = city.lower()

    sunny_ideas = [
        "☀️ Go for a sketching session of your street/building.",
        "🎧 Listen to classical Indian ragas that reflect sunshine.",
        "📷 Take golden hour photos from your balcony.",
        "🧘 Try sun salutation yoga poses and reflect on gratitude.",
        "🎨 Paint or draw using only warm colors (yellows, reds, oranges).",
        "🌿 Tend to a plant or start a small herb garden.",
        "📚 Read a self-help or productivity book outside.",
        "💬 Call a friend and share your wins from the week.",
        "🖼️ Make a vision board with your goals and affirmations.",
        "📱 Build a weather visualization app using Python!",
        "💪 Do a short full-body home workout using YouTube.",
        "📔 Start a habit tracker journal.",
        "🎥 Create a motivational reel using today’s weather as backdrop.",
        "🧵 Try embroidery or handcrafting something small and sunny.",
    ]

    rainy_ideas = [
        "☔ Create rain-inspired digital art using Krita or Canva.",
        "📖 Read a short story from an Indian author and reflect on it.",
        "📜 Write a poem called 'When the Clouds Cried'.",
        "🧁 Try baking something easy and decorate it.",
        "🎮 Play a brain puzzle or learn coding logic via game-based tools.",
        "🧠 Watch a TEDx talk and summarize it in 4 sentences.",
        "🎤 Record your voice reading a short story or tongue twister.",
        "🌧️ Make a rain-inspired music playlist and share it online.",
        "📈 Track your learning progress and make goals for the week.",
        "📝 Make a gratitude list while sipping your favorite hot drink.",
        "🎨 Try coloring mandalas to relax your mind.",
        "📚 Enroll in a 1-hour free workshop from Coursera/EdX.",
        "📸 Do a photo shoot indoors with creative lighting.",
        "🔧 Fix something small at home: tidy cables, repair broken zippers, etc.",
        "🧘 Try rain-themed guided meditation from YouTube.",
    ]

    cloudy_ideas = [
        "☁️ Record ambient sounds of your surroundings.",
        "🎬 Watch an indie Indian short film and write a critique.",
        "🧠 Solve one crossword or sudoku puzzle.",
        "🧵 Knit, crochet, or make something with your hands.",
        "🎤 Try rapping or beatboxing to express cloudy thoughts.",
        "📸 Take low-light photography challenges.",
        "📚 Learn about a famous Indian scientist or writer.",
        "🖊️ Write a letter to your future self.",
        "📱 Build an Instagram carousel with weather-based affirmations.",
        "🔍 Try ‘how stuff works’ — learn about clouds and rain formation.",
        "💬 Learn sign language basics for 30 minutes.",
        "🎧 Explore Indian classical instrumentals and journal emotions.",
        "🪔 Rearrange your desk or study corner for productivity.",
        "📊 Analyze your phone usage and reduce digital clutter.",
        "🧘 Practice breathwork techniques to clear mental fog.",
    ]

    snow_ideas = [
        "❄️ Learn about the Himalayas’ influence on India’s climate.",
        "📖 Write a fictional story about a snowfall in Ladakh.",
        "🖼️ Design a snowflake pattern using symmetry in art.",
        "📸 Make a 'white color' photo theme post using things around you.",
        "🎧 Listen to peaceful winter-themed background music.",
        "📚 Research Indian army outposts in Siachen and their bravery.",
        "💬 Learn new vocabulary around winter and snow.",
        "🧠 Try binaural beats or concentration music and study deeply.",
        "🎮 Code a basic snow animation using Python + Turtle.",
        "🎥 Watch a documentary on Himalayan wildlife.",
    ]

    thunder_ideas = [
        "⛈️ Read a science blog about thunder & lightning safely indoors.",
        "🎭 Write a dramatic short scene titled 'Storm Within'.",
        "🔊 Create a thunderstorm beat using free music tools online.",
        "📖 Study the calming effects of sound and how to use white noise.",
        "🧠 Visualize your thoughts using mind-mapping apps.",
        "📱 Build a 'calm app clone' UI on Figma.",
        "🎨 Try painting with grayscale only to mimic a stormy mood.",
        "🎤 Sing or hum something calming for voice training.",
        "📚 Learn how batteries and surge protectors work.",
        "🧘 Try a candle-lit meditation session (safely at home).",
    ]

    fog_ideas = [
        "🌫️ Try perspective sketching to mimic fog depth.",
        "📖 Read about Uttarakhand or Himachal winter life.",
        "📹 Create a timelapse of the outside visibility.",
        "🎨 Paint a misty forest digitally or on paper.",
        "🧠 Meditate while visualizing mental clarity.",
        "📊 Track how the fog affects your productivity today.",
        "📱 Create an infographic explaining air quality index.",
        "📚 Write a short thriller titled 'Fog in the Valley'.",
        "🧩 Complete a jigsaw puzzle — great for concentration!",
        "🎧 Explore Indian Lo-fi music and rate your top 3.",
    ]

    default_ideas = [
        "📚 Learn something new from YouTube or Skillshare!",
        "🧠 Organize your week using Notion or Trello.",
        "🎯 Take a 15-minute break from screens and stretch.",
        "🎨 Draw or write about today’s weather using a metaphor.",
        "📱 Explore a new educational mobile app.",
        "🎬 Create a 30-sec story using your home objects.",
        "🗣️ Call your grandparent or someone elder and ask for a life lesson.",
    ]

    condition_mapping = {
        "sun": sunny_ideas,
        "clear": sunny_ideas,
        "rain": rainy_ideas,
        "shower": rainy_ideas,
        "cloud": cloudy_ideas,
        "overcast": cloudy_ideas,
        "snow": snow_ideas,
        "thunder": thunder_ideas,
        "fog": fog_ideas,
        "mist": fog_ideas
    }

    base_ideas = default_ideas
    for keyword, ideas in condition_mapping.items():
        if keyword in condition:
            base_ideas = ideas
            break

    city_idea = random.choice(city_suggestions[city]) if city in city_suggestions else ""
    suggestion = f"{random.choice(base_ideas)}\n📍 {city_idea}" if city_idea else random.choice(base_ideas)
    quote = random.choice(quotes)

    return f"{suggestion}\n\n💬 {quote}"
