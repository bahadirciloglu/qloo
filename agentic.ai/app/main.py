from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import httpx
import asyncio
from typing import Dict, Any

from app.schemas.chat import ChatRequest, ChatResponse, HotelInfoResponse, RecommendationResponse
from app.core.concierge import AIConcierge
from app.core.metrics import metrics_collector
from app.config import settings
from app.utils.logger import logger

# Create FastAPI application
app = FastAPI(
    title="AI Concierge",
    description="AI-powered Concierge system for hotel guests",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8080", 
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8080",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create AI Concierge instance
try:
    concierge = AIConcierge(settings)
    logger.info("AI Concierge successfully started")
except Exception as e:
    logger.error(f"Failed to start AI Concierge: {e}")
    concierge = None

@app.get("/", response_class=HTMLResponse)
async def chat_interface():
    """Chat interface"""
    try:
        with open("static/chat.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="""
        <html>
        <head><title>AI Concierge</title></head>
        <body>
            <h1>🏨 AI Concierge</h1>
            <p>Chat interface could not be loaded. Please check the static/chat.html file.</p>
        </body>
        </html>
        """)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Chat API endpoint"""
    if not concierge:
        raise HTTPException(status_code=500, detail="AI Concierge could not be started")
    
    # Start metric collection
    import uuid
    request_id = str(uuid.uuid4())
    metrics = await metrics_collector.start_request(request_id)
    
    try:
        logger.info(f"Chat request received: {request.guest_id} - {request.message[:50]}...")
        
        response = await concierge.process_guest_request(
            guest_id=request.guest_id,
            message=request.message
        )
        
        # End successful request
        await metrics_collector.end_request(request_id, success=True)
        
        return ChatResponse(
            message=response,
            guest_id=request.guest_id
        )
    except Exception as e:
        logger.error(f"Chat endpoint error: {e}")
        # End failed request
        await metrics_collector.end_request(request_id, success=False, error_message=str(e))
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics")
async def get_metrics():
    """Get system metrics"""
    try:
        return {
            "system": metrics_collector.get_system_metrics(),
            "performance": metrics_collector.get_performance_metrics(),
            "language_usage": metrics_collector.get_language_metrics(),
            "intent_usage": metrics_collector.get_intent_metrics(),
            "recent_requests": metrics_collector.get_recent_metrics(5)
        }
    except Exception as e:
        logger.error(f"Error getting metrics: {e}")
        return {"error": str(e)}

@app.get("/metrics/performance")
async def get_performance_metrics():
    """Get performance metrics"""
    try:
        return metrics_collector.get_performance_metrics()
    except Exception as e:
        logger.error(f"Error getting performance metrics: {e}")
        return {"error": str(e)}

@app.get("/metrics/system")
async def get_system_metrics():
    """Get system metrics"""
    try:
        return metrics_collector.get_system_metrics()
    except Exception as e:
        logger.error(f"Error getting system metrics: {e}")
        return {"error": str(e)}





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 