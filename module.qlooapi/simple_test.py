#!/usr/bin/env python3
"""
Simple Qloo API Test
===================

A minimal test to debug API connection issues.
"""

import requests
import json

def test_basic_insights():
    """Test the most basic insights call"""
    
    api_key = "mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw"
    base_url = "https://hackathon.api.qloo.com"
    
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': api_key
    }
    
    # Test 1: Basic GET request with minimal parameters
    print("🔍 Test 1: Basic GET request...")
    try:
        url = f"{base_url}/v2/insights"
        params = {
            'filter.type': 'urn:entity:movie',
            'filter.tags': 'urn:tag:genre:media:action',
            'take': 1
        }
        
        response = requests.get(url, headers=headers, params=params)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:500]}...")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ GET request successful!")
            return True
        else:
            print(f"❌ GET request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def test_basic_post():
    """Test basic POST request"""
    
    api_key = "mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw"
    base_url = "https://hackathon.api.qloo.com"
    
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': api_key
    }
    
    print("\n📝 Test 2: Basic POST request...")
    try:
        url = f"{base_url}/v2/insights"
        payload = {
            'filter.type': 'urn:entity:movie',
            'filter.tags': 'urn:tag:genre:media:action',
            'take': 1
        }
        
        response = requests.post(url, headers=headers, json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:500]}...")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ POST request successful!")
            return True
        else:
            print(f"❌ POST request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def test_with_query():
    """Test with query parameter"""
    
    api_key = "mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw"
    base_url = "https://hackathon.api.qloo.com"
    
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': api_key
    }
    
    print("\n🔍 Test 3: GET request with query...")
    try:
        url = f"{base_url}/v2/insights"
        params = {
            'filter.type': 'urn:entity:movie',
            'query': 'audi'
        }
        
        response = requests.get(url, headers=headers, params=params)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:500]}...")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Query request successful!")
            return True
        else:
            print(f"❌ Query request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Simple Qloo API Test")
    print("=" * 30)
    
    tests = [
        ("Basic GET", test_basic_insights),
        ("Basic POST", test_basic_post),
        ("Query GET", test_with_query)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*15} {test_name} {'='*15}")
        if test_func():
            passed += 1
            print(f"✅ {test_name} PASSED")
        else:
            print(f"❌ {test_name} FAILED")
    
    print(f"\n{'='*30}")
    print(f"📊 Results: {passed}/{total} tests passed")
    
    if passed > 0:
        print("🎉 At least one test passed! The API is accessible.")
    else:
        print("⚠️ All tests failed. Check API access and configuration.")

if __name__ == "__main__":
    main() 