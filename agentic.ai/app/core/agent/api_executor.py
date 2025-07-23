import logging
from typing import Dict, List
from ..tools.qloo_tools import QlooRestaurantTool, QlooActivityTool

logger = logging.getLogger(__name__)

class APICallExecutor:
    """API çağrılarını yöneten sınıf"""
    
    def __init__(self, qloo_integration):
        self.qloo = qloo_integration  # Qloo integration'ı sakla
        self.tools = {
            "qloo_restaurant_api": QlooRestaurantTool(qloo_integration),
            "qloo_activity_api": QlooActivityTool(qloo_integration)
        }
    
    async def execute_api_calls(self, api_calls: List[Dict]) -> Dict:
        """API çağrılarını paralel olarak çalıştır"""
        results = {}
        
        for api_call in api_calls:
            api_name = api_call["api"]
            parameters = api_call["parameters"]
            
            if api_name in self.tools:
                logger.info(f"API çağrısı yapılıyor: {api_name}")
                result = await self.tools[api_name].execute(parameters)
                results[api_name] = result
            else:
                logger.warning(f"Bilinmeyen API: {api_name}")
                results[api_name] = {"error": f"Unknown API: {api_name}"}
        
        return results
