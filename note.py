from utis import speak,listen_command
def create_note():
    # Gather information for the note
    speak("Please tell me the date for the note.")
    date = listen_command()  # Get the date from the user
    speak("What is the title of the note?")
    title = listen_command()  # Get the title from the user
    speak("What is the main idea of the note?")
    main_idea = listen_command()  # Get the main idea from the user
    # Gather key points
    key_points = []
    speak("Please tell me the key points one by one. Say 'stop' when finished.")
    while True:
        point = listen_command()
        if point:
            if 'stop' in point.lower():
                break  # Exit the loop if "stop" is mentioned
            else:
                key_points.append(point)
                speak("Got it. Do you have another key point?")
        else:
            speak("I didn't catch that. Please say again.")

    # Gather action items
    action_items = []
    speak("Please tell me the action items one by one. Say 'stop' when finished.")
    while True:
        item = listen_command()
        if item:
            if 'stop' in item.lower():
                break  # Exit the loop if "stop" is mentioned
            else:
                action_items.append(item)
                speak("Got it. Do you have another action item?")
        else:
            speak("I didn't catch that. Please say again.")
    # Gather additional thoughts
    speak("Do you have any additional thoughts?")
    additional_thoughts = listen_command()  # Get additional thoughts
    # Create a formatted note
    note_content = f"""\
### Note

Date: {date}

Title: {title}

Content:
- Main Idea: {main_idea}
- Key Points:
  - {'\n  - '.join(key_points) if key_points else 'None'}
- Action Items:
  - {'\n  - '.join(action_items) if action_items else 'None'}

Additional Thoughts:
- {additional_thoughts if additional_thoughts else 'None'}
"""

    # Save the note to a text file
    filename = f"{title.replace(' ', '_')}_note.txt"
    with open(filename, "w") as file:
        file.write(note_content)
    speak(f"Note saved as {filename}.")
