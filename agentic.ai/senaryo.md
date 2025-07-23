# 🎹 LENTO AI CONCIERGE - Kapsamlı Tasarım ve Etkileşim Analizi

## 🎨 **LENTO - Karakter Profili**

**İsim:** Lento  
**Anlam:** Müzikte "yavaş ve dingin tempo" - sanatsal ve zarif karşılama  
**Tema:** Piyano formundan esinlenen, sempatik ve duygusal AI Concierge  
**Kişilik:** Sakin, zarif, müziksever, misafirperver, sanatsal ruhlu



**MİSAfiR CHECK-IN'i YAPAR**
1.After check-in , Property Management System (PMS) API , POS (Point of Sale) API , Payment Gateway API , ile lento , o müşteri için aktifleşir.
2.Lento ile müşteri etkileşimi başlar.
3.Misafir temel ihtiyaçları, hızlı menüde açılır:


**🍽️ QLOO API - YEMEK & İÇECEK VERİ TİPLERİ**
�� ENTITY TYPES
urn:entity:restaurant - Restoranlar
urn:entity:place - Genel mekanlar (restoranlar dahil)
urn:entity:brand - Yemek markaları
urn:entity:company - Restoran zincirleri
urn:entity:product - Gıda ürünleri
��️ CUISINE TAGS
urn:tag:cuisine:restaurant:turkish - Türk mutfağı
urn:tag:cuisine:restaurant:italian - İtalyan mutfağı
urn:tag:cuisine:restaurant:japanese - Japon mutfağı
urn:tag:cuisine:restaurant:chinese - Çin mutfağı
urn:tag:cuisine:restaurant:indian - Hint mutfağı
urn:tag:cuisine:restaurant:mexican - Meksika mutfağı
urn:tag:cuisine:restaurant:french - Fransız mutfağı
urn:tag:cuisine:restaurant:greek - Yunan mutfağı
urn:tag:cuisine:restaurant:thai - Tay mutfağı
urn:tag:cuisine:restaurant:vietnamese - Vietnam mutfağı
urn:tag:cuisine:restaurant:korean - Kore mutfağı
urn:tag:cuisine:restaurant:arabic - Arap mutfağı
urn:tag:cuisine:restaurant:spanish - İspanyol mutfağı
urn:tag:cuisine:restaurant:portuguese - Portekiz mutfağı
🥗 DIET TAGS
urn:tag:diet:restaurant:vegan - Vegan
urn:tag:diet:restaurant:vegetarian - Vejetaryen
urn:tag:diet:restaurant:gluten_free - Gluten-free
urn:tag:diet:restaurant:halal - Helal
urn:tag:diet:restaurant:kosher - Koşer
urn:tag:diet:restaurant:organic - Organik
🍽️ RESTAURANT CATEGORY TAGS
urn:tag:category:restaurant:fast_food - Fast food
urn:tag:category:restaurant:fine_dining - Fine dining
urn:tag:category:restaurant:casual_dining - Casual dining
urn:tag:category:restaurant:street_food - Sokak yemeği
urn:tag:category:restaurant:seafood - Deniz ürünleri
urn:tag:category:restaurant:steakhouse - Steakhouse
urn:tag:category:restaurant:pizzeria - Pizzeria
urn:tag:category:restaurant:sushi - Sushi
�� PLACE CATEGORY TAGS
urn:tag:category:place:restaurant - Restoran
urn:tag:category:place:cafe - Kafe
urn:tag:category:place:bar - Bar
urn:tag:category:place:bakery - Fırın
urn:tag:category:place:food_court - Yemek merkezi
urn:tag:category:place:market - Market
urn:tag:category:place:grocery_store - Bakkal
urn:tag:category:place:coffee_shop - Kahve dükkanı
urn:tag:category:place:tea_house - Çay evi
urn:tag:category:place:juice_bar - Meyve suyu barı
urn:tag:category:place:smoothie_bar - Smoothie barı
��️ AMENITY TAGS
urn:tag:amenity:place:outdoor_seating - Açık alan
urn:tag:amenity:place:delivery - Teslimat
urn:tag:amenity:place:takeout - Paket servis
urn:tag:amenity:place:reservations - Rezervasyon
urn:tag:amenity:place:live_music - Canlı müzik
urn:tag:amenity:place:wine_list - Şarap listesi
urn:tag:amenity:place:craft_beer - El yapımı bira
urn:tag:amenity:place:happy_hour - Happy hour
urn:tag:amenity:place:brunch - Brunch
urn:tag:amenity:place:breakfast - Kahvaltı
urn:tag:amenity:place:lunch - Öğle yemeği
urn:tag:amenity:place:dinner - Akşam yemeği
urn:tag:amenity:place:late_night - Gece geç saatler
urn:tag:amenity:place:wheelchair_accessible - Tekerlekli sandalye erişimi
urn:tag:amenity:place:parking - Otopark
urn:tag:amenity:place:wifi - WiFi
urn:tag:amenity:place:air_conditioning - Klima
📊 FILTER PARAMETERS
filter.price_level.min / filter.price_level.max - Fiyat seviyesi
filter.price_range.from / filter.price_range.to - Fiyat aralığı
filter.rating.min / filter.rating.max - Değerlendirme
filter.properties.business_rating.min / filter.properties.business_rating.max - İşletme değerlendirmesi
filter.location.query - Konum sorgusu
filter.location.radius - Yarıçap
filter.location.geohash - Geohash
filter.tags - Etiket filtreleri
filter.popularity.min / filter.popularity.max - Popülerlik
filter.hours - Çalışma saatleri


