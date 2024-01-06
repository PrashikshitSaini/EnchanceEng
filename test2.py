import io
import requests
import csv
from datetime import datetime, timedelta
import random

i = 1
today_date = datetime.now()
yester_date = today_date - timedelta(days=1)
final_date = yester_date.strftime("%Y-%m-%d")



API = "575s8ijtzogffrbabvejs4vctw2zxf5qn2p9str44hlk3vpeh"
url = 'https://api.wordnik.com/v4/words.json/wordOfTheDay'
params = {'date': f'{final_date}', 'api_key': f'{API}'}
headers = {'Accept': 'application/json'}
request = f"https://api.wordnik.com/v4/words.json/wordOfTheDay?date=2024-06-01&api_key={API}"
response = requests.get(url, params=params, headers=headers)


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


def get_motivating_quote_from_file(file_path, line_number):
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            motivating_quotes = file.readlines()

            if line_number <= 0 or line_number > len(motivating_quotes):
                print("Invalid line number requested.")
                return

            # Get the quote at the specified line number
            quote = motivating_quotes[line_number - 1]

            # Split the line into number and quote, then strip leading/trailing whitespaces
            _, stripped_quote = quote.split(maxsplit=1)
            return stripped_quote.strip()

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")



def give_it_out() -> str:
    global i
    output_buffer = io.StringIO()

    try:
        if response.status_code == 200:
            emojis = [
                "🧠",  # Brain
                "📚",  # Books
                "🌟",  # Star
                "🔍",  # Magnifying Glass
                "💡",  # Lightbulb
                "🗝️",  # Key
                "🤔",  # Thinking Face
                "🚀",  # Rocket
                "🌈",  # Rainbow
                "🌌",  # Galaxy
                "🔮",  # Crystal Ball
                "📖",  # Open Book
                "🌱",  # Seedling
                "🌠",  # Shooting Star
                "🗣️",  # Speaking Head
            ]
            emoji = random.choice(emojis)
            output_buffer.write(f"**Daily Bites by Rupali Saini{emoji}**\n\n")
            output_buffer.write("**Empowering Quote:**\n")
            motivating_quote = get_motivating_quote_from_file("quotes.txt", i)
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
            i += 1

        else:
            output_buffer.write(f"Error: {response.status_code}, {response.text}\n")

    except FileNotFoundError as e:
        output_buffer.write(f"File not found: {e.filename}\n")
    except Exception as e:
        output_buffer.write(f"An error occurred: {e}\n")

    result_string = output_buffer.getvalue()
    output_buffer.close()

    return result_string

# print(give_it_out()) 