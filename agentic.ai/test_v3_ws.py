import asyncio
import websockets
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_token():
    """Get new token from AssemblyAI"""
    url = "https://streaming.assemblyai.com/v3/token"
    params = {'expires_in_seconds': 60}
    headers = {"Authorization": f"Bearer {os.getenv('ASSEMBLYAI_API_KEY')}"}
    response = requests.get(url, params=params, headers=headers)
    print("Token response:", response.status_code, response.text)
    if response.status_code == 200:
        data = response.json()
        print("✅ Token received!")
        return data.get("token")
    else:
        print("❌ Could not get token!")
        return None

async def test_ws(token):
    ws_url = f"wss://streaming.assemblyai.com/v3/ws?sample_rate=16000&encoding=pcm_s16le&token={token}"
    print("WebSocket URL:", ws_url[:100] + "...")
    try:
        async with websockets.connect(ws_url) as ws:
            print("✅ WebSocket connection established.")
            await ws.send(bytes(1600))
            print("📤 Dummy audio packet sent.")
            try:
                response = await asyncio.wait_for(ws.recv(), timeout=5)
                print("📥 Response received:", response)
            except asyncio.TimeoutError:
                print("⚠️ No response received within 5 seconds.")
            await ws.close()
            print("🔌 WebSocket connection closed.")
    except Exception as e:
        print(f"❌ WebSocket connection failed: {e}")

if __name__ == "__main__":
    print("🔄 Getting new token...")
    token = get_token()
    if token:
        print("🚀 Starting WebSocket test...")
        asyncio.run(test_ws(token))
    else:
        print("❌ Cannot run test because token could not be obtained.") 