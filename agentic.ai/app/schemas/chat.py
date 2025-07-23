from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class ChatRequest(BaseModel):
    """Chat isteği şeması"""
    guest_id: str
    message: str

class ChatResponse(BaseModel):
    """Chat yanıtı şeması"""
    message: str
    guest_id: str
    timestamp: datetime = datetime.now()

class HotelInfoResponse(BaseModel):
    """Otel bilgileri yanıtı"""
    name: str
    location: str
    amenities: list[str]
    services: list[str]

class RecommendationResponse(BaseModel):
    """Öneri yanıtı"""
    category: str
    items: list[Dict[str, Any]]
    total_count: int 