# 🔍 Passive Reconnaissance Tool

## 📌 Introduction
L'information est la clé de toute attaque ou défense en cybersécurité. L'un des premiers pas d'un pentest consiste à recueillir un maximum de renseignements sur une cible. Ce processus est connu sous le nom de **reconnaissance passive**.

Le but de cet outil est de vous aider à effectuer une collecte d'informations en utilisant des techniques OSINT (*Open Source Intelligence*). Il vous permettra d'effectuer des recherches sur :

- 📌 **Nom complet** : Recherche de l'adresse et du numéro de téléphone dans les annuaires publics et a l'aide des recherches avancées (*eg: Google Dorks*).
- 🌍 **Adresse IP** : Identification de l'ISP et de la localisation approximative et d'autre informations connexes.
- 🕵️‍♂️ **Nom d'utilisateur** : Vérification de la présence d'un compte sur plusieurs réseaux sociaux.

⚠️ **Cet outil est à des fins éducatives uniquement. Toute utilisation abusive est sous votre propre responsabilité.**

---

## 🚀 Installation et utilisation

### 📥 Prérequis
- Python 3.x
- Bibliothèques requises : `requests`, `fake_useragent`

Installez les dépendances avec :
```bash
pip install -r requirements.txt
```

### 🎯 Commandes disponibles
Affichez l'aide avec :
```bash
passive --help
```

| Option | Description |
|--------|-------------|
| `-fn`  | Recherche par **nom complet** |
| `-ip`  | Recherche par **adresse IP** |
| `-u`   | Recherche par **nom d'utilisateur** |

### 📌 Exemples d'utilisation

#### 🔎 Recherche d'un nom complet
```bash
python3 main.py -fn "Jean Dupont"
```
📌 Résultat :
```
📌 First name: Jean
📌 Last name: Dupont
📍 Address: Ottawa, ON, CA
📞 Number: (514) 381-3391

💾 Saved in result.txt
```

#### 🌍 Recherche d'une adresse IP
```bash
python3 main.py -ip 8.8.8.8
```
📌 Résultat :
```
🌐 IP Address: 8.8.8.8
🏙️ City: Ashburn
🌍 Region: Virginia
🏳️ Country: United States
🖥️ ISP: Google LLC
🧭 City Lat/Lon: (39.03)/(-77.5)

💾 Saved in result2.txt
```

#### 🕵️‍♂️ Recherche d'un nom d'utilisateur
```bash
python3 main.py -u "@jeanga7"
```
📌 Résultat :
```
🎯 Résultat pour 'jeanga7':

✅ Instagram: YES https://www.instagram.com/jeanga7
✅ GitHub: YES https://github.com/jeanga7
❌ Reddit: NO https://www.reddit.com/user/jeanga7
❌ TikTok: NO https://www.tiktok.com/@jeanga7
✅ Threads: YES https://www.threads.net/@jeanga7
❌ LinkedIn: NO https://www.linkedin.com/in/jeanga7
❌ YouTube: NO https://www.youtube.com/@jeanga7
❌ Facebook: NO (Error: No connection adapters were fo...) https://www.facebook.com/jeanga7
❌ Medium: NO https://medium.com/@jeanga7
❌ Snapchat: NO https://www.snapchat.com/add/jeanga7
❌ StackOverflow: NO https://stackoverflow.com/users/jeanga7

🔍 3 profils found.

💾 Saved in result3.txt
```
#### 🖥️ Utilisation de l'interface web

En plus des commandes en ligne, ce programme propose une **interface graphique** simple et intuitive pour effectuer vos recherches OSINT. Pour l'utiliser :

1. **Lancez l'application en mode API** :
   ```bash
   python3 main.py
   ```
   Vous verrez un message indiquant que le serveur Flask est démarré.

2. **Accédez à l'interface** :  
   Ouvrez votre navigateur et rendez-vous sur **[http://127.0.0.1:5000](http://127.0.0.1:5000)**.

3. **Effectuez une recherche** :  
   - Entrez un **nom complet**, une **adresse IP** ou un **nom d'utilisateur** dans le champ correspondant.
   - Cliquez sur **Rechercher** pour obtenir les résultats instantanément.

Cette interface facilite l'utilisation de l'outil sans passer par le terminal et permet une exploration plus fluide des résultats. 🚀

---

## 🛠️ Fonctionnalités et principes clés

### 🔍 **Reconnaissance passive vs active**
- **Passive Reconnaissance** : Aucune interaction directe avec la cible. L'outil utilise uniquement des sources publiques.
- **Active Reconnaissance** : Interaction avec la cible (ex : scan de ports, requêtes directes).

### 📡 **OSINT (Open Source Intelligence)**
L'OSINT regroupe l'ensemble des techniques permettant de collecter des informations accessibles publiquement, comme :
- Annuaires en ligne 📚
- Réseaux sociaux 📲
- Bases de données publiques 🗃️
- Whois & DNS 📌

### 🔐 **Éthique et responsabilité**
Cet outil est destiné **uniquement** à des fins éducatives et légales. L'utilisation de ces techniques sans autorisation peut enfreindre la loi.

---

## 🏆 Bonus & Améliorations
🔹 Ajout de **nouvelles API** pour plus de données 📊  
🔹 Interface web pour une utilisation simplifiée 🎨  
🔹 Système de **proxy** pour éviter d'être détecté 🛡️  

---

## 📜 Licence
Ce projet est sous licence [**AGPL**](/LICENSE). Utilisation libre mais **responsable**.

### WARNING 

⚠️ Ces méthodes et outils sont uniquement destinés à des fins éducatives, afin que vous puissiez mieux comprendre comment vous protéger contre des vulnérabilités similaires. Vous devez vous assurer que vous ne tentez aucune activité de type exploit sans l'autorisation explicite du propriétaire de la machine, du système ou de l'application. Si vous n'obtenez pas cette autorisation, vous risquez d'enfreindre la loi.
---

## 💡 Ressources utiles
- 🔗 [Liste d'outils OSINT](https://en.kali.tools/all/?category=recon)
- 📖 [OSINT sur Wikipedia](https://en.wikipedia.org/wiki/Open-source_intelligence)
- 📚 [Apprendre l'OSINT](https://github.com/topics/osint-tools)

---

🚀 **Happy Hacking & Stay Ethical!** 👨‍💻🔥

