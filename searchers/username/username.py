from bs4 import BeautifulSoup
import requests
import time

from searchers.full_name.dynamic_scraper import fetch_dynamic_data
from utils.utils import get_session

SOCIAL_NETWORKS = {
    "Instagram": {
        "url": "https://www.instagram.com/{}",
        "verification": lambda r: not verify_instagram(r)
    },
    "GitHub": {
        "url": "https://github.com/{}",
        "verification": lambda r: not "Not Found" in r.text
    },
    "Reddit": {
        "url": "https://www.reddit.com/user/{}",
        "verification": lambda r: not "Sorry, nobody on Reddit goes by that name" in r.text
    },
    "TikTok": {
        "url": "https://www.tiktok.com/@{}",
        "verification": lambda r: not verify_tiktok(r)
    },
    "Threads": {
        "url": "https://www.threads.net/@{}",
        "verification": lambda r: not verify_threads(r)
    },
    "LinkedIn": {
        "url": "https://www.linkedin.com/in/{}",
        "verification": lambda r: not ("Page not found" in r.text or "profile you're looking for isn't available" in r.text)
    },
    "YouTube": {
        "url": "https://www.youtube.com/@{}",
        "verification": lambda r: not "This page isn't available" in r.text
    },
    "Facebook": {
        "url": "https://www.facebook.com/{}",
        "verification": lambda r: not ("Page not found" in r.text or "Cette page n'est pas disponible" in r.text)
    },
    "Medium": {
        "url": "https://medium.com/@{}",
        "verification": lambda r: "404" not in r.text
    },
    "Snapchat": {
        "url": "https://www.snapchat.com/add/{}",
        "verification": lambda r: "snapcode-img" in r.text
    },
    "StackOverflow": {
        "url": "https://stackoverflow.com/users/{}",
        "verification": lambda r: not "Page not found" in r.text
    }
}

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def verify_instagram(url):
    response = fetch_dynamic_data(url, mode="instagram")
    return response["status"] == "not found"

def verify_threads(url):
    response = fetch_dynamic_data(url, mode="threads")
    return response["status"] == "not found"

def verify_tiktok(url):
    response = fetch_dynamic_data(url, mode="tiktok")
    return response["status"] == "not found"

def search_username(username):
    """Recherche un username sur plusieurs réseaux sociaux"""

    found_networks = []
    session = get_session()
    
    for platform, info in SOCIAL_NETWORKS.items():
        profile_url = info["url"].format(username)
        verification_func = info["verification"]
        
        try:
            print(f"🔍 Analyse de {platform}...", end="\r")

            time.sleep(1)
            response = session.get(profile_url, timeout=10)
            
            if 'instagram' in profile_url:
                exists = verification_func(profile_url)
            elif 'threads' in profile_url:
                exists = verification_func(profile_url)
            elif 'tiktok' in profile_url:
                exists = verification_func(profile_url)
            else:
                response = session.get(profile_url, timeout=10)
                exists = response.status_code == 200 and verification_func(response)
                
            if exists:
                found_networks.append(f"✅ {platform}: {GREEN}YES{RESET} {profile_url}")
            else:
                found_networks.append(f"❌ {platform}: {RED}NO{RESET} {profile_url}")
                
        except requests.RequestException as e:
            found_networks.append(f"❌ {platform}: {RED}NO (Error: {str(e)[:30]}...){RESET} {profile_url}")
    
    result_message = f"\n🎯 Résultat pour '{username}':\n\n"
    result_message += "\n".join(found_networks)
    result_message += f"\n\n🔍 {len([n for n in found_networks if '✅' in n])} profils found.\n"
    
    return result_message


