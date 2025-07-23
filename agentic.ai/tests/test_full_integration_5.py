#!/usr/bin/env python3
"""
5. Tam Entegrasyon Testi
Kullanıcı sorusu → LLM Intent Analysis → API Çağrısı → Yanıt Oluşturma
"""

import asyncio
import json
import sys
import os

# App path'ini ekle
app_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(app_path)

from app.core.agent.concierge_agent import LLMCentricConciergeAgent
from app.config import settings

async def test_full_integration():
    """Tam entegrasyon testi - Kullanıcı sorusundan yanıta kadar"""
    print("5️⃣ Tam Entegrasyon Testi")
    print("=" * 60)
    print("Kullanıcı Sorusu → LLM Intent → API Çağrısı → Yanıt")
    print("=" * 60)
    
    try:
        # Concierge Agent'ı başlat
        print("🔧 Concierge Agent başlatılıyor...")
        agent = LLMCentricConciergeAgent(settings)
        print("✅ Agent başarıyla başlatıldı")
        
        # Test kullanıcı soruları
        test_questions = [
            {
                "question": "İstanbul'da Türk restoranı önerisi alabilir miyim?",
                "expected_intent": "restaurant_recommendation",
                "expected_location": "Istanbul"
            },
            {
                "question": "Müze ve tarihi yerler görmek istiyorum",
                "expected_intent": "activity_recommendation", 
                "expected_location": "Istanbul"
            },
            {
                "question": "Otel hakkında bilgi alabilir miyim?",
                "expected_intent": "hotel_info",
                "expected_location": None
            },
            {
                "question": "Ankara'da ne yapabilirim?",
                "expected_intent": "activity_recommendation",
                "expected_location": "Ankara"
            },
            {
                "question": "İzmir'de restoran önerisi",
                "expected_intent": "restaurant_recommendation",
                "expected_location": "Izmir"
            }
        ]
        
        for i, test_case in enumerate(test_questions, 1):
            print(f"\n📝 Test {i}: {test_case['question']}")
            print("-" * 50)
            
            # 1. Kullanıcı sorusunu işle
            print("🤖 LLM Intent Analysis başlıyor...")
            response = await agent.process_request(test_case['question'])
            
            print(f"💬 AI Yanıtı:")
            print(f"   {response}")
            
            # 2. Yanıtın kalitesini kontrol et
            print(f"\n📊 Yanıt Analizi:")
            
            # Yanıt uzunluğu kontrolü
            if len(response) > 50:
                print("   ✅ Yanıt yeterince detaylı")
            else:
                print("   ⚠️ Yanıt çok kısa")
            
            # Yanıt içeriği kontrolü
            if "restoran" in test_case['question'].lower() and "restoran" in response.lower():
                print("   ✅ Restoran konusu yanıtta var")
            elif "müze" in test_case['question'].lower() and ("müze" in response.lower() or "aktivite" in response.lower()):
                print("   ✅ Aktivite konusu yanıtta var")
            elif "otel" in test_case['question'].lower() and ("otel" in response.lower() or "hotel" in response.lower()):
                print("   ✅ Otel konusu yanıtta var")
            else:
                print("   ⚠️ Yanıt konuyla tam uyuşmuyor")
            
            # Lokasyon kontrolü
            if test_case['expected_location'] and test_case['expected_location'].lower() in response.lower():
                print(f"   ✅ {test_case['expected_location']} lokasyonu yanıtta var")
            elif test_case['expected_location']:
                print(f"   ⚠️ {test_case['expected_location']} lokasyonu yanıtta yok")
            
            print()
        
        print("✅ Tam entegrasyon testi tamamlandı!")
        return True
        
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_detailed_integration():
    """Detaylı entegrasyon testi - Her adımı göster"""
    print("\n🔬 Detaylı Entegrasyon Testi")
    print("=" * 60)
    
    try:
        agent = LLMCentricConciergeAgent(settings)
        
        # Tek bir test sorusu ile detaylı analiz
        test_question = "İstanbul'da Türk restoranı önerisi alabilir miyim?"
        
        print(f"📝 Test Sorusu: {test_question}")
        print("-" * 50)
        
        # 1. Intent Analysis
        print("🔍 1. Adım: Intent Analysis")
        intent = await agent.intent_analyzer.analyze_intent(test_question)
        print(f"   Intent: {intent.get('intent', 'Bilinmiyor')}")
        print(f"   Entities: {intent.get('entities', {})}")
        print(f"   API Calls: {len(intent.get('api_calls_needed', []))}")
        
        # 2. API Çağrıları
        print("\n📡 2. Adım: API Çağrıları")
        api_results = await agent.api_executor.execute_api_calls(
            intent.get('api_calls_needed', [])
        )
        print(f"   API Sonuçları: {len(api_results)} adet")
        for api_name, result in api_results.items():
            success = result.get('success', False)
            data_count = len(result.get('data', []))
            print(f"   - {api_name}: {'✅' if success else '❌'} ({data_count} sonuç)")
        
        # 3. Response Generation
        print("\n💬 3. Adım: Response Generation")
        response = await agent.response_generator.generate_response(
            test_question, api_results, intent
        )
        print(f"   Yanıt: {response[:200]}...")
        
        print("\n✅ Detaylı entegrasyon testi tamamlandı!")
        
    except Exception as e:
        print(f"❌ Detaylı test hatası: {e}")

if __name__ == "__main__":
    print("🚀 Tam Entegrasyon Test Suite Başlatılıyor...")
    
    # Ana test
    success = asyncio.run(test_full_integration())
    
    if success:
        # Detaylı test için kullanıcıdan onay al
        response = input("\n🔬 Detaylı entegrasyon testi yapmak ister misiniz? (y/n): ")
        if response.lower() in ['y', 'yes', 'evet']:
            asyncio.run(test_detailed_integration())
    
    print("\n�� Test tamamlandı!") 