#!/usr/bin/env python3
"""
Gemini API Test Scripti
=======================

Bu script Gemini 2.0 Flash API'sini test eder.
"""

import requests
import json
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

def test_gemini_api():
    """Gemini API'sini test et"""
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY bulunamadı!")
        return False
    
    print("🧪 Gemini 2.0 Flash API Testi")
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
                        "text": "Merhaba! Sen bir otel concierge'ısın. Konuklara nasıl yardımcı olursun? Kısa bir yanıt ver."
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
        print("📡 API isteği gönderiliyor...")
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        
        print("✅ API yanıtı alındı!")
        print(f"📊 Status Code: {response.status_code}")
        
        # Yanıtı çıkar
        if 'candidates' in result and len(result['candidates']) > 0:
            content = result['candidates'][0]['content']
            if 'parts' in content and len(content['parts']) > 0:
                text = content['parts'][0]['text']
                print(f"🤖 AI Yanıtı: {text}")
                return True
        
        print("❌ Yanıt formatı beklenenden farklı")
        print(f"📄 Tam yanıt: {json.dumps(result, indent=2)}")
        return False
        
    except requests.exceptions.RequestException as e:
        print(f"❌ API hatası: {e}")
        return False
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")
        return False

def test_concierge_integration():
    """Concierge entegrasyonunu test et"""
    
    print("\n🏨 Concierge Entegrasyon Testi")
    print("=" * 40)
    
    try:
        from app.core.concierge import AIConcierge
        from app.config import settings
        
        print("🔧 Concierge başlatılıyor...")
        concierge = AIConcierge(settings)
        
        print("💬 Test mesajı gönderiliyor...")
        response = asyncio.run(concierge.process_guest_request(
            guest_id="test_guest",
            message="Merhaba, otel hakkında bilgi alabilir miyim?"
        ))
        
        print(f"✅ Concierge yanıtı: {response[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ Concierge hatası: {e}")
        return False

if __name__ == "__main__":
    import asyncio
    
    # Gemini API testi
    gemini_success = test_gemini_api()
    
    # Concierge entegrasyon testi
    concierge_success = test_concierge_integration()
    
    print("\n" + "=" * 40)
    print("📊 Test Sonuçları:")
    print(f"   Gemini API: {'✅ Başarılı' if gemini_success else '❌ Başarısız'}")
    print(f"   Concierge: {'✅ Başarılı' if concierge_success else '❌ Başarısız'}")
    
    if gemini_success and concierge_success:
        print("\n🎉 Tüm testler başarılı! Sistem hazır.")
    else:
        print("\n⚠️  Bazı testler başarısız. Lütfen kontrol edin.") 