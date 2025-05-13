from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from utils.utils import get_random_user_agent
import time

def fetch_dynamic_data(url, mode="default"):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument(f'user-agent={get_random_user_agent()}')
    
    # chrome_options.binary_location = "/snap/bin/chromium"

    result = {"address": "Address not found", "phone": "Phone not found", "status": "unknown"}
    
    try:
        #service = Service(ChromeDriverManager().install())
        #driver = webdriver.Chrome(service=service, options=chrome_options)

        service = Service(ChromeDriverManager(chrome_type="chromium").install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.set_page_load_timeout(30)
        
        driver.get(url)
        
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)
        
        if mode == "instagram" or mode == "threads":
            try:
                spans = driver.find_elements(By.TAG_NAME, "span")
                for span in spans:
                    if "Sorry, this page isn't available" in span.text:
                        result["status"] = "not found"
                        break
            except Exception as e:
                print(f"Erreur lors de la vérification d'Instagram: {str(e)}")
        elif mode == "tiktok":
            try:
                spans = driver.find_elements(By.TAG_NAME, "p")
                for span in spans:
                    if "Couldn't find this account" in span.text:
                        result["status"] = "not found"
                        break
            except Exception as e:
                print(f"Erreur lors de la vérification de TikTok: {str(e)}")
        else:
            selectors = {
                "address": [
                    ".d-address-link p", 
                    ".contact-address", 
                    ".address", 
                    "[itemprop='address']", 
                    ".d-text.d-header-office-address p",
                    ".location-text",
                    ".vcard-detail [itemprop='homeLocation'] span",
                    "span.address",
                    ".contact-info .location"
                ],
                "phone": [
                    ".contact-phone", 
                    ".phone", 
                    "[itemprop='telephone']", 
                    "a[href^='tel:']",
                    ".phone-number",
                    "span[data-phone]"
                ]
            }
            for key, paths in selectors.items():
                for path in paths:
                    try:
                        elements = driver.find_elements(By.CSS_SELECTOR, path)
                        if elements and elements[0].text.strip():
                            result[key] = elements[0].text.strip()
                            break
                    except Exception as e:
                        print(f"Erreur avec le sélecteur {path}: {str(e)}")
                        continue
        
        if result["address"] == "Address not found":
            try:
                address_keywords = ["avenue", "street", "boulevard", "road", "ave", "st", "blvd", "rd", 
                                   "suite", "apt", "apartment", "floor"]
                
                paragraphs = driver.find_elements(By.TAG_NAME, "p")
                spans = driver.find_elements(By.TAG_NAME, "span")
                divs = driver.find_elements(By.TAG_NAME, "div")
                
                for element in paragraphs + spans + divs:
                    text = element.text.lower()
                    if any(keyword in text for keyword in address_keywords):
                        result["address"] = element.text.strip()
                        break
            except:
                pass
                
    except Exception as e:
        print(f"❌ Error retrieving dynamic data from {url}: {str(e)}")
    finally:
        try:
            driver.quit()
        except:
            pass
            
    return result