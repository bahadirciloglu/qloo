# 📋 Qloo + LLM Entegrasyon Projesi - Code Specification

## 🎯 Proje Genel Bakış

### Proje Adı
**Qloo Taste AI + Gemini LLM Integration Module**

### Proje Amacı
Qloo'nun consumer intelligence platformunu Google Gemini LLM ile entegre ederek, kişiselleştirilmiş ve kültürel bağlamda zengin AI deneyimleri yaratan modüler bir sistem geliştirmek.

### Teknoloji Stack
- **Backend**: Python 3.8+
- **LLM Provider**: Google Gemini (gemini-2.0-flash)
- **API**: RESTful endpoints
- **Data Source**: Qloo Taste AI API
- **Dependencies**: requests, google-generativeai, flask

## 🏗️ Modüler Mimari Yapı

### 1. Core Modules

#### `qloo_llm_integration.py` - Ana Entegrasyon Modülü
```python
# Ana entegrasyon sınıfları
@dataclass
class QlooConfig:
    api_key: str = "mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw"
    base_url: str = "https://hackathon.api.qloo.com"
    headers: Dict[str, str] = None

class QlooLLMIntegration:
    def get_insights(entity_type, interests, location, demographics, filters, limit)
    def get_heatmap(entity_id, location)
    def get_demographic_insights(entity_id, demographics)
    def search_entities(query, entity_type)
    def get_trending_entities(entity_type, limit)
    def analyze_user_taste_profile(user_interests)

class LLMEnhancer:
    def enhance_recommendation_prompt(user_interests, recommendation_type)
    def create_location_based_prompt(location, interests)
```

#### `gemini_qloo_integration.py` - Gemini Entegrasyon Modülü
```python
class GeminiQlooIntegration:
    def __init__(self):
        self.gemini_api_key = "AIzaSyBJ61NA77E5raFEVUKSrwsKabrjA0ASU3E"
        self.model = 'gemini-2.0-flash'
        
    def get_enhanced_movie_recommendations(user_interests)
    def get_location_based_recommendations(location, interests)
    def analyze_taste_profile(user_interests)
    def create_personalized_chatbot(user_message, user_interests)
    def get_multi_modal_recommendations(image_path, user_interests)
    def generate_cultural_insights(user_interests, context)
```

### 2. Modüler API Endpoints

#### Qloo API Endpoints
```
GET /v2/insights
- Purpose: Get personalized insights and recommendations
- Parameters: entity_type, interests, location, demographics, filters, limit
- Response: JSON with entities, popularity scores, cultural insights

GET /v2/entities/search
- Purpose: Search for entities by name
- Parameters: query, entity_type
- Response: JSON with matching entities

GET /v2/insights (heatmap)
- Purpose: Get geographic distribution of interest
- Parameters: entity_id, location
- Response: JSON with heatmap data

GET /v2/insights (demographics)
- Purpose: Get demographic affinity scores
- Parameters: entity_id, demographics
- Response: JSON with demographic analysis
```

#### Gemini API Endpoints
```
POST /api/gemini/generate
- Purpose: Generate content with Gemini
- Parameters: prompt, model (gemini-2.0-flash)
- Response: Generated text content

POST /api/gemini/chat
- Purpose: Conversational AI with Gemini
- Parameters: messages, context, user_profile
- Response: Conversational response
```

## 📊 Veri Modelleri

### 1. Qloo Entity Model
```python
@dataclass
class QlooEntity:
    entity_id: str
    name: str
    type: str
    subtype: str
    popularity: float
    properties: Dict[str, Any]
    tags: List[Dict[str, str]]
    external: Dict[str, List[Dict[str, Any]]]
    query: Dict[str, Any]
```

### 2. User Profile Model
```python
@dataclass
class UserProfile:
    interests: List[str]
    location: Optional[str]
    demographics: Optional[Dict[str, Any]]
    cultural_patterns: List[str]
    preferences: Dict[str, Any]
    session_id: str
    created_at: datetime
```

### 3. Recommendation Model
```python
@dataclass
class Recommendation:
    name: str
    popularity: float
    description: str
    cultural_context: str
    affinity_score: float
    tags: List[str]
    location: Optional[str]
    price_range: Optional[str]
    rating: Optional[float]
```

### 4. Cultural Analysis Model
```python
@dataclass
class CulturalAnalysis:
    archetype: str
    cultural_patterns: List[str]
    cross_cultural_connections: List[str]
    potential_interests: List[str]
    lifestyle_insights: Dict[str, Any]
    social_context: Dict[str, Any]
    confidence_score: float
```

