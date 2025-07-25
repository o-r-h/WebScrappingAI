from playwright.sync_api import sync_playwright
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#== CONFIGURATION ==
url_api = "https://openrouter.ai/api/v1/chat/completions"
api_key = os.getenv("QWEN_API_KEY")
web_url = os.getenv("WEB_URL")
save_file = True

#== FUNCTIONS ==

def get_data(prompt):
    response = requests.post(
        url=url_api,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://shop.mtwyouth.org/collections/literature-fiction-new",  # Optional
            "X-Title": "Book Scraper",  # Optional
        },
        data=json.dumps({
            "model": "deepseek/deepseek-chat-v3-0324:free",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an expert in HTML and CSS. "
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.1,  # Lower = more deterministic
            "max_tokens": 2000
        })
    )
    return response.json()

#== MAIN ==
htmlblock = None
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(web_url)
    page.wait_for_timeout(5000)

    # Scroll to bottom to load all books
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(6000)

    try:
        page.wait_for_selector("div.collection.page-width", state="visible", timeout=10000)
        htmlblock = page.locator("div.collection.page-width").inner_html()
    except Exception as e:
        print("Error waiting for content:", e)
    finally:
        browser.close()

if not htmlblock:
    print("Failed to retrieve page content.")
else:


# === PROMPT ENGINEERING: Clean, strict, reliable output ===
    prompt = f"""
You are given HTML from a book store. Each book is in a <li> element.
Inside each <li>, there is:
- An <a> tag containing the book title
- A <div class="price"> containing the price

Extract every book as a line in this exact format:
bookname, price

Rules:
- Do not include any text before or after the data
- No numbering, no headers, no explanations
- Preserve the exact spelling and price format (e.g., S/. 539.78 PEN)
- One book per line

Example output:
The Great Gatsby, S/. 539.78 PEN
1984, S/. 420.00 PEN

Now process this HTML:
{htmlblock}
"""

    try:
        result = get_data(prompt)
        content = result["choices"][0]["message"]["content"]
        print(content.strip())

        # Optional: Save to CSV or process further
        lines = content.strip().splitlines()
        for line in lines:
            print(line)

        #Optional: Save to file
        if save_file:
            with open("extracted_books.txt", "w") as f:
                f.write(content.strip())   

    except KeyError:
        print("Error: Unexpected response format from API")
        print(result)
    except Exception as e:
        print("Error processing AI response:", e)
    
    
        

   

    
   
    