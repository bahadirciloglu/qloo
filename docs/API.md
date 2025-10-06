API Overview
Insights API
With our enhanced Insights API, you can input any supported data category—entities, tags, demographics, audiences, and location—and receive detailed insights in return. It provides relevant recommendations based on your specified parameters, making it a powerful tool for data-driven decision-making.

Ways to Use Our API
Basic Insights: Retrieve recommendations based on the entity type
Demographic Insights: Retrieve the demographic affinity scores for an entity or tag
Heatmaps: Generate heatmap data
Location Insights: Retrieve recommendations based on location
Taste Analysis: Retrieve tag metadata.
Supporting APIs
The Supporting APIs extend the Insights API by providing lookup and analysis capabilities. Use these endpoints to discover valid tags and audiences, and to perform deeper entity analysis and comparisons.

Capabilities include:

Searching for supported tags and their IDs
Listing available audience types and audiences
Retrieving tag types by entity category
APIs:

Analysis
Analysis Compare
Find Audiences
Get Audience Types
Tags Search
Tag Types
Entity Data APIs
These APIs allow you to search for and retrieve detailed information on entities, including identifying trends, properties, and related data. These APIs support functions like searching by name, fetching entities by IDs, and analyzing trends for specific entities.

Entity Search
Entity Search by ID
Trending Entities
Week-Over-Week Trending Data

API Onboarding and Authentication
Welcome to the Insights API! With our powerful API, you can take advantage of advanced AI-driven recommendations and insights. This guide will help you get up and running quickly by walking you through authentication, making your first API call, and exploring key features.

Accessing the API
Get an API Key
To get started, you'll need an API key. Simply contact us, and we'll generate one for you.

Authentication
Once you have your API key, authenticate your requests by including it in the request headers.

cURL
JavaScript
Python

curl --location --request GET 'https://staging.api.qloo.com/v2/insights?query=audi' \
--header 'Content-Type: application/json' \
--header 'X-Api-Key: <your-api-key>'
Making Your First API Call
Now that you're set up, you can make your first request. Here’s a request example that returns a list of movies tagged as comedies. It includes:

The API request URL
An entity type filter indicating the results should only include movies
A filter narrowing results to entities tagged with "comedy"
Your API key for authentication
Basic Insights Request Example

curl --location 'https://staging.api.qloo.com/v2/insights/?filter.type=urn:entity:movie&filter.tags=urn:tag:genre:media:comedy' \
--header 'x-api-key: x-api-key'
To dig deeper into a basic Insights request, explore our basic request use case.

Handling Responses
After making a request, you’ll receive a response like this:

Basic Insights Response Example

