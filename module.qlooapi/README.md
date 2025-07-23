# Qloo LLM Integration Project

This project demonstrates how to integrate Qloo's Taste AI with Large Language Models (LLMs) to create more truthful and personalized AI experiences. It leverages Qloo's consumer taste intelligence to enhance LLM responses with real-world behavioral data.

## 🎯 What is Qloo LLM Integration?

Qloo's LLM Integration method allows you to embed consumer taste intelligence into your AI applications, making them more accurate and personalized. Instead of relying solely on text-based training data, this integration provides:

- **Real consumer behavior data** from 3.7B+ entities and 10T+ behavioral signals
- **Privacy-compliant insights** with no Personally Identifiable Information (PII)
- **Cultural affinity analysis** across diverse domains (movies, music, restaurants, etc.)
- **Location-based personalization** with geographic insights
- **Demographic targeting** for audience-specific recommendations

## 🚀 Key Features

### 1. **Personalized Recommendations**
- Generate movie, restaurant, music, and book recommendations based on user interests
- Use real consumer behavior patterns instead of generic suggestions
- Include popularity scores and trend analysis

### 2. **Location-Based Insights**
- Get recommendations specific to geographic locations
- Heatmap visualization of interest distribution
- Local cultural affinity analysis

### 3. **Demographic Analysis**
- Understand audience preferences across different demographics
- Target specific age groups, genders, and cultural segments
- Create more relevant content and recommendations

### 4. **Entity Correlation**
- Discover connections between different cultural entities
- Build comprehensive user profiles based on interests
- Enable cross-domain recommendations

## 📋 Prerequisites

- Python 3.7 or higher
- Qloo API key (included in this project)
- Internet connection for API access

## 🛠️ Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd qloo-llm-integration
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify your API configuration**
   The project is pre-configured with:
   - API Server URL: `https://hackathon.api.qloo.com`
   - API Key: `mo8xSbrp5xOwLs7iYIQG3oLRVxMwIxluONFfDlkbZaw`

## 🎮 Quick Start

### Basic Usage

```python
from qloo_llm_integration import QlooConfig, QlooLLMIntegration, LLMEnhancer

# Initialize the integration
config = QlooConfig()
qloo_integration = QlooLLMIntegration(config)
enhancer = LLMEnhancer(qloo_integration)

# Create enhanced prompts for your LLM
user_interests = ["Inception", "Interstellar", "The Matrix"]
enhanced_prompt = enhancer.enhance_recommendation_prompt(user_interests, "movies")

# Use this enhanced prompt with your LLM
print(enhanced_prompt)
```

### Run the Demo

```bash
python qloo_llm_integration.py
```

This will demonstrate:
- Enhanced movie recommendations
- Location-based suggestions
- Trending entity analysis
- Demographic insights

## 📚 API Reference

### QlooLLMIntegration Class

#### `get_insights(entity_type, interests, location, demographics, filters, limit)`
Get personalized insights and recommendations.

**Parameters:**
- `entity_type` (str): Type of entities to return (e.g., "urn:entity:movie")
- `interests` (List[str]): User interests (entity names or IDs)
- `location` (str, optional): Geographic location for filtering
- `demographics` (Dict, optional): Demographic filters
- `filters` (Dict, optional): Additional API filters
- `limit` (int): Number of results to return

**Returns:** Dictionary with insights and recommendations

#### `get_heatmap(entity_id, location)`
Get geographic heatmap data for an entity.

#### `get_demographic_insights(entity_id, demographics)`
Get demographic affinity scores for an entity.

#### `search_entities(query, entity_type)`
Search for entities by name.

#### `get_trending_entities(entity_type, limit)`
Get trending entities of a specific type.

### LLMEnhancer Class

#### `enhance_recommendation_prompt(user_interests, recommendation_type)`
Create enhanced prompts with Qloo insights for LLM input.

#### `create_location_based_prompt(location, interests)`
Create location-specific recommendation prompts.

## 🔧 Integration Examples

### 1. **Movie Recommendation System**

```python
# Get movie recommendations based on user interests
insights = qloo_integration.get_insights(
    entity_type="urn:entity:movie",
    interests=["The Matrix", "Inception"],
    limit=5
)

# Extract recommendations for LLM prompt
recommendations = []
for entity in insights["results"]["entities"]:
    recommendations.append({
        "name": entity["name"],
        "popularity": entity["popularity"],
        "description": entity["properties"]["description"]
    })
```

