import requests

def easy_word():
    request_url = "https://random-word-api.vercel.app/api?words=1"
    response = requests.get(request_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Access the content of the response
        word_data = response.json()[0]

        # Print the random words
        # print("Random Words:", word_data)
    else:
        print("Error:", response.status_code)



    #Meaning and Examples
    def display_top_meaning(word_data):
        print("Word:", word_data["word"])

        if "meanings" in word_data and len(word_data["meanings"]) > 0:
            top_meaning = word_data["meanings"][0]
            part_of_speech = top_meaning.get("partOfSpeech", "N/A")
            definition = top_meaning["definitions"][0]["definition"]

            print("Part of Speech:", part_of_speech)
            print("Definition:", definition)

            # Display all examples for the top meaning
            for definition in top_meaning["definitions"]:
                if "example" in definition:
                        print("Example:", definition["example"])

        else:
            print("No meanings found for the word.")


    def get_word_data(word):
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()[0]
        else:
            print(f"Failed to fetch data for '{word}'. Check the word and try again.")
            return None

    # Input the word you want to search for


    # Fetch word data from the API
    word= get_word_data(word_data)

    # Display information if data is available
    if word_data:
        display_top_meaning(word)

easy_word()