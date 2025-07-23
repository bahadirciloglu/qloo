#!/usr/bin/env python3
"""
Intent Analysis Test Script
LLM'in kullanıcı sorgusundan intent çıkarıp çıkarmadığını test eder
"""

import asyncio
import json
from app.core.agent.intent_analyzer import IntentAnalysisLLM
from app.core.llm.gemini_wrapper import GeminiWrapper
from app.config import settings

async def test_intent_analysis():
    """Intent analysis'i test et"""
    print("🧪 LLM Intent Analysis Test")
    print("=" * 50)
    
    try:
        # LLM wrapper'ı başlat
        llm = GeminiWrapper(settings)
        intent_analyzer = IntentAnalysisLLM(llm)
        
        # Test mesajları
        test_messages = [
            "İstanbul'da Türk restoranı önerisi",
            "Müze ve tarihi yerler görmek istiyorum"
        ]
        
        for i, message in enumerate(test_messages, 1):
            print(f"\n📝 Test {i}: {message}")
            print("-" * 40)
            
            # LLM'e direkt prompt gönder
            from app.core.llm.prompts.intent_prompts import INTENT_ANALYSIS_PROMPT
            prompt = INTENT_ANALYSIS_PROMPT.format(user_message=message)
            
            print("🤖 LLM'e gönderilen prompt:")
            print(prompt)
            print("\n📡 LLM'den gelen ham yanıt:")
            
            # Ham yanıtı al
            raw_response = await llm.generate_content(prompt)
            print(f"'{raw_response}'")
            
            # JSON parse etmeye çalış
            try:
                intent_data = json.loads(raw_response)
                print(f"\n✅ JSON parse başarılı:")
                print(json.dumps(intent_data, indent=2, ensure_ascii=False))
            except json.JSONDecodeError as e:
                print(f"\n❌ JSON parse hatası: {e}")
                print("LLM yanıtı JSON formatında değil!")
            
            print()
        
        print("✅ Intent Analysis testi tamamlandı!")
        
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_intent_analysis()) 