import logging
from typing import Dict
from ..llm.gemini_wrapper import GeminiWrapper
from ..llm.prompts.response_prompts import RESPONSE_GENERATION_PROMPT

logger = logging.getLogger(__name__)

class ResponseGenerationLLM:
    """Response Generation için LLM sınıfı"""
    
    def __init__(self, llm: GeminiWrapper):
        self.llm = llm
    
    async def generate_response(self, user_message: str, api_results: Dict, intent: Dict) -> str:
        """API sonuçlarını kullanarak doğal dil yanıtı oluştur"""
        try:
            prompt = RESPONSE_GENERATION_PROMPT.format(
                user_message=user_message,
                intent=intent.get("intent", "unknown"),
                api_results=str(api_results)
            )
            
            response = await self.llm.generate_content(prompt)
            logger.info("Yanıt oluşturuldu")
            
            return response
            
        except Exception as e:
            logger.error(f"Yanıt oluşturma hatası: {e}")
            return f"Sorry, I couldn't generate a response. Error: {str(e)}"
