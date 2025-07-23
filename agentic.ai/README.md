# 🏨 AI Concierge - Basit Chat Sistemi

Otellerde müşterileri karşılayan basit AI Concierge chat sistemi. FastAPI, LangChain, LLM ve Qloo API entegrasyonu ile geliştirilmiş minimal konuk deneyimi platformu.

## 🎯 Özellikler

### 🤖 AI Concierge Chat Yetenekleri
- **Kişiselleştirilmiş Öneriler**: Qloo API ile kültürel zeka tabanlı öneriler
- **Çok Dilli Destek**: Türkçe, İngilizce ve diğer dillerde konuşma
- **Lokasyon Bazlı Öneriler**: Otel çevresindeki restoran, aktivite ve mekanlar
- **Otel Bilgileri**: Oda servisi, spa, havuz, fitness merkezi bilgileri
- **Basit Chat Arayüzü**: Web tabanlı chat arayüzü

### 🏗️ Teknik Mimari
- **FastAPI**: Hızlı ve modern web API framework
- **LangChain**: LLM entegrasyonu ve prompt yönetimi
- **Qloo API**: Kültürel zeka ve kişiselleştirilmiş öneriler
- **OpenAI GPT**: Chat modeli
- **Basit Dosya Tabanlı Storage**: JSON dosyaları ile veri saklama

## 📁 Basit Proje Yapısı

```
ai.concierge/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI uygulaması
│   ├── config.py              # Konfigürasyon ayarları
│   ├── core/
│   │   ├── __init__.py
│   │   ├── concierge.py       # Ana Concierge sınıfı
│   │   ├── qloo_integration.py # Qloo API entegrasyonu
│   │   └── prompt_templates.py # Prompt şablonları
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── chat.py           # Chat şemaları
│   └── utils/
│       ├── __init__.py
│       └── logger.py         # Logging utility
├── data/
│   ├── guests.json           # Konuk verileri
│   └── chat_history.json     # Chat geçmişi
├── static/
│   └── chat.html             # Basit chat arayüzü
├── tests/
│   └── test_concierge.py
├── requirements.txt
├── env.example
└── README.md
```

## 🚀 Hızlı Kurulum

### 1. Gereksinimler
```bash
# Python 3.9+ gerekli
python --version

# Virtual environment oluştur
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Bağımlılıkları yükle
pip install -r requirements.txt
```

### 2. Ortam Değişkenleri
```bash
# .env dosyasını oluştur
cp env.example .env

# OpenAI API anahtarını ekle
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Uygulamayı Çalıştır
```bash
# Development modunda
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Tarayıcıda aç
# http://localhost:8000
```

## 🔧 Konfigürasyon

### Ana Konfigürasyon (`app/config.py`)
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Keys
    openai_api_key: str
    qloo_api_key: str = "mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw"
    qloo_base_url: str = "https://hackathon.api.qloo.com"
    
    # Hotel Configuration
    hotel_name: str = "Grand Hotel Istanbul"
    hotel_location: str = "Istanbul, Turkey"
    
    # LLM Configuration
    llm_model: str = "gpt-4"
    max_tokens: int = 1000
    temperature: float = 0.7
    
    class Config:
        env_file = ".env"
```

## 🤖 AI Concierge Sınıfı

### Ana Concierge Sınıfı (`app/core/concierge.py`)
```python
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from .qloo_integration import QlooIntegration
from .prompt_templates import CONCIERGE_PROMPT_TEMPLATE

class AIConcierge:
    def __init__(self, config):
        self.config = config
        self.llm = ChatOpenAI(
            model_name=config.llm_model,
            temperature=config.temperature,
            max_tokens=config.max_tokens
        )
        self.qloo = QlooIntegration(config)
        self.chain = LLMChain(
            llm=self.llm,
            prompt=CONCIERGE_PROMPT_TEMPLATE
        )
    
    async def process_guest_request(self, guest_id: str, message: str):
        """Konuk isteğini işle ve yanıt ver"""
        
        # Qloo'dan kişiselleştirilmiş öneriler al
        recommendations = await self.qloo.get_personalized_recommendations(
            location=self.config.hotel_location
        )
        
        # LangChain ile yanıt oluştur
        response = await self.chain.arun(
            guest_message=message,
            recommendations=recommendations,
            hotel_info=self.config.hotel_name,
            location=self.config.hotel_location
        )
        
        return response
```

## 🌐 API Endpoints

### Chat API (`app/main.py`)
```python
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.schemas.chat import ChatRequest, ChatResponse
from app.core.concierge import AIConcierge
from app.config import Settings

app = FastAPI(title="AI Concierge", version="1.0.0")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Konfigürasyon
settings = Settings()
concierge = AIConcierge(settings)

@app.get("/", response_class=HTMLResponse)
async def chat_interface():
    """Chat arayüzü"""
    with open("static/chat.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Chat API endpoint"""
    try:
        response = await concierge.process_guest_request(
            guest_id=request.guest_id,
            message=request.message
        )
        
        return ChatResponse(
            message=response,
            guest_id=request.guest_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

## 📊 Qloo Entegrasyonu

### Qloo Entegrasyon Sınıfı (`app/core/qloo_integration.py`)
```python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'llm.qlooapi'))

from qloo_llm_integration import QlooLLMIntegration, QlooConfig

