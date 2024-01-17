import io
import requests
import csv
from datetime import datetime, timedelta
import random
from quote import give_out_quote


today_date = datetime.now()
yester_date = today_date - timedelta(days=300)
final_date = yester_date.strftime("%Y-%m-%d")



API = "575s8ijtzogffrbabvejs4vctw2zxf5qn2p9str44hlk3vpeh"
url = 'https://api.wordnik.com/v4/words.json/wordOfTheDay'
params = {'date': f'{final_date}', 'api_key': f'{API}'}
headers = {'Accept': 'application/json'}
request = f"https://api.wordnik.com/v4/words.json/wordOfTheDay?date=2024-06-01&api_key={API}"
response = requests.get(url, params=params, headers=headers)


def get_motivating_quote_from_file():
    quote = give_out_quote()
    return quote




def get_word_definition(word, api_key):
    url = f'https://api.wordnik.com/v4/word.json/{word}/definitions'
    params = {
        'limit': 5,
        'includeRelated': False,
        'useCanonical': False,
        'includeTags': False,
        'api_key': api_key,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for any errors in the response

        # Assuming the response contains a JSON object with an array of definitions
        definitions = response.json()

        if definitions:
            # Extract information for the first meaning (index 0)
            first_meaning = definitions[1]
            word = first_meaning.get('word', '')
            part_of_speech = first_meaning.get('partOfSpeech', '')
            definition = first_meaning.get('text', '')

            # Display the result
            return definition

        else:
            return f"No definitions found for the word: {word}"

    except requests.exceptions.RequestException as e:
        return f"Error fetching data from Wordnik API: {e}"

# Replace 'YOURAPIKEY' with your actual Wordnik API key


def display_idioms(idioms, entry_number):
    with open(idioms, 'r') as file:
        reader = csv.DictReader(file)

        # Skip entries until reaching the desired number
        for _ in range(entry_number - 1):
            next(reader)

        # Get the entry at the specified number
        entry = next(reader)

        idiom = entry['Idiom']
        meaning = entry['Meaning']
        sentence = entry['Sentence']

        return f"Idiom: {idiom}\nMeaning: {meaning}\nSentence: {sentence}"



def give_it_out() -> str:
    i = random.randint(25, 128)
    output_buffer = io.StringIO()

    try:
        if response.status_code == 200:
            emojis = [
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
            emoji = random.choice(emojis)
            output_buffer.write(f"**Daily Bites by Rupali Saini{emoji}**\n\n")
            output_buffer.write("**Empowering Quote:**\n")
            motivating_quote = get_motivating_quote_from_file()
            output_buffer.write(motivating_quote)

            data = response.json()
            word = data['word']
            meaning = data['definitions'][0]['text']
            sentence = data['examples'][1]['text']

            emoji = random.choice(emojis)
            output_buffer.write(f"\n\n**Word to ponder:**{emoji}\n**{word}**\n")
            output_buffer.write(f"Meaning: {meaning}\n")
            output_buffer.write(f"Sentence: {sentence}\n")

            emoji = random.choice(emojis)
            csv_file_path = 'idioms.csv'
            output_buffer.write(f"\n**Idiom to Embrace:{emoji}**\n")
            idiom_info = display_idioms(idioms=csv_file_path, entry_number=i)
            output_buffer.write(idiom_info)
           

        else:
            output_buffer.write(f"Error: {response.status_code}, {response.text}\n")

    except FileNotFoundError as e:
        output_buffer.write(f"File not found: {e.filename}\n")
    except Exception as e:
        output_buffer.write(f"An error occurred: {e}\n")

    result_string = output_buffer.getvalue()
    output_buffer.close()

    return result_string


