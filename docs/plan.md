# Qloo API ile Restoranlar İçin Sorgulanabilen Veri Türleri

## 1. Temel Bilgiler
- İsim (name)
- Adres (address)
- Lokasyon (koordinatlar, şehir, ülke, bölge)
- Açıklama / Kısa Tanım (description, short_description)
- Görsel (image URL)
- Entity ID (Qloo’nun benzersiz restoran kimliği)

## 2. Kültürel ve Davranışsal Analiz
- Popülerlik Skoru (popularity percentile)
- Trend Skoru (trend: percentile, son 6 ayda yükseliş/gidişat)
- Affinity Skoru (belirli bir kullanıcı profiliyle yakınlık)
- Kültürel ve davranışsal etiketler (örn. “Foodie Destination”)

## 3. Etiketler (Tags) ve Kategoriler
- Mutfak Türü (örn. İtalyan, vegan, deniz ürünleri, Asya mutfağı)
- Ambiyans (örn. romantik, aile dostu, lüks, casual)
- Fiyat Seviyesi (1-4 arası, $ işareti gibi)
- Özellikler (örn. brunch, gece açık, rezervasyon gerekli, engelli dostu)
- Diyet Kısıtları (vegan, glutensiz, helal, kosher)
- Erişilebilirlik (engelli dostu, çocuk dostu)
- Özel günler/servisler (brunch, happy hour, canlı müzik)

## 4. Dış Kaynaklarla Eşleşme ve Ekstra Alanlar
- Michelin, Resy, Tripadvisor, Tablet gibi rehberlerle eşleşme (filter.external.exists ile)
- Bu kaynaklardan alınan rating, review count gibi alanlar (varsa)
- Öne çıkan şefler (notable executive chefs)
- Fiyat aralığı (price range)
- Açık olduğu saatler (hours)
- Geohash (coğrafi kodlama)
- Parent/child entity ilişkileri (örn. bir alışveriş merkezindeki restoran)
- İlgili entity’ler (benzer restoranlar, yakın mekanlar)

## 5. Menü ve Yiyecek Detayı
- Menü öğeleri (menu items) – bazı restoranlarda olabilir, garanti değildir
- Restoran menüsü detayları – bazı restoranlarda olabilir, API dökümantasyonunda geçiyor fakat örnek response gösterilmiyor

## 6. Kullanıcı ve Demografi Analizi
- Kullanıcı profiline göre öneri ve affinity skoru
- Demografik segmentasyon (yaş, cinsiyet, ülke, şehir, vb.)
- Lokasyon bazlı analiz ve öneri

## 7. Öneri ve Analiz Fonksiyonları
- Belirli bir restoran/mekan için benzer yerler önerisi
- Belirli bir mutfak veya özelliğe göre en iyi mekanlar
- Lokasyon bazlı trend ve popülerlik analizi
- Tag ve entity bazlı karşılaştırma ve analiz
- Isı haritası (heatmap) ile ilgi yoğunluğu gösterimi



1.Hangi robotik uygulamalar? (Servis robotu, temizlik robotu, teslimat robotu, barista robotu, vb.)
2.Coğrafi kapsam: Global mi, belirli bir ülke/bölge/şehir mi?
3.Restoran türü: Sadece restoranlar mı, kafe, otel, bar, fast food zinciri de dahil mi?
4.Veri Kaynaklarını Belirle , Birincil Kaynaklar
Robot üreticilerinin referans/müşteri listeleri:
Pudu Robotics, Keenon Robotics, Bear Robotics, Softbank Robotics, vb.Web sitelerinde “case studies”, “global customers”, “success stories” bölümlerini incele.Teknoloji ve sektör haberleri:
TechCrunch, Robotics Business Review, HospitalityNet, Wired, The Spoon, vb.Restoranların kendi web siteleri ve sosyal medya hesapları:“Bizde robotik servis var!” duyuruları, basın bültenleri, Instagram/Facebook paylaşımları.
YouTube ve medya içerikleri:“Robot garsonlu restoran” gibi anahtar kelimelerle video ve haber taraması.
5.İkincil Kaynaklar
TripAdvisor, Google Maps, Yelp gibi platformlarda kullanıcı yorumları:“Robot garson vardı, çok ilginçti!” gibi anahtar kelimelerle arama.LinkedIn ve Twitter:
Restoran sahipleri, robot üreticileri ve teknoloji influencer’larının paylaşımları.Akademik makaleler ve sektör raporları:“Robotics in hospitality” başlıklı yayınlar.
6.Veri Toplama ve Temizleme
Manuel tarama:İlk aşamada, yukarıdaki kaynaklardan restoran adı, adresi, ülke/şehir, robotik uygulama türü, robot markası, uygulama tarihi, varsa görsel/link gibi temel alanları topla.
Yarı-otomatik toplama:Web scraping (BeautifulSoup, Selenium, Scrapy gibi araçlarla) ile üretici sitelerinden veya haber sitelerinden veri çekebilirsin.
Crowdsourcing:Kendi web sitende veya sosyal medya kanallarında “Robotik servisli restoran biliyor musunuz?” gibi bir form ile topluluk katkısı alabilirsin.
7.Veri Doğrulama ve Zenginleştirme
Çapraz kontrol:
Aynı restoranın birden fazla kaynakta geçip geçmediğini kontrol et.Adres ve isim normalizasyonu:Farklı yazımları ve adres formatlarını standartlaştır.
Ek alanlar ekle:Qloo API ile eşleştirme için “city”, “country”, “restaurant type”, “website”, “Qloo entity ID” (varsa) gibi alanlar ekle.
6.Sürekli Güncelleme ve Sürdürülebilirlik
Düzenli aralıklarla yeni kaynakları tarayarak veri tabanını güncelle.
Kullanıcı ve sektör paydaşlarından gelen yeni restoranları ekle.
Veri tabanını Qloo API ile eşleştirerek zenginleştir ve analiz için hazır hale getir.
7.Otomasyon ve API Kullanımı
Büyük ölçekli veri için, üretici firmalardan veya teknoloji platformlarından API erişimi talep edebilirsin.
Web scraping ile haber siteleri ve sosyal medya platformlarından otomatik veri çekebilirsin.
8.Etik ve Yasal Hususlar
Web scraping yaparken ilgili sitelerin kullanım koşullarına dikkat et.
Kişisel veri (PII) toplamamaya ve GDPR gibi regülasyonlara uymaya özen göster.


