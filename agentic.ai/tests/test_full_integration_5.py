#!/usr/bin/env python3
"""
5. Full Integration Test
User Question → LLM Intent Analysis → API Call → Response Generation
"""

import asyncio
import json
import sys
import os

# Add app path
app_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(app_path)

from app.core.agent.concierge_agent import LLMCentricConciergeAgent
from app.config import settings

async def test_full_integration():
    """Full integration test - From user question to response"""
    print("5️⃣ Full Integration Test")
    print("=" * 60)
    print("User Question → LLM Intent → API Call → Response")
    print("=" * 60)
    
    try:
        # Initialize Concierge Agent
        print("🔧 Starting Concierge Agent...")
        agent = LLMCentricConciergeAgent(settings)
        print("✅ Agent started successfully")
        
        # Test user questions
        test_questions = [
            {
                "question": "Can I get a Turkish restaurant recommendation in Istanbul?",
                "expected_intent": "restaurant_recommendation",
                "expected_location": "Istanbul"
            },
            {
                "question": "I want to see museums and historical places",
                "expected_intent": "activity_recommendation", 
                "expected_location": "Istanbul"
            },
            {
                "question": "Can I get information about the hotel?",
                "expected_intent": "hotel_info",
                "expected_location": None
            },
            {
                "question": "What can I do in Ankara?",
                "expected_intent": "activity_recommendation",
                "expected_location": "Ankara"
            },
            {
                "question": "Restaurant recommendation in Izmir",
                "expected_intent": "restaurant_recommendation",
                "expected_location": "Izmir"
            }
        ]
        
        for i, test_case in enumerate(test_questions, 1):
            print(f"\n📝 Test {i}: {test_case['question']}")
            print("-" * 50)
            
            # 1. Process user question
            print("🤖 Starting LLM Intent Analysis...")
            response = await agent.process_request(test_case['question'])
            
            print(f"💬 AI Response:")
            print(f"   {response}")
            
            # 2. Check response quality
            print(f"\n📊 Response Analysis:")
            
            # Response length check
            if len(response) > 50:
                print("   ✅ Response is detailed enough")
            else:
                print("   ⚠️ Response is too short")
            
            # Response content check
            if "restaurant" in test_case['question'].lower() and "restaurant" in response.lower():
                print("   ✅ Restaurant topic is in response")
            elif "museum" in test_case['question'].lower() and ("museum" in response.lower() or "activity" in response.lower()):
                print("   ✅ Activity topic is in response")
            elif "hotel" in test_case['question'].lower() and ("hotel" in response.lower() or "hotel" in response.lower()):
                print("   ✅ Hotel topic is in response")
            else:
                print("   ⚠️ Response doesn't fully match the topic")
            
            # Location check
            if test_case['expected_location'] and test_case['expected_location'].lower() in response.lower():
                print(f"   ✅ {test_case['expected_location']} location is in response")
            elif test_case['expected_location']:
                print(f"   ⚠️ {test_case['expected_location']} location is not in response")
            
            print()
        
        print("✅ Full integration test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Test error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_detailed_integration():
    """Detailed integration test - Show each step"""
    print("\n🔬 Detailed Integration Test")
    print("=" * 60)
    
    try:
        agent = LLMCentricConciergeAgent(settings)
        
        # Detailed analysis with a single test question
        test_question = "Can I get a Turkish restaurant recommendation in Istanbul?"
        
        print(f"📝 Test Question: {test_question}")
        print("-" * 50)
        
        # 1. Intent Analysis
        print("🔍 Step 1: Intent Analysis")
        intent = await agent.intent_analyzer.analyze_intent(test_question)
        print(f"   Intent: {intent.get('intent', 'Unknown')}")
        print(f"   Entities: {intent.get('entities', {})}")
        print(f"   API Calls: {len(intent.get('api_calls_needed', []))}")
        
        # 2. API Calls
        print("\n📡 Step 2: API Calls")
        api_results = await agent.api_executor.execute_api_calls(
            intent.get('api_calls_needed', [])
        )
        print(f"   API Results: {len(api_results)} items")
        for api_name, result in api_results.items():
            success = result.get('success', False)
            data_count = len(result.get('data', []))
            print(f"   - {api_name}: {'✅' if success else '❌'} ({data_count} results)")
        
        # 3. Response Generation
        print("\n💬 Step 3: Response Generation")
        response = await agent.response_generator.generate_response(
            test_question, api_results, intent
        )
        print(f"   Response: {response[:200]}...")
        
        print("\n✅ Detailed integration test completed!")
        
    except Exception as e:
        print(f"❌ Detailed test error: {e}")

if __name__ == "__main__":
    print("🚀 Starting Full Integration Test Suite...")
    
    # Main test
    success = asyncio.run(test_full_integration())
    
    if success:
        # Ask user for detailed test
        response = input("\n🔬 Do you want to run detailed integration test? (y/n): ")
        if response.lower() in ['y', 'yes', 'evet']:
            asyncio.run(test_detailed_integration())
    
    print("\n🎉 Test completed!") 