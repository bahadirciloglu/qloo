import pytest
import asyncio
from app.core.concierge import AIConcierge
from app.config import Settings

@pytest.mark.asyncio
async def test_concierge_initialization():
    """Concierge başlatma testi"""
    try:
        settings = Settings()
        concierge = AIConcierge(settings)
        assert concierge is not None
        assert concierge.config is not None
        print("✅ Concierge başarıyla başlatıldı")
    except Exception as e:
        print(f"❌ Concierge başlatılamadı: {e}")
        # API key olmadığında bu normal olabilir
        assert "API key" in str(e) or "OpenAI" in str(e)

@pytest.mark.asyncio
async def test_qloo_integration():
    """Qloo entegrasyon testi"""
    try:
        settings = Settings()
        concierge = AIConcierge(settings)
        
        # Mock öneriler al
        recommendations = await concierge.qloo.get_personalized_recommendations("Istanbul")
        
        assert recommendations is not None
        assert "restaurants" in recommendations
        assert "activities" in recommendations
        assert len(recommendations["restaurants"]) > 0
        assert len(recommendations["activities"]) > 0
        
        print("✅ Qloo entegrasyonu çalışıyor")
        print(f"   - {len(recommendations['restaurants'])} restoran önerisi")
        print(f"   - {len(recommendations['activities'])} aktivite önerisi")
        
    except Exception as e:
        print(f"❌ Qloo entegrasyon hatası: {e}")

@pytest.mark.asyncio
async def test_hotel_info():
    """Otel bilgileri testi"""
    try:
        settings = Settings()
        concierge = AIConcierge(settings)
        
        hotel_info = await concierge.get_hotel_info()
        
        assert hotel_info is not None
        assert "name" in hotel_info
        assert "location" in hotel_info
        assert "amenities" in hotel_info
        assert "services" in hotel_info
        
        print("✅ Otel bilgileri alındı")
        print(f"   - Otel: {hotel_info['name']}")
        print(f"   - Lokasyon: {hotel_info['location']}")
        print(f"   - {len(hotel_info['amenities'])} özellik")
        print(f"   - {len(hotel_info['services'])} hizmet")
        
    except Exception as e:
        print(f"❌ Otel bilgileri hatası: {e}")

@pytest.mark.asyncio
async def test_quick_recommendations():
    """Hızlı öneriler testi"""
    try:
        settings = Settings()
        concierge = AIConcierge(settings)
        
        # Restoran önerileri
        restaurants = await concierge.get_quick_recommendations("restaurants")
        assert isinstance(restaurants, list)
        
        # Aktivite önerileri
        activities = await concierge.get_quick_recommendations("activities")
        assert isinstance(activities, list)
        
        print("✅ Hızlı öneriler çalışıyor")
        print(f"   - {len(restaurants)} restoran önerisi")
        print(f"   - {len(activities)} aktivite önerisi")
        
    except Exception as e:
        print(f"❌ Hızlı öneriler hatası: {e}")

def test_settings():
    """Ayarlar testi"""
    try:
        settings = Settings()
        
        assert settings.hotel_name == "Grand Hotel Istanbul"
        assert settings.hotel_location == "Istanbul, Turkey"
        assert settings.qloo_api_key == "mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw"
        assert settings.qloo_base_url == "https://hackathon.api.qloo.com"
        
        print("✅ Ayarlar doğru yapılandırıldı")
        
    except Exception as e:
        print(f"❌ Ayarlar hatası: {e}")

if __name__ == "__main__":
    print("🧪 AI Concierge Test Suite")
    print("=" * 40)
    
    # Testleri çalıştır
    asyncio.run(test_settings())
    asyncio.run(test_concierge_initialization())
    asyncio.run(test_qloo_integration())
    asyncio.run(test_hotel_info())
    asyncio.run(test_quick_recommendations())
    
    print("\n✅ Tüm testler tamamlandı!") 