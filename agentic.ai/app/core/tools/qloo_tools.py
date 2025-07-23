import requests
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

from typing import Dict, Any
from .base_tool import BaseTool
from ..qloo_integration import QlooIntegration

class QlooRestaurantTool(BaseTool):
    """Qloo Restaurant API Tool"""
    
    def __init__(self, qloo_integration: QlooIntegration):
        super().__init__(
            name="qloo_restaurant_api",
            description="Restoran önerileri al"
        )
        self.qloo = qloo_integration
    
    async def execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Restoran önerileri al"""
        try:
            location = parameters.get("location", "Istanbul")
            cuisine = parameters.get("cuisine")
            limit = parameters.get("limit", 5)
            
            # Qloo API çağrısı
            result = await self.qloo.get_personalized_recommendations(
                location=location,
                user_message=f"restoran {cuisine or ''}"
            )
            
            return {
                "success": True,
                "data": result.get("restaurants", []),
                "source": "Qloo API"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "data": []
            }

class QlooActivityTool(BaseTool):
    """Qloo Activity API Tool"""
    
    def __init__(self, qloo_integration: QlooIntegration):
        super().__init__(
            name="qloo_activity_api", 
            description="Aktivite önerileri al"
        )
        self.qloo = qloo_integration
    
    async def execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Aktivite önerileri al"""
        try:
            location = parameters.get("location", "Istanbul")
            activity_type = parameters.get("activity_type")
            limit = parameters.get("limit", 5)
            
            result = await self.qloo.get_personalized_recommendations(
                location=location,
                user_message=f"aktivite {activity_type or ''}"
            )
            
            return {
                "success": True,
                "data": result.get("activities", []),
                "source": "Qloo API"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "data": []
            }
