#!/usr/bin/env python3
"""
Qloo + Gemini API Integration
=============================

This project demonstrates how to integrate Qloo's Taste AI with Google's Gemini API
to create enhanced, personalized AI experiences with consumer intelligence data.

Key Features:
- Personalized recommendations using Qloo's consumer data
- Enhanced prompts with Gemini's advanced reasoning
- Multi-modal capabilities (text, images, etc.)
- Real-time consumer insights integration
"""

import google.generativeai as genai
import json
import time
from typing import Dict, List, Optional, Any
from qloo_llm_integration import QlooConfig, QlooLLMIntegration, LLMEnhancer

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyBJ61NA77E5raFEVUKSrwsKabrjA0ASU3E"
genai.configure(api_key=GEMINI_API_KEY)

class GeminiQlooIntegration:
    """
    Integration class combining Qloo's Taste AI with Google's Gemini API
    """
    
    def __init__(self):
        # Initialize Qloo integration
        self.qloo_config = QlooConfig()
        self.qloo_integration = QlooLLMIntegration(self.qloo_config)
        self.enhancer = LLMEnhancer(self.qloo_integration)
        
        # Initialize Gemini models
        self.gemini_pro = genai.GenerativeModel('gemini-2.0-flash')
        self.gemini_pro_vision = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    def get_enhanced_movie_recommendations(self, user_interests: List[str]) -> str:
        """
        Get enhanced movie recommendations using Qloo + Gemini
        
        Args:
            user_interests: List of user interests (movies, shows, etc.)
            
        Returns:
            Enhanced recommendation response from Gemini
        """
        # Get Qloo insights first
        enhanced_prompt = self.enhancer.enhance_recommendation_prompt(user_interests, "movies")
        
        # Create Gemini prompt
        gemini_prompt = f"""
You are an expert movie recommendation assistant with access to advanced consumer intelligence data.

{enhanced_prompt}

Please provide:
1. Additional personalized movie recommendations based on the data above
2. Explain why these choices would appeal to someone with these specific interests
3. Include cultural context and thematic connections
4. Suggest viewing order or thematic groupings
5. Mention any upcoming releases that might interest this user

Be conversational, engaging, and provide rich cultural insights.
"""
        
        try:
            response = self.gemini_pro.generate_content(gemini_prompt)
            return response.text
        except Exception as e:
            return f"Error with Gemini API: {e}"
    
    def get_location_based_recommendations(self, location: str, interests: List[str]) -> str:
        """
        Get location-based recommendations using Qloo + Gemini
        
        Args:
            location: Target location (city, neighborhood, etc.)
            interests: User interests (food, activities, etc.)
            
        Returns:
            Location-based recommendations from Gemini
        """
        # Get Qloo location insights
        enhanced_prompt = self.enhancer.create_location_based_prompt(location, interests)
        
        # Create Gemini prompt
        gemini_prompt = f"""
You are a local expert and cultural guide with access to consumer intelligence data.

{enhanced_prompt}

Please provide:
1. Additional local recommendations for {location}
2. Cultural significance and local context for each suggestion
3. Best times to visit or experience these places
4. Hidden gems or off-the-beaten-path options
5. Cultural etiquette or local customs to be aware of
6. Seasonal considerations or special events

Be informative, culturally sensitive, and provide authentic local insights.
"""
        
        try:
            response = self.gemini_pro.generate_content(gemini_prompt)
            return response.text
        except Exception as e:
            return f"Error with Gemini API: {e}"
    
    def analyze_taste_profile(self, user_interests: List[str]) -> Dict:
        """
        Analyze user taste profile using Qloo data and Gemini insights
        
        Args:
            user_interests: List of user interests
            
        Returns:
            Comprehensive taste analysis
        """
        # Get Qloo analysis
        qloo_analysis = self.enhancer.qloo.analyze_user_taste_profile(user_interests)
        
        # Create Gemini analysis prompt
        analysis_prompt = f"""
You are a cultural intelligence analyst. Based on the following consumer data, provide deep insights:

User Interests: {user_interests}

Qloo Analysis Data:
{json.dumps(qloo_analysis, indent=2)}

Please provide:
1. Cultural archetype analysis (what type of person this represents)
2. Cross-cultural connections and patterns
3. Potential new interests they might enjoy
4. Lifestyle and personality insights
5. Social and cultural context
6. Recommendations for expanding their cultural horizons

Be analytical, insightful, and provide cultural depth.
"""
        
        try:
            response = self.gemini_pro.generate_content(analysis_prompt)
            
            # Combine Qloo data with Gemini insights
            enhanced_analysis = {
                "qloo_data": qloo_analysis,
                "gemini_insights": response.text,
                "user_interests": user_interests
            }
            
            return enhanced_analysis
        except Exception as e:
            return {
                "qloo_data": qloo_analysis,
                "gemini_insights": f"Error with Gemini API: {e}",
                "user_interests": user_interests
            }
    
    def create_personalized_chatbot(self, user_message: str, user_interests: List[str]) -> str:
        """
        Create a personalized chatbot response using Qloo + Gemini
        
        Args:
            user_message: User's message
            user_interests: User's interests for context
            
        Returns:
            Personalized response from Gemini
        """
        # Get Qloo context
        insights = self.qloo_integration.get_insights(
            entity_type="urn:entity:movie",
            interests=user_interests,
            limit=3
        )
        
        # Create context from insights
        context = ""
        if "results" in insights and "entities" in insights["results"]:
            context = "Based on your interests, here are some relevant cultural insights:\n"
            for entity in insights["results"]["entities"]:
                context += f"- {entity.get('name', 'Unknown')}: {entity.get('properties', {}).get('description', 'No description')}\n"
        
        # Create Gemini prompt
        gemini_prompt = f"""
You are a helpful, culturally-aware assistant with access to consumer intelligence data.

{context}

User Interests: {user_interests}
User Message: {user_message}

Please respond in a helpful, personalized way that takes into account:
1. The user's cultural interests and preferences
2. The context provided from consumer intelligence data
3. Cultural sensitivity and awareness
4. Relevant recommendations or insights

Be conversational, knowledgeable, and culturally informed.
"""
        
        try:
            response = self.gemini_pro.generate_content(gemini_prompt)
            return response.text
        except Exception as e:
            return f"Error: {e}"
    
    def get_multi_modal_recommendations(self, image_path: str, user_interests: List[str]) -> str:
        """
        Get recommendations based on image and user interests using Gemini Vision
        
        Args:
            image_path: Path to image file
            user_interests: User interests for context
            
        Returns:
            Multi-modal recommendations
        """
        try:
            # Load image
            import PIL.Image
            image = PIL.Image.open(image_path)
            
            # Get Qloo context
            qloo_context = self.enhancer.enhance_recommendation_prompt(user_interests, "general")
            
            # Create multi-modal prompt
            prompt = f"""
You are analyzing an image and providing personalized recommendations.

User Interests: {user_interests}

Qloo Cultural Context:
{qloo_context}

Please analyze the image and provide:
1. What you see in the image
2. How it relates to the user's interests
3. Personalized recommendations based on the image and interests
4. Cultural connections and insights
5. Similar experiences or items they might enjoy

Be detailed, culturally aware, and provide rich recommendations.
"""
            
            response = self.gemini_pro_vision.generate_content([prompt, image])
            return response.text
            
        except Exception as e:
            return f"Error with multi-modal analysis: {e}"

