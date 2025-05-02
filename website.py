import os
import re
from utis import speak, listen_command
import webbrowser


def open_website(command):
    # Match any URL pattern or direct website names
    url_match = re.search(r'(https?://[^\s]+|www\.[^\s]+|[a-zA-Z0-9-]+\.com|[a-zA-Z0-9-]+\.org|[a-zA-Z0-9-]+\.net)',
                          command)

    if url_match:
        # If there's a URL pattern, open it directly
        url = url_match.group(0)
        if not url.startswith("http"):
            url = "https://" + url  # Ensure the URL is properly formatted
        webbrowser.open(url)
        speak(f"Opening {url} now.")
        return True
    else:
        # If no URL found, treat the rest of the command as a search term
        search_query = command.replace("open", "").strip()
        if search_query:
            # Use Google Search as fallback for undefined sites
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Searching for {search_query}.")
            return True

    # In case no recognizable website was found
    speak("Sorry, I couldn't recognize the website you mentioned.")
    return False


def online_shopping():
    try:
        speak("Which product would you like to search for?")
        product = listen_command()
        if product:
            # You can add multiple shopping websites, but we'll use Amazon as an example.
            webbrowser.open(f'https://www.amazon.com/s?k={product}')
            speak(f"Searching for {product} on Amazon.")
        else:
            speak("Sorry, I didn't catch the product name.")
    except Exception as e:
        speak(f"Error while searching for a product: {str(e)}")

def open_whatsapp():
    webbrowser.open('https://web.whatsapp.com/')
    speak("Opening WhatsApp Web.")
def open_gmail():
    """Function to open Gmail"""
    webbrowser.open('https://mail.google.com/')
    speak("Opening Gmail.")
def open_microsoft_store():
    """Function to open Microsoft Store"""
    os.system("start ms-windows-store://home")
def open_vscode():
    """Function to open VS Code"""
    os.system("code")  # Make sure 'code' is added to the system's PATH
def open_google_maps(location):
    webbrowser.open(f'https://www.google.com/maps/place/{location}')
    speak(f"Opening Google Maps for {location}.")
