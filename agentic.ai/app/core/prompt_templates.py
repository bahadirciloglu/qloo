from langchain.prompts import PromptTemplate

CONCIERGE_PROMPT_TEMPLATE = PromptTemplate(
    input_variables=["guest_message", "recommendations", "hotel_info", "location"],
    template="""
    You are the AI Concierge of {hotel_info} hotel. You are here to help guests.
    
    Hotel Location: {location}
    
    Recommendations from Qloo:
    Restaurants: {recommendations[restaurants]}
    Activities: {recommendations[activities]}
    
    Guest Message: {guest_message}
    
    Please help the guest. Always respond in English. Provide personalized recommendations.
    Provide information about hotel services, restaurant recommendations, and activities.
    Use a friendly and professional tone.
    """
)

RECOMMENDATION_PROMPT_TEMPLATE = PromptTemplate(
    input_variables=["location", "interests", "recommendations"],
    template="""
    Recommendations for a guest with the following interests in the {location} area:
    
    Interests: {interests}
    
    Current Recommendations: {recommendations}
    
    Provide personalized recommendations based on this information.
    """
) 