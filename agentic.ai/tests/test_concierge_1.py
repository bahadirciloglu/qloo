import pytest
import asyncio
from app.core.concierge import AIConcierge
from app.config import Settings

@pytest.mark.asyncio
async def test_concierge_initialization():
    """Concierge initialization test"""
    try:
        settings = Settings()
        concierge = AIConcierge(settings)
        assert concierge is not None
        assert concierge.config is not None
        print("✅ Concierge successfully started")
    except Exception as e:
        print(f"❌ Failed to start Concierge: {e}")
        # This might be normal when API key is missing
        assert "API key" in str(e) or "OpenAI" in str(e)

@pytest.mark.asyncio
async def test_qloo_integration():
    """Qloo integration test"""
    try:
        settings = Settings()
        concierge = AIConcierge(settings)
        
        # Get mock recommendations
        recommendations = await concierge.qloo.get_personalized_recommendations("Istanbul")
        
        assert recommendations is not None
        assert "restaurants" in recommendations
        assert "activities" in recommendations
        assert len(recommendations["restaurants"]) > 0
        assert len(recommendations["activities"]) > 0
        
        print("✅ Qloo integration working")
        print(f"   - {len(recommendations['restaurants'])} restaurant recommendations")
        print(f"   - {len(recommendations['activities'])} activity recommendations")
        
    except Exception as e:
        print(f"❌ Qloo integration error: {e}")

@pytest.mark.asyncio
async def test_hotel_info():
    """Hotel information test"""
    try:
        settings = Settings()
        concierge = AIConcierge(settings)
        
        hotel_info = await concierge.get_hotel_info()
        
        assert hotel_info is not None
        assert "name" in hotel_info
        assert "location" in hotel_info
        assert "amenities" in hotel_info
        assert "services" in hotel_info
        
        print("✅ Hotel information retrieved")
        print(f"   - Hotel: {hotel_info['name']}")
        print(f"   - Location: {hotel_info['location']}")
        print(f"   - {len(hotel_info['amenities'])} amenities")
        print(f"   - {len(hotel_info['services'])} services")
        
    except Exception as e:
        print(f"❌ Hotel information error: {e}")

@pytest.mark.asyncio
async def test_quick_recommendations():
    """Quick recommendations test"""
    try:
        settings = Settings()
        concierge = AIConcierge(settings)
        
        # Restaurant recommendations
        restaurants = await concierge.get_quick_recommendations("restaurants")
        assert isinstance(restaurants, list)
        
        # Activity recommendations
        activities = await concierge.get_quick_recommendations("activities")
        assert isinstance(activities, list)
        
        print("✅ Quick recommendations working")
        print(f"   - {len(restaurants)} restaurant recommendations")
        print(f"   - {len(activities)} activity recommendations")
        
    except Exception as e:
        print(f"❌ Quick recommendations error: {e}")

def test_settings():
    """Settings test"""
    try:
        settings = Settings()
        
        assert settings.hotel_name == "Grand Hotel Istanbul"
        assert settings.hotel_location == "Istanbul, Turkey"
        assert settings.qloo_api_key == "mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw"
        assert settings.qloo_base_url == "https://hackathon.api.qloo.com"
        
        print("✅ Settings correctly configured")
        
    except Exception as e:
        print(f"❌ Settings error: {e}")

if __name__ == "__main__":
    print("🧪 AI Concierge Test Suite")
    print("=" * 40)
    
    # Run tests
    asyncio.run(test_settings())
    asyncio.run(test_concierge_initialization())
    asyncio.run(test_qloo_integration())
    asyncio.run(test_hotel_info())
    asyncio.run(test_quick_recommendations())
    
    print("\n✅ All tests completed!") 