## ⚙️ Konfigürasyon

### Environment Variables
```bash
# Qloo Configuration
QLOO_API_KEY=mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw
QLOO_BASE_URL=https://hackathon.api.qloo.com

# Gemini Configuration
GEMINI_API_KEY=AIzaSyBJ61NA77E5raFEVUKSrwsKabrjA0ASU3E
GEMINI_MODEL=gemini-2.0-flash

# Application Configuration
DEBUG=True
LOG_LEVEL=INFO
REQUEST_TIMEOUT=30
MAX_RETRIES=3
CACHE_TTL=3600
```

### Dependencies (requirements.txt)
```
requests>=2.28.0
google-generativeai>=0.3.0
flask>=2.3.0
python-dotenv>=1.0.0
dataclasses-json>=0.6.0
typing-extensions>=4.5.0
redis>=4.5.0
celery>=5.3.0
```

Bu comprehensive code specification, mevcut projenizin tüm detaylarını kapsar ve Gemini API odaklı modüler bir yapı sunar. Diğer projelerde kullanım için hazır bir modül olarak tasarlanmıştır.

## 🔧 Modüler Entegrasyon

### 1. Ana Entegrasyon Sınıfı
```python
class QlooGeminiModule:
    """
    Ana modül sınıfı - diğer projelerde kullanım için
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.qloo_config = QlooConfig()
        self.qloo_integration = QlooLLMIntegration(self.qloo_config)
        self.gemini_integration = GeminiQlooIntegration()
        self.enhancer = LLMEnhancer(self.qloo_integration)
        
    def get_personalized_recommendations(self, 
                                       user_interests: List[str], 
                                       recommendation_type: str = "movies",
                                       location: Optional[str] = None) -> Dict:
        """Kişiselleştirilmiş öneriler al"""
        
    def analyze_user_culture(self, user_interests: List[str]) -> CulturalAnalysis:
        """Kullanıcı kültürel profilini analiz et"""
        
    def create_cultural_chatbot(self, 
                               message: str, 
                               user_profile: UserProfile) -> str:
        """Kültürel bağlamda chatbot yanıtı oluştur"""
        
    def get_location_insights(self, 
                             location: str, 
                             interests: List[str]) -> Dict:
        """Lokasyon bazlı içgörüler al"""
        
    def get_trending_analysis(self, 
                             entity_type: str = "urn:entity:movie") -> Dict:
        """Trend analizi yap"""
```

### 2. Flask Blueprint Entegrasyonu
```python
from flask import Blueprint, request, jsonify

qloo_gemini_bp = Blueprint('qloo_gemini', __name__)
qloo_module = QlooGeminiModule()

@qloo_gemini_bp.route('/recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    user_interests = data.get('interests', [])
    recommendation_type = data.get('type', 'movies')
    location = data.get('location')
    
    result = qloo_module.get_personalized_recommendations(
        user_interests, recommendation_type, location
    )
    return jsonify(result)

@qloo_gemini_bp.route('/cultural-analysis', methods=['POST'])
def analyze_culture():
    data = request.json
    user_interests = data.get('interests', [])
    
    analysis = qloo_module.analyze_user_culture(user_interests)
    return jsonify(analysis.__dict__)

@qloo_gemini_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    user_profile = UserProfile(**data.get('user_profile', {}))
    
    response = qloo_module.create_cultural_chatbot(message, user_profile)
    return jsonify({'response': response})
```

## 🧪 Test Specifications

### 1. Unit Tests
```python
# test_qloo_module.py
import unittest
from qloo_gemini_module import QlooGeminiModule

class TestQlooGeminiModule(unittest.TestCase):
    def setUp(self):
        self.module = QlooGeminiModule()
        
    def test_get_personalized_recommendations(self):
        interests = ["The Matrix", "Inception"]
        result = self.module.get_personalized_recommendations(interests, "movies")
        self.assertIsInstance(result, dict)
        self.assertIn('recommendations', result)
        
    def test_analyze_user_culture(self):
        interests = ["Nirvana", "Pulp Fiction"]
        analysis = self.module.analyze_user_culture(interests)
        self.assertIsInstance(analysis, CulturalAnalysis)
        self.assertIsNotNone(analysis.archetype)
        
    def test_location_insights(self):
        location = "Istanbul"
        interests = ["Turkish coffee", "historical sites"]
        insights = self.module.get_location_insights(location, interests)
        self.assertIsInstance(insights, dict)
        self.assertIn('recommendations', insights)
```

