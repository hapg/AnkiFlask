import logging
from flask import Flask, request, jsonify
import requests

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

# Ensure Flask uses the same logging level
flask_logger = logging.getLogger('werkzeug')
flask_logger.setLevel(logging.INFO)

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/anki_flask'

# Function to add a card to Anki
def add_card_to_anki(front, back):
    anki_url = "http://localhost:8765"
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "Spanish A2",
                "modelName": "Basic",
                "fields": {
                    "Front": front,
                    "Back": back
                },
                "tags": ["SpanishTutor"]
            }
        }
    }
    response = requests.post(anki_url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "AnkiConnect error"}

# Define the /add_card endpoint
@app.route('/anki_flask/add_card', methods=['POST'])
def add_card_route():
    data = request.json
    _logger.info(f"Received payload: {data}")
    if not all(k in data for k in ("front", "back")):
        return jsonify({"error": "Invalid payload. Must include 'front', and 'back'."}), 400
    result = add_card_to_anki(data['front'], data['back'])
    _logger.info(f"AnkiConnect response: {result}")
    return jsonify(result)

@app.route('/test')
def test():
    return 'Server is running', 200

if __name__ == '__main__':
    app.run(port=443)