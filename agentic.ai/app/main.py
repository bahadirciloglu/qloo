from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os

from app.schemas.chat import ChatRequest, ChatResponse, HotelInfoResponse, RecommendationResponse
from app.core.concierge import AIConcierge
from app.core.metrics import metrics_collector
from app.config import settings
from app.utils.logger import logger

# FastAPI uygulamasını oluştur
app = FastAPI(
    title="AI Concierge",
    description="Otel konukları için AI destekli Concierge sistemi",
    version="1.0.0"
)

# CORS middleware ekle
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static dosyaları serve et
app.mount("/static", StaticFiles(directory="static"), name="static")

# AI Concierge instance'ını oluştur
try:
    concierge = AIConcierge(settings)
    logger.info("AI Concierge başarıyla başlatıldı")
except Exception as e:
    logger.error(f"AI Concierge başlatılamadı: {e}")
    concierge = None

@app.get("/", response_class=HTMLResponse)
async def chat_interface():
    """Chat arayüzü"""
    try:
        with open("static/chat.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="""
        <html>
        <head><title>AI Concierge</title></head>
        <body>
            <h1>🏨 AI Concierge</h1>
            <p>Chat arayüzü yüklenemedi. Lütfen static/chat.html dosyasını kontrol edin.</p>
        </body>
        </html>
        """)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Chat API endpoint"""
    if not concierge:
        raise HTTPException(status_code=500, detail="AI Concierge başlatılamadı")
    
    # Metrik toplama başlat
    import uuid
    request_id = str(uuid.uuid4())
    metrics = await metrics_collector.start_request(request_id)
    
    try:
        logger.info(f"Chat isteği alındı: {request.guest_id} - {request.message[:50]}...")
        
        response = await concierge.process_guest_request(
            guest_id=request.guest_id,
            message=request.message
        )
        
        # Başarılı istek sonlandır
        await metrics_collector.end_request(request_id, success=True)
        
        return ChatResponse(
            message=response,
            guest_id=request.guest_id
        )
    except Exception as e:
        logger.error(f"Chat endpoint hatası: {e}")
        # Hatalı istek sonlandır
        await metrics_collector.end_request(request_id, success=False, error_message=str(e))
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics")
async def get_metrics():
    """Sistem metriklerini getir"""
    try:
        return {
            "system": metrics_collector.get_system_metrics(),
            "performance": metrics_collector.get_performance_metrics(),
            "language_usage": metrics_collector.get_language_metrics(),
            "intent_usage": metrics_collector.get_intent_metrics(),
            "recent_requests": metrics_collector.get_recent_metrics(5)
        }
    except Exception as e:
        logger.error(f"Metrikler alınırken hata: {e}")
        return {"error": str(e)}

@app.get("/metrics/performance")
async def get_performance_metrics():
    """Performans metriklerini getir"""
    try:
        return metrics_collector.get_performance_metrics()
    except Exception as e:
        logger.error(f"Performans metrikleri alınırken hata: {e}")
        return {"error": str(e)}

@app.get("/metrics/system")
async def get_system_metrics():
    """Sistem metriklerini getir"""
    try:
        return metrics_collector.get_system_metrics()
    except Exception as e:
        logger.error(f"Sistem metrikleri alınırken hata: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 