### 2. **Restaurant Discovery**

```python
# Find restaurants in a specific location
restaurants = qloo_integration.get_insights(
    entity_type="urn:entity:place",
    interests=["sushi", "fine dining"],
    location="New York City",
    filters={"filter.tags": "urn:tag:cuisine:restaurant:japanese"}
)
```

### 3. **Audience Analysis**

```python
# Analyze demographic preferences for a movie
demo_insights = qloo_integration.get_demographic_insights(
    entity_id="movie_entity_id",
    demographics={"age": "36_to_55", "gender": "male"}
)
```

### 4. **Trend Analysis**

```python
# Get trending movies
trending = qloo_integration.get_trending_entities(
    entity_type="urn:entity:movie",
    limit=10
)
```

## 🌍 Entity Types

Qloo supports various entity types for different use cases:

- **Movies**: `urn:entity:movie`
- **TV Shows**: `urn:entity:tv_show`
- **Music Artists**: `urn:entity:artist`
- **Books**: `urn:entity:book`
- **Restaurants/Places**: `urn:entity:place`
- **Brands**: `urn:entity:brand`
- **Destinations**: `urn:entity:destination`

## 🎨 Use Cases

### 1. **Content Recommendation Engines**
Enhance your recommendation systems with real consumer behavior data.

### 2. **Personalized Marketing**
Create targeted campaigns based on cultural affinities and demographic insights.

### 3. **Travel Planning**
Provide personalized travel recommendations based on user interests and location data.

### 4. **E-commerce Personalization**
Improve product recommendations with cultural and behavioral insights.

### 5. **Content Creation**
Generate more relevant and engaging content based on audience preferences.

## 🔒 Privacy & Compliance

- **No PII**: Qloo's system never uses Personally Identifiable Information
- **GDPR Compliant**: Built with privacy regulations in mind
- **Anonymized Data**: All insights are based on anonymized behavioral signals
- **Secure API**: Enterprise-grade security for all API communications

## 📊 Data Sources

Qloo's insights are powered by:
- **3.7B+ Lifestyle Entities**: People, places, things, and interests
- **10T+ Behavioral Signals**: Transactions, locations, interactions
- **Real-time Updates**: Continuously refreshed data
- **Global Coverage**: Multi-cultural and multi-lingual support

## 🛠️ Advanced Configuration

### Custom Filters

```python
# Apply advanced filters
filters = {
    "filter.release_year.min": 2020,
    "filter.popularity.min": 0.8,
    "filter.tags": "urn:tag:genre:media:action"
}

insights = qloo_integration.get_insights(
    entity_type="urn:entity:movie",
    interests=["action movies"],
    filters=filters
)
```

### Demographic Targeting

```python
# Target specific demographics
demographics = {
    "age": "36_to_55",
    "gender": "female",
    "age.weight": 0.8,
    "gender.weight": 0.6
}

insights = qloo_integration.get_insights(
    entity_type="urn:entity:place",
    interests=["yoga", "organic food"],
    demographics=demographics
)
```

## 🚨 Error Handling

The integration includes comprehensive error handling:

```python
try:
    insights = qloo_integration.get_insights(...)
    if "error" in insights:
        print(f"API Error: {insights['error']}")
    else:
        # Process successful response
        pass
except Exception as e:
    print(f"Integration Error: {e}")
```

## 📈 Performance Tips

1. **Cache Results**: Store frequently requested insights to reduce API calls
2. **Batch Requests**: Combine multiple queries when possible
3. **Use Appropriate Limits**: Set reasonable result limits based on your needs
4. **Handle Rate Limits**: Implement retry logic for API rate limiting

## 🤝 Support

For questions or issues:
- Check the API documentation in the `docs/` folder
- Review the example code in `qloo_llm_integration.py`
- Contact Qloo support for API-specific questions

## 📄 License

This project is provided as-is for educational and development purposes. Please refer to Qloo's terms of service for commercial usage.

---

**Happy coding! 🎉**

Transform your LLM applications with the power of real consumer intelligence from Qloo's Taste AI. 