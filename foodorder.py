# Online food booking
from utis import listen_command, speak
import webbrowser
from food_utils import online_food_booking


def online_food_booking():
    try:
        speak("Which food delivery service would you like to use? You can choose from Uber Eats, DoorDash, or Grubhub.")
        service = listen_command()

        if service:
            if 'uber eats' in service.lower():
                webbrowser.open('https://www.ubereats.com/')
                speak("Opening Uber Eats.")
            elif 'doordash' in service.lower():
                webbrowser.open('https://www.doordash.com/')
                speak("Opening DoorDash.")
            elif 'grubhub' in service.lower():
                webbrowser.open('https://www.grubhub.com/')
                speak("Opening Grubhub.")
            else:
                speak(
                    f"Sorry, I don't have information about {service}. Please try one of Uber Eats, DoorDash, or Grubhub.")
        else:
            speak("I didn't catch the service name. Please say it again.")
    except Exception as e:
        speak(f"An error occurred while trying to book food: {str(e)}")