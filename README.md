# 🧠 Guide d’utilisation de Mistral avec VS Code

Ce guide couvre deux façons d’utiliser l’API Mistral :
- Avec l’extension **Continue** pour une intégration dans VS Code
- Avec un simple **script Python**, sans extension

---

## ✅ 1. Utilisation avec l’extension Continue (VS Code ou JetBrains)

### 📦 Étapes :

1️⃣ **Créer une clé API Mistral**  
👉 https://console.mistral.ai  
> Copiez la clé générée (attention : ne jamais la partager)

2️⃣ **Installer l’extension Continue**  
- VS Code : via Marketplace → *Continue*  
- IntelliJ/WebStorm : Plugins → *Continue*

🔗 https://www.continue.dev/

3️⃣ **Configurer Mistral dans `.continue/config.json`**

```json
{
  "models": [
    {
      "title": "💬 Mistral Large",
      "provider": "mistral",
      "model": "mistral-large-latest",
      "apiKey": "<VOTRE_CLE_API>"
    }
  ],
  "tabAutocompleteModel": {
    "title": "⚡ Codestral",
    "provider": "mistral",
    "model": "codestral-latest",
    "apiBase": "https://codestral.mistral.ai/v1"
  },
  "embeddingsProvider": {
    "provider": "mistral",
    "model": "mistral-embed",
    "apiKey": "<VOTRE_CLE_API>",
    "apiBase": "https://api.mistral.ai/v1"
  }
}
4️⃣ Lancer Continue

Raccourci : Ctrl+I / Cmd+I

Profitez du chat, de l’autocomplétion et des embeddings avec Mistral

🐍 2. Utilisation avec un script Python (sans extension)
📁 Structure du projet
bash
Copier
Modifier
mistral_chat/
├── main.py
├── .env
├── requirements.txt
📄 .env
env
Copier
Modifier
MISTRAL_API_KEY=ta_clé_api_ici
📄 requirements.txt
txt
Copier
Modifier
requests
python-dotenv
📄 main.py
python
Copier
Modifier
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

url = "https://api.mistral.ai/v1/chat/completions"

def ask_mistral(prompt):
    payload = {
        "model": "mistral-large-latest",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]

question = input("Pose une question à Mistral : ")
print("Réponse :", ask_mistral(question))
▶️ Lancer le script
bash
Copier
Modifier
python -m venv venv
source venv/bin/activate      # ou .\venv\Scripts\activate sur Windows
pip install -r requirements.txt
python main.py
🛡️ Bonnes pratiques
Ne jamais partager .env ni vos clés API

Ajouter .env dans .gitignore

Séparer les clés de prod/test si besoin

📚 Ressources
Mistral AI – Docs

Continue – Docs
