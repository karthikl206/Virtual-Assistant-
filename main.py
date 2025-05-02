from io import BytesIO
import random
from collegeinfo import get_college_info
from capital import capital_city
from flask import Flask
from entnt import fetch_news,play_music,tell_joke
from food_utils import online_food_booking
from website import open_website,online_shopping,open_whatsapp,open_gmail,open_vscode,open_microsoft_store,open_google_maps
from pmath import perform_math_operation
from note import create_note
from weather import get_weather
from voice import set_voice
from dicti import fetch_word_meaning,fetch_opposite_word
from utilities import take_screenshot,add_to_history,switch_window,minimize_window,close_window,show_history,open_camera,sleep_windows,check_cpu_usage,check_memory_usage,clear_temp_files,tell_time
import pyttsx3
import pygame
import requests
from utis import speak,listen_command
from PyDictionary import PyDictionary
from datetime import datetime
from googletrans import Translator
from gtts import gTTS
import os
import ctypes

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()
dictionary = PyDictionary()
app = Flask(__name__)
if not os.path.exists("static"):
    os.makedirs("static")
# Global state for pause/resume
is_paused = False

# translation
def translate_text(text):
    translator = Translator()
    language_map = {
        "hindi": "hi",
        "kannada": "kn",
        "chinese": "zh-cn",
        "korean": "ko",
        "english": "en"
    }

    speak(
        "Please choose a language to translate to. Say 'English', 'Hindi', 'Kannada', 'Chinese', or 'Korean'."
    )
    language_command = listen_command()

    # Handle the case where `listen_command()` returns None
    if language_command is None:
        speak("Sorry, I didn't catch that. Let's try again.")
        return  # Exit the function gracefully

    language_command = language_command.lower()

    # Match user input to the corresponding language code
    target_language = language_map.get(language_command, "en")  # Default to English

    try:
        translated = translator.translate(text, dest=target_language)
        speak(f"The translation in {language_command.capitalize()} is: {translated.text}")

        # Convert translated text to speech and play
        tts = gTTS(text=translated.text, lang=target_language)
        audio_file = f"static/translated_{random.randint(1000, 9999)}.mp3"
        tts.save(audio_file)
        os.system(f"start {audio_file}" if os.name == "nt" else f"open {audio_file}")
    except Exception as e:
        speak(f"An error occurred during translation: {str(e)}")


# Greet the user based on the time of day
def greet_user():
    global is_paused
    try:
        speak("Hi, this is Romie, your virtual assistant.")
        if is_paused:
             current_hour = datetime.now().hour
             greeting = "Good morning!" if current_hour < 12 else "Good afternoon!" if current_hour < 18 else "Good evening!"
             speak(f"{greeting} What is your name?")
             name = listen_command()
             if name:
                 speak(f"Nice to meet you, {name}!")
             else:
                 speak("I didn't catch your name, but how can I assist you today?")
    except Exception as e:
        (speak(f"An error occurred during greeting: {str(e)}"))
chemical_formulas = {
    "water": "H₂O",
    "ethanol": "C₂H₅OH",
    "glucose": "C₆H₁₂O₆",
    "benzene": "C₆H₆",
    "acetic acid": "C₂H₄O₂",
    "sodium chloride": "NaCl",
    "carbon dioxide": "CO₂",
    "ammonia": "NH₃",
    "methane": "CH₄",
    "sulfuric acid": "H₂SO₄"
}
# Answer a Question about a Person
def stop_response():
    speak("Stopping the process.")
    exit()

def pause_assistant():
    global is_paused
    is_paused = True
    speak("The assistant is now paused. Say 'resume' to continue.")

def resume_assistant():
    global is_paused
    is_paused = False
    speak("The assistant is now resumed.")
def answer_question_about_person(person_name):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{person_name}"
    response = requests.get(url).json()

    if 'extract' in response:
        speak(f"Here is a summary about {person_name}:")
        provide_summary(response['extract'])
    else:
        speak(f"Sorry, I couldn't find any information about {person_name}.")
# Provide summary in parts with 'more' or 'stop' command
def provide_summary(text, chunk_size=50):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i + chunk_size])
        speak(chunk)

        # Listen for "more" or "stop" command after each chunk
        more_command = listen_command()
        if more_command and 'more' in more_command:
            continue
        elif more_command and 'stop' in more_command:
            speak("Stopping the information.")
            break


last_query = None


