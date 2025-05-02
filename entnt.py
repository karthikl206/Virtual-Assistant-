from utis import speak,listen_command
import feedparser
import pywhatkit as kit
import pyjokes

# Fetch and Read News
def fetch_news():
    feed_url = "http://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(feed_url)
    if feed.entries:
        speak("Here are the top 5 news headlines.")
        for entry in feed.entries[:5]:
            title = entry.title
            summary = entry.summary
            speak(f"Title: {title}. Summary: {summary}")
            command = listen_command()
            if command and 'end' in command:
                speak("Stopping the news reading.")
                break
    else:
        speak("Sorry, no news is available at the moment.")

        # Play music using PyWhatKit
def play_music(song_name):
    speak(f"Playing {song_name}.")
    kit.playonyt(song_name)
def send_whatsapp_message(phone_number, message):
    kit.sendwhatmsg_instantly(phone_number, message)
    speak(f"Sending your message to {phone_number}.")
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)