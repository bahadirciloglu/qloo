#!/usr/bin/env python3
"""
Qloo LLM Integration Project
============================

This project demonstrates how to integrate Qloo's Taste AI with LLMs to create
more truthful and personalized AI experiences. It uses Qloo's consumer taste
intelligence to enhance LLM responses with real-world behavioral data.

Key Features:
- Personalized recommendations based on user interests
- Location-based insights and heatmaps
- Demographic analysis and audience targeting
- Entity correlation and affinity scoring
- Integration with popular LLM frameworks

API Configuration:
- Server URL: https://hackathon.api.qloo.com
- API Key: mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw
"""

import requests
import json
import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class QlooConfig:
    """Configuration for Qloo API integration"""
    api_key: str = "mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw"
    base_url: str = "https://hackathon.api.qloo.com"
    headers: Dict[str, str] = None
    
    def __post_init__(self):
        if self.headers is None:
            self.headers = {
                'Content-Type': 'application/json',
                'X-Api-Key': self.api_key
            }

class QlooLLMIntegration:
    """
    Main class for integrating Qloo's Taste AI with LLMs
    """
    
    def __init__(self, config: QlooConfig):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update(config.headers)
    
    def get_insights(self, 
                    entity_type: str = "urn:entity:movie",
                    interests: Optional[List[str]] = None,
                    location: Optional[str] = None,
                    demographics: Optional[Dict] = None,
                    filters: Optional[Dict] = None,
                    limit: int = 10) -> Dict:
        """
        Get personalized insights from Qloo's Taste AI
        
        Args:
            entity_type: Type of entities to return (e.g., "urn:entity:movie", "urn:entity:place")
            interests: List of entity IDs or names that represent user interests
            location: Location query (e.g., "New York City", "Los Angeles")
            demographics: Demographic filters (age, gender, etc.)
            filters: Additional filters for the query
            limit: Number of results to return
            
        Returns:
            Dictionary containing insights and recommendations
        """
        url = f"{self.config.base_url}/v2/insights"
        
        # Base parameters
        params = {
            'filter.type': entity_type,
            'take': limit
        }
        
        # Add interests if provided
        if interests:
            if isinstance(interests[0], str) and interests[0].startswith('urn:'):
                # Entity IDs
                params['signal.interests.entities'] = ','.join(interests)
            else:
                # Entity names - use POST method for query resolution
                return self._post_insights_with_queries(url, entity_type, interests, location, demographics, filters, limit)
        
        # Add location filter
        if location:
            params['filter.location.query'] = location
        
        # Add demographic filters
        if demographics:
            for key, value in demographics.items():
                params[f'signal.demographics.{key}'] = value
        
        # Add additional filters
        if filters:
            params.update(filters)
        
        # Ensure we have at least one valid signal or filter
        if not interests and not location and not demographics and not filters:
            # Add a default filter to ensure the request is valid
            params['filter.tags'] = 'urn:tag:category:place:restaurant'
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting insights: {e}")
            return {"error": str(e)}
    
    def _post_insights_with_queries(self, url: str, entity_type: str, interests: List[str], 
                                   location: Optional[str], demographics: Optional[Dict], 
                                   filters: Optional[Dict], limit: int) -> Dict:
        """Handle POST requests for entity name resolution"""
        payload = {
            'filter.type': entity_type,
            'take': limit,
            'feature.explainability': True,
            'signal.interests.entities.query': interests,
            'filter.tags': 'urn:tag:genre:media:action'  # Ensure valid request
        }
        
        if location:
            payload['filter.location.query'] = location
        
        if demographics:
            for key, value in demographics.items():
                payload[f'signal.demographics.{key}'] = value
        
        if filters:
            payload.update(filters)
        
        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error posting insights: {e}")
            return {"error": str(e)}
    
    def get_heatmap(self, entity_id: str, location: str) -> Dict:
        """
        Get heatmap data for an entity in a specific location
        
        Args:
            entity_id: Qloo entity ID
            location: Location query
            
        Returns:
            Heatmap data showing geographic distribution of interest
        """
        url = f"{self.config.base_url}/v2/insights"
        
        params = {
            'filter.type': 'urn:heatmap',
            'filter.location.query': location,
            'signal.interests.entities': entity_id
        }
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting heatmap: {e}")
            return {"error": str(e)}
    
    def get_demographic_insights(self, entity_id: str, demographics: Optional[Dict] = None) -> Dict:
        """
        Get demographic affinity scores for an entity
        
        Args:
            entity_id: Qloo entity ID
            demographics: Demographic filters to apply
            
        Returns:
            Demographic analysis and affinity scores
        """
        url = f"{self.config.base_url}/v2/insights"
        
        params = {
            'filter.type': 'urn:demographics',
            'signal.interests.entities': entity_id
        }
        
        if demographics:
            for key, value in demographics.items():
                params[f'signal.demographics.{key}'] = value
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting demographic insights: {e}")
            return {"error": str(e)}
    
    def search_entities(self, query: str, entity_type: Optional[str] = None) -> Dict:
        """
        Search for entities by name using the insights endpoint
        
        Args:
            query: Search query
            entity_type: Optional entity type filter
            
        Returns:
            Search results with entity information
        """
        url = f"{self.config.base_url}/v2/insights"
        
        params = {
            'filter.type': entity_type or "urn:entity:movie",
            'take': 10,
            'signal.interests.entities.query': [query],
            'filter.tags': 'urn:tag:genre:media:action'  # Ensure valid request
        }
        
        try:
            response = self.session.post(url, json=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error searching entities: {e}")
            return {"error": str(e)}
    
    def get_trending_entities(self, entity_type: str = "urn:entity:movie", limit: int = 10) -> Dict:
        """
        Get trending entities of a specific type using the insights endpoint
        
        Args:
            entity_type: Type of entities to return
            limit: Number of results to return
            
        Returns:
            Trending entities with trend scores
        """
        url = f"{self.config.base_url}/v2/insights"
        
        params = {
            'filter.type': entity_type,
            'take': limit,
            'bias.trends': 'high',  # Bias towards trending entities
            'filter.tags': 'urn:tag:genre:media:action'  # Ensure valid request
        }
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting trending entities: {e}")
            return {"error": str(e)}
    
    def analyze_user_taste_profile(self, user_interests: List[str]) -> Dict:
        """
        Analyze user taste profile based on their interests
        
        Args:
            user_interests: List of user interests (movies, music, books, etc.)
            
        Returns:
            Comprehensive taste analysis with insights
        """
        analysis = {
            "user_interests": user_interests,
            "movie_insights": {},
            "music_insights": {},
            "book_insights": {},
            "cultural_patterns": [],
            "recommendations": []
        }
        
        # Get movie insights
        try:
            movie_insights = self.get_insights(
                entity_type="urn:entity:movie",
                interests=user_interests,
                limit=5
            )
            analysis["movie_insights"] = movie_insights
        except Exception as e:
            analysis["movie_insights"] = {"error": str(e)}
        
        # Get music insights
        try:
            music_insights = self.get_insights(
                entity_type="urn:entity:music",
                interests=user_interests,
                limit=5
            )
            analysis["music_insights"] = music_insights
        except Exception as e:
            analysis["music_insights"] = {"error": str(e)}
        
        # Get book insights
        try:
            book_insights = self.get_insights(
                entity_type="urn:entity:book",
                interests=user_interests,
                limit=5
            )
            analysis["book_insights"] = book_insights
        except Exception as e:
            analysis["book_insights"] = {"error": str(e)}
        
        # Analyze cultural patterns
        all_interests = " ".join(user_interests).lower()
        
        if any(word in all_interests for word in ["rock", "punk", "grunge", "nirvana"]):
            analysis["cultural_patterns"].append("Alternative/Indie Culture")
        
        if any(word in all_interests for word in ["classic", "literature", "philosophy"]):
            analysis["cultural_patterns"].append("Intellectual/Literary")
        
        if any(word in all_interests for word in ["action", "thriller", "crime"]):
            analysis["cultural_patterns"].append("High-Energy/Adventure")
        
        if any(word in all_interests for word in ["drama", "romance", "emotional"]):
            analysis["cultural_patterns"].append("Emotional/Introspective")
        
        return analysis

class LLMEnhancer:
    """
    Class to enhance LLM responses with Qloo insights
    """
    
    def __init__(self, qloo_integration: QlooLLMIntegration):
        self.qloo = qloo_integration
    
    def enhance_recommendation_prompt(self, user_interests: List[str], 
                                    recommendation_type: str = "movies") -> str:
        """
        Create an enhanced prompt for LLM with Qloo insights
        
        Args:
            user_interests: List of user interests
            recommendation_type: Type of recommendations to generate
            
        Returns:
            Enhanced prompt with Qloo insights
        """
        # Get Qloo insights
        entity_type_map = {
            "movies": "urn:entity:movie",
            "restaurants": "urn:entity:place",
            "music": "urn:entity:artist",
            "books": "urn:entity:book",
            "tv_shows": "urn:entity:tv_show"
        }
        
        entity_type = entity_type_map.get(recommendation_type, "urn:entity:movie")
        
        insights = self.qloo.get_insights(
            entity_type=entity_type,
            interests=user_interests,
            limit=5
        )
        
        if "error" in insights:
            return f"Based on your interests in {', '.join(user_interests)}, here are some {recommendation_type} recommendations:"
        
        # Extract top recommendations
        recommendations = []
        if "results" in insights and "entities" in insights["results"]:
            for entity in insights["results"]["entities"][:3]:
                name = entity.get("name", "Unknown")
                popularity = entity.get("popularity", 0)
                description = entity.get("properties", {}).get("description", "")
                
                recommendations.append({
                    "name": name,
                    "popularity": popularity,
                    "description": description
                })
        
        # Create enhanced prompt
        prompt = f"""Based on your interests in {', '.join(user_interests)}, I've analyzed your taste preferences using advanced consumer intelligence data.

Here are some highly personalized {recommendation_type} recommendations based on real consumer behavior patterns:

"""
        
        for i, rec in enumerate(recommendations, 1):
            prompt += f"{i}. **{rec['name']}** (Popularity: {rec['popularity']:.1%})\n"
            if rec['description']:
                prompt += f"   {rec['description']}\n"
            prompt += "\n"
        
        prompt += f"""These recommendations are based on:
- Cultural affinity analysis across 3.7B+ entities
- Real consumer behavior patterns
- Trend analysis and popularity metrics
- Cross-cultural taste correlations

Please provide additional personalized recommendations and explain why these choices would appeal to someone with these specific interests."""

        return prompt
    
    def create_location_based_prompt(self, location: str, interests: List[str]) -> str:
        """
        Create a location-based recommendation prompt
        
        Args:
            location: Target location
            interests: User interests
            
        Returns:
            Location-based prompt with Qloo insights
        """
        # Get location-based insights
        insights = self.qloo.get_insights(
            entity_type="urn:entity:place",
            interests=interests,
            location=location,
            limit=5
        )
        
        if "error" in insights:
            return f"Based on your interests in {', '.join(interests)}, here are some recommendations for {location}:"
        
        # Extract recommendations
        recommendations = []
        if "results" in insights and "entities" in insights["results"]:
            for entity in insights["results"]["entities"][:3]:
                name = entity.get("name", "Unknown")
                address = entity.get("properties", {}).get("address", "")
                tags = [tag.get("name", "") for tag in entity.get("tags", [])[:3]]
                
                recommendations.append({
                    "name": name,
                    "address": address,
                    "tags": tags
                })
        
        # Create enhanced prompt
        prompt = f"""Based on your interests in {', '.join(interests)}, here are some highly recommended places in {location} based on consumer intelligence data:

"""
        
        for i, rec in enumerate(recommendations, 1):
            prompt += f"{i}. **{rec['name']}**\n"
            if rec['address']:
                prompt += f"   Address: {rec['address']}\n"
            if rec['tags']:
                prompt += f"   Features: {', '.join(rec['tags'])}\n"
            prompt += "\n"
        
        prompt += f"""These recommendations are based on:
- Local consumer behavior patterns in {location}
- Cultural affinity analysis
- Real-time popularity and trend data
- Cross-cultural taste correlations

Please provide additional local recommendations and explain the cultural significance of these choices for someone with these interests visiting {location}."""

        return prompt

def main():
    """Main function to demonstrate Qloo LLM integration"""
    
    # Initialize Qloo integration
    config = QlooConfig()
    qloo_integration = QlooLLMIntegration(config)
    enhancer = LLMEnhancer(qloo_integration)
    
    print("🎯 Qloo LLM Integration Demo")
    print("=" * 50)
    
    # Example 1: Movie recommendations
    print("\n📽️ Example 1: Enhanced Movie Recommendations")
    print("-" * 40)
    
    user_interests = ["Inception", "Interstellar", "The Matrix"]
    enhanced_prompt = enhancer.enhance_recommendation_prompt(user_interests, "movies")
    print(enhanced_prompt)
    
    # Example 2: Location-based recommendations
    print("\n🗽 Example 2: Location-Based Recommendations")
    print("-" * 40)
    
    location_prompt = enhancer.create_location_based_prompt("New York City", ["sushi", "art galleries"])
    print(location_prompt)
    
    # Example 3: Direct API usage
    print("\n🔍 Example 3: Direct API Usage")
    print("-" * 40)
    
    # Get trending movies
    trending = qloo_integration.get_trending_entities("urn:entity:movie", 3)
    if "results" in trending and "entities" in trending["results"]:
        print("Trending Movies:")
        for entity in trending["results"]["entities"]:
            print(f"- {entity.get('name', 'Unknown')} (Trend Score: {entity.get('trend', {}).get('percentile', 0):.1%})")
    
    # Example 4: Demographic insights
    print("\n👥 Example 4: Demographic Insights")
    print("-" * 40)
    
    # Search for a movie first
    search_results = qloo_integration.search_entities("Inception", "urn:entity:movie")
    if "results" in search_results and "entities" in search_results["results"]:
        movie_id = search_results["results"]["entities"][0]["entity_id"]
        
        # Get demographic insights
        demo_insights = qloo_integration.get_demographic_insights(movie_id)
        if "results" in demo_insights and "demographics" in demo_insights["results"]:
            print("Demographic Analysis for 'Inception':")
            for demo in demo_insights["results"]["demographics"][:3]:
                print(f"- {demo.get('name', 'Unknown')}: {demo.get('affinity', 0):.2f}")

if __name__ == "__main__":
    main() 