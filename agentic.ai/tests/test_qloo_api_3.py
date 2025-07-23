#!/usr/bin/env python3
"""
Qloo API Test Script
Gerçek Qloo API çağrıları ile test yapar
"""

import asyncio
import json
from app.core.qloo_integration import QlooIntegration
from app.config import settings

async def test_qloo_api():
    """Qloo API'yi test et"""
    print("🧪 Qloo API Test Başlıyor...")
    print("=" * 50)
    
    try:
        # Qloo Integration'ı başlat
        qloo = QlooIntegration(settings)
        print("✅ Qloo Integration başarıyla başlatıldı")
        
        # Test 1: İstanbul için restoran önerileri
        print("\n🍽️ Test 1: İstanbul Restoran Önerileri")
        print("-" * 40)
        
        restaurants = await qloo.get_personalized_recommendations(
            location="Istanbul",
            user_message="İstanbul'da Türk restoranı önerisi"
        )
        
        print(f"📊 Sonuç: {len(restaurants.get('restaurants', []))} restoran bulundu")
        for i, restaurant in enumerate(restaurants.get('restaurants', [])[:3]):
            print(f"  {i+1}. {restaurant.get('name', 'Bilinmeyen')}")
            print(f"     📍 {restaurant.get('properties', {}).get('location', 'Konum bilgisi yok')}")
            print(f"     ⭐ {restaurant.get('properties', {}).get('rating', 0)}")
        
        # Test 2: İstanbul için aktivite önerileri
        print("\n🎭 Test 2: İstanbul Aktivite Önerileri")
        print("-" * 40)
        
        activities = await qloo.get_personalized_recommendations(
            location="Istanbul", 
            user_message="İstanbul'da müze ve tarihi yerler"
        )
        
        print(f"📊 Sonuç: {len(activities.get('activities', []))} aktivite bulundu")
        for i, activity in enumerate(activities.get('activities', [])[:3]):
            print(f"  {i+1}. {activity.get('name', 'Bilinmeyen')}")
            print(f"     📍 {activity.get('properties', {}).get('location', 'Konum bilgisi yok')}")
            print(f"     🏷️ {', '.join(activity.get('properties', {}).get('tags', [])[:3])}")
        
        # Test 3: Lokasyon insights
        print("\n🗺️ Test 3: İstanbul Lokasyon Insights")
        print("-" * 40)
        
        insights = await qloo.get_location_insights("Istanbul")
        print(f"📊 İstanbul insights alındı")
        if 'properties' in insights:
            print(f"  📈 Popülerlik: {insights['properties'].get('popularity', 'Bilinmiyor')}")
            print(f"  🏷️ Tag'lar: {', '.join(insights.get('tags', [])[:5])}")
        
        # Test 4: Entity arama
        print("\n🔍 Test 4: Entity Arama")
        print("-" * 40)
        
        search_results = await qloo.search_entities("Topkapı Sarayı", "urn:entity:place")
        print(f"📊 Arama sonucu: {len(search_results.get('results', {}).get('entities', []))} sonuç")
        
        # Test 5: Trend yerler
        print("\n🔥 Test 5: Trend Yerler")
        print("-" * 40)
        
        trending = await qloo.get_trending_places("Istanbul", 3)
        print(f"📊 Trend yerler: {len(trending.get('results', {}).get('entities', []))} sonuç")
        
        print("\n✅ Tüm testler tamamlandı!")
        
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_qloo_api()) 