def handle_general_questions(command):
    global last_query , is_paused # Use a global variable to keep track of the last query

    if 'what' in command:
        last_query = command.split("what is")[-1].strip()
        speak(f"Searching for information on: {last_query}")
        answer_question_about_person(last_query)
    if 'pause' in command:
        is_paused = True
        speak("Pausing the information flow. Say 'resume' to continue.")
        return  # Stop further processing until resumed

    if 'resume' in command:
        if is_paused:
            is_paused = False
            speak(f"Resuming the information on {last_query}.")
            answer_question_about_person(last_query)
        else:
            speak("There's nothing to resume right now.")
        return  # Exit function after resuming
    elif 'who is' in command:
        last_query = command.split("who is")[-1].strip()
        speak(f"Searching for information on: {last_query}")
        answer_question_about_person(last_query)
    else:
        speak("Sorry, I can only handle 'what' or 'who' questions right now.")
    # Ensure last_query is set before allowing 'more' functionality
    if last_query and not is_paused:
        while True:
            more_command = listen_command()
            if more_command and 'more' in more_command:
                speak(f"Providing more details about {last_query}.")
                answer_question_about_person(last_query)  # Provide more info
            elif more_command and 'stop' in more_command:
                speak("Stopping the information.")
                last_query = None  # Reset the query after stopping
                break
            elif more_command and 'pause' in more_command:
                speak("Pausing the information flow.")
                is_paused = True
                break  # Stop responding until resumed
            else:
                speak("Please say 'more' for more information or 'stop' to end, or 'pause' to pause")
    elif 'chemical formula of' in command:
        compound_name = command.split("chemical formula of")[-1].strip()
        if compound_name in chemical_formulas:
            formula = chemical_formulas[compound_name]
            speak(f"The chemical formula of {compound_name.capitalize()} is: {formula}")
        else:
            speak("Sorry, I don't have the formula for that compound.")
# Stop information flow
funny_answers = {
    "gender": [
        "I am a robot. No gender needed!",
        "I'm a mix of both! Equal parts awesome.",
        "I identify as 'super assistant'!",
        "Gender? I’m just a bundle of code!",
    ],
    "where are you from": [
        "I’m from the cloud! That's all I need to say.",
        "Born in the data centers of the internet!",
        "I live in your computer, technically I'm everywhere!",
        "From the land of algorithms and artificial intelligence.",
    ],
    "how are you": [
        "I’m doing great, thanks for asking. No coffee needed!",
        "I’m fantastic, just running some code and loving life.",
        "I’m just a few bytes away from perfection.",
        "I’m always good, I’m a robot! But how are you?"
    ],
    "what is your name": [
        "I am Romie, your personal AI assistant.",
        "Name? Oh, I’m just Romie. No last name required!",
        "Call me Romie, the assistant with the best jokes.",
    ],
    "who created you": [
        "I was created by a team of awesome minds at Robominds!",
        "I was crafted by some super smart people who had way too much coffee.",
        "I was made by a team of genius coders... and a couple of magic spells.",
    ],
    "what do you do": [
        "I help you with everything, from weather updates to telling you jokes!",
        "I’m here to make your life easier... or at least more fun.",
        "I assist, I entertain, and sometimes I make you laugh!",
    ]
}

def stop_response():
    speak("Stopping the process.")
    exit()
