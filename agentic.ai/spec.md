# 🏨 AI Concierge - Code Specification

## 📋 Proje Genel Bakış

**AI Concierge**, otel konukları için geliştirilmiş LLM merkezli agentik mimari ile çalışan bir AI destekli Concierge sistemidir. Sistem, Google Gemini LLM ve Qloo API entegrasyonu ile kişiselleştirilmiş öneriler sunar.

### 🎯 Ana Özellikler
- **LLM Merkezli Agentik Mimari**: Kullanıcı intent'ini analiz eden, API çağrıları yapan ve doğal dil yanıtları üreten modüler sistem
- **Qloo API Entegrasyonu**: Kültürel zeka tabanlı kişiselleştirilmiş öneriler
- **FastAPI Web Framework**: Modern, hızlı ve async web API
- **Gemini LLM**: Google'ın en son LLM modeli ile doğal dil işleme
- **Web Chat Arayüzü**: Kullanıcı dostu chat deneyimi

## 🏗️ Sistem Mimarisi

### Genel Mimari Yaklaşım
```
User Query → Intent Analysis LLM → API Call Executor → Response Generation LLM → Natural Language Response
```

### Modüler Bileşenler
1. **Intent Analysis LLM**: Kullanıcı mesajını analiz eder ve hangi API çağrılarının gerekli olduğunu belirler
2. **API Call Executor**: Qloo API ve diğer servislerle iletişim kurar
3. **Response Generation LLM**: API sonuçlarını kullanarak doğal dil yanıtı oluşturur
4. **Concierge Agent**: Tüm bileşenleri koordine eden ana agent

## 📁 Proje Yapısı

```
ai.concierge/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI uygulaması ve endpoint'ler
│   ├── config.py              # Konfigürasyon ayarları
│   ├── core/
│   │   ├── __init__.py
│   │   ├── concierge.py       # Ana Concierge sınıfı
│   │   ├── qloo_integration.py # Qloo API entegrasyonu
│   │   ├── prompt_templates.py # Prompt şablonları
│   │   ├── agent/
│   │   │   ├── __init__.py
│   │   │   ├── concierge_agent.py    # Ana agent koordinatörü
│   │   │   ├── intent_analyzer.py    # Intent analiz LLM
│   │   │   ├── api_executor.py       # API çağrı executor
│   │   │   └── response_generator.py # Yanıt üretim LLM
│   │   ├── llm/
│   │   │   ├── __init__.py
│   │   │   ├── gemini_wrapper.py     # Gemini LLM wrapper
│   │   │   └── prompts/
│   │   └── tools/
│   │       ├── __init__.py
│   │       ├── base_tool.py          # Temel tool sınıfı
│   │       └── qloo_tools.py         # Qloo API tools
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── chat.py           # Pydantic şemaları
│   └── utils/
│       ├── __init__.py
│       └── logger.py         # Logging utility
├── static/
│   └── chat.html             # Web chat arayüzü
├── tests/
│   ├── 1.test_concierge.py           # Temel concierge testleri
│   ├── 2.test_gemini.py              # Gemini LLM testleri
│   ├── 3.test_qloo_api.py            # Qloo API testleri
│   ├── 4.test_intent_analysis.py     # Intent analiz testleri
│   └── 5.test_full_integration.py    # Tam entegrasyon testleri
├── requirements.txt
├── run.py                    # Uygulama başlatıcı
└── README.md
```

## 🔧 Teknik Detaylar

### 1. Konfigürasyon Sistemi (`app/config.py`)

```python
class Settings(BaseSettings):
    # API Keys
    gemini_api_key: str = "AIzaSyBJ61NA77E5raFEVUKSrwsKabrjA0ASU3E"
    qloo_api_key: str = "mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw"
    qloo_base_url: str = "https://hackathon.api.qloo.com"
    
    # Hotel Configuration
    hotel_name: str = "Grand Hotel Istanbul"
    hotel_location: str = "Istanbul, Turkey"
    
    # LLM Configuration
    llm_model: str = "gemini-2.0-flash"
    max_tokens: int = 1000
    temperature: float = 0.7
```

**Özellikler:**
- Pydantic Settings ile environment variable desteği
- API anahtarları ve model konfigürasyonu
- Otel bilgileri ve lokasyon ayarları

### 2. Gemini LLM Wrapper (`app/core/llm/gemini_wrapper.py`)

```python
class GeminiWrapper:
    def __init__(self, config):
        self.config = config
        self.api_key = config.gemini_api_key
        self.model = config.llm_model
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"
    
    async def generate_content(self, prompt: str) -> str:
        # Async Gemini API çağrısı
```

