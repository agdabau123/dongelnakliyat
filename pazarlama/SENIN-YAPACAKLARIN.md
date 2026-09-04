# Mustafa'nın Yapacakları — sade liste

Sıra önem sırasıdır. Her maddede "neden" ve "nasıl" var. Bir maddeyi bitirince bana "1 bitti" de, gerisini ben devralırım.

Son güncelleme: 4 Eylül 2026

---

## 1. Search Console'a beni ekle (5 dakika) — EN ACİL

**Neden:** Her sabah hangi kelimede kaçıncı sıradayız, hangi sayfa indekslendi, nerede hata var — bunları ancak buradan görebiliyorum. Şu an göremiyorum, kör çalışıyorum.

**Nasıl:**
1. Bilgisayarda `mustafaagurman@gmail.com` ile giriş yap.
2. Şu adrese git: https://search.google.com/search-console
3. Sol üstten mülkü seç: **dongelnakliyat.com**
4. Sol menüde en altta **Ayarlar** → **Kullanıcılar ve izinler** → sağ üstte **Kullanıcı ekle**
5. E-posta: `acemoglumg61@gmail.com` — İzin: **Tam** (Sahip değil, "Tam" yeterli) → **Ekle**

Bu kadar. Ertesi sabahki raporda gerçek sıralama verisi görürsün.

---

## 2. Google İşletme Profili'ni aç (30-40 dakika) — EN BÜYÜK KALDIRAÇ

**Neden:** "istanbul evden eve nakliyat" yazınca en üstte reklamlar, hemen altında **3 firmalık harita kutusu** çıkıyor. Oraya girmenin tek yolu bu profil. Site tek başına haritaya giremez. Bugün itibarıyla o kutuda biz yokuz, olamayız da — profil yok.

**Nasıl:** Adım adım hazır: `pazarlama/ISLETME-PROFILI-ACILIS.md`
Özet:
- İşletme adı: **Dönmar Nakliyat** (başka kelime ekleme — askıya alırlar)
- Tür: **Hizmet bölgesi işletmesi** (adres gizli kalır)
- Telefon: **0538 861 41 10** (sitedekiyle birebir)
- Site: **https://www.dongelnakliyat.com** (www ile)
- Video doğrulama: dosyadaki 5 adımı okuduktan sonra tek çekimde yap

**Bitince bana ilet:** Yorum linki (`g.page/r/...`) — QR kartı ve sitedeki yorum bölümünü o linkle hazırlarım.

---

## 3. Cloudflare'de www yönlendirmesi (5 dakika)

**Neden:** Site şu an hem `dongelnakliyat.com` hem `www.dongelnakliyat.com` olarak açılıyor. Google ikisini ayrı site sayıp puanı bölüyor — aramalarda iki adres birden görünüyor. Tek adrese toplamamız lazım.

**Nasıl:**
1. https://dash.cloudflare.com → giriş → **dongelnakliyat.com** alan adına tıkla
2. Sol menü: **Rules** → **Redirect Rules** → **Create rule**
3. Hazır şablon varsa: **"Redirect from Root to WWW"** şablonunu seç → **Deploy**. Şablon yoksa elle:
   - Rule name: `root to www`
   - When incoming requests match → **Hostname** — **equals** — `dongelnakliyat.com`
   - Then → **Dynamic** → Expression kutusuna şunu yapıştır:
     `concat("https://www.dongelnakliyat.com", http.request.uri.path)`
   - Status code: **301** — "Preserve query string" işaretli
   - **Deploy**
4. Test: tarayıcıya `dongelnakliyat.com/blog` yaz → `www.dongelnakliyat.com/blog` açılmalı.

---

## 4. Fotoğraf çek (30 dakika, tek seferde)

**Neden:** Sitede 3 hizmet sayfasının görseli hâlâ geçici çizim. Google İşletme Profili de fotoğrafsız profili öne çıkarmaz. Gerçek fotoğraf hem siteyi hem profili güçlendirir; stok görsel işe yaramaz.