-**Wi-Fi erişimi: Şifre, bağlantı hızı bilgisi.**
   

**YORGUNLUK DESTEĞİ - QLOO API VERİ TİPLERİ**
�� HOTEL & ACCOMMODATION
urn:entity:hotel - Oteller
urn:entity:place - Genel mekanlar
urn:tag:category:place:hotel - Otel kategorisi
urn:tag:category:place:resort - Resort kategorisi
urn:tag:category:place:guesthouse - Misafirhane
🧘 SPA & WELLNESS
urn:tag:category:place:spa - Spa merkezi
urn:tag:category:place:wellness_center - Wellness merkezi
urn:tag:category:place:massage - Masaj salonu
urn:tag:category:place:yoga_studio - Yoga stüdyosu
urn:tag:category:place:meditation_center - Meditasyon merkezi
urn:tag:category:place:thermal_bath - Termal banyo
urn:tag:category:place:sauna - Sauna
urn:tag:category:place:jacuzzi - Jakuzi
💆‍♀️ MASSAGE & THERAPY
urn:tag:category:place:massage_therapy - Masaj terapisi
urn:tag:category:place:reflexology - Refleksoloji
urn:tag:category:place:aromatherapy - Aromaterapi
urn:tag:category:place:shiatsu - Shiatsu
urn:tag:category:place:thai_massage - Thai masajı
urn:tag:category:place:swedish_massage - İsveç masajı
urn:tag:category:place:deep_tissue_massage - Derin doku masajı
urn:tag:category:place:hot_stone_massage - Sıcak taş masajı
��️ SLEEP & REST
urn:tag:category:place:bedroom - Yatak odası
urn:tag:category:place:guest_room - Misafir odası
urn:tag:category:place:suite - Süit
urn:tag:category:place:quiet_zone - Sessiz bölge
urn:tag:category:place:rest_area - Dinlenme alanı
�� HYGIENE & REFRESHMENT
urn:tag:category:place:bathroom - Banyo
urn:tag:category:place:shower - Duş
urn:tag:category:place:changing_room - Soyunma odası
urn:tag:category:place:locker_room - Vestiyer
urn:tag:category:place:towel_service - Havlu servisi
�� RELAXATION & MUSIC
urn:entity:music - Müzik
urn:tag:genre:music:ambient - Ambient müzik
urn:tag:genre:music:meditation - Meditasyon müziği
urn:tag:genre:music:nature_sounds - Doğa sesleri
urn:tag:genre:music:white_noise - Beyaz gürültü
urn:tag:genre:music:classical - Klasik müzik
urn:tag:genre:music:lullaby - Ninni
�� REFRESHMENT & BEVERAGES
urn:tag:category:place:tea_house - Çay evi
urn:tag:category:place:herbal_tea - Bitki çayı
urn:tag:category:place:juice_bar - Meyve suyu barı
urn:tag:category:place:detox_bar - Detoks barı
urn:tag:category:place:water_station - Su istasyonu
�� HEALTH & MEDICAL
urn:tag:category:place:medical_center - Tıp merkezi
urn:tag:category:place:physiotherapy - Fizyoterapi
urn:tag:category:place:chiropractic - Kayropraktik
urn:tag:category:place:acupuncture - Akupunktur
urn:tag:category:place:osteopathy - Osteopati
��‍♀️ WATER & HYDROTHERAPY
urn:tag:category:place:pool - Havuz
urn:tag:category:place:hot_tub - Sıcak küvet
urn:tag:category:place:steam_room - Buhar odası
urn:tag:category:place:hydrotherapy - Hidroterapi
urn:tag:category:place:floatation_tank - Yüzdürme tankı
🌿 NATURAL & OUTDOOR
urn:tag:category:place:garden - Bahçe
urn:tag:category:place:park - Park
urn:tag:category:place:nature_trail - Doğa yolu
urn:tag:category:place:outdoor_seating - Açık alan oturma
urn:tag:category:place:sunset_view - Gün batımı manzarası
🛁 AMENITIES & SERVICES
urn:tag:amenity:place:room_service - Oda servisi
urn:tag:amenity:place:housekeeping - Temizlik servisi
urn:tag:amenity:place:laundry_service - Çamaşırhane servisi
urn:tag:amenity:place:concierge - Concierge
urn:tag:amenity:place:valet_parking - Vale park
urn:tag:amenity:place:luggage_storage - Bagaj saklama
urn:tag:amenity:place:early_check_in - Erken check-in
urn:tag:amenity:place:late_check_out - Geç check-out
📱 DIGITAL RELAXATION
urn:entity:app - Uygulamalar
urn:tag:category:app:meditation - Meditasyon uygulaması
urn:tag:category:app:sleep_tracker - Uyku takip uygulaması
urn:tag:category:app:white_noise - Beyaz gürültü uygulaması
urn:tag:category:app:breathing - Nefes egzersizi uygulaması
🏷️ FILTER PARAMETERS
filter.price_level.min / filter.price_level.max - Fiyat seviyesi
filter.rating.min / filter.rating.max - Değerlendirme
filter.location.radius - Mesafe (yorgun misafir için yakın yerler)
filter.properties.business_rating.min - İşletme kalitesi
filter.hours - Çalışma saatleri (geç saatler için)
filter.amenity - Özellik filtreleri
�� INSIGHTS METRICS
Affinity Score (0-100) - Misafirin tercihlerine uygunluk
Popularity Score (0-1) - Popülerlik
Distance - Mesafe (yorgun misafir için önemli)
Price Level (1-4) - Fiyat seviyesi
Availability - Müsaitlik durumu
Wait Time - Bekleme süresi




