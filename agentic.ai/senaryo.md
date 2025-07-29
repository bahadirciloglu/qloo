# 🎹 LENTO AI CONCIERGE - Comprehensive Design and Interaction Analysis

## 🎨 **LENTO - Character Profile**

**Name:** Lento  
**Meaning:** "Slow and calm tempo" in music - artistic and elegant welcome  
**Theme:** Piano-inspired, sympathetic and emotional AI Concierge  
**Personality:** Calm, elegant, music-loving, hospitable, artistic soul



**GUEST CHECK-IN PROCESS**
1.After check-in, Property Management System (PMS) API, POS (Point of Sale) API, Payment Gateway API, Lento becomes active for that customer.
2.Guest interaction with Lento begins.
3.Guest's basic needs open in the quick menu:


**🍽️ QLOO API - FOOD & BEVERAGE DATA TYPES**
🏪 ENTITY TYPES
urn:entity:restaurant - Restaurants
urn:entity:place - General venues (including restaurants)
urn:entity:brand - Food brands
urn:entity:company - Restaurant chains
urn:entity:product - Food products
🍽️ CUISINE TAGS
urn:tag:cuisine:restaurant:turkish - Turkish cuisine
urn:tag:cuisine:restaurant:italian - Italian cuisine
urn:tag:cuisine:restaurant:japanese - Japanese cuisine
urn:tag:cuisine:restaurant:chinese - Chinese cuisine
urn:tag:cuisine:restaurant:indian - Indian cuisine
urn:tag:cuisine:restaurant:mexican - Mexican cuisine
urn:tag:cuisine:restaurant:french - French cuisine
urn:tag:cuisine:restaurant:greek - Greek cuisine
urn:tag:cuisine:restaurant:thai - Thai cuisine
urn:tag:cuisine:restaurant:vietnamese - Vietnamese cuisine
urn:tag:cuisine:restaurant:korean - Korean cuisine
urn:tag:cuisine:restaurant:arabic - Arabic cuisine
urn:tag:cuisine:restaurant:spanish - Spanish cuisine
urn:tag:cuisine:restaurant:portuguese - Portuguese cuisine
🥗 DIET TAGS
urn:tag:diet:restaurant:vegan - Vegan
urn:tag:diet:restaurant:vegetarian - Vegetarian
urn:tag:diet:restaurant:gluten_free - Gluten-free
urn:tag:diet:restaurant:halal - Halal
urn:tag:diet:restaurant:kosher - Kosher
urn:tag:diet:restaurant:organic - Organic
🍽️ RESTAURANT CATEGORY TAGS
urn:tag:category:restaurant:fast_food - Fast food
urn:tag:category:restaurant:fine_dining - Fine dining
urn:tag:category:restaurant:casual_dining - Casual dining
urn:tag:category:restaurant:street_food - Street food
urn:tag:category:restaurant:seafood - Seafood
urn:tag:category:restaurant:steakhouse - Steakhouse
urn:tag:category:restaurant:pizzeria - Pizzeria
urn:tag:category:restaurant:sushi - Sushi
🏪 PLACE CATEGORY TAGS
urn:tag:category:place:restaurant - Restaurant
urn:tag:category:place:cafe - Cafe
urn:tag:category:place:bar - Bar
urn:tag:category:place:bakery - Bakery
urn:tag:category:place:food_court - Food court
urn:tag:category:place:market - Market
urn:tag:category:place:grocery_store - Grocery store
urn:tag:category:place:coffee_shop - Coffee shop
urn:tag:category:place:tea_house - Tea house
urn:tag:category:place:juice_bar - Juice bar
urn:tag:category:place:smoothie_bar - Smoothie bar
🏷️ AMENITY TAGS
urn:tag:amenity:place:outdoor_seating - Outdoor seating
urn:tag:amenity:place:delivery - Delivery
urn:tag:amenity:place:takeout - Takeout
urn:tag:amenity:place:reservations - Reservations
urn:tag:amenity:place:live_music - Live music
urn:tag:amenity:place:wine_list - Wine list
urn:tag:amenity:place:craft_beer - Craft beer
urn:tag:amenity:place:happy_hour - Happy hour
urn:tag:amenity:place:brunch - Brunch
urn:tag:amenity:place:breakfast - Breakfast
urn:tag:amenity:place:lunch - Lunch
urn:tag:amenity:place:dinner - Dinner
urn:tag:amenity:place:late_night - Late night
urn:tag:amenity:place:wheelchair_accessible - Wheelchair accessible
urn:tag:amenity:place:parking - Parking
urn:tag:amenity:place:wifi - WiFi
urn:tag:amenity:place:air_conditioning - Air conditioning
📊 FILTER PARAMETERS
filter.price_level.min / filter.price_level.max - Price level
filter.price_range.from / filter.price_range.to - Price range
filter.rating.min / filter.rating.max - Rating
filter.properties.business_rating.min / filter.properties.business_rating.max - Business rating
filter.location.query - Location query
filter.location.radius - Radius
filter.location.geohash - Geohash
filter.tags - Tag filters
filter.popularity.min / filter.popularity.max - Popularity
filter.hours - Operating hours


