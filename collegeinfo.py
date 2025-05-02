import wikipedia
from utis import speak


def get_college_info(college_name):
    try:
        if not college_name:
            speak("Please provide a valid college name.")
            return

        # Search for the college on Wikipedia
        search_result = wikipedia.search(college_name, results=1)
        if not search_result:
            speak(f"Sorry, I couldn't find any information about {college_name} on Wikipedia.")
            return

        # Get the first search result's page
        page = wikipedia.page(search_result[0])

        # Fetch the summary of the page
        summary = page.summary
        speak(summary)

    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"There are multiple results for '{college_name}'. Please be more specific.")
    except wikipedia.exceptions.HTTPTimeoutError as e:
        speak("Sorry, there was a timeout while fetching information.")
    except wikipedia.exceptions.RequestError as e:
        speak("There was an error with the request. Please try again later.")
    except wikipedia.exceptions.WikipediaException as e:
        speak(f"Wikipedia error: {str(e)}")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")
