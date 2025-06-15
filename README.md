# 📘 USER GUIDE – Chat Mistral API avec Python

Ce guide explique comment configurer et utiliser un script Python dans VS Code pour discuter avec l'API Mistral.

---

## 📁 Structure du projet

mistral_chat/
├── main.py # Script principal
├── .env # Clé API privée (non versionnée)
├── requirements.txt # Dépendances Python
└── USER_GUIDE.md # Ce guide

---

## ✅ Étapes d’installation

### 1. Cloner ou créer le dossier

Ouvre VS Code et crée un dossier appelé `mistral_chat`.

### 2. Créer les fichiers

Crée les fichiers suivants :
- `.env`

---

## 🔐 Configuration de la clé API

Ajoute ta clé API Mistral dans le fichier `.env` :

MISTRAL_API_KEY=ta_clé_api_ici

> ⚠️ Ne jamais partager ce fichier `.env`. Ajoute-le à `.gitignore` si tu utilises Git.

---

## 📦 Installation des dépendances

1. Crée un environnement virtuel :

```bash
python -m venv venv
Active-le :
.\venv\Scripts\activate

Installe les dépendances :
pip install -r requirements.txt

▶️ Exécution du script
Lance le script principal :
python main.py

Tu pourras taper une question, et Mistral te répondra dans le terminal.

🛠️ Personnalisation
Change le modèle en remplaçant "mistral-medium" par mistral-small ou mistral-large.

Modifie la temperature pour rendre les réponses plus créatives ou précises.

📌 Remarques
Nécessite Python 3.8+

Utilise l’API officielle de Mistral AI

Ne partage jamais ta clé API.