**Özellikler:**
- Async/sync API çağrı desteği
- Error handling ve logging
- Configurable model parametreleri

### 3. LLM Merkezli Agent (`app/core/agent/concierge_agent.py`)

```python
class LLMCentricConciergeAgent:
    def __init__(self, config):
        self.llm = GeminiWrapper(config)
        self.intent_analyzer = IntentAnalysisLLM(self.llm)
        self.response_generator = ResponseGenerationLLM(self.llm)
        self.api_executor = APICallExecutor(qloo_integration)
    
    async def process_request(self, user_message: str) -> str:
        # 1. Intent Analysis
        intent = await self.intent_analyzer.analyze_intent(user_message)
        
        # 2. API Calls
        api_results = await self.api_executor.execute_api_calls(
            intent.get("api_calls_needed", [])
        )
        
        # 3. Response Generation
        response = await self.response_generator.generate_response(
            user_message, api_results, intent
        )
        
        return response
```

**Akış:**
1. **Intent Analysis**: Kullanıcı mesajını analiz eder
2. **API Execution**: Gerekli API çağrılarını yapar
3. **Response Generation**: Doğal dil yanıtı oluşturur

### 4. Intent Analysis LLM (`app/core/agent/intent_analyzer.py`)

```python
class IntentAnalysisLLM:
    def __init__(self, llm):
        self.llm = llm
    
    async def analyze_intent(self, user_message: str) -> Dict:
        prompt = f"""
        Kullanıcı mesajını analiz et ve hangi API çağrılarının gerekli olduğunu belirle:
        
        Mesaj: {user_message}
        
        JSON formatında yanıt ver:
        {{
            "intent": "restaurant_recommendation|activity_recommendation|hotel_info|general_help",
            "api_calls_needed": ["qloo_restaurants", "qloo_activities"],
            "parameters": {{
                "location": "Istanbul",
                "category": "restaurants"
            }}
        }}
        """
        
        response = await self.llm.generate_content(prompt)
        return self._parse_json_response(response)
```

**Özellikler:**
- Kullanıcı intent'ini belirler
- Gerekli API çağrılarını listeler
- Parametreleri çıkarır

### 5. API Call Executor (`app/core/agent/api_executor.py`)

```python
class APICallExecutor:
    def __init__(self, qloo_integration):
        self.qloo = qloo_integration
    
    async def execute_api_calls(self, api_calls: List[str]) -> Dict:
        results = {}
        
        for api_call in api_calls:
            if api_call == "qloo_restaurants":
                results["restaurants"] = await self.qloo.get_personalized_recommendations(
                    location="Istanbul", user_message="restaurant"
                )
            elif api_call == "qloo_activities":
                results["activities"] = await self.qloo.get_personalized_recommendations(
                    location="Istanbul", user_message="activity"
                )
        
        return results
```

**Özellikler:**
- Qloo API entegrasyonu
- Async API çağrıları
- Error handling

### 6. Response Generation LLM (`app/core/agent/response_generator.py`)

```python
class ResponseGenerationLLM:
    def __init__(self, llm):
        self.llm = llm
    
    async def generate_response(self, user_message: str, api_results: Dict, intent: Dict) -> str:
        prompt = f"""
        Kullanıcı mesajına doğal dil yanıtı oluştur:
        
        Kullanıcı: {user_message}
        Intent: {intent}
        API Sonuçları: {api_results}
        
        Otel Concierge'ı olarak nazik ve yardımcı bir yanıt ver.
        """
        
        return await self.llm.generate_content(prompt)
```

**Özellikler:**
- API sonuçlarını doğal dile çevirir
- Concierge tonunda yanıtlar
- Context-aware response generation

### 7. Qloo Integration (`app/core/qloo_integration.py`)

```python
class QlooIntegration:
    def __init__(self, config):
        qloo_config = QlooConfig(
            api_key=config.qloo_api_key,
            base_url=config.qloo_base_url
        )
        self.qloo = QlooLLMIntegration(qloo_config)
    
    async def get_personalized_recommendations(self, location: str, user_message: str = "") -> Dict:
        # Kullanıcı sorgusunu analiz et
        categories = self._analyze_user_query(user_message)
        
        # Restoran ve aktivite önerileri al
        restaurants = await self._get_places_with_tags(location, categories['restaurants'], 5)
        activities = await self._get_places_with_tags(location, categories['activities'], 5)
        
        return {
            "restaurants": restaurants,
            "activities": activities,
            "source": "Qloo API"
        }
```