### 2. Integration Tests
```python
# test_integration.py
def test_full_recommendation_flow():
    """Tam öneri akışını test et"""
    
def test_cultural_analysis_flow():
    """Kültürel analiz akışını test et"""
    
def test_chatbot_interaction():
    """Chatbot etkileşimini test et"""
    
def test_location_based_recommendations():
    """Lokasyon bazlı önerileri test et"""
```

## 📈 Kullanım Senaryoları

### 1. Film Önerileri
```python
# Input
user_interests = ["The Matrix", "Inception", "Blade Runner"]

# Process
module = QlooGeminiModule()
result = module.get_personalized_recommendations(user_interests, "movies")

# Output
# {
#   "recommendations": [
#     {
#       "name": "Dark City",
#       "popularity": 0.825,
#       "cultural_context": "Late 90s reality questioning",
#       "affinity_score": 0.95
#     }
#   ],
#   "cultural_insights": "Existential themes and cyberpunk aesthetics",
#   "viewing_suggestions": ["Thematic grouping", "Chronological order"]
# }
```

### 2. Lokasyon Bazlı Öneriler
```python
# Input
location = "Istanbul"
interests = ["Turkish coffee", "historical sites", "local markets"]

# Process
insights = module.get_location_insights(location, interests)

# Output
# {
#   "recommendations": [
#     {
#       "name": "Pierre Loti Hill",
#       "type": "cafe",
#       "cultural_significance": "Iconic view of Golden Horn",
#       "best_time": "Early morning or sunset",
#       "local_tips": "Take cable car up, enjoy Turkish coffee"
#     }
#   ],
#   "cultural_context": "Turkish hospitality and coffee culture",
#   "seasonal_considerations": "Spring and autumn are ideal"
# }
```

### 3. Kullanıcı Profil Analizi
```python
# Input
user_interests = ["Nirvana", "Pulp Fiction", "The Catcher in the Rye"]

# Process
analysis = module.analyze_user_culture(user_interests)

# Output
# {
#   "archetype": "Existential Aesthete/Cynic",
#   "cultural_patterns": ["Alternative/Indie Culture", "Intellectual/Literary"],
#   "cross_cultural_connections": ["American counterculture", "Postmodernism"],
#   "potential_interests": ["Beat Generation literature", "Indie rock"],
#   "lifestyle_insights": {
#     "independent": True,
#     "introspective": True,
#     "value_authenticity": True
#   },
#   "confidence_score": 0.92
# }
```

### 4. Conversational AI
```python
# Input
message = "I'm planning a weekend trip. What should I do?"
user_profile = UserProfile(
    interests=["art galleries", "local cuisine", "walking tours"],
    location="Istanbul"
)

# Process
response = module.create_cultural_chatbot(message, user_profile)

# Output
# "Based on your interests in art galleries, local cuisine, and walking tours, 
# here's a perfect weekend itinerary for Istanbul that combines cultural 
# exploration with authentic local experiences..."
```

## 🔒 Güvenlik ve Privacy

### 1. API Key Management
```python
import os
from dotenv import load_dotenv

load_dotenv()

class SecureConfig:
    QLOO_API_KEY = os.getenv('QLOO_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    
    @classmethod
    def validate_keys(cls):
        if not cls.QLOO_API_KEY or not cls.GEMINI_API_KEY:
            raise ValueError("Missing required API keys")
```

### 2. Data Privacy
```python
class PrivacyManager:
    def anonymize_user_data(self, user_data: Dict) -> Dict:
        """Kullanıcı verilerini anonimleştir"""
        
    def validate_gdpr_compliance(self, data_usage: str) -> bool:
        """GDPR uyumluluğunu kontrol et"""
        
    def get_user_consent(self, user_id: str, data_type: str) -> bool:
        """Kullanıcı onayını al"""
```

### 3. Error Handling
```python
class ErrorHandler:
    def handle_api_error(self, error: Exception) -> Dict:
        """API hatalarını handle et"""
        
    def handle_rate_limit(self, retry_after: int) -> None:
        """Rate limit durumunu handle et"""
        
    def handle_timeout(self, operation: str) -> Dict:
        """Timeout durumunu handle et"""
```

## 📊 Monitoring ve Logging

