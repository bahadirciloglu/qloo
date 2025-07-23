#!/usr/bin/env python3
"""
Qloo API Test Script
====================

This script tests the basic functionality of the Qloo API integration
to ensure everything is working correctly.
"""

import sys
import json
from qloo_llm_integration import QlooConfig, QlooLLMIntegration

def test_api_connection():
    """Test basic API connection"""
    print("🔌 Testing Qloo API Connection...")
    
    config = QlooConfig()
    qloo = QlooLLMIntegration(config)
    
    # Test 1: Search for a well-known movie
    print("\n📽️ Test 1: Searching for 'Inception'...")
    try:
        results = qloo.search_entities("Inception", "urn:entity:movie")
        if "error" in results:
            print(f"❌ Search failed: {results['error']}")
            return False
        elif "results" in results and "entities" in results["results"]:
            entities = results["results"]["entities"]
            if entities:
                print(f"✅ Found {len(entities)} entities")
                for entity in entities[:2]:
                    print(f"   - {entity['name']} (ID: {entity['entity_id']})")
                return True
            else:
                print("❌ No entities found")
                return False
        else:
            print("❌ Unexpected response format")
            print(f"Response: {results}")
            return False
    except Exception as e:
        print(f"❌ Exception during search: {e}")
        return False

def test_insights_api():
    """Test insights API"""
    print("\n🔍 Test 2: Testing Insights API...")
    
    config = QlooConfig()
    qloo = QlooLLMIntegration(config)
    
    try:
        # Get movie recommendations based on some interests
        insights = qloo.get_insights(
            entity_type="urn:entity:movie",
            interests=["The Matrix"],
            limit=3,
            filters={"filter.tags": "urn:tag:genre:media:action"}
        )
        
        if "error" in insights:
            print(f"❌ Insights failed: {insights['error']}")
            return False
        elif "results" in insights and "entities" in insights["results"]:
            entities = insights["results"]["entities"]
            print(f"✅ Got {len(entities)} movie recommendations")
            for entity in entities:
                print(f"   - {entity['name']} (Popularity: {entity.get('popularity', 0):.1%})")
            return True
        else:
            print("❌ Unexpected insights response format")
            return False
    except Exception as e:
        print(f"❌ Exception during insights: {e}")
        return False

def test_trending_api():
    """Test trending entities API"""
    print("\n📈 Test 3: Testing Trending API...")
    
    config = QlooConfig()
    qloo = QlooLLMIntegration(config)
    
    try:
        trending = qloo.get_trending_entities("urn:entity:movie", 3)
        
        if "error" in trending:
            print(f"❌ Trending failed: {trending['error']}")
            return False
        elif "results" in trending and "entities" in trending["results"]:
            entities = trending["results"]["entities"]
            print(f"✅ Got {len(entities)} trending movies")
            for entity in entities:
                trend_score = entity.get("trend", {}).get("percentile", 0)
                print(f"   - {entity['name']} (Trend: {trend_score:.1%})")
            return True
        else:
            print("❌ Unexpected trending response format")
            return False
    except Exception as e:
        print(f"❌ Exception during trending: {e}")
        return False

def test_configuration():
    """Test configuration setup"""
    print("\n⚙️ Test 4: Testing Configuration...")
    
    try:
        config = QlooConfig()
        
        # Check API key
        if not config.api_key or config.api_key == "your-api-key":
            print("❌ API key not properly configured")
            return False
        
        # Check base URL
        if not config.base_url:
            print("❌ Base URL not configured")
            return False
        
        # Check headers
        if "X-Api-Key" not in config.headers:
            print("❌ API key header missing")
            return False
        
        print(f"✅ Configuration looks good")
        print(f"   - API Key: {config.api_key[:10]}...")
        print(f"   - Base URL: {config.base_url}")
        print(f"   - Headers: {list(config.headers.keys())}")
        return True
        
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Qloo API Integration Test Suite")
    print("=" * 40)
    
    tests = [
        ("Configuration", test_configuration),
        ("API Connection", test_api_connection),
        ("Insights API", test_insights_api),
        ("Trending API", test_trending_api)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} PASSED")
            else:
                print(f"❌ {test_name} FAILED")
        except Exception as e:
            print(f"❌ {test_name} FAILED with exception: {e}")
    
    print(f"\n{'='*50}")
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your Qloo integration is working correctly.")
        print("\nNext steps:")
        print("1. Run: python qloo_llm_integration.py")
        print("2. Run: python example_llm_integration.py")
        print("3. Start building your own LLM integration!")
    else:
        print("⚠️ Some tests failed. Please check your configuration and API access.")
        print("\nTroubleshooting:")
        print("1. Verify your API key is correct")
        print("2. Check your internet connection")
        print("3. Ensure you're using the correct API endpoint")
        print("4. Contact Qloo support if issues persist")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 