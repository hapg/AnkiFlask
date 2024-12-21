import requests
import random

def test_add_card():
    url = " https://9ab6-93-176-147-127.ngrok-free.app/anki_flask/add_card"
    # url = "http://localhost:443/anki_flask/add_card"
    payload = {
        "front": f"card{random.randint(0, 1000)}",
        "back": "puta"
    }
    response = requests.post(url, json=payload, verify=False)
    if response.status_code == 200:
        print("Response JSON:", response.json())
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    test_add_card()