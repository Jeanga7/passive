from googlesearch import search
import random
import time
from .scraper import fetch_static_data
from .dynamic_scraper import fetch_dynamic_data
from utils.utils import get_session

def search_full_name(full_name):
    query = f'"{full_name}" address phone'
    search_results = list(search(query, num_results=10))
    
    address = "Address not found"
    phone = "Number not found"

    session = get_session()
    
    dynamic_sites = ['remax.com', 'realtor.com', 'zillow.com', 'trulia.com', 'homes.com']
    
    for result in search_results:
        print(f"Analyzing {result}")
        
        use_selenium = any(site in result for site in dynamic_sites)
        
        if use_selenium:
            data = fetch_dynamic_data(result)
        else:
            time.sleep(random.uniform(1, 3))
            data = fetch_static_data(result, session)
        
        if data.get('address'):
            address = data['address']
        if data.get('phone'):
            phone = data['phone']
        
        if address != "Address not found" and phone != "Number not found":
            break
    
    result_text = (
        f"📌 First name: {' '.join(full_name.split()[:-1])}\n"
        f"📌 Last name: {full_name.split()[-1]}\n"
        f"📍 Address: {address}\n"
        f"📞 Number: {phone}\n"
    )
    
    with open("result.txt", "w", encoding="utf-8") as file:
        file.write(result_text)
    
    print("💾 Saved in result.txt")
    return result_text
