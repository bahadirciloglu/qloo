import logging
from .agent.concierge_agent import LLMCentricConciergeAgent

logger = logging.getLogger(__name__)

class AIConcierge:
    """AI Concierge ana sınıfı - LLM Agent kullanacak"""
    
    def __init__(self, config):
        self.config = config
        
        # LLM merkezli agent'ı kullan
        self.agent = LLMCentricConciergeAgent(config)
        logger.info("LLM Merkezli AI Concierge başlatıldı")
    
    async def process_guest_request(self, guest_id: str, message: str) -> str:
        """Konuk isteğini LLM merkezli agent ile işle"""
        try:
            logger.info(f"Konuk {guest_id} için LLM agent isteği: {message[:50]}...")
            
            # LLM merkezli agent'ı kullan
            response = await self.agent.process_request(message)
            
            logger.info(f"LLM agent yanıtı oluşturuldu: {response[:50]}...")
            return response
            
        except Exception as e:
            logger.error(f"LLM agent hatası: {e}")
            return f"Üzgünüm, şu anda size yardımcı olamıyorum. Hata: {str(e)}"
    
    async def get_hotel_info(self) -> dict:
        """Otel bilgilerini döndür"""
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
        """Hızlı öneriler al"""
        try:
            # LLM agent ile öneriler al
            response = await self.agent.process_request(f"{category} önerileri")
            return [{"name": "LLM Agent Response", "description": response}]
                
        except Exception as e:
            logger.error(f"Öneriler alınırken hata: {e}")
            return [] 