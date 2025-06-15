import os

import requests
from dotenv import load_dotenv

# Charger la clé depuis le fichier .env
load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")

if not API_KEY:
    raise ValueError("Clé API manquante. Vérifie le fichier .env.")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

url = "https://api.mistral.ai/v1/chat/completions"

def ask_mistral(prompt):
    payload = {
        "model": "mistral-medium",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Exemple d'utilisation
question = input("Pose une question à Mistral : ")
response = ask_mistral(question)
print("\nRéponse de Mistral :", response)
