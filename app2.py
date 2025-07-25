from playwright.sync_api import sync_playwright
import requests
import json
import os

#== CONFIGURATION ==
url = "https://openrouter.ai/api/v1/chat/completions"
api_key = os.getenv("QWEN_API_KEY", "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")

web_url = os.getenv("WEB_URL", "https://practicesoftwaretesting.com/")

#== FUNCTIONS ==
def is_even(number):
    """Returns True if the number is even."""
    return number % 2 == 0

def is_valid_url(url):
    """Returns True if the URL is a valid HTTP/HTTPS URL."""
    return url.startswith(('http://', 'https://'))

def is_positive(number):
    """Returns True if the number is positive."""
    return number > 0


#== MAIN ==
htmlblock = None
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(web_url)
    page.wait_for_timeout(5000)
    try:
         # Probar filtros   
         # Esperar a que los filtros estén cargados
        print("Probar Filtros...")
        page.wait_for_selector('[data-test^="category-"]')
    
        # Marcar solo las categorías padre usando data-test
        parent_categories = [
            'category-01K11JQZBRNV6QTAAR6HQ1Q5EX',  # Hand Tools
            'category-01K11JQZBRNV6QTAAR6HQ1Q5EY',  # Power Tools
        'category-01K11JQZBRNV6QTAAR6HQ1Q5EZ'   # Other
    ]
    
        for category in parent_categories:
            checkbox = page.locator(f'[data-test="{category}"]')
            if not checkbox.is_checked():
                checkbox.click()
    
        page.wait_for_timeout(5000)
            
        # Probar agregar un producto
        print("Probar Agregar un Producto...")
        # <div class="container"> inside have   <card>
        first_product = page.locator('.container .card').first
        first_product.click()
        #increase quantity
        page.locator('#btn-increase-quantity').click()
        page.wait_for_timeout(3000)
        #decrease quantity
        page.locator('#btn-decrease-quantity').click()
        page.wait_for_timeout(3000)
        #add to card id=btn-add-to-cart
        page.locator('#btn-add-to-cart').click()
        page.wait_for_timeout(5000)
        
      
      
    except Exception as e:
        print("Error waiting for content:", e)
    finally:
        browser.close()



