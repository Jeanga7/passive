import sys
from googlesearch import search
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def search_full_name(full_name):
    query = f'"{full_name}" address phone'
    search_results = search(query, num_results=5)
    
    address = "Address not found"
    phone = "Number not found"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    session = requests.Session()
    
    for result in search_results:
        try:
            response = session.get(result, headers=headers, timeout=10)
            print(f"result {result}")
            
            if response.status_code == 403:
                print(f"❌ Access forbidden (403) for {result}. Trying with different headers...")
                headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
                response = session.get(result, headers=headers, timeout=10)
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            if "rocketreach.co" in result:
                address_tag = soup.select_one(".history p")
                phone_tags = soup.select(".teaser.revealed a")
            
            elif "taksainvestment.com" in result:
                address_tag = soup.select_one(".ai-font-location-c p")
                phone_tag = soup.select_one(".aios-ai-phone")

            elif "remax.com" in result:
                address_tag = soup.select_one(".d-address-link p, .d-text.d-header-office-address p")
                phone_tag = soup.select(".d-text.d-bio-phone-numbers p")
                if phone_tag:
                    phone = ", ".join([tag.text.strip() for tag in phone_tags])
            else:
                address_tag = soup.select_one(".bi-address")
                phone_tag = soup.select_one(".bi-phone")
            
            if address == "Address not found" and address_tag:
                address = address_tag.text.strip()
            
            if phone == "Number not found" and phone_tag:
                phone = phone_tag.text.strip()
            
            if address != "Address not found" and phone != "Number not found":
                break
        except requests.exceptions.RequestException as e:
            print(f"❌ Error retrieving data from {result}: {e}")
            continue
    
    result = (
        f"📌 First name: {' '.join(full_name.split()[:-1])}\n"
        f"📌 Last name: {full_name.split()[-1]}\n"
        f"📍 Address: {address}\n"
        f"📞 Number: {phone}\n"
    )

    with open("result.txt", "w", encoding="utf-8") as file:
        file.write(result)

    print(result)
    print("💾 Saved in result.txt")



def fetch_dynamic_page(url, address_selectors, phone_selectors):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    address, phone = "Address not found", "Number not found"

    try:
        driver.get(url)
        time.sleep(5)  # Attendre que la page se charge

        # 🔎 Chercher l'adresse en testant plusieurs classes
        for selector in address_selectors:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            if elements:
                address = elements[0].text.strip()
                break  # On arrête dès qu'on trouve une valeur

        # 🔎 Chercher le téléphone en testant plusieurs classes
        for selector in phone_selectors:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            if elements:
                phone = elements[0].text.strip()
                break  # On arrête dès qu'on trouve une valeur

    except Exception as e:
        print(f"❌ Error retrieving dynamic content from {url}: {e}")
    finally:
        driver.quit()

    return address, phone