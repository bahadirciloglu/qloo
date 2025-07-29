import logging
from typing import Dict
from .intent_analyzer import IntentAnalysisLLM
from .api_executor import APICallExecutor
from .response_generator import ResponseGenerationLLM
from ..llm.gemini_wrapper import GeminiWrapper

logger = logging.getLogger(__name__)

class LLMCentricConciergeAgent:
    """LLM-Centric Concierge Agent"""
    
    def __init__(self, config):
        self.config = config
        
        # LLM wrapper
        self.llm = GeminiWrapper(config)
        
        # Agent components
        self.intent_analyzer = IntentAnalysisLLM(self.llm)
        self.response_generator = ResponseGenerationLLM(self.llm)
        
        # API executor (with Qloo integration)
        from ..qloo_integration import QlooIntegration
        qloo_integration = QlooIntegration(config)
        self.api_executor = APICallExecutor(qloo_integration)
    
    async def process_request(self, user_message: str) -> str:
        """Process user request"""
        try:
            # 1. Intent Analysis with LLM
            logger.info("🔍 Performing intent analysis with LLM...")
            intent = await self.intent_analyzer.analyze_intent(user_message)
            logger.info(f"📋 Intent: {intent}")
            
            # 2. API Calls
            logger.info("️ Making API calls...")
            api_results = await self.api_executor.execute_api_calls(
                intent.get("api_calls_needed", [])
            )
            logger.info(f"📊 API Results: {api_results}")
            
            # 3. Response Generation with LLM
            logger.info("💬 Generating response...")
            response = await self.response_generator.generate_response(
                user_message, api_results, intent
            )
            
            return response
            
        except Exception as e:
            logger.error(f"❌ Agent error: {e}")
            return f"Sorry, I cannot help you right now. Error: {str(e)}"