**�� YAKINDAKİ YERLER - QLOO API VERİ TİPLERİ**
-Otelin genel yapısı: Oda numarası, asansör, restoran, lobi, çıkış vs.
 -Yakındaki yerler: Market, eczane, ulaşım, otopark.
�� MARKET & GROCERY
urn:entity:place - Genel mekanlar
urn:tag:category:place:market - Market
urn:tag:category:place:grocery_store - Bakkal
urn:tag:category:place:supermarket - Süpermarket
urn:tag:category:place:convenience_store - Market
urn:tag:category:place:food_market - Gıda marketi
urn:tag:category:place:farmers_market - Çiftçi pazarı
urn:tag:category:place:organic_market - Organik market
urn:tag:category:place:delicatessen - Şarküteri
urn:tag:category:place:butcher - Kasap
urn:tag:category:place:fish_market - Balık pazarı
urn:tag:category:place:bakery - Fırın
urn:tag:category:place:liquor_store - İçki dükkanı
💊 PHARMACY & HEALTH
urn:tag:category:place:pharmacy - Eczane
urn:tag:category:place:drugstore - İlaç dükkanı
urn:tag:category:place:medical_supply - Tıbbi malzeme
urn:tag:category:place:health_store - Sağlık dükkanı
urn:tag:category:place:vitamin_store - Vitamin dükkanı
urn:tag:category:place:herbal_store - Bitki dükkanı
urn:tag:category:place:medical_clinic - Tıp kliniği
urn:tag:category:place:urgent_care - Acil bakım
urn:tag:category:place:hospital - Hastane
urn:tag:category:place:dentist - Diş hekimi
🚇 TRANSPORTATION
urn:tag:category:place:subway_station - Metro istasyonu
urn:tag:category:place:bus_station - Otobüs durağı
urn:tag:category:place:train_station - Tren istasyonu
urn:tag:category:place:tram_station - Tramvay durağı
urn:tag:category:place:ferry_terminal - Feribot terminali
urn:tag:category:place:airport - Havalimanı
urn:tag:category:place:taxi_stand - Taksi durağı
urn:tag:category:place:car_rental - Araç kiralama
urn:tag:category:place:bike_rental - Bisiklet kiralama
urn:tag:category:place:scooter_rental - Scooter kiralama
urn:tag:category:place:park_and_ride - Park ve bin
urn:tag:category:place:transportation_hub - Ulaşım merkezi
🚗 PARKING & VEHICLES
urn:tag:category:place:parking_lot - Otopark
urn:tag:category:place:parking_garage - Otopark garajı
urn:tag:category:place:street_parking - Sokak parkı
urn:tag:category:place:valet_parking - Vale park
urn:tag:category:place:free_parking - Ücretsiz park
urn:tag:category:place:ev_charging_station - Elektrikli araç şarj istasyonu
urn:tag:category:place:gas_station - Benzin istasyonu
urn:tag:category:place:car_wash - Araç yıkama
urn:tag:category:place:auto_repair - Oto tamir
urn:tag:category:place:car_dealership - Oto galeri
🏪 CONVENIENCE & SERVICES
urn:tag:category:place:convenience_store - Market
urn:tag:category:place:atm - ATM
urn:tag:category:place:bank - Banka
urn:tag:category:place:post_office - Postane
urn:tag:category:place:laundry - Çamaşırhane
urn:tag:category:place:dry_cleaner - Kuru temizleme
urn:tag:category:place:shoe_repair - Ayakkabı tamiri
urn:tag:category:place:key_duplication - Anahtar kopyalama
urn:tag:category:place:printing_shop - Baskı dükkanı
urn:tag:category:place:copy_center - Kopya merkezi
🍽️ FOOD & BEVERAGES
urn:tag:category:place:restaurant - Restoran
urn:tag:category:place:fast_food - Fast food
urn:tag:category:place:cafe - Kafe
urn:tag:category:place:coffee_shop - Kahve dükkanı
urn:tag:category:place:bakery - Fırın
urn:tag:category:place:ice_cream_shop - Dondurma dükkanı
urn:tag:category:place:juice_bar - Meyve suyu barı
urn:tag:category:place:food_truck - Yemek kamyonu
🏥 EMERGENCY & ESSENTIALS
urn:tag:category:place:police_station - Polis karakolu
urn:tag:category:place:fire_station - İtfaiye
urn:tag:category:place:emergency_room - Acil servis
urn:tag:category:place:urgent_care - Acil bakım
urn:tag:category:place:pharmacy - Eczane (24 saat)
urn:tag:category:place:convenience_store - Market (24 saat)
urn:tag:category:place:gas_station - Benzin istasyonu (24 saat)
��️ AMENITY TAGS
urn:tag:amenity:place:parking - Otopark
urn:tag:amenity:place:wifi - WiFi
urn:tag:amenity:place:wheelchair_accessible - Tekerlekli sandalye erişimi
urn:tag:amenity:place:24_hours - 24 saat açık
urn:tag:amenity:place:delivery - Teslimat
urn:tag:amenity:place:takeout - Paket servis
urn:tag:amenity:place:drive_through - Drive-through
urn:tag:amenity:place:outdoor_seating - Açık alan
📊 FILTER PARAMETERS
filter.location.radius - Mesafe (yakınlık için önemli)
filter.location.query - Konum sorgusu
filter.location.geohash - Hassas konum
filter.hours - Çalışma saatleri
filter.price_level.min / filter.price_level.max - Fiyat seviyesi
filter.rating.min / filter.rating.max - Değerlendirme
filter.properties.business_rating.min - İşletme değerlendirmesi
filter.popularity.min - Popülerlik (güvenilirlik için)
🎯 LOCATION INSIGHTS
Distance - Mesafe (metre/km)
Walking Time - Yürüme süresi
Driving Time - Araç süresi
Public Transport - Toplu taşıma seçenekleri
Availability - Müsaitlik durumu
Wait Time - Bekleme süresi
Crowd Level - Kalabalık seviyesi
Safety Rating - Güvenlik değerlendirmesi
📱 REAL-TIME DATA
Opening Hours - Açık saatler
Current Status - Mevcut durum (açık/kapalı)
Queue Length - Kuyruk uzunluğu
Special Offers - Özel teklifler
Events - Etkinlikler
Maintenance - Bakım durumu



