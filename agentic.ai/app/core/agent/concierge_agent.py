import logging
from typing import Dict
from .intent_analyzer import IntentAnalysisLLM
from .api_executor import APICallExecutor
from .response_generator import ResponseGenerationLLM
from ..llm.gemini_wrapper import GeminiWrapper

logger = logging.getLogger(__name__)

class LLMCentricConciergeAgent:
    """LLM Merkezli Concierge Agent"""
    
    def __init__(self, config):
        self.config = config
        
        # LLM wrapper
        self.llm = GeminiWrapper(config)
        
        # Agent bileşenleri
        self.intent_analyzer = IntentAnalysisLLM(self.llm)
        self.response_generator = ResponseGenerationLLM(self.llm)
        
        # API executor (Qloo integration ile)
        from ..qloo_integration import QlooIntegration
        qloo_integration = QlooIntegration(config)
        self.api_executor = APICallExecutor(qloo_integration)
    
    async def process_request(self, user_message: str) -> str:
        """Kullanıcı isteğini işle"""
        try:
            # 1. LLM ile Intent Analysis
            logger.info("🔍 LLM ile intent analizi yapılıyor...")
            intent = await self.intent_analyzer.analyze_intent(user_message)
            logger.info(f"📋 Intent: {intent}")
            
            # 2. API Çağrıları
            logger.info("️ API çağrıları yapılıyor...")
            api_results = await self.api_executor.execute_api_calls(
                intent.get("api_calls_needed", [])
            )
            logger.info(f"📊 API Sonuçları: {api_results}")
            
            # 3. LLM ile Response Generation
            logger.info("💬 Yanıt oluşturuluyor...")
            response = await self.response_generator.generate_response(
                user_message, api_results, intent
            )
            
            return response
            
        except Exception as e:
            logger.error(f"❌ Agent hatası: {e}")
            return f"Üzgünüm, şu anda size yardımcı olamıyorum. Hata: {str(e)}"
