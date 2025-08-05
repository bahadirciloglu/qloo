from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    """AI Concierge uygulama ayarları"""
    
    # API Keys
    openrouter_api_key: str = "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"
    qloo_api_key: str = "mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw"
    qloo_base_url: str = "https://hackathon.api.qloo.com"
    
    # Hotel Configuration
    hotel_name: str = "Grand Hotel Istanbul"
    hotel_location: str = "Istanbul, Turkey"
    
    # LLM Configuration
    llm_model: str = "openrouter/horizon-beta"
    max_tokens: int = 1000
    temperature: float = 0.7
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        extra = "ignore"

# Global settings instance
settings = Settings() 