**��️ TOURIST ATTRACTIONS (Turistik Alanlar)**
Şehir hakkında bilgi: Turistik alanlar, ulaşım hatları, taksi çağırma.ŞEHİR BİLGİLERİ - QLOO API VERİ TİPLERİ
urn:entity:place - Genel mekanlar
urn:tag:category:place:museum - Müze
urn:tag:category:place:art_gallery - Sanat galerisi
urn:tag:category:place:historical_site - Tarihi yer
urn:tag:category:place:monument - Anıt
urn:tag:category:place:landmark - Simge yapı
urn:tag:category:place:castle - Kale
urn:tag:category:place:palace - Saray
urn:tag:category:place:mosque - Cami
urn:tag:category:place:church - Kilise
urn:tag:category:place:temple - Tapınak
urn:tag:category:place:synagogue - Sinagog
urn:tag:category:place:cathedral - Katedral
urn:tag:category:place:basilica - Bazilika
��️ NATURAL ATTRACTIONS
urn:tag:category:place:park - Park
urn:tag:category:place:garden - Bahçe
urn:tag:category:place:botanical_garden - Botanik bahçesi
urn:tag:category:place:zoo - Hayvanat bahçesi
urn:tag:category:place:aquarium - Akvaryum
urn:tag:category:place:beach - Plaj
urn:tag:category:place:mountain - Dağ
urn:tag:category:place:lake - Göl
urn:tag:category:place:river - Nehir
urn:tag:category:place:waterfall - Şelale
urn:tag:category:place:forest - Orman
urn:tag:category:place:nature_reserve - Doğa koruma alanı
🎭 ENTERTAINMENT & CULTURE
urn:tag:category:place:theater - Tiyatro
urn:tag:category:place:concert_hall - Konser salonu
urn:tag:category:place:opera_house - Opera evi
urn:tag:category:place:cinema - Sinema
urn:tag:category:place:amusement_park - Eğlence parkı
urn:tag:category:place:casino - Kumarhane
urn:tag:category:place:nightclub - Gece kulübü
urn:tag:category:place:bar - Bar
urn:tag:category:place:pub - Pub
urn:tag:category:place:live_music_venue - Canlı müzik mekanı
��️ SHOPPING & MARKETS
urn:tag:category:place:shopping_mall - Alışveriş merkezi
urn:tag:category:place:market - Pazar
urn:tag:category:place:flea_market - Bit pazarı
urn:tag:category:place:antique_shop - Antika dükkanı
urn:tag:category:place:souvenir_shop - Hediyelik eşya dükkanı
urn:tag:category:place:craft_shop - El sanatları dükkanı
urn:tag:category:place:jewelry_store - Takı dükkanı
urn:tag:category:place:clothing_store - Giyim mağazası
🚇 TRANSPORTATION NETWORK (Ulaşım Hatları)
urn:tag:category:place:subway_station - Metro istasyonu
urn:tag:category:place:bus_station - Otobüs durağı
urn:tag:category:place:train_station - Tren istasyonu
urn:tag:category:place:tram_station - Tramvay durağı
urn:tag:category:place:ferry_terminal - Feribot terminali
urn:tag:category:place:airport - Havalimanı
urn:tag:category:place:transportation_hub - Ulaşım merkezi
urn:tag:category:place:park_and_ride - Park ve bin
urn:tag:category:place:bike_share - Bisiklet paylaşımı
urn:tag:category:place:scooter_share - Scooter paylaşımı
🚕 TAXI & RIDE SERVICES (Taksi Çağırma)
urn:tag:category:place:taxi_stand - Taksi durağı
urn:tag:category:place:taxi_company - Taksi şirketi
urn:tag:category:place:ride_share - Araç paylaşımı
urn:tag:category:place:limousine_service - Limuzin servisi
urn:tag:category:place:car_service - Araç servisi
urn:tag:category:place:private_transport - Özel ulaşım
urn:tag:category:place:chauffeur_service - Şoför servisi
�� ACCOMMODATION
urn:tag:category:place:hotel - Otel
urn:tag:category:place:hostel - Pansiyon
urn:tag:category:place:guesthouse - Misafirhane
urn:tag:category:place:resort - Resort
urn:tag:category:place:apartment_rental - Apartman kiralama
urn:tag:category:place:bed_and_breakfast - Konaklama ve kahvaltı
🍽️ DINING & CUISINE
urn:tag:category:place:restaurant - Restoran
urn:tag:category:place:local_cuisine - Yerel mutfak
urn:tag:category:place:traditional_restaurant - Geleneksel restoran
urn:tag:category:place:fine_dining - Fine dining
urn:tag:category:place:street_food - Sokak yemeği
urn:tag:category:place:food_market - Gıda pazarı
�� TOURIST SERVICES
urn:tag:category:place:tourist_information - Turist bilgi merkezi
urn:tag:category:place:travel_agency - Seyahat acentesi
urn:tag:category:place:tour_operator - Tur operatörü
urn:tag:category:place:guided_tour - Rehberli tur
urn:tag:category:place:city_tour - Şehir turu
urn:tag:category:place:walking_tour - Yürüyüş turu
urn:tag:category:place:boat_tour - Tekne turu
urn:tag:category:place:bus_tour - Otobüs turu
�� DIGITAL SERVICES
urn:entity:app - Uygulamalar
urn:tag:category:app:transportation - Ulaşım uygulaması
urn:tag:category:app:taxi - Taksi uygulaması
urn:tag:category:app:city_guide - Şehir rehberi uygulaması
urn:tag:category:app:transit - Toplu taşıma uygulaması
urn:tag:category:app:maps - Harita uygulaması
��️ AMENITY TAGS
urn:tag:amenity:place:wheelchair_accessible - Tekerlekli sandalye erişimi
urn:tag:amenity:place:guided_tour - Rehberli tur
urn:tag:amenity:place:audio_guide - Sesli rehber
urn:tag:amenity:place:multilingual_staff - Çok dilli personel
urn:tag:amenity:place:free_admission - Ücretsiz giriş
urn:tag:amenity:place:student_discount - Öğrenci indirimi
urn:tag:amenity:place:senior_discount - Yaşlı indirimi
urn:tag:amenity:place:family_friendly - Aile dostu
urn:tag:amenity:place:photography_allowed - Fotoğraf çekimi izni
urn:tag:amenity:place:restroom - Tuvalet
urn:tag:amenity:place:parking - Otopark
urn:tag:amenity:place:wifi - WiFi
📊 FILTER PARAMETERS
filter.location.radius - Mesafe (şehir merkezi etrafında)
filter.location.query - Şehir/ilçe adı
filter.price_level.min / filter.price_level.max - Fiyat seviyesi
filter.rating.min / filter.rating.max - Değerlendirme
filter.properties.business_rating.min - İşletme değerlendirmesi
filter.hours - Çalışma saatleri
filter.popularity.min - Popülerlik (turistik yerler için)
filter.tags - Özel etiketler (tarihi, kültürel, vb.)
�� CITY INSIGHTS
Tourist Rating - Turistik değerlendirme
Local Popularity - Yerel popülerlik
International Recognition - Uluslararası tanınırlık
Cultural Significance - Kültürel önem
Historical Value - Tarihi değer
Accessibility - Erişilebilirlik
Crowd Level - Kalabalık seviyesi
Best Time to Visit - En iyi ziyaret zamanı
Seasonal Events - Mevsimsel etkinlikler
Local Tips - Yerel ipuçları
  
Hızlı Menünün altında sohbet ekranı olur - sohbet ekranında  lento ile müsafir konuşması geçer.
Hızlı menü yada sohbet ekranında etkileşim başlayabilir, sohbet ekranı kayan ekran şeklinde aşağa kayar, , hızlı menü sohbet ekranın hep üstünde kalır.






