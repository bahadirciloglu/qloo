import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
print("API_KEY:", repr(API_KEY))

def get_token():
    url = "https://streaming.assemblyai.com/v3/token"
    params = urlencode({'expires_in_seconds': 60})
    headers = {"Authorization": API_KEY}
    response = requests.get(f"{url}?{params}", headers=headers)
    print("Token response:", response.status_code, response.text)
    if response.status_code == 200:
        data = response.json()
        print("✅ Token:", data.get("token"))
        return data.get("token")
    else:
        print("❌ Could not get token!")
        return None

if __name__ == "__main__":
    get_token() 