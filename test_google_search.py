import os
from dotenv import load_dotenv
import requests

load_dotenv()

def test_search():
    api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

    print(f"\nTesting with:")
    print(f"Search Engine ID: {search_engine_id}")
    print(f"API Key (first 8 chars): {api_key[:8]}...\n")

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': search_engine_id,
        'q': 'nike running shoes',
        'num': 1
    }

    try:
        response = requests.get(url, params=params)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if 'items' in data:
                print("\nSuccess! Found search results:")
                print(f"Title: {data['items'][0]['title']}")
                print(f"Link: {data['items'][0]['link']}")
            else:
                print("\nAPI responded but no results found")
        else:
            print(f"\nError Response: {response.text}")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_search() 