-**Wi-Fi access: Password, connection speed information.**
   

**FATIGUE SUPPORT - QLOO API DATA TYPES**
🏨 HOTEL & ACCOMMODATION
urn:entity:hotel - Hotels
urn:entity:place - General venues
urn:tag:category:place:hotel - Hotel category
urn:tag:category:place:resort - Resort category
urn:tag:category:place:guesthouse - Guesthouse
🧘 SPA & WELLNESS
urn:tag:category:place:spa - Spa center
urn:tag:category:place:wellness_center - Wellness center
urn:tag:category:place:massage - Massage salon
urn:tag:category:place:yoga_studio - Yoga studio
urn:tag:category:place:meditation_center - Meditation center
urn:tag:category:place:thermal_bath - Thermal bath
urn:tag:category:place:sauna - Sauna
urn:tag:category:place:jacuzzi - Jacuzzi
💆‍♀️ MASSAGE & THERAPY
urn:tag:category:place:massage_therapy - Massage therapy
urn:tag:category:place:reflexology - Reflexology
urn:tag:category:place:aromatherapy - Aromatherapy
urn:tag:category:place:shiatsu - Shiatsu
urn:tag:category:place:thai_massage - Thai massage
urn:tag:category:place:swedish_massage - Swedish massage
urn:tag:category:place:deep_tissue_massage - Deep tissue massage
urn:tag:category:place:hot_stone_massage - Hot stone massage
😴 SLEEP & REST
urn:tag:category:place:bedroom - Bedroom
urn:tag:category:place:guest_room - Guest room
urn:tag:category:place:suite - Suite
urn:tag:category:place:quiet_zone - Quiet zone
urn:tag:category:place:rest_area - Rest area
🧼 HYGIENE & REFRESHMENT
urn:tag:category:place:bathroom - Bathroom
urn:tag:category:place:shower - Shower
urn:tag:category:place:changing_room - Changing room
urn:tag:category:place:locker_room - Locker room
urn:tag:category:place:towel_service - Towel service
🎵 RELAXATION & MUSIC
urn:entity:music - Music
urn:tag:genre:music:ambient - Ambient music
urn:tag:genre:music:meditation - Meditation music
urn:tag:genre:music:nature_sounds - Nature sounds
urn:tag:genre:music:white_noise - White noise
urn:tag:genre:music:classical - Classical music
urn:tag:genre:music:lullaby - Lullaby
🥤 REFRESHMENT & BEVERAGES
urn:tag:category:place:tea_house - Tea house
urn:tag:category:place:herbal_tea - Herbal tea
urn:tag:category:place:juice_bar - Juice bar
urn:tag:category:place:detox_bar - Detox bar
urn:tag:category:place:water_station - Water station
🏥 HEALTH & MEDICAL
urn:tag:category:place:medical_center - Medical center
urn:tag:category:place:physiotherapy - Physiotherapy
urn:tag:category:place:chiropractic - Chiropractic
urn:tag:category:place:acupuncture - Acupuncture
urn:tag:category:place:osteopathy - Osteopathy
💧 WATER & HYDROTHERAPY
urn:tag:category:place:pool - Pool
urn:tag:category:place:hot_tub - Hot tub
urn:tag:category:place:steam_room - Steam room
urn:tag:category:place:hydrotherapy - Hydrotherapy
urn:tag:category:place:floatation_tank - Floatation tank
🌿 NATURAL & OUTDOOR
urn:tag:category:place:garden - Garden
urn:tag:category:place:park - Park
urn:tag:category:place:nature_trail - Nature trail
urn:tag:category:place:outdoor_seating - Outdoor seating
urn:tag:category:place:sunset_view - Sunset view
🛁 AMENITIES & SERVICES
urn:tag:amenity:place:room_service - Room service
urn:tag:amenity:place:housekeeping - Housekeeping service
urn:tag:amenity:place:laundry_service - Laundry service
urn:tag:amenity:place:concierge - Concierge
urn:tag:amenity:place:valet_parking - Valet parking
urn:tag:amenity:place:luggage_storage - Luggage storage
urn:tag:amenity:place:early_check_in - Early check-in
urn:tag:amenity:place:late_check_out - Late check-out
📱 DIGITAL RELAXATION
urn:entity:app - Applications
urn:tag:category:app:meditation - Meditation app
urn:tag:category:app:sleep_tracker - Sleep tracker app
urn:tag:category:app:white_noise - White noise app
urn:tag:category:app:breathing - Breathing exercise app
🏷️ FILTER PARAMETERS
filter.price_level.min / filter.price_level.max - Price level
filter.rating.min / filter.rating.max - Rating
filter.location.radius - Distance (important for tired guests)
filter.properties.business_rating.min - Business quality
filter.hours - Operating hours (for late hours)
filter.amenity - Feature filters
📊 INSIGHTS METRICS
Affinity Score (0-100) - Suitability to guest preferences
Popularity Score (0-1) - Popularity
Distance - Distance (important for tired guests)
Price Level (1-4) - Price level
Availability - Availability status
Wait Time - Wait time