**Ne çekilecek (telefonla, gündüz):**
- Araç dıştan, firma yazısı görünecek şekilde (2-3 kare)
- Araç içi: battaniye, streç, koli, kayışlar (2 kare)
- Ekip çalışırken: paketleme anı, koltuk sarılırken, koli taşınırken (3-4 kare)
- Asansörlü taşıma anı, varsa (2 kare)
- Ofis/iş yeri taşıması varsa bir kare, şehirlerarası yükleme bir kare

**Nereye:** `pazarlama/fotograflar/` klasörü aç, içine at. Ben seçer, boyutlandırır, siteye ve profile uygun hale getiririm.

---

## 5. Rehber kayıtlarını kontrol et (10 dakika)

**Neden:** Google "Dönmar Nakliyat" yazınca bizi tanımıyor, "Dönmez Nakliyat" diye düzeltiyor. Markanın Google'da "gerçek bir işletme" sayılması için isim-telefon-site üçlüsünün her yerde **aynı** olması lazım.

**Nasıl:**
- bulurum.com'da "DÖNMAR TAŞIMACILIK (İsa Döngel), Başakşehir, 0545 271 79 54" diye bir kayıt var. **Bu senin işletmen mi?**
  - Evetse: kaydı sahiplen, adı **Dönmar Nakliyat**, telefonu **0538 861 41 10**, siteyi **www.dongelnakliyat.com** yap.
  - Değilse: dokunma, bana söyle.
- Başka bir yerde (eski ilan siteleri, Yandex, sahibinden vb.) firma kaydın varsa aynı düzeltmeyi yap. Farklı numara ve farklı isim, Google için "iki ayrı firma" demek.

---

## 6. Instagram + Facebook sayfası aç (20 dakika, sonra haftada 1 paylaşım)

**Neden:** Takipçi için değil. Google, markanın var olduğuna ancak birden fazla kaynakta aynı bilgiyi görünce inanır. İki sosyal hesap + İşletme Profili + site = "gerçek marka" sinyali.

**Nasıl:**
- İsim: **Dönmar Nakliyat** — Bio'da: telefon `0538 861 41 10` + `www.dongelnakliyat.com`
- Haftada 1 paylaşım yeter: gerçek iş fotoğrafı + iki cümle. Slogan, stok görsel, hashtag yığını yok.
- Hesap adreslerini bana ilet, sitenin şemasına (sameAs) eklerim.

---

## 7. Her iş sonrası yorum iste (Profil açılınca başlar)

**Neden:** Harita kutusunda sıralamayı belirleyen üç şey: yakınlık, yorum sayısı, yorum kalitesi. Rakiplerin yorumu var, bizim sıfır.

**Nasıl:** `pazarlama/YORUM-TOPLAMA.md` — teslimattan sonra WhatsApp'tan tek mesaj. Sahte yorum, tanıdıktan yorum, indirim karşılığı yorum **yok** — profil askıya alınır, geri almak aylar sürer.

---

## Benim tarafım (senden bir şey istemez)

- Her sabah 08:00: ölçüm → 3 içerik → doğrulama → otomatik yayın. Push çalışıyor.
- Bugün yapılan büyük değişiklik: 117 ince ilçe×hizmet sayfası ilçe sayfalarına birleştirildi (Google'ın "kapı sayfası" cezası riskini kaldırmak için). Site 274 → 157 sayfa, ama her sayfa daha dolu.
- Sıradaki 6 hafta: 33 ilçenin evden eve sayfasını mahalle mahalle derinleştirme (Esenyurt, Bahçelievler, Pendik, Ümraniye, Kadıköy, Küçükçekmece bitti) + fiyat içerikleri + semt rehberleri.

**Push "token" hatası verirse** raporda yazarım; `TOKEN-KUR.bat` dosyasını tekrar çalıştırman yeter.
