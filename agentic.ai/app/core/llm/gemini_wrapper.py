import aiohttp
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class GeminiWrapper:
    """OpenRouter Gemini LLM Wrapper"""
    
    def __init__(self, config):
        self.config = config
        self.api_key = config.openrouter_api_key
        self.model = config.llm_model
        self.base_url = "https://openrouter.ai/api/v1"
    
    def _get_mock_response(self, prompt: str) -> str:
        """Generate mock response for testing when API is rate limited"""
        if "restaurant" in prompt.lower() or "food" in prompt.lower():
            return """Hello! I'd be happy to recommend some excellent Turkish restaurants in Istanbul. Here are a few wonderful options:

🍽️ **Mikla Restaurant** - Located in the Marmara Pera Hotel, this award-winning restaurant offers modern Turkish cuisine with stunning city views. Chef Mehmet Gürs creates innovative dishes that blend traditional Turkish flavors with contemporary techniques.

🍽️ **Çiya Sofrası** - A hidden gem in Kadıköy, this restaurant specializes in authentic Anatolian cuisine. They serve traditional dishes from various regions of Turkey, prepared with fresh, local ingredients.

🍽️ **Balıkçı Lokantası** - For seafood lovers, this restaurant in Beşiktaş offers the freshest catch of the day. Their grilled sea bass and meze platters are particularly popular.

🍽️ **Kebapçı Selim Usta** - For the best kebabs in Istanbul, this family-run restaurant in Sultanahmet serves perfectly grilled meats with traditional accompaniments.

As your AI Concierge at Grand Hotel Istanbul, I can also help you make reservations at any of these restaurants or suggest other dining options based on your preferences. Would you like me to provide more details about any of these restaurants or help you with reservations?

Don't forget that we also have excellent dining options right here at the hotel! Our in-house restaurants offer both traditional Turkish cuisine and international dishes. Just let me know if you'd like to explore our hotel's dining options as well."""
        
        elif "attraction" in prompt.lower() or "tourist" in prompt.lower():
            return """Istanbul is a city rich in history and culture! Here are some must-visit attractions:

🏛️ **Hagia Sophia** - This architectural marvel has served as both a church and mosque throughout history. The stunning mosaics and massive dome are truly breathtaking.

🏛️ **Blue Mosque (Sultanahmet Mosque)** - Known for its beautiful blue tiles and six minarets, this mosque is one of Istanbul's most iconic landmarks.

🏛️ **Topkapi Palace** - The former residence of Ottoman sultans, this palace complex offers fascinating insights into Ottoman history and culture.

🏛️ **Grand Bazaar** - One of the world's largest and oldest covered markets, perfect for shopping for souvenirs, spices, and traditional crafts.

🏛️ **Bosphorus Cruise** - Take a boat tour to see Istanbul from the water, with views of both European and Asian sides of the city.

As your AI Concierge, I can help you plan your visits, arrange guided tours, or provide more specific information about any of these attractions. Would you like me to help you with tour bookings or provide more details about visiting hours and ticket information?

Remember, our hotel is conveniently located near many of these attractions, making it easy to explore the city!"""
        
        else:
            return """Hello! I'm Lento, your AI Concierge at Grand Hotel Istanbul. 🎹

I'm here to help you with anything you need during your stay in Istanbul. I can assist you with:

🍽️ Restaurant recommendations and reservations
🏛️ Tourist attraction information and tour bookings
🚇 Transportation and getting around the city
🏨 Hotel services and amenities
🎭 Entertainment and cultural events
🛍️ Shopping recommendations
📞 Local information and emergency contacts

How can I make your stay in Istanbul more enjoyable? Just let me know what you're looking for, and I'll be happy to help!

Also, don't forget to check out our hotel's own amenities - we have excellent dining options, spa services, and can arrange for various activities to enhance your experience."""
    
    async def generate_content(self, prompt: str) -> str:
        """OpenRouter API'ye async istek gönder"""
        try:
            url = f"{self.base_url}/chat/completions"
            
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.api_key}',
                'HTTP-Referer': 'https://github.com/bahadirciloglu/qloo',
                'X-Title': 'Qloo AI Concierge'
            }
            
            data = {
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": self.config.temperature,
                "max_tokens": self.config.max_tokens
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=data) as response:
                    if response.status == 429:
                        logger.warning("OpenRouter API rate limited, using mock response")
                        return self._get_mock_response(prompt)
                    
                    response.raise_for_status()
                    result = await response.json()
            
            if 'choices' in result and len(result['choices']) > 0:
                content = result['choices'][0]['message']['content']
                return content
            
            return "Sorry, I couldn't generate a response."
            
        except Exception as e:
            logger.error(f"OpenRouter API error: {e}")
            logger.info("Using mock response as fallback")
            return self._get_mock_response(prompt)
    
    def generate_content_sync(self, prompt: str) -> str:
        """OpenRouter API'ye sync istek gönder (fallback için)"""
        try:
            import requests
            
            url = f"{self.base_url}/chat/completions"
            
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.api_key}',
                'HTTP-Referer': 'https://github.com/bahadirciloglu/qloo',
                'X-Title': 'Qloo AI Concierge'
            }
            
            data = {
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": self.config.temperature,
                "max_tokens": self.config.max_tokens
            }
            
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 429:
                logger.warning("OpenRouter API rate limited, using mock response")
                return self._get_mock_response(prompt)
            
            response.raise_for_status()
            
            result = response.json()
            
            if 'choices' in result and len(result['choices']) > 0:
                content = result['choices'][0]['message']['content']
                return content
            
            return "Sorry, I couldn't generate a response."
            
        except Exception as e:
            logger.error(f"OpenRouter API error: {e}")
            logger.info("Using mock response as fallback")
            return self._get_mock_response(prompt)