def demo_gemini_integration():
    """Demonstrate Gemini + Qloo integration"""
    print("🤖 Gemini + Qloo Integration Demo")
    print("=" * 50)
    
    integration = GeminiQlooIntegration()
    
    # Example 1: Enhanced movie recommendations
    print("\n📽️ Enhanced Movie Recommendations")
    print("-" * 40)
    
    user_interests = ["The Matrix", "Inception", "Blade Runner"]
    print(f"User Interests: {user_interests}")
    
    response = integration.get_enhanced_movie_recommendations(user_interests)
    print(f"\nGemini Response:\n{response}")
    
    # Example 2: Location-based recommendations
    print("\n🗽 Location-Based Recommendations")
    print("-" * 40)
    
    location = "Istanbul"
    interests = ["Turkish coffee", "historical sites", "local markets"]
    print(f"Location: {location}")
    print(f"Interests: {interests}")
    
    response = integration.get_location_based_recommendations(location, interests)
    print(f"\nGemini Response:\n{response}")
    
    # Example 3: Taste profile analysis
    print("\n🎨 Enhanced Taste Profile Analysis")
    print("-" * 40)
    
    interests = ["Nirvana", "Pulp Fiction", "The Catcher in the Rye"]
    print(f"Analyzing interests: {interests}")
    
    analysis = integration.analyze_taste_profile(interests)
    print(f"\nEnhanced Analysis:\n{json.dumps(analysis, indent=2)}")
    
    # Example 4: Personalized chatbot
    print("\n💬 Personalized Chatbot")
    print("-" * 40)
    
    user_message = "I'm planning a weekend trip. What should I do?"
    interests = ["art galleries", "local cuisine", "walking tours"]
    
    print(f"User: {user_message}")
    print(f"Interests: {interests}")
    
    response = integration.create_personalized_chatbot(user_message, interests)
    print(f"\nGemini Response:\n{response}")

def main():
    """Main function"""
    print("🎯 Qloo + Gemini Integration")
    print("=" * 50)
    
    try:
        demo_gemini_integration()
        print("\n✅ Demo completed successfully!")
        print("\n🚀 Next steps:")
        print("1. Customize the prompts for your specific use case")
        print("2. Add more entity types (restaurants, music, books)")
        print("3. Implement multi-modal features with images")
        print("4. Create a conversational interface")
        
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        print("\nTroubleshooting:")
        print("1. Check your Gemini API key")
        print("2. Verify internet connection")
        print("3. Ensure all dependencies are installed")

if __name__ == "__main__":
    main() 