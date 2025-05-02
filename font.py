from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)
assistant_process = None  # Global variable to store the process

# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Route to start the voice assistant
@app.route('/start_voice_assistant', methods=['POST'])
def start_voice_assistant():
    global assistant_process
    if assistant_process is None or assistant_process.poll() is not None:
        assistant_process = subprocess.Popen(['python', 'main.py'])  # Starts the voice assistant
        return 'Voice assistant started!'
    else:
        return 'Voice assistant is already running.'

# Route to stop the voice assistant
@app.route('/stop_voice_assistant', methods=['POST'])
def stop_voice_assistant():
    global assistant_process
    if assistant_process is not None and assistant_process.poll() is None:
        assistant_process.terminate()  # Attempt to stop the process
        assistant_process = None
        return 'Voice assistant stopped!'
    else:
        return 'Voice assistant is not running.'

if __name__ == '__main__':
    app.run(debug=False)
