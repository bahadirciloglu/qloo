#!/usr/bin/env python3
"""
Gemini API Test Script
======================

This script tests the Gemini 2.0 Flash API.
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def test_gemini_api():
    """Test Gemini API"""
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY not found!")
        return False
    
    print("🧪 Gemini 2.0 Flash API Test")
    print("=" * 40)
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    
    headers = {
        'Content-Type': 'application/json',
        'X-goog-api-key': api_key
    }
    
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "Hello! You are a hotel concierge. How do you help guests? Give a short response."
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 200
        }
    }
    
    try:
        print("📡 Sending API request...")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        
        print("✅ API response received!")
        print(f"📊 Status Code: {response.status_code}")
        
        # Extract response
        if 'candidates' in result and len(result['candidates']) > 0:
            content = result['candidates'][0]['content']
            if 'parts' in content and len(content['parts']) > 0:
                text = content['parts'][0]['text']
                print(f"🤖 AI Response: {text}")
                return True
        
        print("❌ Response format is different than expected")
        print(f"📄 Full response: {json.dumps(result, indent=2)}")
        return False
        
    except requests.exceptions.RequestException as e:
        print(f"❌ API error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_concierge_integration():
    """Test concierge integration"""
    
    print("\n🏨 Concierge Integration Test")
    print("=" * 40)
    
    try:
        from app.core.concierge import AIConcierge
        from app.config import settings
        
        print("🔧 Starting Concierge...")
        concierge = AIConcierge(settings)
        
        print("💬 Sending test message...")
        response = asyncio.run(concierge.process_guest_request(
            guest_id="test_guest",
            message="Hello, can I get information about the hotel?"
        ))
        
        print(f"✅ Concierge response: {response[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ Concierge error: {e}")
        return False

if __name__ == "__main__":
    import asyncio
    
    # Gemini API test
    gemini_success = test_gemini_api()
    
    # Concierge integration test
    concierge_success = test_concierge_integration()
    
    print("\n" + "=" * 40)
    print("📊 Test Results:")
    print(f"   Gemini API: {'✅ Successful' if gemini_success else '❌ Failed'}")
    print(f"   Concierge: {'✅ Successful' if concierge_success else '❌ Failed'}")
    
    if gemini_success and concierge_success:
        print("\n🎉 All tests successful! System is ready.")
    else:
        print("\n⚠️  Some tests failed. Please check.") 