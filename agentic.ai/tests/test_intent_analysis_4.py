#!/usr/bin/env python3
"""
Intent Analysis Test Script
Tests whether LLM can extract intent from user queries
"""

import asyncio
import json
from app.core.agent.intent_analyzer import IntentAnalysisLLM
from app.core.llm.gemini_wrapper import GeminiWrapper
from app.config import settings

async def test_intent_analysis():
    """Test intent analysis"""
    print("🧪 LLM Intent Analysis Test")
    print("=" * 50)
    
    try:
        # Initialize LLM wrapper
        llm = GeminiWrapper(settings)
        intent_analyzer = IntentAnalysisLLM(llm)
        
        # Test messages
        test_messages = [
            "Turkish restaurant recommendation in Istanbul",
            "I want to see museums and historical places"
        ]
        
        for i, message in enumerate(test_messages, 1):
            print(f"\n📝 Test {i}: {message}")
            print("-" * 40)
            
            # Send direct prompt to LLM
            from app.core.llm.prompts.intent_prompts import INTENT_ANALYSIS_PROMPT
            prompt = INTENT_ANALYSIS_PROMPT.format(user_message=message)
            
            print("🤖 Prompt sent to LLM:")
            print(prompt)
            print("\n📡 Raw response from LLM:")
            
            # Get raw response
            raw_response = await llm.generate_content(prompt)
            print(f"'{raw_response}'")
            
            # Try to parse JSON
            try:
                intent_data = json.loads(raw_response)
                print(f"\n✅ JSON parse successful:")
                print(json.dumps(intent_data, indent=2, ensure_ascii=False))
            except json.JSONDecodeError as e:
                print(f"\n❌ JSON parse error: {e}")
                print("LLM response is not in JSON format!")
            
            print()
        
        print("✅ Intent Analysis test completed!")
        
    except Exception as e:
        print(f"❌ Test error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_intent_analysis()) 