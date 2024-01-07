import requests
import random

def give_out_quote():
    url = "https://quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com/quote"

    querystring = {"token":"ipworld.info"}

    headers = {
        "X-RapidAPI-Key": "9106f9bb61mshd7d179b9ecb68d5p1b1b84jsn1e20219fa208",
        "X-RapidAPI-Host": "quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    author = response.json()['author']
    quote = response.json()['text']
    wisdom_emojis = [
        "🧠",  # Brain
        "📚",  # Books
        "💡",  # Lightbulb
        "🔍",  # Magnifying Glass
        "🌟",  # Star
        "🎓",  # Graduation Cap
        "🤔",  # Thinking Face
        "📖",  # Open Book
        "🗝️",  # Key
        "🔮",  # Crystal Ball
        "🌐",  # Globe
        "🔭",  # Telescope
        "📜",  # Scroll
        "🖋️",  # Fountain Pen
        "🕰️",  # Mantelpiece Clock
        "🧭",  # Compass
        "📡",  # Satellite Antenna
        "🔬",  # Microscope
        "🧬",  # DNA
        "📊",  # Bar Chart
        "🎯",  # Bullseye
        "📌",  # Pushpin
        "🗓️",  # Spiral Calendar
        "🚀",  # Rocket
        "🔗",  # Link
        "🕊️",  # Dove
        "🌌",  # Milky Way
        "🧘",  # Person in Lotus Position
        "🌠",  # Shooting Star
        "🎇",  # Sparkler
        "🔱",  # Trident Emblem
        "🏹",  # Bow and Arrow
        "📡",  # Satellite Dish
        "🔍",  # Left-Pointing Magnifying Glass
        "🔬",  # Microscope
        "🔭",  # Telescope
        "🛡️",  # Shield
        "📝",  # Memo
        "📈",  # Chart Increasing
        "📉",  # Chart Decreasing
        "💬",  # Speech Balloon
        "🔗",  # Link
        "🗣️",  # Speaking Head
        "🤯",  # Exploding Head
        "🌐",  # Globe with Meridians
        "🔒",  # Locked
        "🔓",  # Unlocked
        "🔍",  # Magnifying Glass Tilted Left
        "🔎",  # Magnifying Glass Tilted Right
    ]

    # Printing the list of 50 wisdom emojis
    emoji = random.choice(wisdom_emojis)

    return f'"{quote}" - {author}{emoji}'