### 1. Application Logs
```python
import logging
from datetime import datetime

class QlooLogger:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('qloo_gemini.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger('qloo_gemini')
        
    def log_recommendation_request(self, user_interests: List[str], 
                                 recommendation_type: str):
        self.logger.info(f"Recommendation request: {recommendation_type} for {user_interests}")
        
    def log_cultural_analysis(self, user_interests: List[str], 
                            archetype: str):
        self.logger.info(f"Cultural analysis: {archetype} for {user_interests}")
```

### 2. Performance Metrics
```python
class PerformanceMonitor:
    def track_api_response_time(self, endpoint: str, duration: float):
        """API response time'ını takip et"""
        
    def track_success_rate(self, endpoint: str, success: bool):
        """Başarı oranını takip et"""
        
    def track_token_usage(self, model: str, tokens: int):
        """Token kullanımını takip et"""
```

## 📈 Deployment

### 1. Development Environment
```bash
# Setup
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Environment setup
cp .env.example .env
# Edit .env with your API keys

# Run tests
python -m pytest tests/

# Run module
python -c "from qloo_gemini_module import QlooGeminiModule; module = QlooGeminiModule()"
```

### 2. Production Environment
```bash
# Docker
docker build -t qloo-gemini-module .
docker run -p 5000:5000 qloo-gemini-module

# Environment variables
export QLOO_API_KEY="your_key"
export GEMINI_API_KEY="your_key"
export DEBUG=False
export LOG_LEVEL=WARNING
```

### 3. Integration with Other Projects
```python
# Diğer projelerde kullanım
from qloo_gemini_module import QlooGeminiModule

# Initialize module
qloo_module = QlooGeminiModule()

# Use in your application
def recommend_for_user(user_id: str, interests: List[str]):
    recommendations = qloo_module.get_personalized_recommendations(interests)
    return recommendations

def analyze_user_culture(user_id: str, interests: List[str]):
    analysis = qloo_module.analyze_user_culture(interests)
    return analysis
```

## 📈 Documentation

### 1. API Documentation
```python
# OpenAPI/Swagger specification
"""
openapi: 3.0.0
info:
  title: Qloo Gemini Integration API
  version: 1.0.0
  description: Cultural intelligence and personalized recommendations

paths:
  /recommendations:
    post:
      summary: Get personalized recommendations
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                interests:
                  type: array
                  items:
                    type: string
                type:
                  type: string
                  default: movies
                location:
                  type: string
      responses:
        '200':
          description: Successful recommendation
"""
```

### 2. User Guide
```markdown
# Qloo Gemini Module - User Guide

## Installation
```bash
pip install qloo-gemini-module
```

## Quick Start
```python
from qloo_gemini_module import QlooGeminiModule

module = QlooGeminiModule()
recommendations = module.get_personalized_recommendations(
    ["The Matrix", "Inception"], "movies"
)
```

## Configuration
Set environment variables:
- QLOO_API_KEY
- GEMINI_API_KEY
```

### 3. Developer Guide
```markdown
# Developer Guide

## Architecture
- QlooGeminiModule: Main integration class
- QlooLLMIntegration: Qloo API integration
- GeminiQlooIntegration: Gemini LLM integration
- LLMEnhancer: Prompt enhancement

## Contributing
1. Fork the repository
2. Create feature branch
3. Add tests
4. Submit pull request
```

## 🎯 Success Metrics

### 1. Technical Metrics
- API response time < 2 seconds
- 99.9% uptime
- < 1% error rate
- Successful integration rate > 95%
- Token usage optimization < 1000 tokens per request

### 2. Business Metrics
- User satisfaction score > 4.5/5
- Recommendation accuracy > 85%
- Cultural relevance score > 90%
- User engagement increase > 40%
- Cross-cultural understanding improvement > 60%

### 3. Quality Metrics
- Code coverage > 90%
- Documentation completeness > 95%
- Security audit score > A
- Performance benchmark compliance > 100%

## 🔄 Version Control

### Git Workflow
```bash
# Feature development
git checkout -b feature/cultural-analysis
git add .
git commit -m "Add cultural analysis functionality"
git push origin feature/cultural-analysis

# Release
git checkout main
git merge feature/cultural-analysis
git tag v1.0.0
git push origin main --tags
```

### Version History
- v1.0.0: Initial release with basic integration
- v1.1.0: Added cultural analysis
- v1.2.0: Enhanced location-based recommendations
- v1.3.0: Added conversational AI capabilities

Bu code specification, Qloo + Gemini entegrasyon modülünün tüm teknik detaylarını, mimarisini ve diğer projelerde kullanım için gerekli tüm bilgileri kapsamlı bir şekilde tanımlar. 🎉
