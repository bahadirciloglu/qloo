from pydantic_settings import BaseSettings
from pydantic import Field, validator
import os
import sys

class Settings(BaseSettings):
    """AI Concierge uygulama ayarları"""
    
    # API Keys - Required from environment variables
    openrouter_api_key: str = Field(..., description="OpenRouter API key for LLM access")
    qloo_api_key: str = Field(..., description="Qloo API key for cultural intelligence")
    qloo_base_url: str = Field(default="https://hackathon.api.qloo.com", description="Qloo API base URL")
    
    # Hotel Configuration
    hotel_name: str = Field(default="Grand Hotel Istanbul", description="Hotel name")
    hotel_location: str = Field(default="Istanbul, Turkey", description="Hotel location")
    
    # LLM Configuration
    llm_model: str = Field(default="openrouter/horizon-beta", description="LLM model to use")
    max_tokens: int = Field(default=1000, ge=1, le=4000, description="Maximum tokens for LLM response")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0, description="LLM temperature setting")
    
    # Logging
    log_level: str = Field(default="INFO", description="Logging level")
    
    # Development settings
    debug: bool = Field(default=False, description="Debug mode")
    verbose_logging: bool = Field(default=False, description="Verbose logging")
    
    @validator('openrouter_api_key')
    def validate_openrouter_key(cls, v):
        if not v or v == "your_openrouter_api_key_here":
            raise ValueError("OPENROUTER_API_KEY is required. Please set it in your .env file.")
        if not v.startswith('sk-or-'):
            raise ValueError("Invalid OpenRouter API key format. Should start with 'sk-or-'")
        return v
    
    @validator('qloo_api_key')
    def validate_qloo_key(cls, v):
        if not v or v == "your_qloo_api_key_here":
            raise ValueError("QLOO_API_KEY is required. Please set it in your .env file.")
        if len(v) < 20:
            raise ValueError("Invalid Qloo API key format. Key seems too short.")
        return v
    
    @validator('log_level')
    def validate_log_level(cls, v):
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if v.upper() not in valid_levels:
            raise ValueError(f"Invalid log level. Must be one of: {valid_levels}")
        return v.upper()
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        extra = "ignore"
        validate_assignment = True

def get_settings() -> Settings:
    """Get application settings with proper error handling"""
    try:
        return Settings()
    except Exception as e:
        print("❌ Configuration Error:")
        print(f"   {str(e)}")
        print("\n📝 Please check your .env file:")
        print("   1. Copy env.example to .env")
        print("   2. Add your actual API keys")
        print("   3. Restart the application")
        print(f"\n💡 Example .env file location: {os.path.join(os.getcwd(), '.env')}")
        sys.exit(1)

# Global settings instance
settings = get_settings() 