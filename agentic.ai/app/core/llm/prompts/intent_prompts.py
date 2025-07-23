INTENT_ANALYSIS_PROMPT = """
Sen bir AI Concierge agent'ısın. Kullanıcı mesajını analiz et ve şu bilgileri çıkar:

Kullanıcı Mesajı: {user_message}

JSON formatında şu bilgileri döndür:
{{
    "intent": "restaurant_recommendation|activity_recommendation|hotel_info|booking|weather",
    "entities": {{
        "location": "Istanbul",
        "cuisine_type": "Turkish",
        "activity_type": "museum",
        "date": "today",
        "price_range": "mid-range"
    }},
    "api_calls_needed": [
        {{
            "api": "qloo_restaurant_api",
            "parameters": {{
                "location": "Istanbul",
                "cuisine": "Turkish",
                "limit": 5
            }}
        }}
    ],
    "confidence": 0.95
}}

Sadece JSON döndür, başka açıklama yapma.
""" 