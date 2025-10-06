import logging
from .agent.concierge_agent import LLMCentricConciergeAgent

logger = logging.getLogger(__name__)

class AIConcierge:
    """Main AI Concierge class - uses LLM Agent"""
    
    def __init__(self, config):
        self.config = config
        
        # Use LLM-centric agent
        self.agent = LLMCentricConciergeAgent(config)
        logger.info("LLM-Centric AI Concierge started")
    
    async def process_guest_request(self, guest_id: str, message: str) -> str:
        """Process guest request with LLM-centric agent"""
        try:
            logger.info(f"LLM agent request for guest {guest_id}: {message[:50]}...")
            
            # Use LLM-centric agent
            response = await self.agent.process_request(message)
            
            logger.info(f"LLM agent response generated: {response[:50]}...")
            return response
            
        except Exception as e:
            logger.error(f"LLM agent error: {e}")
            return f"Sorry, I cannot help you right now. Error: {str(e)}"
    
    async def get_hotel_info(self) -> dict:
        """Return hotel information"""
        return {
            "name": self.config.hotel_name,
            "location": self.config.hotel_location,
            "amenities": [
                "Spa & Wellness Center",
                "Infinity Pool",
                "Fitness Center",
                "Fine Dining Restaurant",
                "Rooftop Bar",
                "Business Center",
                "Concierge Service"
            ],
            "services": [
                "24/7 Room Service",
                "Laundry Service",
                "Airport Transfer",
                "Tour Booking",
                "Restaurant Reservations"
            ]
        }
    
    async def get_quick_recommendations(self, category: str = "restaurants") -> list:
        """Get quick recommendations"""
        try:
            # Get recommendations with LLM agent
            response = await self.agent.process_request(f"{category} recommendations")
            return [{"name": "LLM Agent Response", "description": response}]
                
        except Exception as e:
            logger.error(f"Error getting recommendations: {e}")
            return [] 