# 📘 USER GUIDE – Chat Mistral API avec Python

Ce guide explique comment configurer et utiliser un script Python dans VS Code pour discuter avec l'API Mistral.

---

## 📁 Structure du projet

mistral_chat/
├── main.py # Script principal
├── .env # Clé API privée (non versionnée)
├── requirements.txt # Dépendances Python
└── USER_GUIDE.md # Ce guide

yaml
Copier
Modifier

---

## ✅ Étapes d’installation

### 1. Cloner ou créer le dossier

Ouvre VS Code et crée un dossier appelé `mistral_chat`.

### 2. Créer les fichiers

Crée les fichiers suivants :
- `main.py`
- `.env`
- `requirements.txt`
- `USER_GUIDE.md`

---

## 🔐 Configuration de la clé API

Ajoute ta clé API Mistral dans le fichier `.env` :

MISTRAL_API_KEY=ta_clé_api_ici

yaml
Copier
Modifier

> ⚠️ Ne jamais partager ce fichier `.env`. Ajoute-le à `.gitignore` si tu utilises Git.

---

## 📦 Installation des dépendances

1. Crée un environnement virtuel :

```bash
python -m venv venv
Active-le :

Windows :

bash
Copier
Modifier
.\venv\Scripts\activate
Mac/Linux :

bash
Copier
Modifier
source venv/bin/activate
Installe les dépendances :

bash
Copier
Modifier
pip install -r requirements.txt
▶️ Exécution du script
Lance le script principal :

bash
Copier
Modifier
python main.py
Tu pourras taper une question, et Mistral te répondra dans le terminal.

💬 Exemple d’échange
yaml
Copier
Modifier
Pose une question à Mistral : Qui est Alan Turing ?
Réponse de Mistral : Alan Turing est un mathématicien britannique considéré comme l’un des pères fondateurs de l’informatique...
🛠️ Personnalisation
Change le modèle en remplaçant "mistral-medium" par mistral-small ou mistral-large.

Modifie la temperature pour rendre les réponses plus créatives ou précises.

📌 Remarques
Nécessite Python 3.8+

Utilise l’API officielle de Mistral AI

Ne partage jamais ta clé API.

