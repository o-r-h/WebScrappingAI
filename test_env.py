from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Print environment variables
print("Environment variables:")
print(f"QWEN_API_KEY: {'*' * (len(os.getenv('QWEN_API_KEY', '')) - 4) + os.getenv('QWEN_API_KEY', '')[-4:] if os.getenv('QWEN_API_KEY') else 'None'}")
print(f"WEB_URL: {os.getenv('WEB_URL', 'Not set')}")

# Check if python-dotenv is working
if os.getenv('QWEN_API_KEY'):
    print("python-dotenv is working correctly!")
else:
    print("python-dotenv might not be working or QWEN_API_KEY is not set in .env file")