class QlooIntegration:
    def __init__(self, config):
        qloo_config = QlooConfig(
            api_key=config.qloo_api_key,
            base_url=config.qloo_base_url
        )
        self.qloo = QlooLLMIntegration(qloo_config)
    
    async def get_personalized_recommendations(self, location: str):
        """Kişiselleştirilmiş öneriler al"""
        
        # Restoran önerileri
        restaurants = await self.qloo.get_insights(
            entity_type="urn:entity:place",
            location=location,
            filters={"filter.tags": "urn:tag:cuisine:restaurant"},
            limit=5
        )
        
        # Aktivite önerileri
        activities = await self.qloo.get_insights(
            entity_type="urn:entity:place",
            location=location,
            filters={"filter.tags": "urn:tag:activity"},
            limit=5
        )
        
        return {
            "restaurants": restaurants.get("results", {}).get("entities", []),
            "activities": activities.get("results", {}).get("entities", [])
        }
```

## 📝 Prompt Şablonları

### Prompt Şablonları (`app/core/prompt_templates.py`)
```python
from langchain.prompts import PromptTemplate

CONCIERGE_PROMPT_TEMPLATE = PromptTemplate(
    input_variables=["guest_message", "recommendations", "hotel_info", "location"],
    template="""
    Sen {hotel_info} otelinin AI Concierge'ısın. Konuklara yardımcı olmak için buradasın.
    
    Otel Lokasyonu: {location}
    
    Qloo'dan gelen öneriler:
    Restoranlar: {recommendations[restaurants]}
    Aktiviteler: {recommendations[activities]}
    
    Konuk Mesajı: {guest_message}
    
    Lütfen konuğa yardımcı ol. Türkçe yanıt ver. Kişiselleştirilmiş öneriler sun.
    Otel hizmetleri, restoran önerileri, aktiviteler hakkında bilgi ver.
    """
)
```

## 📋 Veri Şemaları

### Chat Şemaları (`app/schemas/chat.py`)
```python
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ChatRequest(BaseModel):
    guest_id: str
    message: str

class ChatResponse(BaseModel):
    message: str
    guest_id: str
    timestamp: datetime = datetime.now()
```

## 🎨 Basit Chat Arayüzü

### HTML Arayüzü (`static/chat.html`)
```html
<!DOCTYPE html>
<html>
<head>
    <title>AI Concierge Chat</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .chat-container { max-width: 600px; margin: 0 auto; }
        .chat-box { height: 400px; border: 1px solid #ccc; overflow-y: scroll; padding: 10px; }
        .input-area { margin-top: 10px; }
        .input-area input { width: 80%; padding: 10px; }
        .input-area button { width: 18%; padding: 10px; }
        .message { margin: 10px 0; padding: 10px; border-radius: 5px; }
        .user-message { background: #e3f2fd; text-align: right; }
        .bot-message { background: #f5f5f5; }
    </style>
</head>
<body>
    <div class="chat-container">
        <h1>🏨 AI Concierge</h1>
        <div class="chat-box" id="chatBox"></div>
        <div class="input-area">
            <input type="text" id="messageInput" placeholder="Mesajınızı yazın...">
            <button onclick="sendMessage()">Gönder</button>
        </div>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value;
            if (!message) return;

            // Kullanıcı mesajını göster
            addMessage(message, 'user');
            input.value = '';

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        guest_id: 'guest_123',
                        message: message
                    })
                });

                const data = await response.json();
                addMessage(data.message, 'bot');
            } catch (error) {
                addMessage('Üzgünüm, bir hata oluştu.', 'bot');
            }
        }

        function addMessage(message, sender) {
            const chatBox = document.getElementById('chatBox');
            const div = document.createElement('div');
            div.className = `message ${sender}-message`;
            div.textContent = message;
            chatBox.appendChild(div);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        // Enter tuşu ile gönderme
        document.getElementById('messageInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    </script>
</body>
</html>
```

## 🧪 Test

### Test Dosyası (`tests/test_concierge.py`)
```python
import pytest
from app.core.concierge import AIConcierge
from app.config import Settings

@pytest.mark.asyncio
async def test_concierge_response():
    """Concierge yanıt testi"""
    settings = Settings()
    concierge = AIConcierge(settings)
    
    response = await concierge.process_guest_request(
        guest_id="test_guest",
        message="Merhaba, otel hakkında bilgi alabilir miyim?"
    )
    
    assert response is not None
    assert len(response) > 10
```

## 🚀 Çalıştırma

```bash
# 1. Bağımlılıkları yükle
pip install -r requirements.txt

# 2. .env dosyasını oluştur ve API anahtarını ekle
cp env.example .env
# .env dosyasını düzenle ve OPENAI_API_KEY ekle

# 3. Uygulamayı çalıştır
uvicorn app.main:app --reload

# 4. Tarayıcıda aç
# http://localhost:8000
```

## 📊 Özellikler

- ✅ **Basit Chat Arayüzü**: Web tabanlı chat
- ✅ **Qloo Entegrasyonu**: Kişiselleştirilmiş öneriler
- ✅ **LangChain**: LLM yönetimi
- ✅ **FastAPI**: Modern API framework
- ✅ **Çok Dilli Destek**: Türkçe/İngilizce
- ✅ **Lokasyon Bazlı Öneriler**: Restoran ve aktivite önerileri

## 🔧 Geliştirme

Bu basit yapı üzerine şu özellikler eklenebilir:
- Konuk profilleri
- Chat geçmişi saklama
- Rezervasyon sistemi
- Daha gelişmiş UI
- Ses entegrasyonu
- Mobil uygulama

Bu minimal yapı ile hızlıca çalışan bir AI Concierge sistemi oluşturabilirsiniz! 