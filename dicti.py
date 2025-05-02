from utis import speak

# Fetch word meaning
def fetch_word_meaning(word):
    try:
        from main import dictionary  # Import dynamically to ensure up-to-date object
        meanings = dictionary.meaning(word)
        if meanings:
            for pos, definitions in meanings.items():
                speak(f"The word '{word}' as a {pos} means: {definitions[0]}")
                # Break after first meaning; remove 'break' to read all meanings
                break
        else:
            speak(f"Sorry, I couldn't find the meaning for the word '{word}'.")
    except AttributeError:
        speak("It seems the dictionary is not initialized or is missing required methods.")
    except Exception as e:
        speak(f"Error in finding the word meaning: {str(e)}")

# Fetch word antonym
def fetch_opposite_word(word):
    try:
        from main import dictionary  # Import dynamically to ensure up-to-date object
        antonyms = dictionary.antonym(word)
        if antonyms:
            speak(f"The opposite of '{word}' is: {antonyms[0]}")
        else:
            speak(f"Sorry, I couldn't find the opposite for the word '{word}'.")
    except AttributeError:
        speak("It seems the dictionary is not initialized or is missing required methods.")
    except Exception as e:
        speak(f"Error in finding the opposite word: {str(e)}")