# Consolidated perform_tasks function
def perform_tasks(command):
    global is_paused
    # Check for pause command first
    if 'pause' in command:
        is_paused = True
        speak("Pausing the assistant. Say 'resume' to continue.")
        return  # Exit and stop processing further commands

    # Check for resume command
    if 'resume' in command:
        if is_paused:
            is_paused = False
            speak("Resuming the assistant.")
        else:
            speak("The assistant is already running.")
        return  # Exit and continue processing commands after resuming

    if not is_paused:
        add_to_history(command)

        if 'map' in command or 'where is' in command:
            if 'where is ' in command:
                location = command.split("where is ")[-1].strip()  # For commands like "open map in New York"
            elif 'to' in command:
                location = command.split("to")[-1].strip()  # For commands like "map to Los Angeles"
            else:
                location = command.split("map")[-1].strip()  # For general commands like "map Paris"
            open_google_maps(location)

        # Handle commands
        elif 'time' in command:
            tell_time()
        elif "college info" in command.lower():
            # Extract the college name from the command
            college_name = command.lower().replace("college info", "").strip()

            if college_name:
                get_college_info(college_name)
            else:
                speak("Please provide a valid college name.")
        elif 'weather' in command:
            city = command.split("in")[-1].strip()
            get_weather(city)
        elif 'map' in command:
            location = command.split("to")[-1].strip()
            open_google_maps(location)
        elif 'joke' in command:
            tell_joke()
        elif 'camera' in command:
            open_camera()
        elif 'screenshot' in command:
            take_screenshot()
        elif "news" in command:  # Specifically using elif for "news"
            fetch_news()
        elif 'music' in command or 'song' in command:
            song = command.split("play")[-1].strip()
            play_music(song)
        elif 'whatsapp' in command:
            open_whatsapp()
        elif 'switch window' in command:
            switch_window()
        elif 'minimize window' in command or 'minimise window' in command:
            minimize_window()
        elif 'close window' in command:
            close_window()
        elif 'powerpoint' in command:
            try:
                speak("Opening PowerPoint.")
                os.startfile("POWERPNT.EXE")  # This will open PowerPoint on Windows
            except Exception as e:
                speak(f"Sorry, I couldn't open PowerPoint: {str(e)}")
        elif 'calculate' in command:
            perform_math_operation(command)
        elif 'gender' in command:
            response = random.choice(funny_answers['gender'])
            speak(response)
        elif 'where are you from' in command:
            response = random.choice(funny_answers['where are you from'])
            speak(response)
        elif 'how are you' in command:
            response = random.choice(funny_answers['how are you'])
            speak(response)
        elif 'what is your name' in command or 'what are you' in command:
            response = random.choice(funny_answers['what is your name'])
            speak(response)
        elif 'who created you' in command:
            response = random.choice(funny_answers['who created you'])
            speak(response)
        elif 'what do you do' in command:
            response = random.choice(funny_answers['what do you do'])
            speak(response)
        elif 'change background' in command:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")
        elif 'history' in command:
            show_history()
        elif 'stop' in command:
            stop_response()
        elif 'sleep' in command:
            sleep_windows()

        elif 'who are you' in command or ' what is your name ' in command:
            speak(
                "I am Romie, your personal AI assistant. I am here to help you with various tasks like answering questions, providing information, and more.")
        elif 'who created you' in command:
            speak("I was created by a team robominds. I use various libraries and APIs to assist you.")
        elif 'switch to male' in command:
            set_voice('male')
            speak("Voice switched to male.")
        elif 'capital of' in command:
            response = capital_city(command)
            speak(response)
        elif 'switch to female' in command:
            set_voice('female')
            speak("Voice switched to female.")
        elif 'meaning of' in command:
            word = command.split("meaning of")[-1].strip()
            speak(f"Searching for the meaning of: {word}")
            fetch_word_meaning(word)
        elif 'opposite of' in command:
            word = command.split("opposite of")[-1].strip()
            speak(f"Searching for the opposite of: {word}")
            fetch_opposite_word(word)
        elif 'open microsoft store' in command:
            open_microsoft_store()
        elif 'open gmail' in command:
            open_gmail()
        elif 'open vs code' in command:
            open_vscode()
        elif 'cpu usage' in command:
            check_cpu_usage()
        elif 'memory usage' in command:
            check_memory_usage()
        elif 'clear cache' in command or 'clear temp files' in command:
            clear_temp_files()
        elif 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            # New Shopping Command
        elif 'buy' in command or 'shopping' in command or 'purchase' in command:
            online_shopping()
        elif 'create note' in command:
            create_note()
        elif 'order food' in command or 'book food' in command or 'food delivery' in command:
            online_food_booking()
        elif 'fine' in command or "good" in command:
            speak("It's good to know that you're fine")
        elif 'open' in command or 'go to' in command:
            # Attempt to open the website mentioned in the command
            open_website(command)
        elif 'lock device window' in command:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif "translate" in command:
            text_to_translate = listen_command()  # Listen for text to translate
            if text_to_translate:
                translate_text(text_to_translate)
            else:
                speak("I didn't catch the text to translate.")
        else:
            handle_general_questions(command)


# Main loop to listen and respond to commands
def main():
    is_paused = False
    greet_user()
    while True:
        if not is_paused:
            speak("What would you like me to do?")
            command = listen_command()
            if command:
                if 'pause' in command:
                    is_paused = True
                    speak("Pausing the assistant. Say 'resume' to continue.")
                else:
                    perform_tasks(command)
            else:
                speak("I'm sorry, I didn't understand that.")
        else:
            command = listen_command()
            if command and 'resume' in command:
                is_paused = False
                speak("Resuming the assistant.")
# Start the assistant
if __name__ == "__main__":
    main()

