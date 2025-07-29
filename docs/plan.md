# Queryable Data Types for Restaurants with Qloo API

## 1. Basic Information
- Name (name)
- Address (address)
- Location (coordinates, city, country, region)
- Description / Short Description (description, short_description)
- Image (image URL)
- Entity ID (Qloo's unique restaurant identifier)

## 2. Cultural and Behavioral Analysis
- Popularity Score (popularity percentile)
- Trend Score (trend: percentile, rise/trend in last 6 months)
- Affinity Score (closeness to a specific user profile)
- Cultural and behavioral tags (e.g., "Foodie Destination")

## 3. Tags and Categories
- Cuisine Type (e.g., Italian, vegan, seafood, Asian cuisine)
- Ambiance (e.g., romantic, family-friendly, luxury, casual)
- Price Level (1-4 range, like $ signs)
- Features (e.g., brunch, late night, reservations required, accessible)
- Dietary Restrictions (vegan, gluten-free, halal, kosher)
- Accessibility (accessible, child-friendly)
- Special occasions/services (brunch, happy hour, live music)

## 4. External Source Matching and Extra Fields
- Matching with guides like Michelin, Resy, Tripadvisor, Tablet (with filter.external.exists)
- Rating, review count fields from these sources (if available)
- Notable executive chefs
- Price range (price range)
- Operating hours (hours)
- Geohash (geographic encoding)
- Parent/child entity relationships (e.g., restaurant in a shopping mall)
- Related entities (similar restaurants, nearby venues)

## 5. Menu and Food Details
- Menu items (menu items) – may be available in some restaurants, not guaranteed
- Restaurant menu details – may be available in some restaurants, mentioned in API documentation but no example response shown

## 6. User and Demographic Analysis
- Recommendation and affinity score based on user profile
- Demographic segmentation (age, gender, country, city, etc.)
- Location-based analysis and recommendations

## 7. Recommendation and Analysis Functions
- Similar places recommendation for a specific restaurant/venue
- Best venues based on specific cuisine or feature
- Location-based trend and popularity analysis
- Tag and entity-based comparison and analysis
- Heatmap showing interest intensity



1.What robotic applications? (Service robot, cleaning robot, delivery robot, barista robot, etc.)
2.Geographic scope: Global or specific country/region/city?
3.Restaurant type: Only restaurants or cafes, hotels, bars, fast food chains included?
4.Determine Data Sources, Primary Sources
Robot manufacturers' reference/customer lists:
Pudu Robotics, Keenon Robotics, Bear Robotics, Softbank Robotics, etc. Examine "case studies", "global customers", "success stories" sections on websites.Technology and industry news:
TechCrunch, Robotics Business Review, HospitalityNet, Wired, The Spoon, etc.Restaurants' own websites and social media accounts:"We have robotic service!" announcements, press releases, Instagram/Facebook posts.
YouTube and media content:Video and news search with keywords like "restaurant with robot waiter".
5.Secondary Sources
TripAdvisor, Google Maps, Yelp platforms user reviews:Search with keywords like "There was a robot waiter, very interesting!"LinkedIn and Twitter:
Posts from restaurant owners, robot manufacturers, and technology influencers.Academic articles and industry reports:Publications titled "Robotics in hospitality".
6.Data Collection and Cleaning
Manual scanning:In the first stage, collect basic fields like restaurant name, address, country/city, robotic application type, robot brand, application date, image/link if available from the above sources.
Semi-automatic collection:You can extract data from manufacturer sites or news sites with web scraping (tools like BeautifulSoup, Selenium, Scrapy).
Crowdsourcing:You can get community contributions with a form like "Do you know a restaurant with robotic service?" on your website or social media channels.
7.Data Validation and Enrichment
Cross-checking:
Check if the same restaurant appears in multiple sources.Name and address normalization:Standardize different spellings and address formats.
Add extra fields:Add fields like "city", "country", "restaurant type", "website", "Qloo entity ID" (if available) for matching with Qloo API.
6.Continuous Updates and Sustainability
Regularly scan new sources to update the database.
Add new restaurants from users and industry stakeholders.
Enrich the database by matching with Qloo API and prepare it for analysis.
7.Automation and API Usage
For large-scale data, you can request API access from manufacturers or technology platforms.
You can automatically extract data from news sites and social media platforms with web scraping.
8.Ethical and Legal Considerations
Pay attention to the terms of use of relevant sites when doing web scraping.
Be careful not to collect personal data (PII) and comply with regulations like GDPR.


