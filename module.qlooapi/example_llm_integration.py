#!/usr/bin/env python3
"""
Example LLM Integration with Qloo
=================================

This script demonstrates how to integrate Qloo's Taste AI with popular LLM frameworks
to create enhanced, personalized AI experiences.

Examples include:
- OpenAI GPT integration
- Local LLM integration (using transformers)
- Chatbot with personalized recommendations
"""

import os
import json
from typing import List, Dict, Optional
from qloo_llm_integration import QlooConfig, QlooLLMIntegration, LLMEnhancer

# Try to import OpenAI (install with: pip install openai)
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("OpenAI not available. Install with: pip install openai")

# Try to import Google Gemini (install with: pip install google-generativeai)
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("Gemini not available. Install with: pip install google-generativeai")

# Try to import transformers for local models (install with: pip install transformers torch)
try:
    from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("Transformers not available. Install with: pip install transformers torch")

class QlooLLMExample:
    """Example class showing LLM integration with Qloo"""
    
    def __init__(self):
        # Initialize Qloo integration
        config = QlooConfig()
        self.qloo_integration = QlooLLMIntegration(config)
        self.enhancer = LLMEnhancer(self.qloo_integration)
        
        # Initialize LLM components
        self.openai_client = None
        self.gemini_client = None
        self.local_model = None
        
        if OPENAI_AVAILABLE:
            # Set your OpenAI API key here
            openai.api_key = os.getenv("OPENAI_API_KEY", "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")
            self.openai_client = openai
        
        if GEMINI_AVAILABLE:
            # Set your Gemini API key here
            genai.configure(api_key="AIzaSyBJ61NA77E5raFEVUKSrwsKabrjA0ASU3E")
            self.gemini_client = genai
        
        if TRANSFORMERS_AVAILABLE:
            # Initialize a local model (this is just an example)
            try:
                self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
                self.model = AutoModelForCausalLM.from_pretrained("gpt2")
                self.local_model = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)
            except Exception as e:
                print(f"Could not load local model: {e}")
    
    def get_movie_recommendations_with_openai(self, user_interests: List[str]) -> str:
        """
        Get movie recommendations using OpenAI GPT with Qloo insights
        """
        if not self.openai_client:
            return "OpenAI not available"
        
        # Get enhanced prompt from Qloo
        enhanced_prompt = self.enhancer.enhance_recommendation_prompt(user_interests, "movies")
        
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.openai_client.api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a knowledgeable movie recommendation assistant that provides personalized suggestions based on user interests and cultural intelligence data."},
                    {"role": "user", "content": enhanced_prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error with OpenAI API: {e}"
    
    def get_movie_recommendations_with_gemini(self, user_interests: List[str]) -> str:
        """
        Get movie recommendations using Google Gemini with Qloo insights
        """
        if not self.gemini_client:
            return "Gemini not available"
        
        # Get enhanced prompt from Qloo
        enhanced_prompt = self.enhancer.enhance_recommendation_prompt(user_interests, "movies")
        
        try:
            # Generate response with Gemini
            model = genai.GenerativeModel('gemini-1.5-pro')
            response = model.generate_content(enhanced_prompt)
            
            return response.text
            
        except Exception as e:
            return f"Error with Gemini API: {e}"
    
    def get_restaurant_recommendations_with_gemini(self, location: str, interests: List[str]) -> str:
        """
        Get restaurant recommendations using Google Gemini with Qloo insights
        """
        if not self.gemini_client:
            return "Gemini not available"
        
        # Get location-based prompt from Qloo
        enhanced_prompt = self.enhancer.create_location_based_prompt(location, interests)
        
        try:
            # Generate response with Gemini
            model = genai.GenerativeModel('gemini-1.5-pro')
            response = model.generate_content(enhanced_prompt)
            
            return response.text
            
        except Exception as e:
            return f"Error with Gemini API: {e}"
    
    def create_personalized_chatbot_response_with_gemini(self, user_message: str, user_interests: List[str]) -> str:
        """
        Create a personalized chatbot response using Gemini with Qloo insights
        """
        if not self.gemini_client:
            return "Gemini not available"
        
        # Get some context from Qloo based on user interests
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
        
        try:
            # Generate response with Gemini
            model = genai.GenerativeModel('gemini-pro')
            system_prompt = f"You are a helpful assistant with access to cultural intelligence data. {context}"
            full_prompt = f"{system_prompt}\n\nUser: {user_message}\n\nAssistant:"
            
            response = model.generate_content(full_prompt)
            
            return response.text
            
        except Exception as e:
            return f"Error: {e}"
    
    def get_restaurant_recommendations_with_local_llm(self, location: str, interests: List[str]) -> str:
        """
        Get restaurant recommendations using a local LLM with Qloo insights
        """
        if not self.local_model:
            return "Local model not available"
        
        # Get location-based prompt from Qloo
        enhanced_prompt = self.enhancer.create_location_based_prompt(location, interests)
        
        try:
            # Generate response with local model
            response = self.local_model(
                enhanced_prompt,
                max_length=200,
                num_return_sequences=1,
                temperature=0.8,
                do_sample=True
            )
            
            return response[0]['generated_text']
            
        except Exception as e:
            return f"Error with local model: {e}"
    
    def create_personalized_chatbot_response(self, user_message: str, user_interests: List[str]) -> str:
        """
        Create a personalized chatbot response using Qloo insights
        """
        if not self.openai_client:
            return "OpenAI not available"
        
        # Get some context from Qloo based on user interests
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
        
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.openai_client.api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a helpful assistant with access to cultural intelligence data. {context}"},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=300,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error: {e}"
    
    def analyze_user_taste_profile(self, user_interests: List[str]) -> Dict:
        """
        Analyze a user's taste profile using Qloo insights
        """
        analysis = {
            "interests": user_interests,
            "recommendations": {},
            "demographics": {},
            "trends": {}
        }
        
        # Get movie recommendations
        movie_insights = self.qloo_integration.get_insights(
            entity_type="urn:entity:movie",
            interests=user_interests,
            limit=5
        )
        
        if "results" in movie_insights and "entities" in movie_insights["results"]:
            analysis["recommendations"]["movies"] = [
                {
                    "name": entity["name"],
                    "popularity": entity.get("popularity", 0),
                    "description": entity.get("properties", {}).get("description", "")
                }
                for entity in movie_insights["results"]["entities"]
            ]
        
        # Get music recommendations
        music_insights = self.qloo_integration.get_insights(
            entity_type="urn:entity:artist",
            interests=user_interests,
            limit=5
        )
        
        if "results" in music_insights and "entities" in music_insights["results"]:
            analysis["recommendations"]["music"] = [
                {
                    "name": entity["name"],
                    "popularity": entity.get("popularity", 0)
                }
                for entity in music_insights["results"]["entities"]
            ]
        
        # Get trending entities
        trending = self.qloo_integration.get_trending_entities("urn:entity:movie", 5)
        if "results" in trending and "entities" in trending["results"]:
            analysis["trends"]["movies"] = [
                {
                    "name": entity["name"],
                    "trend_score": entity.get("trend", {}).get("percentile", 0)
                }
                for entity in trending["results"]["entities"]
            ]
        
        return analysis

def demo_openai_integration():
    """Demonstrate OpenAI integration with Qloo"""
    print("🤖 OpenAI + Qloo Integration Demo")
    print("=" * 40)
    
    example = QlooLLMExample()
    
    # Example 1: Movie recommendations
    user_interests = ["The Matrix", "Inception", "Blade Runner"]
    print(f"\n📽️ Getting movie recommendations for interests: {user_interests}")
    
    response = example.get_movie_recommendations_with_openai(user_interests)
    print(f"AI Response:\n{response}")
    
    # Example 2: Personalized chatbot
    print(f"\n💬 Personalized Chatbot Response")
    user_message = "What kind of movies should I watch this weekend?"
    
    response = example.create_personalized_chatbot_response(user_message, user_interests)
    print(f"User: {user_message}")
    print(f"AI: {response}")

def demo_gemini_integration():
    """Demonstrate Gemini integration with Qloo"""
    print("\n🤖 Gemini + Qloo Integration Demo")
    print("=" * 40)
    
    example = QlooLLMExample()
    
    # Example 1: Movie recommendations with Gemini
    user_interests = ["The Matrix", "Inception", "Blade Runner"]
    print(f"\n📽️ Getting movie recommendations for interests: {user_interests}")
    
    response = example.get_movie_recommendations_with_gemini(user_interests)
    print(f"Gemini Response:\n{response}")
    
    # Example 2: Restaurant recommendations with Gemini
    location = "Istanbul"
    interests = ["kebab", "turkish coffee", "historical sites"]
    print(f"\n🍽️ Getting restaurant recommendations for {location} based on interests: {interests}")
    
    response = example.get_restaurant_recommendations_with_gemini(location, interests)
    print(f"Gemini Response:\n{response}")
    
    # Example 3: Personalized chatbot with Gemini
    print(f"\n💬 Personalized Chatbot Response with Gemini")
    user_message = "What kind of movies should I watch this weekend?"
    
    response = example.create_personalized_chatbot_response_with_gemini(user_message, user_interests)
    print(f"User: {user_message}")
    print(f"Gemini: {response}")

def demo_local_llm_integration():
    """Demonstrate local LLM integration with Qloo"""
    print("\n🏠 Local LLM + Qloo Integration Demo")
    print("=" * 40)
    
    example = QlooLLMExample()
    
    # Example: Restaurant recommendations
    location = "San Francisco"
    interests = ["sushi", "craft beer", "art galleries"]
    
    print(f"\n🍣 Getting restaurant recommendations for {location} based on interests: {interests}")
    
    response = example.get_restaurant_recommendations_with_local_llm(location, interests)
    print(f"Local LLM Response:\n{response}")

def demo_taste_analysis():
    """Demonstrate taste profile analysis"""
    print("\n🎨 Taste Profile Analysis Demo")
    print("=" * 40)
    
    example = QlooLLMExample()
    
    # Analyze user taste profile
    user_interests = ["Nirvana", "Pulp Fiction", "The Catcher in the Rye"]
    print(f"\n🔍 Analyzing taste profile for interests: {user_interests}")
    
    analysis = example.analyze_user_taste_profile(user_interests)
    
    print("\n📊 Analysis Results:")
    print(json.dumps(analysis, indent=2))

def demo_direct_api_usage():
    """Demonstrate direct API usage without LLM integration"""
    print("\n🔌 Direct Qloo API Usage Demo")
    print("=" * 40)
    
    example = QlooLLMExample()
    
    # Example 1: Search for entities
    print("\n🔍 Searching for 'Inception' movie:")
    search_results = example.qloo_integration.search_entities("Inception", "urn:entity:movie")
    
    if "results" in search_results and "entities" in search_results["results"]:
        for entity in search_results["results"]["entities"][:3]:
            print(f"- {entity['name']} (ID: {entity['entity_id']})")
    
    # Example 2: Get demographic insights
    print("\n👥 Getting demographic insights for 'Inception':")
    if "results" in search_results and "entities" in search_results["results"]:
        movie_id = search_results["results"]["entities"][0]["entity_id"]
        demo_insights = example.qloo_integration.get_demographic_insights(movie_id)
        
        if "results" in demo_insights and "demographics" in demo_insights["results"]:
            for demo in demo_insights["results"]["demographics"][:3]:
                print(f"- {demo.get('name', 'Unknown')}: {demo.get('affinity', 0):.2f}")

def main():
    """Main demo function"""
    print("🎯 Qloo LLM Integration Examples")
    print("=" * 50)
    
    # Check what's available
    print(f"OpenAI Available: {OPENAI_AVAILABLE}")
    print(f"Gemini Available: {GEMINI_AVAILABLE}")
    print(f"Transformers Available: {TRANSFORMERS_AVAILABLE}")
    
    # Run demos based on availability
    if GEMINI_AVAILABLE:
        demo_gemini_integration()
    
    if OPENAI_AVAILABLE:
        demo_openai_integration()
    
    if TRANSFORMERS_AVAILABLE:
        demo_local_llm_integration()
    
    # These demos work with just the Qloo API
    demo_taste_analysis()
    demo_direct_api_usage()
    
    print("\n✅ Demo completed!")
    print("\nTo use with your own LLM:")
    print("1. Install required packages: pip install openai google-generativeai transformers torch")
    print("2. Set your API keys in the code")
    print("3. Modify the example code to fit your use case")

if __name__ == "__main__":
    main() 