**🏪 NEARBY PLACES - QLOO API DATA TYPES**
-Hotel general structure: Room number, elevator, restaurant, lobby, exit, etc.
 -Nearby places: Market, pharmacy, transportation, parking.
🏪 MARKET & GROCERY
urn:entity:place - General venues
urn:tag:category:place:market - Market
urn:tag:category:place:grocery_store - Grocery store
urn:tag:category:place:supermarket - Supermarket
urn:tag:category:place:convenience_store - Convenience store
urn:tag:category:place:food_market - Food market
urn:tag:category:place:farmers_market - Farmers market
urn:tag:category:place:organic_market - Organic market
urn:tag:category:place:delicatessen - Delicatessen
urn:tag:category:place:butcher - Butcher
urn:tag:category:place:fish_market - Fish market
urn:tag:category:place:bakery - Bakery
urn:tag:category:place:liquor_store - Liquor store
💊 PHARMACY & HEALTH
urn:tag:category:place:pharmacy - Pharmacy
urn:tag:category:place:drugstore - Drugstore
urn:tag:category:place:medical_supply - Medical supply
urn:tag:category:place:health_store - Health store
urn:tag:category:place:vitamin_store - Vitamin store
urn:tag:category:place:herbal_store - Herbal store
urn:tag:category:place:medical_clinic - Medical clinic
urn:tag:category:place:urgent_care - Urgent care
urn:tag:category:place:hospital - Hospital
urn:tag:category:place:dentist - Dentist
🚇 TRANSPORTATION
urn:tag:category:place:subway_station - Subway station
urn:tag:category:place:bus_station - Bus station
urn:tag:category:place:train_station - Train station
urn:tag:category:place:tram_station - Tram station
urn:tag:category:place:ferry_terminal - Ferry terminal
urn:tag:category:place:airport - Airport
urn:tag:category:place:taxi_stand - Taxi stand
urn:tag:category:place:car_rental - Car rental
urn:tag:category:place:bike_rental - Bike rental
urn:tag:category:place:scooter_rental - Scooter rental
urn:tag:category:place:park_and_ride - Park and ride
urn:tag:category:place:transportation_hub - Transportation hub
🚗 PARKING & VEHICLES
urn:tag:category:place:parking_lot - Parking lot
urn:tag:category:place:parking_garage - Parking garage
urn:tag:category:place:street_parking - Street parking
urn:tag:category:place:valet_parking - Valet parking
urn:tag:category:place:free_parking - Free parking
urn:tag:category:place:ev_charging_station - Electric vehicle charging station
urn:tag:category:place:gas_station - Gas station
urn:tag:category:place:car_wash - Car wash
urn:tag:category:place:auto_repair - Auto repair
urn:tag:category:place:car_dealership - Car dealership
🏪 CONVENIENCE & SERVICES
urn:tag:category:place:convenience_store - Convenience store
urn:tag:category:place:atm - ATM
urn:tag:category:place:bank - Bank
urn:tag:category:place:post_office - Post office
urn:tag:category:place:laundry - Laundry
urn:tag:category:place:dry_cleaner - Dry cleaner
urn:tag:category:place:shoe_repair - Shoe repair
urn:tag:category:place:key_duplication - Key duplication
urn:tag:category:place:printing_shop - Printing shop
urn:tag:category:place:copy_center - Copy center
🍽️ FOOD & BEVERAGES
urn:tag:category:place:restaurant - Restaurant
urn:tag:category:place:fast_food - Fast food
urn:tag:category:place:cafe - Cafe
urn:tag:category:place:coffee_shop - Coffee shop
urn:tag:category:place:bakery - Bakery
urn:tag:category:place:ice_cream_shop - Ice cream shop
urn:tag:category:place:juice_bar - Juice bar
urn:tag:category:place:food_truck - Food truck
🏥 EMERGENCY & ESSENTIALS
urn:tag:category:place:police_station - Police station
urn:tag:category:place:fire_station - Fire station
urn:tag:category:place:emergency_room - Emergency room
urn:tag:category:place:urgent_care - Urgent care
urn:tag:category:place:pharmacy - Pharmacy (24 hours)
urn:tag:category:place:convenience_store - Convenience store (24 hours)
urn:tag:category:place:gas_station - Gas station (24 hours)
🏷️ AMENITY TAGS
urn:tag:amenity:place:parking - Parking
urn:tag:amenity:place:wifi - WiFi
urn:tag:amenity:place:wheelchair_accessible - Wheelchair accessible
urn:tag:amenity:place:24_hours - 24 hours open
urn:tag:amenity:place:delivery - Delivery
urn:tag:amenity:place:takeout - Takeout
urn:tag:amenity:place:drive_through - Drive-through
urn:tag:amenity:place:outdoor_seating - Outdoor seating
📊 FILTER PARAMETERS
filter.location.radius - Distance (important for proximity)
filter.location.query - Location query
filter.location.geohash - Precise location
filter.hours - Operating hours
filter.price_level.min / filter.price_level.max - Price level
filter.rating.min / filter.rating.max - Rating
filter.properties.business_rating.min - Business rating
filter.popularity.min - Popularity (for tourist places)
🎯 LOCATION INSIGHTS
Distance - Distance (meters/km)
Walking Time - Walking time
Driving Time - Driving time
Public Transport - Public transport options
Availability - Availability status
Wait Time - Wait time
Crowd Level - Crowd level
Safety Rating - Safety rating
📱 REAL-TIME DATA
Opening Hours - Opening hours
Current Status - Current status (open/closed)
Queue Length - Queue length
Special Offers - Special offers
Events - Events
Maintenance - Maintenance status