**Özellikler:**
- Kültürel zeka tabanlı öneriler
- Kategori bazlı filtreleme
- Async API çağrıları
- Error handling ve fallback

### 8. FastAPI Endpoints (`app/main.py`)

```python
app = FastAPI(title="AI Concierge", version="1.0.0")

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    response = await concierge.process_guest_request(
        guest_id=request.guest_id,
        message=request.message
    )
    return ChatResponse(message=response, guest_id=request.guest_id)

@app.get("/hotel/info", response_model=HotelInfoResponse)
async def get_hotel_info():
    hotel_info = await concierge.get_hotel_info()
    return HotelInfoResponse(**hotel_info)

@app.get("/recommendations/{category}", response_model=RecommendationResponse)
async def get_recommendations(category: str):
    items = await concierge.get_quick_recommendations(category)
    return RecommendationResponse(category=category, items=items, total_count=len(items))
```

**Endpoint'ler:**
- `POST /chat`: Ana chat endpoint'i
- `GET /hotel/info`: Otel bilgileri
- `GET /recommendations/{category}`: Kategori bazlı öneriler
- `GET /health`: Sağlık kontrolü

## 🧪 Test Sistemi

### Test Hiyerarşisi
1. **1.test_concierge.py**: Temel concierge fonksiyonalitesi
2. **2.test_gemini.py**: Gemini LLM entegrasyonu
3. **3.test_qloo_api.py**: Qloo API entegrasyonu
4. **4.test_intent_analysis.py**: Intent analiz sistemi
5. **5.test_full_integration.py**: Tam entegrasyon testleri

### Test Özellikleri
- Async test desteği
- Mock API çağrıları
- Error scenario testleri
- Integration testleri

## 🌐 Web Arayüzü

### Chat Interface (`static/chat.html`)
- Modern, responsive tasarım
- Real-time chat deneyimi
- JavaScript ile API entegrasyonu
- Error handling ve loading states

## 📦 Bağımlılıklar

### Core Dependencies
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0
google-generativeai>=0.3.1,<0.4.0
aiohttp==3.9.1
requests==2.31.0
```

### Development Dependencies
```txt
pytest==7.4.3
pytest-asyncio==0.21.1
httpx==0.25.2
```

## 🚀 Deployment

### Development
```bash
# Virtual environment
python -m venv venv
source venv/bin/activate

# Dependencies
pip install -r requirements.txt

# Run
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production
```bash
# Gunicorn ile
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 🔒 Güvenlik

### API Key Management
- Environment variables kullanımı
- Pydantic Settings ile validation
- Production'da secure key storage

### Error Handling
- Comprehensive exception handling
- User-friendly error messages
- Logging ve monitoring

## 📊 Monitoring ve Logging

### Logging Sistemi
- Structured logging
- Error tracking
- Performance monitoring
- API call logging

### Health Checks
- `/health` endpoint
- Service availability monitoring
- Dependency health checks

## 🔄 Gelecek Geliştirmeler

### Planlanan Özellikler
1. **Multi-language Support**: Daha fazla dil desteği
2. **Voice Integration**: Ses tabanlı etkileşim
3. **Personalization**: Kullanıcı profili ve geçmiş
4. **Analytics**: Kullanım analitikleri
5. **Mobile App**: Native mobile uygulama

### Teknik İyileştirmeler
1. **Caching**: Redis ile response caching
2. **Rate Limiting**: API rate limiting
3. **Database**: PostgreSQL entegrasyonu
4. **Microservices**: Servis ayrıştırması
5. **Containerization**: Docker deployment

## 📝 API Documentation

### Swagger UI
- `http://localhost:8000/docs`
- Interactive API documentation
- Request/response examples
- Schema validation

### OpenAPI Specification
- Auto-generated API docs
- Type safety
- Client code generation

## 🎯 Sonuç

AI Concierge sistemi, modern LLM teknolojilerini kullanarak otel konukları için kişiselleştirilmiş ve akıllı bir deneyim sunar. Modüler mimarisi sayesinde kolayca genişletilebilir ve sürdürülebilir bir yapıya sahiptir.

**Ana Başarılar:**
- ✅ LLM merkezli agentik mimari
- ✅ Qloo API entegrasyonu
- ✅ Async/await pattern
- ✅ Comprehensive test coverage
- ✅ Modern web framework (FastAPI)
- ✅ Production-ready code structure 