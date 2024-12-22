import requests
import random

def add_card(front, back):
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
    response = requests.post(anki_url, json=payload, verify=False)  # Disable SSL verification
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "AnkiConnect error"}

# Example usage
deck_name = "Spanish A2"
front = f"card{random.randint}"
back = "foo"
result = add_card(front, back)
print(result)