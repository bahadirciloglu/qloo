#!/usr/bin/env python3
"""
Test Gemini 2.0 Flash API and Concierge Integration
===================================================

This test validates the Gemini 2.0 Flash API integration with the Concierge.
"""

import os
import sys
import asyncio
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.llm.gemini_wrapper import GeminiWrapper
from app.config import settings

async def test_gemini_api():
    """Test Gemini API integration"""
    print("🧪 Testing OpenRouter Gemini API Integration...")
    
    # Check API key
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ OPENROUTER_API_KEY not found!")
        return False
    
    print(f"✅ API Key found: {api_key[:20]}...")
    
    # Initialize wrapper
    wrapper = GeminiWrapper(settings)
    
    # Test prompt
    test_prompt = "Hello! Can you tell me about Istanbul in 2 sentences?"
    
    print(f"📝 Test prompt: {test_prompt}")
    
    try:
        # Test async generation
        response = await wrapper.generate_content(test_prompt)
        print(f"🤖 Response: {response}")
        
        if "API error" in response:
            print("❌ API error occurred")
            return False
        
        print("✅ OpenRouter Gemini API test successful!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

async def test_concierge_integration():
    """Test Concierge integration with Gemini"""
    print("\n🏨 Testing Concierge Integration...")
    
    try:
        from app.core.concierge import AIConcierge
        
        # Initialize concierge
        concierge = AIConcierge(settings)
        
        # Test message
        test_message = "Can you recommend a good restaurant in Istanbul?"
        
        print(f"💬 Test message: {test_message}")
        
        # Process request
        response = await concierge.process_chat_request("test_guest", test_message)
        
        print(f"🎹 Concierge response: {response[:200]}...")
        
        if "API error" in response:
            print("❌ Concierge API error")
            return False
        
        print("✅ Concierge integration test successful!")
        return True
        
    except Exception as e:
        print(f"❌ Concierge error: {e}")
        return False

async def main():
    """Main test function"""
    print("🚀 Starting OpenRouter Gemini Integration Tests...\n")
    
    # Test 1: Direct API
    api_success = await test_gemini_api()
    
    # Test 2: Concierge Integration
    concierge_success = await test_concierge_integration()
    
    # Results
    print("\n📊 Test Results:")
    print(f"   API Test: {'✅ PASS' if api_success else '❌ FAIL'}")
    print(f"   Concierge Test: {'✅ PASS' if concierge_success else '❌ FAIL'}")
    
    if api_success and concierge_success:
        print("\n🎉 All tests passed!")
        return True
    else:
        print("\n⚠️ Some tests failed!")
        return False

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1) 