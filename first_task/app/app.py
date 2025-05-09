from flask import Flask, request
import os

app = Flask(__name__)

LOG_DIR = '/app/logs'
LOG_FILE = os.path.join(LOG_DIR, 'app.log')

DEFAULT_PORT = 5000
DEFAULT_GREETINGS = "Welcome to the custom app\n"

open(LOG_FILE, 'a').close()

@app.route('/', methods=['GET'])
def greetings():
    return os.environ.get("APP_GREETINGS", DEFAULT_GREETINGS)

@app.route('/status', methods=['GET'])
def status():
    return {"status": "ok"}

@app.route('/log', methods=['POST'])
def add_log():
    data = request.get_json()
    if not data or 'message' not in data:
        return {"error": "Missing 'message' in request"}, 400
    with open(LOG_FILE, 'a', encoding='utf-8') as file:
        file.write(data['message'] + '\n')
    return {}

@app.route('/logs', methods=['GET'])
def get_logs():
    with open(LOG_FILE, 'r', encoding='utf-8') as file:
        logs = file.read()
    return logs

if __name__ == "__main__":
    port = int(os.environ.get("APP_PORT", DEFAULT_PORT))
    app.run(host="0.0.0.0", port=port)
