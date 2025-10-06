# 🏨 AI Concierge - Simple Chat System

A simple AI Concierge chat system for welcoming customers in hotels. Developed with FastAPI, LangChain, LLM, and Qloo API integration for a minimal guest experience platform.

## 🎯 Features

### 🤖 AI Concierge Chat Capabilities
- **Personalized Recommendations**: Cultural intelligence-based recommendations with Qloo API
- **Multi-language Support**: Conversation in Turkish, English, and other languages
- **Location-based Recommendations**: Restaurants, activities, and venues around the hotel
- **Hotel Information**: Room service, spa, pool, fitness center information
- **Simple Chat Interface**: Web-based chat interface

### 🏗️ Technical Architecture
- **FastAPI**: Fast and modern web API framework
- **LangChain**: LLM integration and prompt management
- **Qloo API**: Cultural intelligence and personalized recommendations
- **Google Gemini**: Chat model
- **Simple File-based Storage**: Data storage with JSON files

## 📁 Simple Project Structure

```
ai.concierge/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application
│   ├── config.py              # Configuration settings
│   ├── core/
│   │   ├── __init__.py
│   │   ├── concierge.py       # Main Concierge class
│   │   ├── qloo_integration.py # Qloo API integration
│   │   └── prompt_templates.py # Prompt templates
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── chat.py           # Chat schemas
│   └── utils/
│       ├── __init__.py
│       └── logger.py         # Logging utility
├── data/
│   ├── guests.json           # Guest data
│   └── chat_history.json     # Chat history
├── static/
│   └── chat.html             # Simple chat interface
├── tests/
│   └── test_concierge.py
├── requirements.txt
├── env.example
└── README.md
```

## 🚀 Quick Setup

### 1. Requirements
```bash
# Python 3.9+ required
python --version

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install production dependencies
pip install -r requirements.txt

# Or install with development tools
pip install -r requirements-dev.txt
```

**📦 Dependency Management:**
- **Production**: `requirements.txt` - Minimal dependencies for production
- **Development**: `requirements-dev.txt` - Includes testing, linting, and dev tools
- **Module**: `module.qlooapi/requirements.txt` - Qloo API module dependencies
- **Python**: `pyproject.toml` - Modern Python packaging configuration

### 2. Environment Variables
```bash
# Create .env file from template
cp env.example .env

# Edit .env file and add your API keys
nano .env  # or use your preferred editor

# Required API keys:
# OPENROUTER_API_KEY=your_openrouter_api_key_here
# QLOO_API_KEY=your_qloo_api_key_here
```

**🔐 Security Note**: Never commit your `.env` file to version control. The `env.example` file provides a template with all required variables.

### 3. Run the Application
```bash
# In development mode
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Open in browser
# http://localhost:8000
```

## 🔧 Configuration

### Environment Variables
The application uses environment variables for secure configuration. Copy `env.example` to `.env` and configure:

```bash
# Required API Keys
OPENROUTER_API_KEY=your_openrouter_api_key_here
QLOO_API_KEY=your_qloo_api_key_here

# Optional Configuration
QLOO_BASE_URL=https://hackathon.api.qloo.com
HOTEL_NAME=Grand Hotel Istanbul
HOTEL_LOCATION=Istanbul, Turkey
LLM_MODEL=openrouter/horizon-beta
MAX_TOKENS=1000
TEMPERATURE=0.7
LOG_LEVEL=INFO
```

### Main Configuration (`app/config.py`)
```python
from pydantic_settings import BaseSettings
from pydantic import Field, validator

class Settings(BaseSettings):
    # API Keys - Required from environment variables
    openrouter_api_key: str = Field(..., description="OpenRouter API key")
    qloo_api_key: str = Field(..., description="Qloo API key")
    qloo_base_url: str = Field(default="https://hackathon.api.qloo.com")
    
    # Hotel Configuration
    hotel_name: str = Field(default="Grand Hotel Istanbul")
    hotel_location: str = Field(default="Istanbul, Turkey")
    
    # LLM Configuration
    llm_model: str = "gemini-2.0-flash"
    max_tokens: int = 1000
    temperature: float = 0.7
    
    class Config:
        env_file = ".env"
```

## 🤖 AI Concierge Class

### Main Concierge Class (`app/core/concierge.py`)
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
        """Process guest request and return response"""
        
        # Get personalized recommendations from Qloo
        recommendations = await self.qloo.get_personalized_recommendations(
            location=self.config.hotel_location
        )
        
        # Generate response with LangChain
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

# Configuration
settings = Settings()
concierge = AIConcierge(settings)

@app.get("/", response_class=HTMLResponse)
async def chat_interface():
    """Chat interface"""
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

## 📊 Qloo Integration

### Qloo Integration Class (`app/core/qloo_integration.py`)
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
        """Get personalized recommendations"""
        
        # Restaurant recommendations
        restaurants = await self.qloo.get_insights(
            entity_type="urn:entity:place",
            location=location,
            filters={"filter.tags": "urn:tag:cuisine:restaurant"},
            limit=5
        )
        
        # Activity recommendations
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

## 📝 Prompt Templates

### Prompt Templates (`app/core/prompt_templates.py`)
```python
from langchain.prompts import PromptTemplate

CONCIERGE_PROMPT_TEMPLATE = PromptTemplate(
    input_variables=["guest_message", "recommendations", "hotel_info", "location"],
    template="""
    You are the AI Concierge of {hotel_info} hotel. You are here to help guests.
    
    Hotel Location: {location}
    
    Recommendations from Qloo:
    Restaurants: {recommendations[restaurants]}
    Activities: {recommendations[activities]}
    
    Guest Message: {guest_message}
    
    Please help the guest. Always respond in English. Provide personalized recommendations.
    Provide information about hotel services, restaurant recommendations, and activities.
    Use a friendly and professional tone.
    """
)
```

## 📋 Data Schemas

### Chat Schemas (`app/schemas/chat.py`)
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

## 🎨 Simple Chat Interface

### HTML Interface (`static/chat.html`)
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
            <input type="text" id="messageInput" placeholder="Type your message...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value;
            if (!message) return;

            // Show user message
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
                addMessage('Sorry, an error occurred.', 'bot');
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

        // Send with Enter key
        document.getElementById('messageInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    </script>
</body>
</html>
```

## 🧪 Testing

### Test File (`tests/test_concierge.py`)
```python
import pytest
from app.core.concierge import AIConcierge
from app.config import Settings

@pytest.mark.asyncio
async def test_concierge_response():
    """Concierge response test"""
    settings = Settings()
    concierge = AIConcierge(settings)
    
    response = await concierge.process_guest_request(
        guest_id="test_guest",
        message="Hello, can I get information about the hotel?"
    )
    
    assert response is not None
    assert len(response) > 10
```

## 🚀 Running

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create .env file and add API key
cp env.example .env
# Edit .env file and add GEMINI_API_KEY

# 3. Run the application
uvicorn app.main:app --reload

# 4. Open in browser
# http://localhost:8000
```

## 📊 Features

- ✅ **Simple Chat Interface**: Web-based chat
- ✅ **Qloo Integration**: Personalized recommendations
- ✅ **LangChain**: LLM management
- ✅ **FastAPI**: Modern API framework
- ✅ **Multi-language Support**: Turkish/English
- ✅ **Location-based Recommendations**: Restaurant and activity recommendations

## 🔧 Development

The following features can be added to this simple structure:
- Guest profiles
- Chat history storage
- Reservation system
- More advanced UI
- Voice integration
- Mobile application

You can quickly create a working AI Concierge system with this minimal structure! 