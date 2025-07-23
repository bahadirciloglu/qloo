import aiohttp
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class GeminiWrapper:
    """Gemini LLM Wrapper"""
    
    def __init__(self, config):
        self.config = config
        self.api_key = config.gemini_api_key
        self.model = config.llm_model
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"
    
    async def generate_content(self, prompt: str) -> str:
        """Gemini API'ye async istek gönder"""
        try:
            url = f"{self.base_url}/models/{self.model}:generateContent"
            
            headers = {
                'Content-Type': 'application/json',
                'X-goog-api-key': self.api_key
            }
            
            data = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": self.config.temperature,
                    "maxOutputTokens": self.config.max_tokens
                }
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=data) as response:
                    response.raise_for_status()
                    result = await response.json()
            
            if 'candidates' in result and len(result['candidates']) > 0:
                content = result['candidates'][0]['content']
                if 'parts' in content and len(content['parts']) > 0:
                    return content['parts'][0]['text']
            
            return "Üzgünüm, yanıt oluşturulamadı."
            
        except Exception as e:
            logger.error(f"Gemini API hatası: {e}")
            return f"API hatası: {str(e)}"
    
    def generate_content_sync(self, prompt: str) -> str:
        """Gemini API'ye sync istek gönder (fallback için)"""
        try:
            import requests
            
            url = f"{self.base_url}/models/{self.model}:generateContent"
            
            headers = {
                'Content-Type': 'application/json',
                'X-goog-api-key': self.api_key
            }
            
            data = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": self.config.temperature,
                    "maxOutputTokens": self.config.max_tokens
                }
            }
            
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            
            result = response.json()
            
            if 'candidates' in result and len(result['candidates']) > 0:
                content = result['candidates'][0]['content']
                if 'parts' in content and len(content['parts']) > 0:
                    return content['parts'][0]['text']
            
            return "Üzgünüm, yanıt oluşturulamadı."
            
        except Exception as e:
            logger.error(f"Gemini API hatası: {e}")
            return f"API hatası: {str(e)}"