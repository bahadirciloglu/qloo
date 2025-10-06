#!/usr/bin/env python3
"""
Qloo API Test Script
Performs tests with real Qloo API calls
"""

import asyncio
import json
from app.core.qloo_integration import QlooIntegration
from app.config import settings

async def test_qloo_api():
    """Test Qloo API"""
    print("🧪 Qloo API Test Starting...")
    print("=" * 50)
    
    try:
        # Initialize Qloo Integration
        qloo = QlooIntegration(settings)
        print("✅ Qloo Integration started successfully")
        
        # Test 1: Restaurant recommendations for Istanbul
        print("\n🍽️ Test 1: Istanbul Restaurant Recommendations")
        print("-" * 40)
        
        restaurants = await qloo.get_personalized_recommendations(
            location="Istanbul",
            user_message="Turkish restaurant recommendation in Istanbul"
        )
        
        print(f"📊 Result: {len(restaurants.get('restaurants', []))} restaurants found")
        for i, restaurant in enumerate(restaurants.get('restaurants', [])[:3]):
            print(f"  {i+1}. {restaurant.get('name', 'Unknown')}")
            print(f"     📍 {restaurant.get('properties', {}).get('location', 'No location info')}")
            print(f"     ⭐ {restaurant.get('properties', {}).get('rating', 0)}")
        
        # Test 2: Activity recommendations for Istanbul
        print("\n🎭 Test 2: Istanbul Activity Recommendations")
        print("-" * 40)
        
        activities = await qloo.get_personalized_recommendations(
            location="Istanbul", 
            user_message="Museums and historical places in Istanbul"
        )
        
        print(f"📊 Result: {len(activities.get('activities', []))} activities found")
        for i, activity in enumerate(activities.get('activities', [])[:3]):
            print(f"  {i+1}. {activity.get('name', 'Unknown')}")
            print(f"     📍 {activity.get('properties', {}).get('location', 'No location info')}")
            print(f"     🏷️ {', '.join(activity.get('properties', {}).get('tags', [])[:3])}")
        
        # Test 3: Location insights
        print("\n🗺️ Test 3: Istanbul Location Insights")
        print("-" * 40)
        
        insights = await qloo.get_location_insights("Istanbul")
        print(f"📊 Istanbul insights received")
        if 'properties' in insights:
            print(f"  📈 Popularity: {insights['properties'].get('popularity', 'Unknown')}")
            print(f"  🏷️ Tags: {', '.join(insights.get('tags', [])[:5])}")
        
        # Test 4: Entity search
        print("\n🔍 Test 4: Entity Search")
        print("-" * 40)
        
        search_results = await qloo.search_entities("Topkapi Palace", "urn:entity:place")
        print(f"📊 Search result: {len(search_results.get('results', {}).get('entities', []))} results")
        
        # Test 5: Trending places
        print("\n🔥 Test 5: Trending Places")
        print("-" * 40)
        
        trending = await qloo.get_trending_places("Istanbul", 3)
        print(f"📊 Trending places: {len(trending.get('results', {}).get('entities', []))} results")
        
        print("\n✅ All tests completed!")
        
    except Exception as e:
        print(f"❌ Test error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_qloo_api()) 