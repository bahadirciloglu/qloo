import json
import logging
import re
from typing import Dict
from ..llm.gemini_wrapper import GeminiWrapper
from ..llm.prompts.intent_prompts import INTENT_ANALYSIS_PROMPT

logger = logging.getLogger(__name__)

class IntentAnalysisLLM:
    """LLM class for Intent Analysis"""
    
    def __init__(self, llm: GeminiWrapper):
        self.llm = llm
    
    async def analyze_intent(self, user_message: str) -> Dict:
        """Analyze user message and extract intent"""
        try:
            prompt = INTENT_ANALYSIS_PROMPT.format(user_message=user_message)
            response = await self.llm.generate_content(prompt)
            
            # Clean markdown code blocks
            cleaned_response = self._clean_llm_response(response)
            
            # Parse JSON
            intent_data = json.loads(cleaned_response)
            logger.info(f"Intent analysis completed: {intent_data}")
            
            return intent_data
            
        except Exception as e:
            logger.error(f"Intent analysis error: {e}")
            # Fallback intent
            return {
                "intent": "general_inquiry",
                "entities": {"location": "Istanbul"},
                "api_calls_needed": [],
                "confidence": 0.5
            }
    
    def _clean_llm_response(self, response: str) -> str:
        """Clean markdown code blocks from LLM response"""
        # Clean ```json ... ``` format
        json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response, re.DOTALL)
        if json_match:
            return json_match.group(1)
        
        # Search for JSON object only
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            return json_match.group(0)
        
        # Return original response if no JSON found
        return response
