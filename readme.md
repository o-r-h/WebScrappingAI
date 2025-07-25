# MTW Youth Literature Scraper

Python script for scraping book data from MTW Youth literature collection using Playwright and OpenRouter API.

## Features
- Automated browser interaction with Playwright
- AI-powered HTML parsing via OpenRouter's Qwen model
- Extraction of book titles and prices in CSV format
- Error handling for robust scraping

## Installation
Install required packages:
```bash
pip install -r requirements.txt
playwright install  # Install browser dependencies
```

## Configuration
Create `.env` file with your API key:
```env
QWEN_API_KEY = "your_openrouter_api_key_here"
```

## Usage
Run the main script:
```bash
python app.py
```

## Output Format
Script outputs books in CSV format:
```
Book Title, Price
The Great Gatsby, S/. 539.78 PEN
1984, S/. 420.00 PEN
...
```

## Dependencies
See [requirements.txt](requirements.txt) for full package list

## Notes
- Keep your API key secure - never commit `.env` to version control
- The scraper runs in visible browser mode (headless=False) for debugging
- Output can be redirected to file: `python app.py > books.csv`