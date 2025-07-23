import json
import logging
import re
from typing import Dict
from ..llm.gemini_wrapper import GeminiWrapper
from ..llm.prompts.intent_prompts import INTENT_ANALYSIS_PROMPT

logger = logging.getLogger(__name__)

class IntentAnalysisLLM:
    """Intent Analysis için LLM sınıfı"""
    
    def __init__(self, llm: GeminiWrapper):
        self.llm = llm
    
    async def analyze_intent(self, user_message: str) -> Dict:
        """Kullanıcı mesajını analiz edip intent çıkar"""
        try:
            prompt = INTENT_ANALYSIS_PROMPT.format(user_message=user_message)
            response = await self.llm.generate_content(prompt)
            
            # Markdown code block'larını temizle
            cleaned_response = self._clean_llm_response(response)
            
            # JSON parse et
            intent_data = json.loads(cleaned_response)
            logger.info(f"Intent analizi tamamlandı: {intent_data}")
            
            return intent_data
            
        except Exception as e:
            logger.error(f"Intent analizi hatası: {e}")
            # Fallback intent
            return {
                "intent": "general_inquiry",
                "entities": {"location": "Istanbul"},
                "api_calls_needed": [],
                "confidence": 0.5
            }
    
    def _clean_llm_response(self, response: str) -> str:
        """LLM yanıtından markdown code block'larını temizle"""
        # ```json ... ``` formatını temizle
        json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response, re.DOTALL)
        if json_match:
            return json_match.group(1)
        
        # Sadece JSON object'i ara
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            return json_match.group(0)
        
        # Hiçbir JSON bulunamazsa orijinal yanıtı döndür
        return response
