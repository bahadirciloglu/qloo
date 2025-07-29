from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    """AI Concierge uygulama ayarları"""
    
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
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        extra = "ignore"

# Global settings instance
settings = Settings() 