from utis import speak,listen_command
import pyautogui
import cv2
import pygetwindow as gw
import random
import os
import psutil
from datetime import datetime

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot taken and saved.")
# Window operations
def switch_window():
    windows = gw.getAllTitles()
    windows = [window for window in windows if window.strip()]  # Filter out empty window titles

    if windows:
        random_window = random.choice(windows)
        try:
            gw.getWindowsWithTitle(random_window)[0].activate()
            speak(f"Switching to {random_window}.")
        except Exception as e:
            speak(f"Could not switch to {random_window}. Error: {str(e)}")
    else:
        speak("No windows with valid titles available to switch.")
def close_window():
    window = gw.getActiveWindow()
    if window:
        window.close()
        speak("Active window closed.")
    else:
        speak("No active window to close.")


def minimize_window():
    active_window = gw.getActiveWindow()
    if active_window:
        try:
            active_window.minimize()
            speak(f"Minimizing {active_window.title}.")
        except Exception as e:
            speak(f"Could not minimize {active_window.title}. Error: {str(e)}")
    else:
        speak("No active window to minimize.")
# History management
history = []
def show_history():
    if history:
        speak("Here is your interaction history:")
        for entry in history:
            speak(entry)
    else:
        speak("No history available.")
def add_to_history(entry):
    history.append(entry)
def open_camera():
    cap = cv2.VideoCapture(0)
    speak("Opening camera.")
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Camera', frame)
        command = listen_command()
        if command and 'capture' in command:
            cv2.imwrite("captured_image.jpg", frame)
            speak("Image captured.")
        if command and 'stop' in command:
            break
    cap.release()
    cv2.destroyAllWindows()
    speak("Camera closed.")
def sleep_windows():
    speak("Putting the computer to sleep.")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
def check_cpu_usage():
    """Function to monitor CPU usage"""
    cpu_usage = psutil.cpu_percent(interval=1)
    speak(f"Current CPU usage is {cpu_usage}%.")
def check_memory_usage():
    """Function to monitor memory usage"""
    memory_info = psutil.virtual_memory()
    speak(f"Memory usage: {memory_info.percent}% of {memory_info.total / (1024 ** 3):.2f} GB.")
def clear_temp_files():
    """Function to clear temporary files on Windows"""
    temp_folder = os.getenv('TEMP')
    os.system(f'del /q/f/s {temp_folder}\\*')  # Clears temporary files
    speak("Temporary files cleared.")
def tell_time():
    time_now = datetime.now().strftime("%H:%M:%S")  # Using the `now` method of the `datetime` class
    speak(f"The current time is {time_now}.")