{
    "success": true,
    "results": {
        "entities": [
            {
                "name": "Django Unchained",
                "entity_id": "369D1544-628B-4C21-95A0-1488117A308A",
                "type": "urn:entity",
                "subtype": "urn:entity:movie",
                "properties": {
                    "release_year": 2012,
                    "release_date": "2012-12-25",
                    "description": "With the help of a German bounty-hunter, a freed slave sets out to rescue his wife from a brutal plantation owner in Mississippi.",
                    "content_rating": "R",
                    "duration": 165,
                    "image": {
                        "url": "https://staging.images.qloo.com/i/369D1544-628B-4C21-95A0-1488117A308A-420x-outside.jpg"
                    },
                    "akas": [
                        {
                            "value": "Django Unchained",
                            "languages": [
                                "fy"
                            ]
                        },
                        {
                            "value": "被解放的姜戈",
                            "languages": [
                                "zh"
                            ]
                        },
                        {
                            "value": "Джанго освобождённый",
                            "languages": [
                                "ru"
                            ]
                        },
. . .
 ],
                    "filming_location": "Evergreen Plantation - 4677 Highway 18, Edgard, Louisiana, USA",
                    "production_companies": [
                        "The Weinstein Company",
                        "Columbia Pictures"
                    ],
                    "release_country": [
                        "United States"
                    ],
                    "short_descriptions": [
                        {
                            "value": "filme de 2012 realizado por Quentin Tarantino",
                            "languages": [
                                "pt"
                            ]
                        },
                        {
                            "value": "அமெரிக்க மேற்கத்திய திரைப்படம்",
                            "languages": [
                                "ta"
                            ]
                        },
. . .
                    "popularity": 0.9998529346882951,
                    "tags": [
                    {
                        "id": "urn:tag:keyword:media:ex_slave",
                        "name": "Ex Slave",
                        "type": "urn:tag:keyword:media"
                    },
                    {
                        "id": "urn:tag:streaming_service:media:universcine",
                        "name": "Universcine",
                        "type": "urn:tag:streaming_service:media"
                    },
                    {
                        "id": "urn:tag:keyword:media:historical_fiction",
                        "name": "Historical Fiction",
                        "type": "urn:tag:keyword:media"
                    },
                    {
                        "id": "urn:tag:streaming_service:media:paramount_roku_premium_channel",
                        "name": "Paramount+ Roku Premium Channel",
                        "type": "urn:tag:streaming_service:media"
                    },
                    {
                        "id": "urn:tag:streaming_service:media:apple_tv",
                        "name": "Apple Tv",
                        "type": "urn:tag:streaming_service:media"
                    },
                    {
                        "id": "urn:tag:streaming_service:media:magentatv",
                        "name": "Magentatv",
                        "type": "urn:tag:streaming_service:media"
                    },
                    {
                        "id": "urn:tag:keyword:media:pre_civil_war",
                        "name": "Pre Civil War",
                        "type": "urn:tag:keyword:media"
                    },
                    {
                        "id": "urn:tag:streaming_service:media:movistar_plus",
                        "name": "Movistar Plus",
                        "type": "urn:tag:streaming_service:media"
                    },
                    {
. . .
               {
                "name": "Guardians of the Galaxy",
                "entity_id": "02F3FF8C-74F3-4188-A39D-24B34BEF3401",
                "type": "urn:entity",
                "subtype": "urn:entity:movie",
                "properties": {
                    "release_year": 2014,
                    "release_date": "2014-08-01",
                    "description": "A group of intergalactic criminals must pull together to stop a fanatical warrior with plans to purge the universe.",
                    "content_rating": "PG-13",
                    "duration": 121,
                    "image": {
                        "url": "https://staging.images.qloo.com/i/02F3FF8C-74F3-4188-A39D-24B34BEF3401-420x-outside.jpg"
                    },
                    "akas": [
                        {
                            "value": "Пазители на Галактиката",
                            "languages": [
                                "bg"
                            ]
                        },
                        {
                            "value": "Галактика сақшылары",
                            "languages": [
                                "kk"
                            ]
                        },
                        {
                            "value": "Galaktikas sargi",
                            "languages": [
                                "lv"
                            ]
                        },
. . .
                    ],
                    "filming_location": "Longcross Studios, Chobham Lane, Longcross, Chertsey, Surrey, England, UK",
                    "production_companies": [
                        "Moving Pictures Company",
                        "Walt Disney Pictures",
                        "Marvel Studios"
                    ],
                    "release_country": [
                        "United States",
                        "United Kingdom"
                    ],
                    "short_descriptions": [
                        {
                            "value": "2014 елның фильмы",
                            "languages": [
                                "tt"
                            ]
                        },
                        {
                            "value": "סרט מדע בדיוני מבית מארוול",
                            "languages": [
                                "he"
                            ]
                        },
                     ],
                    "websites": [
                        "http://www.facebook.com/guardiansmovie",
                        "https://www.instagram.com/guardiansofthegalaxy/"
                    ]
                },
                "popularity": 0.9996176301895672,
                "tags": [
                    {
                        "id": "urn:tag:streaming_service:media:directv",
                        "name": "Directv",
                        "type": "urn:tag:streaming_service:media"
                    },
                    {
                        "id": "urn:tag:keyword:media:raccoon",
                        "name": "Raccoon",
                        "type": "urn:tag:keyword:media"
                    },
                    {
                        "id": "urn:tag:keyword:media:ronan_accuser_character",
                        "name": "Ronan The Accuser Character",
                        "type": "urn:tag:keyword:media"
                    },
                    {
                        "id": "urn:tag:streaming_service:media:mediaset_infinity",
                        "name": "Mediaset Infinity",
                        "type": "urn:tag:streaming_service:media"
                    },
. . .
        ]
    },
    "duration": 22
}
The response contains details about the entities that match your request.

Key Features of the API
Flexible Input and Output: Seamlessly processes a wide range of data types—entities, tags, demographics, audiences, and location—allowing you to input and receive highly relevant results across the same categories.
Extensive Filtering and Customization: With a broad range of filters and signal parameters, you can fine-tune your queries to ensure the results are precisely tailored to your needs. Whether you're focusing on specific genres, demographics, or locations, the Insights API offers the flexibility you need.
Versatile Applications: Suitable for live personalization, CRM optimization, product development, media buying, and more.
Common Use Cases
The Insights API is versatile and can be applied across a wide range of use cases. It gives you the tools to unlock powerful insights into user preferences and behaviors.

API System Status
View the current status of the services listed below:



Insights API Deep Dive
get
https://staging.api.qloo.com/v2/insights
Returns taste-based insights based on the input parameters you provide.

Qloo’s Insights API helps uncover the underlying factors that shape human preferences, offering cultural intelligence about how people relate to different entities like brands, artists, destinations, and more. It draws from billions of signals to deliver nuanced, taste-based insights that reflect real-world behavior and affinities.

This Deep Dive is designed to help users explore the full capabilities of the Insights API, emphasizing how different parameters shape results. It allows you to view and test the complete set of supported parameters directly on this page, making it easier to explore functionality in context and understand how different inputs impact responses.

Helpful Resources
Need to understand how current parameters map to legacy fields? Visit the Parameter Reference.
Want to know which parameters are valid for each entity type (like Actor, Destination, or Brand)? See the Entity Type Parameter Guide.
🚧
Participating in the Qloo LLM Hackathon?

Use the dedicated hackathon API URL for all requests:
https://hackathon.api.qloo.com

Hackathon API keys won’t work on staging or production URLs.

Not signed up yet? Join the hackathon here.

Query Params
filter.type
string
required
Filter by the category of entity to return (urn:entity:place).


urn:entity:artist
bias.trends
string
The level of impact a trending entity has on the results. Supported by select categories only.


low
diversify.by
string
Limits results to a set number of high-affinity entities per city. Set this to "properties.geocode.city" to enable city-based diversification. Cities are ranked based on the highest-affinity entity within them, and entities within each city are ordered by their individual affinities.

diversify.take
integer
≥ 1
Sets the maximum number of results to return per city when using "diversify.by": "properties.geocode.city". For example, if set to 5, the response will include up to 5 entities with the highest affinities in each city.

feature.explainability
boolean
Defaults to false
When set to true, the response includes explainability metadata for each recommendation and for the overall result set.

Per-recommendation: Each result includes a query.explainability section showing which input entities (e.g. signal.interests.entities) contributed to the recommendation and by how much. Scores are normalized between 0–1. Entities with scores ≥ 0.1 are always included; those below may be omitted to reduce response size.

Aggregate impact: The top-level query.explainability object shows average influence of each input entity across top-N result subsets (e.g. top 3, 5, 10, all).

Note: If explainability cannot be computed for the request, a warning is included under query.explainability.warning, but results still return normally.


false
filter.address
string
Filter by address using a partial string query.

filter.content_rating
string
Filter by a comma-separated list of content ratings based on the MPAA film rating system, which determines suitability for various audiences.


PG
filter.date_of_birth.max
date
Filter by the most recent date of birth desired for the queried person.

filter.date_of_birth.min
date
Filter by the earliest date of birth desired for the queried person.

filter.date_of_death.max
date
Filter by the most recent date of death desired for the queried person.

filter.date_of_death.min
date
Filter by the earliest date of death desired for the queried person.

filter.exclude.tags
string
Exclude entities associated with a comma-separated list of tags.

operator.exclude.tags
string
Specifies how multiple filter.exclude.tags values are combined in the query. Use "union" (equivalent to a logical "or") to exclude results that contain at least one of the specified tags, or "intersection" (equivalent to a logical "and") to exclude only results that contain all specified tags. The default is "union".


union
filter.exists
string
Filter results to include only entities that have one or more specified properties. Use properties.image to return only entities that include an image URL.

filter.external.exists
string
Filter by a comma-separated list of external keys. (resy|michelin|tablet).

operator.filter.external.exists
string
Specifies how multiple filter.external.exists values are combined in the query. Use "union" (equivalent to a logical "or") to return results that match at least one of the specified external keys (e.g., resy, michelin, or tablet), or "intersection" (equivalent to a logical "and") to return only results that match all specified external keys. The default is "union".


union
filter.external.resy.count.max
integer
≥ 0
Filter places to include only those with a Resy rating count less than or equal to the specified maximum. Applies only to entities with filter.type of urn:entity:place.

filter.external.resy.count.min
integer
≥ 0
Filter places to include only those with a Resy rating count greater than or equal to the specified minimum. Applies only to entities with filter.type of urn:entity:place.

filter.external.resy.party_size.max
integer
≥ 1
Filter by the maximum supported party size required for a Point of Interest.

filter.external.resy.party_size.min
integer
≥ 1
Filter by the minimum supported party size required for a Point of Interest.

filter.external.resy.rating.max
number
0 to 5
Filter places to include only those with a Resy rating less than or equal to the specified maximum (1–5 scale). Applies only to entities with filter.type of urn:entity:place.

filter.external.resy.rating.min
number
0 to 5
Filter places to include only those with a Resy rating greater than or equal to the specified minimum (1–5 scale). Applies only to entities with filter.type of urn:entity:place.

filter.external.tripadvisor.rating.count.min
integer
≥ 0
Filter places to include only those with a Tripadvisor review count greater than or equal to the specified minimum. This filter only applies to entities with filter.type of urn:entity:place.

filter.external.tripadvisor.rating.count.max
integer
≥ 0
Filter places to include only those with a Tripadvisor review count less than or equal to the specified maximum. This filter only applies to entities with filter.type of urn:entity:place.

filter.external.tripadvisor.rating.max
number
0 to 5
Filter places to include only those with a Tripadvisor rating less than or equal to the specified maximum. This filter only applies to entities with filter.type of urn:entity:place.

filter.external.tripadvisor.rating.min
number
0 to 5
Filter places to include only those with a Tripadvisor rating greater than or equal to the specified minimum. This filter only applies to entities with filter.type of urn:entity:place.

filter.finale_year.max
integer
Filter by the latest desired year for the final season of a TV show.

filter.finale_year.min
integer
Filter by the earliest desired year for the final season of a TV show.

filter.gender
string
Filter results to align with a specific gender identity. Used to personalize output based on known or inferred gender preferences.

filter.geocode.admin1_region
string
Filter by properties.geocode.admin1_region. Exact match (usually state).

filter.geocode.admin2_region
string
Filter by properties.geocode.admin2_region. Exact match (often county or borough).

filter.geocode.country_code
string
Filter by properties.geocode.country_code. Exact match (two-letter country code).

filter.geocode.name
string
Filter by properties.geocode.name. Exact match (usually city or town name).

filter.hotel_class.max
integer
1 to 5
Filter by the maximum desired hotel class (1-5, inclusive).

filter.hotel_class.min
integer
1 to 5
Filter by the minimum desired hotel class (1-5, inclusive).

filter.hours
string
Filter by the day of the week the Point of Interest must be open (Monday, Tuesday, etc.).


monday
filter.latest_known_year.max
integer
Filter by a certain maximum year that shows were released or updated.

filter.latest_known_year.min
integer
Filter by a certain minimum year that shows were released or updated.

filter.location
string
Used to filter by a WKT POINT, POLYGON, MULTIPOLYGON or a single Qloo ID for a named urn:entity:locality. WKT is formatted as X then Y, therefore longitude is first (POINT(-73.99823 40.722668)). If a Qloo ID or WKT POLYGON is passed, filter.location.radius will create a fuzzy boundary when set to a value > 0.

filter.exclude.location
string
Exclude results that fall within a specific location, defined by either a WKT POINT, POLYGON, MULTIPOLYGON, or a Qloo ID for a named urn:entity:locality. WKT is formatted with longitude first (e.g., POINT(-73.99823 40.722668)). When using a locality ID or a WKT POLYGON, setting filter.location.radius to a value > 0 creates a fuzzy exclusion boundary.

filter.location.query
A query used to search for one or more named urn:entity:locality Qloo IDs for filtering requests, equivalent to passing the same Locality Qloo ID(s) into filter.location.

For GET requests: Provide a single locality query as a string.
For POST requests:
You can still send a single locality as a string.
Or you can send an array of locality names to query multiple localities at once. When multiple localities are provided, their geographic shapes are merged, and the system returns results with the highest affinities across the combined area.
Locality queries are fuzzy-matched and case-insensitive. Examples include New York City, Garden City, New York, Los Angeles, Lower East Side, and AKAs like The Big Apple. When a single locality is supplied, the response JSON includes query.locality.signal with the matched Qloo entity. If multiple are supplied, this field is omitted. By default, the API includes a tuning that also captures nearby entities just outside the official boundaries of the locality. To turn this off and limit results strictly to within the locality, set filter.location.radius=0. If no localities are found, the API returns a 400 error.


string

array
filter.exclude.location.query
A query used to exclude results based on one or more named urn:entity:locality Qloo IDs, resolved from fuzzy-matched locality names. This is equivalent to passing the resolved Locality Qloo ID(s) into filter.exclude.location.

For GET requests: Provide a single locality query as a string. - For POST requests:
You can still send a single locality as a string.
Or send an array of locality names to exclude multiple areas at once. When multiple localities are provided, their geographic shapes are merged, and the system excludes results from across the combined area.
Locality queries are case-insensitive and support common AKAs (e.g., The Big Apple for New York). When a single locality is supplied, the response includes query.locality.exclude.signal with the matched Qloo entity. If multiple are supplied, this field is omitted. If no localities are matched, the API returns a 400 error.


string

array
filter.location.geohash
string
Filter by a geohash. Geohashes are generated using the Python package pygeohash with a precision of 12 characters. This parameter returns all POIs that start with the specified geohash. For example, supplying dr5rs would allow returning the geohash dr5rsjk4sr2w.

filter.exclude.location.geohash
string
Exclude all entities whose geohash starts with the specified prefix. Geohashes are generated using the Python package pygeohash with a precision of 12 characters. For example, supplying dr5rs would exclude any result whose geohash begins with dr5rs, such as dr5rsjk4sr2w.

filter.location.radius
integer
Defaults to 15000
Filter by the radius (in meters) when also supplying filter.location or filter.location.query. When this parameter is not provided, the API applies a default tuning that slightly expands the locality boundary to include nearby entities outside its official shape. To disable this behavior and strictly limit results to entities inside the defined locality boundary, set filter.location.radius=0.

15000
filter.parents.types
array of strings
Filter by a comma-separated list of parental entity types (urn:entity:place). Each type must match exactly.


ADD string
filter.popularity.max
number
0 to 1
Filter by the maximum popularity percentile a Point of Interest must have (float, between 0 and 1; closer to 1 indicates higher popularity, e.g., 0.98 for the 98th percentile).

filter.popularity.min
number
0 to 1
Filter by the minimum popularity percentile required for a Point of Interest (float, between 0 and 1; closer to 1 indicates higher popularity, e.g., 0.98 for the 98th percentile).

filter.price_level.max
integer
1 to 4
Filter by the maximum price level a Point of Interest can have (1|2|3|4, similar to dollar signs).

filter.price_level.min
integer
1 to 4
Filter by the minimum price level a Point of Interest can have (1|2|3|4, similar to dollar signs).

filter.price_range.from
integer
0 to 1000000
Filter places by a minimum price level, representing the lowest price in the desired range. Accepts an integer value between 0 and 1,000,000.

filter.price_range.to
integer
0 to 1000000
Filter places by a maximum price level, representing the highest price in the desired range. Accepts an integer value between 0 and 1,000,000. Only applies to places.

filter.price.max
float
maximum price

filter.price.min
float
minimum price

filter.properties.business_rating.max
float
Filter by the highest desired business rating.


3
filter.properties.business_rating.min
float
Filter by the lowest desired business rating.


3
filter.publication_year.max
number
Filter by the latest desired year of initial publication for the work.

filter.publication_year.min
number
Filter by the earliest desired year of initial publication for the work.

filter.rating.max
number
0 to 5
Filter by the maximum Qloo rating a Point of Interest must have (float, between 0 and 5).

filter.rating.min
number
0 to 5
Filter by the minimum Qloo rating a Point of Interest must have (float, between 0 and 5).

filter.references_brand
array of strings
Filter by a comma-separated list of brand entity IDs. Use this to narrow down place recommendations to specific brands. For example, to include only Walmart stores, pass the Walmart brand ID. Each ID must match exactly.


ADD string
filter.release_country
array of strings
Filter by a list of countries where a movie or TV show was originally released.


ADD string
operator.filter.release_country
string
Specifies how multiple `filter.release_country`` values are combined in the query. Use "union" (equivalent to a logical "or") to return results that match at least one of the specified countries, or "intersection" (equivalent to a logical "and") to return only results that match all specified countries. The default is "union".


union
filter.release_date.max
date
Filter by the latest desired release date.

filter.release_date.min
date
Filter by the earliest desired release date.

filter.release_year.max
integer
Filter by the latest desired release year.

filter.release_year.min
integer
Filter by the earliest desired release year.

filter.results.entities
string
Filter by a comma-separated list of entity IDs. Often used to assess the affinity of an entity towards input.

filter.results.entities.query
Search for one or more entities by name to use as filters. - For GET requests: Provide a single entity name as a string. - For POST requests: You can provide a single name or an array of names.


string

array
filter.exclude.entities
string
A comma-separated list of entity IDs to remove from the results.

filter.exclude.entities.query
array
This parameter can only be supplied when using POST HTTP method, since it requires JSON encoded body. The value for filter.exclude.entities.query is a JSON array with objects containing the name and address properties. For a fuzzier search, just include an array of strings. When supplied, it overwrites the filter.exclude.entities object with resolved entity IDs. The response will contain a path query.entities.exclude, with partial Qloo entities that were matched by the query. If no entities are found, the API will throw a 400 error.


ADD
filter.results.tags
array of strings
Filter by a comma-separated list of tag IDs. Often used to assess the affinity of a tag towards input.


ADD string
filter.tags
string
Filter by a comma-separated list of tag IDs (urn:tag:genre:restaurant:Italian).

operator.filter.tags
string
Specifies how multiple filter.tags values are combined in the query. Use "union" (equivalent to a logical "or") to return results that match at least one of the specified tags, or "intersection" (equivalent to a logical "and") to return only results that match all specified tags. The default is "union".


union
offset
integer
The number of results to skip, starting from 0. Allows arbitrary offsets but is less commonly used than page.

output.heatmap.boundary
string
Indicates the type of heatmap output desired: The default is geohashes. The other options are a city or a neighborhood.

page
integer
≥ 1
The page number of results to return. This is equivalent to take + offset and is the recommended approach for most use cases.

signal.demographics.age
string
A comma-separated list of age ranges that influence the affinity score.(35_and_younger|36_to_55|55_and_older).


36_to_55
signal.demographics.age.weight
Specifies the extent to which results should be influenced by age-based demographic signals. Higher values increase the influence of age data; lower values reduce its impact.


number

string
signal.demographics.audiences.weight
Specifies the extent to which results should be influenced by the preferences of the selected audience. Higher values increase the influence of audience preferences; lower values reduce their impact.


number

string
signal.demographics.audiences
array of strings
A comma-separated list of audiences that influence the affinity score. Audience IDs can be retrieved via the v2/audiences search route.


ADD string
signal.demographics.gender
string
Influence the affinity score based on gender (male|female).


male
signal.demographics.gender.weight
Specifies the extent to which results should be influenced by gender-based demographic signals. Higher values increase the influence of gender data; lower values reduce its impact.


number

string
signal.interests.entities
array of strings
Allows you to supply a list of entities to influence affinity scores. You can also include a weight property that will indicate the strength of influence for each entity in your list.

For GET requests: Provide a comma-separated list of entity IDs.
For POST requests, you can either:
Send the same string of comma-separated values.
Send an array of objects with "entity" and "weight" properties, such as: [ { "entity": "urn:entity:movie:inception", "weight": 10 }, { "entity": "urn:entity:movie:interstellar", "weight": 25 } ] Weights must be greater than 0 and are relative. So, a weight of 25 means that entity will more heavily influence affinity scores than a weight of 10.

ADD string
signal.interests.entities.query
array
This parameter can only be supplied when using POST HTTP method, which requires a JSON-encoded body. The value should be a JSON array of objects with 'name' and 'address' properties; supports 'resolve_to' for specifying resolution to place, brand, or both.


ADD
signal.interests.entities.weight
Specifies the extent to which results should be influenced by the relevance of entities (in-domain or cross-domain). Higher values increase the influence of entities; lower values reduce their impact.


number

string
signal.interests.tags
Allows you to supply a list of tags to influence affinity scores. You can also include a weight property that will indicate the strength of influence for each tag in your list.

For GET requests: Provide a comma-separated list of tag IDs.
For POST requests, you can either:
Send the same string of comma-separated values.
Send an array of objects with "tag" and "weight" properties, such as: [ { "tag": "urn:tag:genre:media:horror", "weight": 7 }, { "tag": "urn:tag:genre:media:thriller", "weight": 20 } ] Weights must be greater than 0 and are relative. So, a weight of 20 means that tag will more heavily influence affinity scores than a weight of 7.

array

array
signal.interests.tags.weight
Specifies the extent to which results should be influenced by the presence of tags (taste analysis). Higher values increase the influence of tags; lower values reduce their impact.


number

string
signal.location
string
The geolocation to use for geospatial results. The value will be a WKT POINT, POLYGON or a single Qloo ID for a named urn:entity:locality to filter by. WKT is formatted as X then Y, therefore longitude is first (POINT(-73.99823 40.722668)). Unlike filter.location.radius, signal.location.radius is ignored if a Qloo ID or WKT POLYGON is passed.

signal.location.radius
integer
The optional radius (in meters), used when providing a WKT POINT. We generally recommend avoiding this parameter, as it overrides dynamic density discovery.

signal.location.query
string
A string query used to search for a named urn:entity:locality Qloo ID for geospatial results, effectively equivalent to passing the same Locality Qloo ID into signal.location. Examples of locality queries include New York City, Garden City, New York, Los Angeles, Lower East Side, and AKAs like The Big Apple. These queries are fuzzy-matched and case-insensitive. When filter.location.query is supplied, the response JSON will include query.locality.signal, which contains the partially matched Qloo entity. If no locality is found, the API will return a 400 error.

signal.location.weight
Specifies the extent to which results should be influenced by location-based signals (geospatial). Higher values increase the influence of location; lower values reduce its impact.


number

string
sort_by
string
This parameter modifies the results sorting algorithm (affinity|distance). The distance option can only be used when `filter.location`` is supplied.


affinity
take
integer
≥ 1
The number of results to return.

Responses

200
Successful Operation

400
Bad Request

500
Internal Server Error

Parameter Reference
Parameter categories, descriptions, types, and mappings to Legacy API parameter names

This is a comprehensive list of parameters for the Insights API. It includes a mapping of our legacy API parameter names to the Insights API parameter names where applicable.

All Insights parameters fall into one of the following categories:

Filters: Parameters used to narrow down the results based on criteria such as type, popularity, and tags.
Signal: Parameters that influence recommendations by weighting factors such as demographics, biases, and user interests.
Output: Parameters used to control the output, including the pagination of results.
Filters
Parameter Name	Type	Description	API 1.0 Parameter
filter.address

string

Filter by address using a partial string query.

filter.audience.types

array of strings

Filter by a list of audience types.

filter.content_rating

string

Filter by a comma-separated list of content ratings based on the MPAA film rating system, which determines suitability for various audiences.

filter.date_of_birth.max

string, YYYY-MM-DD

Filter by the most recent date of birth desired for the queried person.

filter.date_of_birth.min

string, YYYY-MM-DD

Filter by the earliest date of birth desired for the queried person.

filter.date_of_death.max

string, YYYY-MM-DD

Filter by the most recent date of death desired for the queried person.

filter.date_of_death.min

string, YYYY-MM-DD

Filter by the earliest date of death desired for the queried person.

filter.entities

string

Filter by a comma-separated list of entity IDs. Often used to assess the affinity of an entity towards input.

filter.entity_ids

filter.exclude.entities

string

A comma-separated list of entity IDs to remove from the results.

filter.exclude.entities.query

This parameter can only be supplied when using POST HTTP method, since it requires JSON encoded body. The value for filter.exclude.entities.query is a JSON array with objects containing the name and address properties. For a fuzzier search, just include an array of strings. When supplied, it overwrites the filter.exclude.entities object with resolved entity IDs. The response will contain a path query.entities.exclude, with partial Qloo entities that were matched by the query. If no entities are found, the API will throw a 400 error.

filter.exclude.tags

string

Exclude entities associated with a comma-separated list of tags.

exclude.tags

operator.exclude.tags

string

Specifies how multiple filter.exclude.tags values are combined in the query. Use "union" (equivalent to a logical "or") to exclude results that contain at least one of the specified tags, or "intersection" (equivalent to a logical "and") to exclude only results that contain all specified tags. The default is "union".

filter.external.exists

string

Filter by a comma-separated list of external keys.
(resy|michelin|tablet).

filter.exists

operator.filter.external.exists

string

Specifies how multiple filter.external.exists values are combined in the query. Use "union" (equivalent to a logical "or") to return results that match at least one of the specified external keys (e.g., resy, michelin, or tablet), or "intersection" (equivalent to a logical "and") to return only results that match all specified external keys. The default is "union".

filter.external.resy.count.max

integer

Filter places to include only those with a Resy rating count less than or equal to the specified maximum. Applies only to entities with filter.type of urn:entity:place.

filter.external.resy.count.min

integer

Filter places to include only those with a Resy rating count greater than or equal to the specified minimum. Applies only to entities with filter.type of urn:entity:place.

filter.external.resy.party_size.max

integer

Filter by the maximum supported party size required for a Point of Interest.

filter.external.resy.party_size.min

integer

Filter by the minimum supported party size required for a Point of Interest.

filter.external.resy.rating.max

float

Filter places to include only those with a Resy rating less than or equal to the specified maximum (1–5 scale). Applies only to entities with filter.type of urn:entity:place.

filter.external.resy.rating.min

float

Filter places to include only those with a Resy rating greater than or equal to the specified minimum (1–5 scale). Applies only to entities with filter.type of urn:entity:place.

filter.external.tripadvisor.rating.count.max

integer

Filter places to include only those with a Tripadvisor review count less than or equal to the specified maximum.
This filter only applies to entities with filter.type of urn:entity:place.

filter.external.tripadvisor.rating.count.min

integer

Filter places to include only those with a Tripadvisor review count greater than or equal to the specified minimum.
This filter only applies to entities with filter.type of urn:entity:place.

filter.external.tripadvisor.rating.max

float

Filter places to include only those with a Tripadvisor rating less than or equal to the specified maximum. This filter only applies to entities with filter.type of urn:entity:place.

filter.external.tripadvisor.rating.min

float

Filter places to include only those with a Tripadvisor rating greater than or equal to the specified minimum. This filter only applies to entities with filter.type of urn:entity:place.

filter.finale_year.max

integer

Filter by the latest desired year for the final season of a TV show.

filter.finale_year.min

integer

Filter by the earliest desired year for the final season of a TV show.

filter.gender

string

Filter results to align with a specific gender identity. Used to personalize output based on known or inferred gender preferences.

filter.geocode.admin1_region

string

Filter by properties.geocode.admin1_region. Exact match (usually state).

filter.geocode.admin2_region

string

Filter by properties.geocode.admin2_region. Exact match (often county or borough).

filter.geocode.country_code

string

Filter by properties.geocode.country_code. Exact match (two-letter country code).

filter.geocode.name

string

Filter by properties.geocode.name. Exact match (usually city or town name).

filter.hotel_class.max

integer

Filter by the maximum desired hotel class (1-5, inclusive).

filter.hotel_class.min

integer

Filter by the minimum desired hotel class (1-5, inclusive).

filter.hours

string

Filter by the day of the week the Point of Interest must be open (Monday, Tuesday, etc.).

filter.ids

string

Filter by a comma-separated list of audience IDs.

filter.latest_known_year.max

integer

Filter by a certain maximum year that shows were released or updated.

filter.latest_known_year.min

integer

Filter by a certain minimum year that shows were released or updated.

filter.location

string

Filter by a WKT POINT, POLYGON, MULTIPOLYGON or a single Qloo ID for a named urn:entity:locality.

WKT is formatted as X then Y, therefore longitude is first (POINT(-73.99823 40.722668)).

If a Qloo ID or WKT POLYGON is passed, filter.location.radius will create a <glossary:fuzzy> boundary when set to a value > 0.

filter.location

filter.exclude.location

string

Exclude results that fall within a specific location, defined by either a WKT POINT, POLYGON, MULTIPOLYGON, or a Qloo ID for a named urn:entity:locality.
WKT is formatted with longitude first (e.g., POINT(-73.99823 40.722668)).
When using a locality ID or a WKT POLYGON, setting filter.location.radius to a value > 0 creates a fuzzy exclusion boundary.

filter.location.query

string

A query used to search for one or more named urn:entity:locality Qloo IDs for filtering requests, equivalent to passing the same Locality Qloo ID(s) into filter.location.

For GET requests: Provide a single locality query as a string.
For POST requests:
You can still send a single locality as a string.
Or you can send an array of locality names to query multiple localities at once. When multiple localities are provided, their geographic shapes are merged, and the system returns results with the highest affinities across the combined area.Locality queries are fuzzy-matched and case-insensitive. Examples include New York City, Garden City, New York, Los Angeles, Lower East Side, and AKAs like The Big Apple. When a single locality is supplied, the response JSON includes query.locality.signal with the matched Qloo entity. If multiple are supplied, this field is omitted. By default, the API includes a tuning that also captures nearby entities just outside the official boundaries of the locality. To turn this off and limit results strictly to within the locality, set filter.location.radius=0. If no localities are found, the API returns a 400 error.
filter.exclude.location.query

string

Exclude results that fall within a specific location, defined by either a WKT POINT, POLYGON, MULTIPOLYGON, or a Qloo ID for a named urn:entity:locality.
WKT is formatted with longitude first (e.g., POINT(-73.99823 40.722668)).
When using a locality ID or a WKT POLYGON, setting filter.location.radius to a value > 0 creates a fuzzy exclusion boundary.

filter.location.geohash

string

Filter by a geohash. Geohashes are generated using the Python package pygeohash with a precision of 12 characters. This parameter returns all POIs that start with the specified geohash. For example, supplying dr5rs would allow returning the geohash dr5rsjk4sr2w.

filter.exclude.location.geohash

string

Exclude all entities whose geohash starts with the specified prefix.
Geohashes are generated using the Python package pygeohash with a precision of 12 characters.
For example, supplying dr5rs would exclude any result whose geohash begins with dr5rs, such as dr5rsjk4sr2w.

filter.location.radius

integer

Filter by the radius (in meters) when also supplying filter.location or filter.location.query.
When this parameter is not provided, the API applies a default tuning that slightly expands the locality boundary to include nearby entities outside its official shape.
To disable this behavior and strictly limit results to entities inside the defined locality boundary, set filter.location.radius=0.

target.radius

filter.parents.types

array of strings

Filter by a comma-separated list of parental entity types (urn:entity:place). Each type must match exactly.

filter.popularity.max

number

Filter by the maximum popularity percentile a Point of Interest must have (float, between 0 and 1; closer to 1 indicates higher popularity, e.g., 0.98 for the 98th percentile).

filter.popularity.min

number

Filter by the minimum popularity percentile required for a Point of Interest (float, between 0 and 1; closer to 1 indicates higher popularity, e.g., 0.98 for the 98th percentile).

filter.popularity

filter.price_level.max

integer

Filter by the maximum price level a Point of Interest can have (1|2|3|4, similar to dollar signs).

filter.price_level.min

integer

Filter by the minimum price level a Point of Interest can have (1|2|3|4, similar to dollar signs).

filter.price_range.from

integer

Filter places by a minimum price level, representing the lowest price in the desired range. Accepts an integer value between 0 and 1,000,000.

filter.price_range.to

integer

Filter places by a maximum price level, representing the highest price in the desired range. Accepts an integer value between 0 and 1,000,000.

filter.properties.business_rating.max

float

Filter by the highest desired business rating.

filter.properties.business_rating.min

float

Filter by the lowest desired business rating.

filter.publication_year.max

number

Filter by the latest desired year of initial publication for the work.

filter.publication_year.min

number

Filter by the earliest desired year of initial publication for the work.

filter.rating.max

number

Filter by the maximum Qloo rating a Point of Interest must have (float, between 0 and 5).

filter.rating.min

number

Filter by the minimum Qloo rating a Point of Interest must have (float, between 0 and 5).

filter.references_brand

array of strings

Filter by a comma-separated list of brand entity IDs. Use this to narrow down place recommendations to specific brands. For example, to include only Walmart stores, pass the Walmart brand ID. Each ID must match exactly.

filter.references

filter.release_country

array of strings

Filter by a list of countries where a movie or TV show was originally released.

filter.results.entities

Filter by a comma-separated list of entity IDs. Often used to assess the affinity of an entity towards input.

filter.results.entities.query

Search for one or more entities by name to use as filters.

For GET requests: Provide a single entity name as a string.
For POST requests: You can provide a single name or an array of names.
operator.filter.release_country

string

Specifies how multiple filter.release_country values are combined in the query. Use "union" (equivalent to a logical "or") to return results that match at least one of the specified countries, or "intersection" (equivalent to a logical "and") to return only results that match all specified countries. The default is "union".

filter.release_date.max

string, YYYY-MM-DD

Filter by the latest desired release date.

filter.release_date.min

string, YYYY-MM-DD

Filter by the earliest desired release date.

filter.release_year.max

integer

Filter by the latest desired release year.

filter.release_year.min

integer

Filter by the earliest desired release year.

filter.tag.types

array of strings

Filter by a comma-separated list of audience types. Each audience type requires an exact match. You can retrieve a complete list of audience types via the v2/audiences/types route.

filter.tags

string

Filter by a comma-separated list of tag IDs (urn:tag:genre:restaurant:Italian).

filter.tags

operator.filter.tags

string

Specifies how multiple filter.tags values are combined in the query. Use "union" (equivalent to a logical "or") to return results that match at least one of the specified tags, or "intersection" (equivalent to a logical "and") to return only results that match all specified tags. The default is "union".

operator.filter.tags

filter.type

string

Filter by the <<glossary:entity type>> to return (urn:entity:place).

type

Signal
Parameter Name	Type	Description	API 1.0 Parameter
bias.trends

string

The level of impact a trending entity has on the results. Supported by select categories only.

bias.trends

signal.demographics.audiences

array of strings

A comma-separated list of audiences that influence the affinity score. Audience IDs can be retrieved via the v2/audiences search route.

bias.audiences

signal.demographics.audiences.weight

string

Specifies the extent to which results should be influenced by the preferences of the chosen audience.

bias.audiences.weight

signal.demographics.age

string

A comma-separated list of age ranges that influence the affinity score.(35_and_younger|36_to_55|55_and_older).

bias.age

signal.demographics.gender

string

Specifies whether to influence the affinity score based on gender (male|female).

bias.gender

signal.interests.entities

array of strings

A list of entity IDs that influence the affinity score. You can also include a weight property to indicate the strength of influence for each entity.

For GET requests: Provide a comma-separated list of entity IDs.
For POST requests, you can either:
-- Send the same string of comma-separated values.
-- Send an array of objects with entity and weight properties, such as:
[ { "entity": "urn:entity:movie:inception", "weight": 10 }, { "entity": "urn:entity:movie:interstellar", "weight": 25 } ]
Weights must be greater than 0 and are relative. A weight of 25 means that entity will more heavily influence affinity scores than a weight of 10.
signal.interests.entities.query

This parameter can only be supplied when using the POST HTTP method, which requires a JSON-encoded body. The value for signal.interests.entities.query is a JSON array containing objects with name and address properties. For a fuzzier search, you can provide an array of strings. When supplied, it overwrites the signal.interests.entities object with resolved entity IDs. The response will contain a path, query.entities.signal, with partial Qloo entities that were matched by the query. If no entities are found, a 400 error will be thrown by the API.

Additionally, you can specify how each signal.interests.entities.query item should resolve. Theresolve_to property determines whether to resolve to a place, brand, or both. Options are:

self: Resolves to a place (default behavior if resolve_to is omitted)

urn:reference:brand: Resolves to the brand.

both: Resolves to both a place and a brandBehavior:

The system will attempt to resolve to a place. If both or urn:reference:brand is used, it will also pull the brand associated with the resolved place.

Resolved entities are returned inside the response.query object:
--- If self or no resolve_to option is provided, the resolved place will include an index property pointing to the position of the query in signal.interests.entities.query.
--- If urn:reference:brand is provided and the brand is available, it will be returned with the resolved place's information, with entity_id changed to the brand's ID and subtype changed to urn:entity:brand.
--- If both is used, both the place and brand will be included, with their index properties pointing to the same value (using the same query). Warnings:

If a place does not resolve, it will be included in signal.interests.entities.query warnings as not_found.

If a place resolves but a requested brand does not, the brand will be added to the warning could_not_resolve_brand.

signal.interests.tags

string

Allows you to supply a list of tags to influence affinity scores. You can also include aweight property that will indicate the strength of influence for each tag in your list.

For GET requests: Provide a comma-separated list of tag IDs.
For POST requests, you can either:
-- Send the same string of comma-separated values.
-- Send an array of objects with "tag" and "weight" properties, such as:
[ { "tag": "urn:tag:genre:media:horror", "weight": 7 }, { "tag": "urn:tag:genre:media:thriller", "weight": 20 } ]
Weights must be greater than 0 and are relative. So, a weight of 20 means that tag will more heavily influence affinity scores than a weight of 7.
operator.signal.interests.tags

string

Specifies how multiple signal.interests.tags values are combined in the query.

Use "union" (equivalent to a logical "or") to return results that contain at least one of the specified tags. In this mode, the tag with the highest affinity is used for scoring. - Use "intersection" (equivalent to a logical "and") or leave this field empty to return results that contain all specified tags, with affinity scores merged across them.
signal.location

string

The geolocation to use for geospatial results. The value will be a WKT POINT, POLYGON or a single Qloo ID for a named urn:entity:locality to filter by.

WKT is formatted as X then Y, therefore longitude is first (POINT(-73.99823 40.722668)). Unlike filter.location.radius, signal.location.radius is ignored if a Qloo ID or WKT POLYGON is passed.

target

signal.location.query

string

A string query used to search for a named urn:entity:locality Qloo ID for geospatial results, effectively equivalent to passing the same Locality Qloo ID into signal.location.

Examples of locality queries include New York City, Garden City, New York, Los Angeles, Lower East Side, and AKAs like The Big Apple. These queries are <glossary:fuzzy>-matched and case-insensitive.

When filter.location.query is supplied, the response JSON will include query.locality.signal, which contains the partially matched Qloo entity. If no locality is found, the API will return a 400 error.

signal.location.radius

integer

The optional radius (in meters), used when providing a WKT POINT. We generally recommend avoiding this parameter, as it overrides dynamic density discovery.

filter.radius

Output
Parameter Name

Type

Description

API 1.0 Parameter

diversify.by

string

Limits results to a set number of high-affinity entities per city. Set this to properties.geocode.city to enable city-based diversification. Cities are ranked based on the highest-affinity entity within them, and entities within each city are ordered by their individual affinities.

diversify.take

integer

Sets the maximum number of results to return per city when using diversify.by: "properties.geocode.city". For example, if set to 5, the response will include up to 5 entities with the highest affinities in each city.

feature.explainability

boolean

When set to true, the response includes explainability metadata for each recommendation and for the overall result set.:


Per-recommendation: Each result includes a query.explainability section showing which input entities (e.g. signal.interests.entities) contributed to the recommendation and by how much. Scores are normalized between 0–1. Entities with scores ≥ 0.1 are always included; those below may be omitted to reduce response size.


Aggregate impact: The top-level query.explainability object shows average influence of each input entity across top-N result subsets (e.g. top 3, 5, 10, all).


Note: If explainability cannot be computed for the request, a warning is included under query.explainability.warning, but results still return normally.

offset

integer

The number of results to skip, starting from 0. Allows arbitrary offsets but is less commonly used than page.

output.heatmap.boundary

string

Indicates the type of heatmap output desired: The default is geohashes. The other options are a city or a neighborhood.

page

integer

The page number of results to return. This is equivalent to take + offset and is the recommended approach for most use cases.

page

sort_by

string

This parameter modifies the results sorting algorithm (affinity|distance). The distance option can only be used when filter.location is supplied.

sort_by

take

integer

The number of results to return.

take

Entity Type Parameter Guide
Retrieve recommendations based on the filter.type value

Recommendations are retrieved based on the selected filter.type, or entity type. A filter.type is a category of entities, such as a brand or destination.

Conditional Parameters
The parameters you can include in a request depend on the selected filter.type value: Album, Artist, Book, Brand, Destination, Movie, Person, Place, Podcast, TV Show, Video Game.

For comprehensive parameter information, visit the Parameters reference page.

Album
If your request is for albums, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
filter.exclude.entities	Optional
filter.parents.types	Optional
filter.popularity.min	Optional
filter.popularity.max	Optional
filter.release_date.min	Optional
filter.release_date.max	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
offset	Optional
signal.interests.entities	Optional
signal.interests.tags	Optional
take	Optional
Artist
If your request is for artists, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
bias.trends	Optional
filter.exclude.entities	Optional
filter.parents.types	Optional
filter.popularity.min	Optional
filter.popularity.max	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
offset	Optional
signal.demographics.age	Optional
signal.demographics.audiences	Optional
signal.demographics.audiences.weight	Optional
signal.demographics.gender	Optional
signal.interests.entities	Optional
signal.interests.tags	Optional
take	Optional
Book
If your request is for books, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
bias.trends	Optional
filter.exclude.entities	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
filter.parents.types	Optional
filter.popularity.min	Optional
filter.popularity.max	Optional
filter.publication_year.min	Optional
filter.publication_year.max	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
offset	Optional
signal.demographics.audiences	Optional
signal.demographics.age	Optional
signal.demographics.audiences.weight	Optional
signal.demographics.gender	Optional
signal.interests.entities	Optional
signal.interests.tags	Optional
take	Optional
Brand
If your request is for brands, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
bias.trends	Optional
filter.exclude.entities	Optional
operator.exclude.tags	Optional
filter.exclude.tags	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
filter.parents.types	Optional
filter.popularity.min	Optional
filter.popularity.max	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
signal.demographics.age	Optional
signal.demographics.audiences	Optional
signal.demographics.audiences.weight	Optional
signal.interests.entities	Optional
signal.demographics.gender	Optional
signal.interests.tags	Optional
offset	Optional
take	Optional
Destination
If your request is for destinations, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
bias.trends	Optional
filter.exclude.entities	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.geocode.name	Optional
filter.geocode.admin1_region	Optional
filter.geocode.admin2_region	Optional
filter.geocode.country_code	Optional
filter.location	Optional
filter.location.radius	Optional
filter.location.geohash	Optional
filter.exclude.location.geohash	Optional
filter.parents.types	Optional
filter.popularity.min	Optional
filter.popularity.max	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
offset	Optional
signal.demographics.age	Optional
signal.demographics.audiences	Optional
signal.demographics.audiences.weight	Optional
signal.demographics.gender	Optional
signal.interests.entities	Required
signal.interests.tags	Optional
take	Optional
Movie
If your request is for movies, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
bias.trends	Optional
filter.content_rating	Optional
filter.exclude.entities	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.parents.types	Optional
filter.popularity.min	Optional
filter.popularity.max	Optional
filter.release_year.min	Optional
filter.release_year.max	Optional
filter.release_country	Optional
operator.filter.release_country	Optional
filter.rating.min	Optional
filter.rating.max	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
offset	Optional
signal.demographics.audiences	Optional
signal.demographics.age	Optional
signal.demographics.audiences.weight	Optional
signal.demographics.gender	Optional
signal.interests.entities	Optional
signal.interests.tags	Optional
take	Optional
Person
If your request is for people, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
bias.trends	Optional
filter.date_of_birth.min	Optional
filter.date_of_birth.max	Optional
filter.date_of_death.min	Optional
filter.date_of_death.max	Optional
filter.exclude.entities	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.gender	Optional
filter.parents.types	Optional
filter.popularity.max	Optional
filter.popularity.min	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
offset	Optional
signal.demographics.age	Optional
signal.demographics.audiences	Optional
signal.demographics.audiences.weight	Optional
signal.demographics.gender	Optional
signal.interests.entities	Optional
signal.interests.tags	Optional
take	Optional
Place
If your request is for places, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
bias.trends	Optional
filter.address	Optional
filter.exclude.entities	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
filter.external.tripadvisor.rating.count.max	Optional
filter.external.tripadvisor.rating.count.min	Optional
filter.external.tripadvisor.rating.max	Optional
filter.external.tripadvisor.rating.min	Optional
filter.geocode.name	Optional
filter.geocode.admin1_region	Optional
filter.geocode.admin2_region	Optional
filter.geocode.country_code	Optional
filter.hotel_class.max	Optional
filter.hotel_class.min	Optional
filter.hours	Optional
filter.location	Optional
filter.location.geohash	Optional
filter.exclude.location.geohash	Optional
filter.location.radius	Optional
filter.parents.types	Optional
filter.popularity.min	Optional
filter.popularity.max	Optional
filter.price_level.min	Optional
filter.price_level.max	Optional
filter.price_range.from	Optional
filter.price_range.to	Optional
filter.properties.business_rating.min	Optional
filter.properties.business_rating.max	Optional
filter.properties.resy.rating.min	Optional
filter.properties.resy.rating.max	Optional
filter.references_brand	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.resy.rating_count.min	Optional
filter.resy.rating_count.max	Optional
filter.resy.rating.party.min	Optional
filter.resy.rating.party.max	Optional
filter.tags	Optional
operator.filter.tags	Optional
offset	Optional
signal.demographics.age	Optional
signal.demographics.audiences	Optional
signal.demographics.audiences.weight	Optional
signal.demographics.gender	Optional
signal.interests.entities	Optional
signal.interests.tags	Optional
take	Optional
Podcast
If your request is for podcasts, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
bias.trends	Optional
filter.exclude.entities	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
filter.parents.types	Optional
filter.popularity.max	Optional
filter.popularity.min	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
offset	Optional
signal.demographics.gender	Optional
signal.demographics.age	Optional
signal.demographics.audiences	Optional
signal.demographics.audiences.weight	Optional
signal.interests.entities	Optional
signal.interests.tags	Optional
take	Optional
TV Show
If your request is for TV shows, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
bias.trends	Optional
filter.content_rating	Optional
filter.exclude.entities	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.finale_year.max	Optional
filter.finale_year.min	Optional
filter.latest_known_year.max	Optional
filter.latest_known_year.min	Optional
filter.parents.types	Optional
filter.popularity.max	Optional
filter.popularity.min	Optional
filter.release_year.max	Optional
filter.release_year.min	Optional
filter.release_country	Optional
operator.filter.release_country	Optional
filter.rating.max	Optional
filter.rating.min	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
offset	Optional
signal.demographics.age	Optional
signal.demographics.audiences	Optional
signal.demographics.audiences.weight	Optional
signal.demographics.gender	Optional
signal.interests.entities	Optional
signal.interests.tags	Optional
take	Optional
Video Game
If your request is for video games, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
bias.trends	Optional
filter.exclude.entities	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
filter.parents.types	Optional
filter.popularity.min	Optional
filter.popularity.max	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
offset	Optional
signal.demographics.age	Optional
signal.demographics.audiences	Optional
signal.demographics.audiences.weight	Optional
signal.demographics.gender	Optional
signal.interests.entities	Optional
signal.interests.tags	Optional
take	Optional
Deprecated Entity Types
🚧
The following entity types are deprecated. We recommend using the Person entity type instead.

Actor
Deprecated: Use the Person entity type instead.

If your request is for actors, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
signal.interests.entities	Optional
signal.interests.tags	Optional
signal.demographics.gender	Optional
signal.demographics.age	Optional
bias.trends	Optional
signal.demographics.audiences	Optional
signal.demographics.audiences.weight	Optional
filter.exclude.entities	Optional
filter.popularity.min	Optional
filter.popularity.max	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
offset	Optional
take	Optional
Author
Deprecated: Use the Person entity type instead.

If your request is for authors, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
signal.interests.entities	Optional
signal.interests.tags	Optional
signal.demographics.gender	Optional
signal.demographics.age	Optional
bias.trends	Optional
signal.demographics.audiences	Optional
signal.demographics.audiences.weight	Optional
filter.exclude.entities	Optional
filter.popularity.min	Optional
filter.popularity.max	Optional
filter.publication_year.min	Optional
filter.publication_year.max	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
offset	Optional
take	Optional
Director
Deprecated: Use the Person entity type instead.

If your request is for directors, these are the parameters you can use:

Parameter Name	Required/Optional
filter.type	Required
signal.interests.entities	Optional
signal.interests.tags	Optional
signal.demographics.gender	Optional
signal.demographics.age	Optional
bias.trends	Optional
signal.demographics.audiences	Optional
signal.demographics.audiences.weight	Optional
filter.exclude.entities	Optional
filter.popularity.min	Optional
filter.popularity.max	Optional
filter.results.entities	Optional
filter.results.entities.query	Optional
filter.tags	Optional
operator.filter.tags	Optional
filter.exclude.tags	Optional
operator.exclude.tags	Optional
filter.external.exists	Optional
operator.filter.external.exists	Optional
operator.filter.external.exists	Optional
take	Optional

Ways to Use Our API
Explore the various ways you can use the Insights API based on your desired input and output. Below you'll find detailed guides for a few of the most common use cases:

Basic Insights: Retrieve recommendations based on the entity type.
Demographic Insights: Retrieve the demographic affinity scores for an entity or tag.
Heatmaps: Generate heatmap data.
Location Insights: Retrieve recommendations based on location.
Taste Analysis: Retrieve tag metadata.
📘
Insights Deep Dive

If you want to understand the Insights endpoint as a whole, check out our Insights Deep Dive for an overview of how the Insights API is set up and all availble parameters.

Basic Insights
This guide shows you how to set up an Insights request to retrieve recommendations based on a particular filter.type. A filter.type is usually an entity type, such as a brand or destination.

📘
This page covers the technical details you need to send a basic Insights request. For a detailed explanation of the benefits and functionality of the Insights API, please refer to the Insights API Deep Dive.

Parameters
Required
filter.type
At least one valid filter or signal parameter in your request
Optional
The available optional parameters depend on the selected filter.type value. Explore the required and optional parameters for each filter.type value here.

For comprehensive parameter descriptions and types, visit the Parameters reference page.

Request
Below is a sample request using the Insights route. Take a look at the sample parameters included and their values:

filter.type is set to urn:entity:movie
filter.tags is set to urn:tag:genre:comedy
filter.release_year.min is set to 2022
This request returns a list of movies tagged as a comedy and released after 2022.

Basic Insights Request Example

curl --location 'https://staging.api.qloo.com/v2/insights/?filter.type=urn:entity:movie&filter.tags=urn:tag:genre:media:comedy&filter.release_year.min=2022' \
--header 'x-api-key: x-api-key'
Response
Below is a truncated sample response showing the first result of the query:

Basic Insights Response Example

{
    "success": true,
    "results": {
        "entities": [
            {
                "name": "Everything Everywhere All at Once",
                "entity_id": "F0D354AA-BA7E-49D2-8ABA-9A8250F5C852",
                "type": "urn:entity",
                "subtype": "urn:entity:movie",
                "properties": {
                    "release_year": 2022,
                    "release_date": "2022-04-08",
                    "description": "A middle-aged Chinese immigrant is swept up into an insane adventure in which she alone can save existence by exploring other universes and connecting with the lives she could have led.",
                    "content_rating": "R",
                    "duration": 139,
                    "image": {
                        "url": "https://staging.images.qloo.com/i/F0D354AA-BA7E-49D2-8ABA-9A8250F5C852-420x-outside.jpg"
                    },
                    "akas": [
                        {
                            "value": "Minden, mindenhol, mindenkor",
                            "languages": [
                                "hu"
                            ]
                        },
                        {
                            "value": "Все завжди і водночас",
                            "languages": [
                                "uk"
                            ]
                        },
                        {
                            "value": "一切隨處可見",
                            "languages": [
                                "zh"
                            ]
                        },
...
                    ],
                    "filming_location": "400 National Way, Simi Valley, California, USA",
                    "production_companies": [
                        "A24",
                        "AGBO",
                        "IAC Films"
                    ],
                    "release_country": [
                        "United States"
                    ],
                    "short_descriptions": [
                        {
                            "value": "film Dana Kwana a Daniela Scheinerta z roku 2022",
                            "languages": [
                                "cs"
                            ]
                        },
                        {
                            "value": "amerikansk film fra 2022",
                            "languages": [
                                "nb"
                            ]
                        },
                        {
                            "value": "فیلم علمی تخیلی ۲۰۲۲",
                            "languages": [
                                "fa"
                            ]
                        },
...
                    ],
                    "websites": [
                        "https://a24films.com/films/everything-everywhere-all-at-once",
                        "https://www.instagram.com/everythingeverywheremovie/"
                    ]
                },
                "popularity": 0.9984116946335868,
                "tags": [
                    {
                        "id": "urn:tag:streaming_service:media:neon_tv",
                        "name": "Neon Tv",
                        "type": "urn:tag:streaming_service:media"
                    },
                    {
                        "id": "urn:tag:keyword:media:multiverse",
                        "name": "Multiverse",
                        "type": "urn:tag:keyword:media"
                    },
                    {
                        "id": "urn:tag:streaming_service:media:cineplex",
                        "name": "Cineplex",
                        "type": "urn:tag:streaming_service:media"
                    },
                    {
                        "id": "urn:tag:streaming_service:media:claro_video",
                        "name": "Claro Video",
                        "type": "urn:tag:streaming_service:media"
                    },
...
                ],
                "query": {
                    "measurements": {
                        "audience_growth": -0.04072975141723856
                    }
                },
                "disambiguation": "2022, Daniel Scheinert, Daniel Kwan",
                "external": {
                    "instagram": [
                        {
                            "id": "everythingeverywheremovie"
                        }
                    ],
                    "wikidata": [
                        {
                            "id": "q83808444"
                        }
                    ],
                    "twitter": [
                        {
                            "id": "allatoncemovie"
                        }
                    ],
                    "letterboxd": [
                        {
                            "id": "everything-everywhere-all-at-once"
                        }
                    ],
                    "metacritic": [
                        {
                            "id": "everything-everywhere-all-at-once",
                            "critic_rating": 81,
                            "user_rating": 7.8
                        }
                    ],
                    "rottentomatoes": [
                        {
                            "id": "everything_everywhere_all_at_once",
                            "user_rating": "89",
                            "user_rating_count": "2500"
                        }
                    ],
                    "imdb": [
                        {
                            "id": "tt6710474",
                            "user_rating": 7.8,
                            "user_rating_count": 549113
                        }
                    ]
                }
            }
    },
    "duration": 34
}
Step-by-Step Example
Recommendations for restaurants similar to Balthazar in NYC
Open Recipe


Demographic Insights
This guide shows you how to set up an Insights request to retrieve demographic data for an entity. Once you include the required parameters, you'll get a response containing the affinity score for various types of demographic data, like age and gender.

Parameters
Required
Only one of the following parameters is required:
signal.interests.entities
signal.interests.tags
For comprehensive parameter descriptions and types, visit the Parameters reference page.

Request
Below is a sample request using the Insights route to retrieve demographic data. Take a look at the sample parameters included and their values:

filter.type is set to urn:demographics
signal.interests.tags is set to urn:tag:genre:media:action
signal.interests.entities is set to B8BEE72B-B321-481F-B81A-A44881D094D6
Demographics Request Example

curl --location 'https://staging.api.qloo.com/v2/insights?filter.type=urn:demographics&signal.interests.tags=urn:tag:genre:media:action&signal.interests.entities=B8BEE72B-B321-481F-B81A-A44881D094D6' \
--header 'x-api-key: x-api-key'
Response
Demographics Response Example

{
  "success": true,
  "results": {
    "demographics": [
      {
        "entity_id": "urn:tag:genre:media:action",
        "query": {
          "age": {
            "24_and_younger": 0,
            "25_to_29": 0.43,
            "30_to_34": 0.23,
            "35_to_44": -0.02,
            "45_to_54": -0.28,
            "55_and_older": -0.17
          },
          "gender": {
            "male": 0.08,
            "female": -0.08
          }
        }
      },
      {
        "entity_id": "B8BEE72B-B321-481F-B81A-A44881D094D6",
        "query": {
          "age": {
            "24_and_younger": -0.09,
            "25_to_29": 0.36,
            "30_to_34": 0.7000000000000001,
            "35_to_44": 0.17,
            "45_to_54": -0.53,
            "55_and_older": -0.32
          },
          "gender": {
            "male": 0.16,
            "female": -0.16
          }
        }
      }
    ]
  },
  "duration": 77
}
Step-by-Step Example
See the affinity scores for demographic data related to Charlize Theron action movies.
Open Recipe

Heatmaps
This guide shows you how to set up an Insights request to generate heatmap data.

📘
This page covers the technical details you need to send a request to create a heatmap. For a detailed explanation of the benefits and functionality of this API use case, please refer to the Heatmaps guide.

Parameters
Required
filter.type with a value of urn:heatmap
Only one of the following parameters is required:
filter.location
filter.location.query
Any signal parameter from the list below
Optional
bias.trends
output.heatmap.boundary
signal.demographics.audiences.weight
signal.demographics.age
signal.demographics.gender
signal.interests.entities
signal.interests.tags
For comprehensive parameter descriptions and types, visit the Parameters reference page.

Request
Below is a sample request using the Insights route to generate heatmap data. Take a look at the sample parameters included and their values:

filter.type is set to urn:heatmap
filter.location.query is set to NYC
signal.interests.tags is set to urn:tag:genre:media:non_fiction
Heatmaps Request Example

curl --location 'https://staging.api.qloo.com/v2/insights/?filter.type=urn:heatmap&filter.location.query=NYC&signal.interests.tags=urn:tag:genre:media:non_fiction' \
--header 'x-api-key: x-api-key'
Response
Heatmaps Response Example

{
    "success": true,
    "results": {
        "heatmap": [
            {
                "location": {
                    "latitude": 40.591736,
                    "longitude": -73.756714,
                    "geohash": "dr5wct"
                },
                "query": {
                    "affinity": 1,
                    "affinity_rank": 0.9976498237367802,
                    "popularity": 0.9717472118959107
                }
            },
            {
                "location": {
                    "latitude": 40.74005,
                    "longitude": -73.87756,
                    "geohash": "dr5ryb"
                },
                "query": {
                    "affinity": 0.9992565055762082,
                    "affinity_rank": 0.9960474308300395,
                    "popularity": 0.5449814126394052
                }
            },
            {
                "location": {
                    "latitude": 40.811462,
                    "longitude": -73.91052,
                    "geohash": "dr72nj"
                },
                "query": {
                    "affinity": 0.9985130111524163,
                    "affinity_rank": 0.9959211420802175,
                    "popularity": 0.9234200743494424
                }
            },
            {
                "location": {
                    "latitude": 40.866394,
                    "longitude": -73.85559,
                    "geohash": "dr72rr"
                },
                "query": {
                    "affinity": 0.9977695167286246,
                    "affinity_rank": 0.9952654717619208,
                    "popularity": 0.6423791821561339
                }
            },
            {
                "location": {
                    "latitude": 40.816956,
                    "longitude": -73.92151,
                    "geohash": "dr72jy"
                },
                "query": {
                    "affinity": 0.9970260223048327,
                    "affinity_rank": 0.9951690821256038,
                    "popularity": 0.7234200743494423
                }
            },
            {
                "location": {
                    "latitude": 40.58075,
                    "longitude": -73.82263,
                    "geohash": "dr5wb5"
                },
                "query": {
                    "affinity": 0.9962825278810409,
                    "affinity_rank": 0.9948072698222489,
                    "popularity": 0.9531598513011152
                }
            },
            {
                "location": {
                    "latitude": 40.73456,
                    "longitude": -73.83362,
                    "geohash": "dr5rxz"
                },
                "query": {
                    "affinity": 0.995539033457249,
                    "affinity_rank": 0.9939903846153846,
                    "popularity": 0.2312267657992565
                }
. . .
            }
        ]
    },
    "query": {
        "localities": {
            "filter": {
                "entity_id": "81E61924-6CEE-4AB4-93D3-282A5C784AB8",
                "name": "New York",
                "subtype": "urn:entity:locality",
                "location": {
                    "lat": -73.93889084762313,
                    "lng": 40.66320611815103
                },
                "popularity": 1,
                "disambiguation": "New York, New York, United States of America"
            }
        }
    },
    "duration": 75
}
Step-by-Step Example
Create a heatmap based on a WKT point for the brand MUJI in NYC
Open Recipe

Location Insights
Retrieve recommendations based on location

This guide shows you how to set up an Insights request with a location. When you include a location in an Insights request, the response provides tailored recommendations based on geospatial data and user interactions.

📘
This page covers the technical details you need to send a location-based Insights request. For a detailed explanation of the benefits and functionality of this API use case, please refer to Insights with Location.

Parameters
Required
filter.type
At least one valid filter or signal parameter in your request
Only one of the following parameters is required:
signal.location
signal.location.query
Optional
The available optional parameters depend on the selected filter.type value:

For location-based filters, see Destination and Place parameters. These include filters that allow you to narrow your results by distance, address, and more.
You can also include any other parameters to refine your request
For comprehensive parameter descriptions and types, visit the Parameters reference page.

Request
Below is a sample request using the Insights route using location data. Take a look at the sample parameters included and their values:

filter.type is set to urn:entity:movie
signal.location.query is set to the Lower East Side.
This request returns a list of movies that have a high affinity score in the Lower East Side.

Insights by Location Request Example

curl --location 'https://staging.api.qloo.com/v2/insights/?filter.type=urn:entity:movie&signal.location.query=Lower%20East%20Side' \
--header 'x-api-key: x-api-key'
Response
Below is a truncated sample response with a list of movie entities tagged as comedies:

Insights by Location Response Example

{
    "success": true,
    "results": {
        "entities": [
            {
                "name": "Queen & Slim",
                "entity_id": "9E2FD257-7E23-483A-8276-36FF51A5DD67",
                "type": "urn:entity",
                "subtype": "urn:entity:movie",
                "properties": {
                    "release_year": 2019,
                    "release_date": "2019-11-27",
                    "description": "A couple's first date takes an unexpected turn when a police officer pulls them over.",
                    "content_rating": "R",
                    "duration": 132,
                    "image": {
                        "url": "https://staging.images.qloo.com/i/9E2FD257-7E23-483A-8276-36FF51A5DD67-420x-outside.jpg"
                    },
                    "akas": [
                        {
                            "value": "Queen and Slim",
                            "languages": [
                                "fr",
                                "en"
                            ]
                        },
                        {
                            "value": "Queen e Slim",
                            "languages": [
                                "gl"
                            ]
                        },
                        {
                            "value": "Queen i Slim",
                            "languages": [
                                "ca"
                            ]
                        },
                        {
                            "value": "Квин и Слим",
                            "languages": [
                                "ru"
                            ]
                        },
                        {
                            "value": "كوين وسليم",
                            "languages": [
                                "ar"
                            ]
                        },
                        {
                            "value": "کوئین و اسلیم",
                            "languages": [
                                "fa"
                            ]
                        },
                        {
                            "value": "クイーン&スリム",
                            "languages": [
                                "ja"
                            ]
                        },
                        {
                            "value": "皇后与瘦子",
                            "languages": [
                                "zh"
                            ]
                        },
                        {
                            "value": "皇后與瘦子",
                            "languages": [
                                "zh"
                            ]
                        },
                        {
                            "value": "퀸 앤 슬림",
                            "languages": [
                                "ko"
                            ]
                        }
                    ],
                    "filming_location": "6900 St. Clair Avenue, Cleveland, Ohio, USA",
                    "production_companies": [
                        "De La Revolución Films",
                        "Hillman Grad",
                        "Makeready"
                    ],
                    "release_country": [
                        "United States",
                        "Canada"
                    ],
                    "short_descriptions": [
                        {
                            "value": "2019 film directed by Melina Matsoukas",
                            "languages": [
                                "en"
                            ]
                        },
 . . .

}
        }
    }
}
Step-by-Step Example
Recommendations for popular brands inside Paris center based on WKT shape
Open Recipe


Taste Analysis
Tag Insights: Retrieve tag metadata.

This guide shows you how to set up an Insights request to retrieve tag metadata associated with a certain audience, entity, tag, or keyword. This is referred to as taste analysis.

Parameters
Required
filter.type with a value of urn:tag
Only one of the following parameters is required. You can include more than one to narrow your results:
filter.tag.types
filter.parents.types
signal.demographics.audiences
signal.interests.entities
signal.interests.tags
signal.location
signal.location.query
For comprehensive parameter descriptions and types, visit the Parameters reference page.

Request
Below is a sample request using the Insights route to retrieve tag data. Take a look at the sample parameters included and their values:

filter.type is set to urn:tag
filter.tag.types is set to urn:tag:keyword:media
filter.parents.types is set to urn:entity:movie, urn:entity:tv_show
Tag Insights Request Example

curl --location 'https://staging.api.qloo.com/v2/insights?filter.type=urn%3Atag&filter.tag.types=urn%3Atag%3Akeyword%3Amedia&filter.parents.types=urn%3Aentity%3Amovie%2C%20urn%3Aentity%3Atv_show' \
--header 'x-api-key: x-api-key'
Response
Tag Insights Response Example

{
    "success": true,
    "results": {
        "tags": [
            {
                "tag_id": "urn:tag:keyword:media:brady_bunch",
                "name": "Brady Bunch",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:brady_bunch",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:mining_accident",
                "name": "Mining Accident",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:mining_accident",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:complex",
                "name": "Complex",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:complex",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:hostile_environment",
                "name": "Hostile Environment",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:hostile_environment",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:jewish_tradition",
                "name": "Jewish Tradition",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:jewish_tradition",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:anthropomorphic_elephant",
                "name": "Anthropomorphic Elephant",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:anthropomorphic_elephant",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:max_goof_character",
                "name": "Max Goof Character",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:max_goof_character",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:gasoline_fire",
                "name": "Gasoline Fire",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:gasoline_fire",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:british_museum",
                "name": "British Museum",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:british_museum",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:math_class",
                "name": "Math Class",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:math_class",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:tinted_film",
                "name": "Tinted Film",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:tinted_film",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:chicago_police_department",
                "name": "Chicago Police Department",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:chicago_police_department",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:search_meaning_life",
                "name": "Search For The Meaning Of Life",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:search_meaning_life",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:woman_farting",
                "name": "Woman Farting",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:woman_farting",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:cultural_clash",
                "name": "Cultural Clash",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:cultural_clash",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:disappearance_father",
                "name": "Disappearance Of Father",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:disappearance_father",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:city_in_panic",
                "name": "City In Panic",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:city_in_panic",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:citroen_d_s",
                "name": "Citroen D S",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:citroen_d_s",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:artful_dodger_character",
                "name": "Artful Dodger Character",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:artful_dodger_character",
                "query": {}
            },
            {
                "tag_id": "urn:tag:keyword:media:eiffel_tower_destroyed",
                "name": "Eiffel Tower Destroyed",
                "types": [
                    "urn:entity:tv_show",
                    "urn:entity:writer",
                    "urn:entity:director",
                    "urn:entity:tv_episode",
                    "urn:entity:actor",
                    "urn:entity:movie"
                ],
                "subtype": "urn:tag:keyword:media",
                "tag_value": "urn:tag:keyword:media:eiffel_tower_destroyed",
                "query": {}
            }
        ]
    },
    "duration": 25
}
Updated about 2 months ago

Location Insights