from utis import speak
def perform_math_operation(command):
    try:
        command = command.replace("calculate", "").replace("times", "").replace("multiplied by", "").strip()
        result = eval(command)  # Evaluate the math expression
        speak(f"The result is {result}.")
    except Exception as e:
        speak("Sorry, I couldn't perform that calculation.")