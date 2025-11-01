# 🕒 Time Agent - Agent Horaire Intelligent

Un agent développé avec Google ADK qui fournit l'heure actuelle pour différentes villes à travers le monde.


## 📁 Structure du Projet

```
my_agent/
├── .env                    # Variables d'environnement (clé API)
├── .env.example           # Exemple de fichier d'environnement
├── .gitignore            # Fichiers à ignorer par Git
└── agent.py              # Code principal de l'agent
```

## 🚀 Fonctionnalités

- ✅ Obtenir l'heure actuelle pour Abidjan
- 🌐 Prise en charge des fuseaux horaires IANA
- 🕒 Format d'heure clair et lisible
- 🔧 Architecture extensible pour ajouter d'autres villes
- 🤖 Piloté par le modèle Gemini 2.0 Flash de Google

## 🛠️ Installation & Configuration

### Prérequis

- Python 3.9 ou supérieur
- Clé API Google AI Studio

### 1. Configuration de l'Environnement

```bash
# Créer un environnement virtuel
python -m venv .venv

# Activer l'environnement
# macOS/Linux :
source .venv/bin/activate
# Windows :
.venv\Scripts\activate
```

### 2. Installation des Dépendances

```bash
# Installer Google ADK
pip install google-adk
```

### 3. Configuration de la Clé API

**Éditez le fichier `.env` :**

```bash
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=votre_cle_api_google_ici
```

**Ou copiez depuis le fichier exemple :**

```bash
cp .env.example .env
# Puis éditez .env avec votre vraie clé API
```

### Contenu de `.env.example` :

```bash
# Configuration pour Google AI Studio
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=votre_cle_api_google_ici

# Alternative: Configuration pour Vertex AI
# GOOGLE_GENAI_USE_VERTEXAI=TRUE
# GOOGLE_CLOUD_PROJECT=votre-project-id
```

## 📋 Code de l'Agent

### `agent.py`

```python
import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_current_time(city: str) -> dict:
    """Retourne l'heure actuelle d'une ville donnée."""
    if city.lower() == "abidjan":
        tz_identifier = "Africa/Abidjan"
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have timezone info for {city}."
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    return {"status": "success", "report": report}

root_agent = Agent(
    name="time_agent",
    model="gemini-2.0-flash",
    description="Agent qui répond aux questions d'heure locale.",
    instruction="Tu es un agent utile qui donne l'heure d'une ville.",
    tools=[get_current_time],
)
```

## 🎯 Utilisation

### Lancer l'Interface de Développement

```bash
# Se placer dans le dossier contenant my_agent/
cd /chemin/vers/le/dossier/parent

# Lancer l'interface web ADK
adk web
```

Ouvrez ensuite http://localhost:8000 dans votre navigateur.

### Dans l'Interface Web :

1. **Sélectionnez votre agent** : "time_agent" dans le menu déroulant
2. **Posez des questions** comme :
   - "Quelle heure est-il à Abidjan ?"
   - "Donne-moi l'heure actuelle à Abidjan"
   - "Time in Abidjan"

### Autres Modes d'Exécution

```bash
# Mode terminal
adk run

# Serveur API
adk api_server
```

## 🔧 Extension du Projet

### Ajouter une Nouvelle Ville

Modifiez la fonction `get_current_time` dans `agent.py` :

```python
def get_current_time(city: str) -> dict:
    """Retourne l'heure actuelle d'une ville donnée."""
    city_timezones = {
        "abidjan": "Africa/Abidjan",
        "paris": "Europe/Paris", 
        "new york": "America/New_York",
        "tokyo": "Asia/Tokyo",
        "london": "Europe/London"
    }
    
    if city.lower() in city_timezones:
        tz_identifier = city_timezones[city.lower()]
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have timezone info for {city}."
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    return {"status": "success", "report": report}
```

### Ajouter d'autres Outils

```python
def get_weather(city: str) -> dict:
    """Récupère la météo pour une ville (exemple)."""
    if city.lower() == "abidjan":
        return {
            "status": "success",
            "report": "The weather in Abidjan is sunny, 28°C"
        }
    else:
        return {
            "status": "error", 
            "error_message": f"Weather info not available for {city}"
        }

# Mettez à jour l'agent avec le nouvel outil
root_agent = Agent(
    name="time_agent",
    model="gemini-2.0-flash",
    description="Agent qui répond aux questions d'heure et météo.",
    instruction="Tu es un agent utile qui donne l'heure et la météo des villes.",
    tools=[get_current_time, get_weather],
)
```

## 🐛 Dépannage

### Problèmes Fréquents

**Agent non visible dans l'interface :**
- Vérifiez que vous exécutez `adk web` depuis le dossier parent de `my_agent`
- Vérifiez que tous les fichiers sont correctement nommés

**Erreurs d'authentification :**
- Vérifiez votre clé API dans le fichier `.env`
- Assurez-vous que `GOOGLE_GENAI_USE_VERTEXAI=FALSE`

**Problèmes sur Windows :**
```bash
adk web --no-reload
```

**Import errors :**
- Vérifiez que Google ADK est installé : `pip list | grep google-adk`
- Vérifiez la version de Python : `python --version`

### Fichier `.gitignore` Recommandé

Votre `.gitignore` devrait inclure :

```gitignore
# Environnements virtuels
.venv/
venv/
env/

# Fichiers d'environnement
.env
*.env

# Cache Python
__pycache__/
*.pyc

# Logs
*.log

# IDE
.vscode/
.idea/
```

## 📊 Monitoring et Debug

### Inspection des Appels

Dans l'interface web ADK :
- **Onglet "Events"** : Voir les appels de fonction détaillés
- **Onglet "Trace"** : Analyser les performances et la latence
- **Console** : Logs détaillés des exécutions

### Logs Avancés

Ajoutez du logging dans votre code :

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_current_time(city: str) -> dict:
    logger.info(f"Demande d'heure pour la ville : {city}")
    # ... reste du code
```

## 🚀 Déploiement

### Préparation pour la Production

1. **Sécurisez les variables d'environnement**
2. **Utilisez Vertex AI** pour les déploiements production :
   ```bash
   GOOGLE_GENAI_USE_VERTEXAI=TRUE
   GOOGLE_CLOUD_PROJECT=votre-project-id
   ```
3. **Authentifiez avec gcloud** :
   ```bash
   gcloud auth application-default login
   ```

## 📝 Exemples d'Interaction

### Questions Supportées
- "Quelle heure est-il à Abidjan ?"
- "Peux-tu me donner l'heure à Abidjan ?"
- "Time in Abidjan"
- "Current time Abidjan"

### Réponses Attendues
```
"The current time in Abidjan is 2024-01-15 14:30:25 GMT+0000"
```

## 🔮 Améliorations Futures

- [ ] Ajouter plus de villes mondiales
- [ ] Support des conversions de fuseaux horaires  
- [ ] Intégration météo
- [ ] Commandes vocales avec Gemini Live API
- [ ] Interface web personnalisée

---

**Développé par Toure Souleymane**  
*#your_automation_guy* - Spécialiste en automatisation intelligente  
📧 GitHub : [toure5013](https://github.com/toure5013)