# Speak function (with print for displaying)
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
def speak(text):
    print(text)  # Display spoken text in the console
    engine.say(text)
    engine.runAndWait()
# Listen for user commands
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        speak("Listening...")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)
            command = recognizer.recognize_google(audio)
            print(f"Recognized command: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError as e:
            speak(f"Error with speech recognition service: {str(e)}")
            return None
        except Exception as e:
            speak(f"Error during listening: {str(e)}")
            return None