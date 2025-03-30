import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

print("Testing API Configuration:")
print(f"Search Engine ID: {search_engine_id}")
print(f"API Key present: {'Yes' if api_key else 'No'}")

test_url = "https://www.googleapis.com/customsearch/v1"
params = {
    'key': api_key,
    'cx': search_engine_id,
    'q': 'test',
    'num': 1
}

try:
    response = requests.get(test_url, params=params)
    print(f"\nResponse Status: {response.status_code}")
    if response.status_code == 200:
        print("✅ API configuration is working!")
    else:
        print(f"❌ Error: {response.text}")
except Exception as e:
    print(f"❌ Error: {str(e)}") 