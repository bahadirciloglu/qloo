import logging
from typing import Dict
from ..llm.gemini_wrapper import GeminiWrapper
from ..llm.prompts.response_prompts import RESPONSE_GENERATION_PROMPT

logger = logging.getLogger(__name__)

class ResponseGenerationLLM:
    """LLM class for Response Generation"""
    
    def __init__(self, llm: GeminiWrapper):
        self.llm = llm
    
    async def generate_response(self, user_message: str, api_results: Dict, intent: Dict) -> str:
        """Generate natural language response using API results"""
        try:
            prompt = RESPONSE_GENERATION_PROMPT.format(
                user_message=user_message,
                intent=intent.get("intent", "unknown"),
                api_results=str(api_results)
            )
            
            response = await self.llm.generate_content(prompt)
            logger.info("Response generated")
            
            return response
            
        except Exception as e:
            logger.error(f"Response generation error: {e}")
            return f"Sorry, I couldn't generate a response. Error: {str(e)}"
