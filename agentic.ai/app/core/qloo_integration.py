import sys
import os
import asyncio
import re
from typing import Dict, List, Optional

# Add path for Qloo API integration
qloo_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'llm.qlooapi')
sys.path.append(qloo_path)

try:
    from qloo_llm_integration import QlooLLMIntegration, QlooConfig
    print(f"✅ Qloo API integration loaded successfully: {qloo_path}")
except ImportError as e:
    print(f"❌ Qloo API integration not found: {e}")
    print(f"🔍 Searched path: {qloo_path}")
    raise ImportError("Qloo API integration required")

class QlooIntegration:
    """Wrapper class for Qloo API integration"""
    
    def __init__(self, config):
        self.config = config
        
        try:
            qloo_config = QlooConfig(
                api_key=config.qloo_api_key,
                base_url=config.qloo_base_url
            )
            self.qloo = QlooLLMIntegration(qloo_config)
            print(f"✅ Qloo API connection established: {config.qloo_base_url}")
        except Exception as e:
            print(f"❌ Qloo API connection failed: {e}")
            raise Exception(f"Qloo API connection failed: {e}")
    
    def _analyze_user_query(self, message: str) -> Dict[str, List[str]]:
        """Analyze user query and determine appropriate tags"""
        message_lower = message.lower()
        
        # Turkish and English keywords
        restaurant_keywords = [
            'restoran', 'restaurant', 'yemek', 'food', 'kahvaltı', 'breakfast',
            'akşam yemeği', 'dinner', 'öğle yemeği', 'lunch', 'kafe', 'cafe',
            'bar', 'pub', 'lokanta', 'mekan', 'place', 'yemek yeri'
        ]
        
        activity_keywords = [
            'aktivite', 'activity', 'gezi', 'tour', 'müze', 'museum',
            'tarihi yer', 'historical', 'park', 'bahçe', 'garden',
            'alışveriş', 'shopping', 'eğlence', 'entertainment',
            'spor', 'sport', 'yüzme', 'swimming', 'fitness'
        ]
        
        # Determine categories
        categories = {
            'restaurants': [],
            'activities': []
        }
        
        # Check restaurant category
        if any(keyword in message_lower for keyword in restaurant_keywords):
            categories['restaurants'] = [
                'urn:tag:category:place:restaurant',
                'urn:tag:cuisine:restaurant:turkish',
                'urn:tag:cuisine:restaurant:mediterranean'
            ]
        
        # Check activity category
        if any(keyword in message_lower for keyword in activity_keywords):
            categories['activities'] = [
                'urn:tag:category:place:entertainment',
                'urn:tag:category:place:museum',
                'urn:tag:category:place:park'
            ]
        
        # If no category is determined, add both by default
        if not categories['restaurants'] and not categories['activities']:
            categories['restaurants'] = ['urn:tag:category:place:restaurant']
            categories['activities'] = ['urn:tag:category:place:entertainment']
        
        return categories
    
    async def get_personalized_recommendations(self, location: str, user_message: str = "") -> Dict:
        """Get personalized recommendations"""
        
        try:
            print(f"🔍 Getting recommendations from Qloo API for {location}...")
            print(f"📝 User message: {user_message}")
            
            # Analyze user query
            categories = self._analyze_user_query(user_message)
            print(f"🏷️ Determined categories: {categories}")
            
            loop = asyncio.get_event_loop()
            
            # Restaurant recommendations
            restaurants = []
            if categories['restaurants']:
                restaurants_response = await loop.run_in_executor(
                    None, 
                    self._get_places_with_tags,
                    location,
                    categories['restaurants'],
                    5
                )
                restaurants = self._process_entities(restaurants_response, "restaurants")
            
            # Activity recommendations
            activities = []
            if categories['activities']:
                activities_response = await loop.run_in_executor(
                    None, 
                    self._get_places_with_tags,
                    location,
                    categories['activities'],
                    5
                )
                activities = self._process_entities(activities_response, "activities")
            
            result = {
                "restaurants": restaurants,
                "activities": activities,
                "source": "Qloo API",
                "categories_used": categories
            }
            
            print(f"✅ {len(restaurants)} restaurant, {len(activities)} activity recommendations received")
            return result
            
        except Exception as e:
            print(f"❌ Qloo API error: {e}")
            raise Exception(f"Could not get data from Qloo API: {str(e)}")
    
    def _get_places_with_tags(self, location: str, tags: List[str], limit: int) -> Dict:
        """Query places with specific tags"""
        try:
            # Use first tag (API only accepts one tag)
            primary_tag = tags[0] if tags else "urn:tag:category:place:restaurant"
            
            print(f"🔍 Query with tag: {primary_tag}")
            
            # Use required parameters for Qloo API
            insights = self.qloo.get_insights(
                entity_type="urn:entity:place",
                location=location,
                limit=limit,
                filters={
                    "filter.tags": primary_tag,
                    "filter.location.query": location
                }
            )
            return insights
        except Exception as e:
            print(f"❌ API error with tag: {e}")
            # Fallback: general place query
            return self._get_fallback_places(location, limit)
    
    def _get_fallback_places(self, location: str, limit: int) -> Dict:
        """Fallback place query"""
        try:
            print(f"🔄 Fallback query: {location}")
            # General place query - only with location
            insights = self.qloo.get_insights(
                entity_type="urn:entity:place",
                location=location,
                limit=limit * 2,  # Get more results
                filters={
                    "filter.location.query": location
                }
            )
            return insights
        except Exception as e:
            print(f"❌ Fallback place API error: {e}")
            return {"error": str(e)}
    
    def _process_entities(self, response: Dict, entity_type: str) -> List[Dict]:
        """Process API response and convert to usable format"""
        try:
            if "error" in response:
                print(f"❌ API error for {entity_type}: {response['error']}")
                return []
            
            entities = response.get("results", {}).get("entities", [])
            processed = []
            
            for entity in entities:
                # Get entity properties
                properties = entity.get("properties", {})
                
                processed_entity = {
                    "name": entity.get("name", "Unknown"),
                    "description": properties.get("description", ""),
                    "popularity": entity.get("popularity", 0.5),
                    "properties": {
                        "category": entity_type,
                        "location": properties.get("address", ""),
                        "tags": [tag.get("name", "") for tag in entity.get("tags", [])],
                        "image": properties.get("image", {}).get("url", ""),
                        "rating": properties.get("rating", 0),
                        "price_level": properties.get("price_level", 0)
                    }
                }
                processed.append(processed_entity)
            
            return processed
            
        except Exception as e:
            print(f"❌ Error processing {entity_type} data: {e}")
            return []
    
    async def get_location_insights(self, location: str) -> Dict:
        """Get location-based insights"""
        try:
            loop = asyncio.get_event_loop()
            
            # General location insights
            insights = await loop.run_in_executor(
                None,
                self.qloo.get_insights,
                "urn:entity:place",
                None,  # interests
                location,
                None,  # demographics
                {"take": 10},
                10
            )
            
            return {
                "location": location,
                "insights": insights,
                "source": "Qloo API"
            }
            
        except Exception as e:
            raise Exception(f"Could not get location insights: {str(e)}")
    
    async def search_entities(self, query: str, entity_type: str = "urn:entity:place") -> Dict:
        """Search entities"""
        try:
            loop = asyncio.get_event_loop()
            results = await loop.run_in_executor(
                None,
                self.qloo.search_entities,
                query,
                entity_type
            )
            
            return {
                "query": query,
                "results": results,
                "source": "Qloo API"
            }
            
        except Exception as e:
            raise Exception(f"Search error: {str(e)}")
    
    async def get_trending_places(self, location: str, limit: int = 5) -> Dict:
        """Get trending places"""
        try:
            print(f"📈 Getting trending places for {location}...")
            
            loop = asyncio.get_event_loop()
            
            # Get trending places from Qloo API
            trending_response = await loop.run_in_executor(
                None,
                self.qloo.get_trending_entities,
                "urn:entity:place",
                limit
            )
            
            places = self._process_entities(trending_response, "places")
            
            result = {
                "places": places,
                "source": "Qloo API",
                "location": location
            }
            
            print(f"✅ {len(places)} trending places received")
            return result
            
        except Exception as e:
            print(f"❌ Trending places error: {e}")
            raise Exception(f"Could not get trending places: {str(e)}")
    
    async def get_movie_recommendations(self, location: str, limit: int = 5) -> Dict:
        """Get movie recommendations"""
        try:
            print(f"🎬 Getting movie recommendations...")
            
            loop = asyncio.get_event_loop()
            
            # Get movie recommendations from Qloo API
            movies_response = await loop.run_in_executor(
                None,
                self.qloo.get_insights,
                "urn:entity:movie",
                None,  # interests
                location,
                None,  # demographics
                {"filter.tags": "urn:tag:genre:media:action"},
                limit
            )
            
            movies = self._process_entities(movies_response, "movies")
            
            result = {
                "movies": movies,
                "source": "Qloo API",
                "location": location
            }
            
            print(f"✅ {len(movies)} movie recommendations received")
            return result
            
        except Exception as e:
            print(f"❌ Movie recommendations error: {e}")
            raise Exception(f"Could not get movie recommendations: {str(e)}")
    
    async def get_music_recommendations(self, location: str, limit: int = 5) -> Dict:
        """Get music recommendations"""
        try:
            print(f"🎵 Getting music recommendations...")
            
            loop = asyncio.get_event_loop()
            
            # Get music recommendations from Qloo API
            music_response = await loop.run_in_executor(
                None,
                self.qloo.get_insights,
                "urn:entity:music",
                None,  # interests
                location,
                None,  # demographics
                {"filter.tags": "urn:tag:genre:music:pop"},
                limit
            )
            
            music = self._process_entities(music_response, "music")
            
            result = {
                "music": music,
                "source": "Qloo API",
                "location": location
            }
            
            print(f"✅ {len(music)} music recommendations received")
            return result
            
        except Exception as e:
            print(f"❌ Music recommendations error: {e}")
            raise Exception(f"Could not get music recommendations: {str(e)}")
    
    async def get_book_recommendations(self, location: str, limit: int = 5) -> Dict:
        """Get book recommendations"""
        try:
            print(f"📚 Getting book recommendations...")
            
            loop = asyncio.get_event_loop()
            
            # Get book recommendations from Qloo API
            books_response = await loop.run_in_executor(
                None,
                self.qloo.get_insights,
                "urn:entity:book",
                None,  # interests
                location,
                None,  # demographics
                {"filter.tags": "urn:tag:genre:media:fiction"},
                limit
            )
            
            books = self._process_entities(books_response, "books")
            
            result = {
                "books": books,
                "source": "Qloo API",
                "location": location
            }
            
            print(f"✅ {len(books)} book recommendations received")
            return result
            
        except Exception as e:
            print(f"❌ Book recommendations error: {e}")
            raise Exception(f"Could not get book recommendations: {str(e)}")
    
    async def get_game_recommendations(self, location: str, limit: int = 5) -> Dict:
        """Get game recommendations"""
        try:
            print(f"🎮 Getting game recommendations...")
            
            loop = asyncio.get_event_loop()
            
            # Get game recommendations from Qloo API
            games_response = await loop.run_in_executor(
                None,
                self.qloo.get_insights,
                "urn:entity:game",
                None,  # interests
                location,
                None,  # demographics
                {"filter.tags": "urn:tag:genre:media:action"},
                limit
            )
            
            games = self._process_entities(games_response, "games")
            
            result = {
                "games": games,
                "source": "Qloo API",
                "location": location
            }
            
            print(f"✅ {len(games)} game recommendations received")
            return result
            
        except Exception as e:
            print(f"❌ Game recommendations error: {e}")
            raise Exception(f"Could not get game recommendations: {str(e)}")
    
    async def get_demographic_analysis(self, location: str) -> Dict:
        """Get demographic analysis"""
        try:
            print(f"👥 Getting demographic analysis for {location}...")
            
            loop = asyncio.get_event_loop()
            
            # Get demographic analysis from Qloo API
            demographics_response = await loop.run_in_executor(
                None,
                self.qloo.get_demographic_insights,
                "urn:entity:place",
                {"location": location}
            )
            
            demographics = self._process_demographics(demographics_response)
            
            result = {
                "demographics": demographics,
                "source": "Qloo API",
                "location": location
            }
            
            print(f"✅ Demographic analysis received")
            return result
            
        except Exception as e:
            print(f"❌ Demographic analysis error: {e}")
            raise Exception(f"Could not get demographic analysis: {str(e)}")
    
    def _process_demographics(self, response: Dict) -> List[Dict]:
        """Process demographic data"""
        try:
            if "error" in response:
                print(f"❌ Demographic API error: {response['error']}")
                return []
            
            # Process demographic data
            demographics = response.get("results", {}).get("demographics", [])
            processed = []
            
            for demo in demographics:
                processed_demo = {
                    "name": demo.get("category", "Unknown"),
                    "description": f"Age group: {demo.get('age_group', 'N/A')}, Gender: {demo.get('gender', 'N/A')}",
                    "percentage": demo.get("percentage", 0),
                    "affinity_score": demo.get("affinity_score", 0)
                }
                processed.append(processed_demo)
            
            return processed
            
        except Exception as e:
            print(f"❌ Demographic data processing error: {e}")
            return [] 