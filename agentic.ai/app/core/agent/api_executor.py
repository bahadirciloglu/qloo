import logging
from typing import Dict, List
from ..tools.qloo_tools import QlooRestaurantTool, QlooActivityTool

logger = logging.getLogger(__name__)

class APICallExecutor:
    """Class that manages API calls"""
    
    def __init__(self, qloo_integration):
        self.qloo = qloo_integration  # Store Qloo integration
        self.tools = {
            "qloo_restaurant_api": QlooRestaurantTool(qloo_integration),
            "qloo_activity_api": QlooActivityTool(qloo_integration)
        }
    
    async def execute_api_calls(self, api_calls: List[Dict]) -> Dict:
        """Execute API calls in parallel"""
        results = {}
        
        for api_call in api_calls:
            api_name = api_call["api"]
            parameters = api_call["parameters"]
            
            if api_name in self.tools:
                logger.info(f"Making API call: {api_name}")
                result = await self.tools[api_name].execute(parameters)
                results[api_name] = result
            else:
                logger.warning(f"Unknown API: {api_name}")
                results[api_name] = {"error": f"Unknown API: {api_name}"}
        
        return results
