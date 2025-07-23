#!/usr/bin/env python3
"""
AI Concierge Çalıştırma Scripti
===============================

Bu script AI Concierge uygulamasını başlatır.
"""

import os
import sys
import uvicorn
from pathlib import Path

def check_requirements():
    """Gerekli dosyaları kontrol et"""
    print("🔍 Gerekli dosyalar kontrol ediliyor...")
    
    # .env dosyası kontrolü
    if not os.path.exists(".env"):
        print("⚠️  .env dosyası bulunamadı!")
        print("📝 env.example dosyasını .env olarak kopyalayın ve OPENAI_API_KEY ekleyin")
        return False
    
    # Static dosyalar kontrolü
    if not os.path.exists("static/chat.html"):
        print("⚠️  static/chat.html dosyası bulunamadı!")
        return False
    
    print("✅ Tüm dosyalar mevcut")
    return True

def check_dependencies():
    """Bağımlılıkları kontrol et"""
    print("📦 Bağımlılıklar kontrol ediliyor...")
    
    try:
        import fastapi
        import uvicorn
        import langchain
        import openai
        print("✅ Tüm bağımlılıklar yüklü")
        return True
    except ImportError as e:
        print(f"❌ Eksik bağımlılık: {e}")
        print("💡 pip install -r requirements.txt komutunu çalıştırın")
        return False

def main():
    """Ana fonksiyon"""
    print("🏨 AI Concierge Başlatılıyor...")
    print("=" * 40)
    
    # Kontroller
    if not check_requirements():
        print("\n❌ Gerekli dosyalar eksik!")
        return 1
    
    if not check_dependencies():
        print("\n❌ Bağımlılıklar eksik!")
        return 1
    
    print("\n🚀 Uygulama başlatılıyor...")
    print("📱 Tarayıcıda http://localhost:8000 adresini açın")
    print("🛑 Durdurmak için Ctrl+C tuşlayın")
    print("=" * 40)
    
    try:
        # Uygulamayı başlat
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 Uygulama durduruldu")
        return 0
    except Exception as e:
        print(f"\n❌ Uygulama başlatılamadı: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 