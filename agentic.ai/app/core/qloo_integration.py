import sys
import os
import asyncio
import re
from typing import Dict, List, Optional

# Qloo API entegrasyonu için path ekle
qloo_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'llm.qlooapi')
sys.path.append(qloo_path)

try:
    from qloo_llm_integration import QlooLLMIntegration, QlooConfig
    print(f"✅ Qloo API entegrasyonu başarıyla yüklendi: {qloo_path}")
except ImportError as e:
    print(f"❌ Qloo API entegrasyonu bulunamadı: {e}")
    print(f"🔍 Aranan path: {qloo_path}")
    raise ImportError("Qloo API entegrasyonu gerekli")

class QlooIntegration:
    """Qloo API entegrasyonu için wrapper sınıfı"""
    
    def __init__(self, config):
        self.config = config
        
        try:
            qloo_config = QlooConfig(
                api_key=config.qloo_api_key,
                base_url=config.qloo_base_url
            )
            self.qloo = QlooLLMIntegration(qloo_config)
            print(f"✅ Qloo API bağlantısı kuruldu: {config.qloo_base_url}")
        except Exception as e:
            print(f"❌ Qloo API bağlantısı kurulamadı: {e}")
            raise Exception(f"Qloo API bağlantısı kurulamadı: {e}")
    
    def _analyze_user_query(self, message: str) -> Dict[str, List[str]]:
        """Kullanıcı sorgusunu analiz edip uygun tag'ları belirle"""
        message_lower = message.lower()
        
        # Türkçe ve İngilizce anahtar kelimeler
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
        
        # Kategori belirleme
        categories = {
            'restaurants': [],
            'activities': []
        }
        
        # Restoran kategorisi kontrolü
        if any(keyword in message_lower for keyword in restaurant_keywords):
            categories['restaurants'] = [
                'urn:tag:category:place:restaurant',
                'urn:tag:cuisine:restaurant:turkish',
                'urn:tag:cuisine:restaurant:mediterranean'
            ]
        
        # Aktivite kategorisi kontrolü
        if any(keyword in message_lower for keyword in activity_keywords):
            categories['activities'] = [
                'urn:tag:category:place:entertainment',
                'urn:tag:category:place:museum',
                'urn:tag:category:place:park'
            ]
        
        # Eğer hiçbir kategori belirlenemezse, varsayılan olarak her ikisini de ekle
        if not categories['restaurants'] and not categories['activities']:
            categories['restaurants'] = ['urn:tag:category:place:restaurant']
            categories['activities'] = ['urn:tag:category:place:entertainment']
        
        return categories
    
    async def get_personalized_recommendations(self, location: str, user_message: str = "") -> Dict:
        """Kişiselleştirilmiş öneriler al"""
        
        try:
            print(f"🔍 {location} için Qloo API'den öneriler alınıyor...")
            print(f"📝 Kullanıcı mesajı: {user_message}")
            
            # Kullanıcı sorgusunu analiz et
            categories = self._analyze_user_query(user_message)
            print(f"🏷️ Belirlenen kategoriler: {categories}")
            
            loop = asyncio.get_event_loop()
            
            # Restoran önerileri
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
            
            # Aktivite önerileri
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
            
            print(f"✅ {len(restaurants)} restoran, {len(activities)} aktivite önerisi alındı")
            return result
            
        except Exception as e:
            print(f"❌ Qloo API hatası: {e}")
            raise Exception(f"Qloo API'den veri alınamadı: {str(e)}")
    
    def _get_places_with_tags(self, location: str, tags: List[str], limit: int) -> Dict:
        """Belirli tag'lar ile place sorgusu"""
        try:
            # İlk tag'ı kullan (API sadece bir tag kabul ediyor)
            primary_tag = tags[0] if tags else "urn:tag:category:place:restaurant"
            
            print(f"🔍 Tag ile sorgu: {primary_tag}")
            
            # Qloo API'nin gerekli parametrelerini kullan
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
            print(f"❌ Tag ile API hatası: {e}")
            # Fallback: genel place sorgusu
            return self._get_fallback_places(location, limit)
    
    def _get_fallback_places(self, location: str, limit: int) -> Dict:
        """Fallback place sorgusu"""
        try:
            print(f"🔄 Fallback sorgu: {location}")
            # Genel place sorgusu - sadece lokasyon ile
            insights = self.qloo.get_insights(
                entity_type="urn:entity:place",
                location=location,
                limit=limit * 2,  # Daha fazla sonuç al
                filters={
                    "filter.location.query": location
                }
            )
            return insights
        except Exception as e:
            print(f"❌ Fallback place API hatası: {e}")
            return {"error": str(e)}
    
    def _process_entities(self, response: Dict, entity_type: str) -> List[Dict]:
        """API yanıtını işle ve kullanılabilir formata dönüştür"""
        try:
            if "error" in response:
                print(f"❌ {entity_type} için API hatası: {response['error']}")
                return []
            
            entities = response.get("results", {}).get("entities", [])
            processed = []
            
            for entity in entities:
                # Entity özelliklerini al
                properties = entity.get("properties", {})
                
                processed_entity = {
                    "name": entity.get("name", "Bilinmeyen"),
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
            print(f"❌ {entity_type} verilerini işlerken hata: {e}")
            return []
    
    async def get_location_insights(self, location: str) -> Dict:
        """Lokasyon bazlı içgörüler al"""
        try:
            loop = asyncio.get_event_loop()
            
            # Genel lokasyon içgörüleri
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
            raise Exception(f"Lokasyon içgörüleri alınamadı: {str(e)}")
    
    async def search_entities(self, query: str, entity_type: str = "urn:entity:place") -> Dict:
        """Varlık arama"""
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
            raise Exception(f"Arama hatası: {str(e)}")
    
    async def get_trending_places(self, location: str, limit: int = 5) -> Dict:
        """Trend olan yerleri al"""
        try:
            print(f"📈 {location} için trend olan yerler alınıyor...")
            
            loop = asyncio.get_event_loop()
            
            # Qloo API'den trend olan place'leri al
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
            
            print(f"✅ {len(places)} trend olan yer alındı")
            return result
            
        except Exception as e:
            print(f"❌ Trend olan yerler hatası: {e}")
            raise Exception(f"Trend olan yerler alınamadı: {str(e)}")
    
    async def get_movie_recommendations(self, location: str, limit: int = 5) -> Dict:
        """Film önerileri al"""
        try:
            print(f"🎬 Film önerileri alınıyor...")
            
            loop = asyncio.get_event_loop()
            
            # Qloo API'den film önerileri al
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
            
            print(f"✅ {len(movies)} film önerisi alındı")
            return result
            
        except Exception as e:
            print(f"❌ Film önerileri hatası: {e}")
            raise Exception(f"Film önerileri alınamadı: {str(e)}")
    
    async def get_music_recommendations(self, location: str, limit: int = 5) -> Dict:
        """Müzik önerileri al"""
        try:
            print(f"🎵 Müzik önerileri alınıyor...")
            
            loop = asyncio.get_event_loop()
            
            # Qloo API'den müzik önerileri al
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
            
            print(f"✅ {len(music)} müzik önerisi alındı")
            return result
            
        except Exception as e:
            print(f"❌ Müzik önerileri hatası: {e}")
            raise Exception(f"Müzik önerileri alınamadı: {str(e)}")
    
    async def get_book_recommendations(self, location: str, limit: int = 5) -> Dict:
        """Kitap önerileri al"""
        try:
            print(f"📚 Kitap önerileri alınıyor...")
            
            loop = asyncio.get_event_loop()
            
            # Qloo API'den kitap önerileri al
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
            
            print(f"✅ {len(books)} kitap önerisi alındı")
            return result
            
        except Exception as e:
            print(f"❌ Kitap önerileri hatası: {e}")
            raise Exception(f"Kitap önerileri alınamadı: {str(e)}")
    
    async def get_game_recommendations(self, location: str, limit: int = 5) -> Dict:
        """Oyun önerileri al"""
        try:
            print(f"🎮 Oyun önerileri alınıyor...")
            
            loop = asyncio.get_event_loop()
            
            # Qloo API'den oyun önerileri al
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
            
            print(f"✅ {len(games)} oyun önerisi alındı")
            return result
            
        except Exception as e:
            print(f"❌ Oyun önerileri hatası: {e}")
            raise Exception(f"Oyun önerileri alınamadı: {str(e)}")
    
    async def get_demographic_analysis(self, location: str) -> Dict:
        """Demografik analiz al"""
        try:
            print(f"👥 {location} için demografik analiz alınıyor...")
            
            loop = asyncio.get_event_loop()
            
            # Qloo API'den demografik analiz al
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
            
            print(f"✅ Demografik analiz alındı")
            return result
            
        except Exception as e:
            print(f"❌ Demografik analiz hatası: {e}")
            raise Exception(f"Demografik analiz alınamadı: {str(e)}")
    
    def _process_demographics(self, response: Dict) -> List[Dict]:
        """Demografik verileri işle"""
        try:
            if "error" in response:
                print(f"❌ Demografik API hatası: {response['error']}")
                return []
            
            # Demografik verileri işle
            demographics = response.get("results", {}).get("demographics", [])
            processed = []
            
            for demo in demographics:
                processed_demo = {
                    "name": demo.get("category", "Bilinmeyen"),
                    "description": f"Yaş grubu: {demo.get('age_group', 'N/A')}, Cinsiyet: {demo.get('gender', 'N/A')}",
                    "percentage": demo.get("percentage", 0),
                    "affinity_score": demo.get("affinity_score", 0)
                }
                processed.append(processed_demo)
            
            return processed
            
        except Exception as e:
            print(f"❌ Demografik veri işleme hatası: {e}")
            return [] 