**🏛️ TOURIST ATTRACTIONS (Tourist Areas)**
City information: Tourist areas, transportation lines, taxi calling. CITY INFORMATION - QLOO API DATA TYPES
urn:entity:place - General venues
urn:tag:category:place:museum - Museum
urn:tag:category:place:art_gallery - Art gallery
urn:tag:category:place:historical_site - Historical site
urn:tag:category:place:monument - Monument
urn:tag:category:place:landmark - Landmark
urn:tag:category:place:castle - Castle
urn:tag:category:place:palace - Palace
urn:tag:category:place:mosque - Mosque
urn:tag:category:place:church - Church
urn:tag:category:place:temple - Temple
urn:tag:category:place:synagogue - Synagogue
urn:tag:category:place:cathedral - Cathedral
urn:tag:category:place:basilica - Basilica
🏞️ NATURAL ATTRACTIONS
urn:tag:category:place:park - Park
urn:tag:category:place:garden - Garden
urn:tag:category:place:botanical_garden - Botanical garden
urn:tag:category:place:zoo - Zoo
urn:tag:category:place:aquarium - Aquarium
urn:tag:category:place:beach - Beach
urn:tag:category:place:mountain - Mountain
urn:tag:category:place:lake - Lake
urn:tag:category:place:river - River
urn:tag:category:place:waterfall - Waterfall
urn:tag:category:place:forest - Forest
urn:tag:category:place:nature_reserve - Nature reserve
🎭 ENTERTAINMENT & CULTURE
urn:tag:category:place:theater - Theater
urn:tag:category:place:concert_hall - Concert hall
urn:tag:category:place:opera_house - Opera house
urn:tag:category:place:cinema - Cinema
urn:tag:category:place:amusement_park - Amusement park
urn:tag:category:place:casino - Casino
urn:tag:category:place:nightclub - Nightclub
urn:tag:category:place:bar - Bar
urn:tag:category:place:pub - Pub
urn:tag:category:place:live_music_venue - Live music venue
🛍️ SHOPPING & MARKETS
urn:tag:category:place:shopping_mall - Shopping mall
urn:tag:category:place:market - Market
urn:tag:category:place:flea_market - Flea market
urn:tag:category:place:antique_shop - Antique shop
urn:tag:category:place:souvenir_shop - Souvenir shop
urn:tag:category:place:craft_shop - Craft shop
urn:tag:category:place:jewelry_store - Jewelry store
urn:tag:category:place:clothing_store - Clothing store
🚇 TRANSPORTATION NETWORK (Transportation Lines)
urn:tag:category:place:subway_station - Subway station
urn:tag:category:place:bus_station - Bus station
urn:tag:category:place:train_station - Train station
urn:tag:category:place:tram_station - Tram station
urn:tag:category:place:ferry_terminal - Ferry terminal
urn:tag:category:place:airport - Airport
urn:tag:category:place:transportation_hub - Transportation hub
urn:tag:category:place:park_and_ride - Park and ride
urn:tag:category:place:bike_share - Bike share
urn:tag:category:place:scooter_share - Scooter share
🚕 TAXI & RIDE SERVICES (Taxi Calling)
urn:tag:category:place:taxi_stand - Taxi stand
urn:tag:category:place:taxi_company - Taxi company
urn:tag:category:place:ride_share - Ride share
urn:tag:category:place:limousine_service - Limousine service
urn:tag:category:place:car_service - Car service
urn:tag:category:place:private_transport - Private transport
urn:tag:category:place:chauffeur_service - Chauffeur service
🏨 ACCOMMODATION
urn:tag:category:place:hotel - Hotel
urn:tag:category:place:hostel - Hostel
urn:tag:category:place:guesthouse - Guesthouse
urn:tag:category:place:resort - Resort
urn:tag:category:place:apartment_rental - Apartment rental
urn:tag:category:place:bed_and_breakfast - Bed and breakfast
🍽️ DINING & CUISINE
urn:tag:category:place:restaurant - Restaurant
urn:tag:category:place:local_cuisine - Local cuisine
urn:tag:category:place:traditional_restaurant - Traditional restaurant
urn:tag:category:place:fine_dining - Fine dining
urn:tag:category:place:street_food - Street food
urn:tag:category:place:food_market - Food market
🏛️ TOURIST SERVICES
urn:tag:category:place:tourist_information - Tourist information center
urn:tag:category:place:travel_agency - Travel agency
urn:tag:category:place:tour_operator - Tour operator
urn:tag:category:place:guided_tour - Guided tour
urn:tag:category:place:city_tour - City tour
urn:tag:category:place:walking_tour - Walking tour
urn:tag:category:place:boat_tour - Boat tour
urn:tag:category:place:bus_tour - Bus tour
📱 DIGITAL SERVICES
urn:entity:app - Applications
urn:tag:category:app:transportation - Transportation app
urn:tag:category:app:taxi - Taxi app
urn:tag:category:app:city_guide - City guide app
urn:tag:category:app:transit - Transit app
urn:tag:category:app:maps - Maps app
🏷️ AMENITY TAGS
urn:tag:amenity:place:wheelchair_accessible - Wheelchair accessible
urn:tag:amenity:place:guided_tour - Guided tour
urn:tag:amenity:place:audio_guide - Audio guide
urn:tag:amenity:place:multilingual_staff - Multilingual staff
urn:tag:amenity:place:free_admission - Free admission
urn:tag:amenity:place:student_discount - Student discount
urn:tag:amenity:place:senior_discount - Senior discount
urn:tag:amenity:place:family_friendly - Family friendly
urn:tag:amenity:place:photography_allowed - Photography allowed
urn:tag:amenity:place:restroom - Restroom
urn:tag:amenity:place:parking - Parking
urn:tag:amenity:place:wifi - WiFi
📊 FILTER PARAMETERS
filter.location.radius - Distance (around city center)
filter.location.query - City/district name
filter.price_level.min / filter.price_level.max - Price level
filter.rating.min / filter.rating.max - Rating
filter.properties.business_rating.min - Business rating
filter.hours - Operating hours
filter.popularity.min - Popularity (for tourist places)
filter.tags - Special tags (historical, cultural, etc.)
🏙️ CITY INSIGHTS
Tourist Rating - Tourist rating
Local Popularity - Local popularity
International Recognition - International recognition
Cultural Significance - Cultural significance
Historical Value - Historical value
Accessibility - Accessibility
Crowd Level - Crowd level
Best Time to Visit - Best time to visit
Seasonal Events - Seasonal events
Local Tips - Local tips
  
The chat screen appears below the Quick Menu - the conversation between Lento and the guest takes place in the chat screen.
Interaction can start in either the Quick Menu or Chat Screen, the chat screen slides down like a sliding screen, the Quick Menu always stays on top of the chat screen.






