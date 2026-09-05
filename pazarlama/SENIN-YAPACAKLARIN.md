# Mustafa'nın Yapacakları — adım adım

Son güncelleme: 5 Eylül 2026

Dört iş var. Kolaydan zora sıraladım. Her birinde **nereye gideceğin (link)**, **ne tıklayacağın** ve **ne yazacağın** yazıyor.
Bir maddeyi bitirince bana "1 bitti" de, gerisini ben devralırım.

| # | İş | Süre | Etki |
|---|---|---|---|
| 1 | Cloudflare www yönlendirmesi | 5 dk | Orta |
| 2 | Google İşletme Profili | 40 dk | **En yüksek** |
| 3 | Fotoğraf çekimi | 30 dk | Yüksek |
| 4 | Marka kayıtları (rehber + sosyal) | 40 dk | Orta |

---

# 1. Cloudflare — www yönlendirmesi (5 dakika)

## Neden

Şu an site iki ayrı adreste açılıyor:
- `dongelnakliyat.com/hakkimizda`
- `www.dongelnakliyat.com/hakkimizda`

İkisi de çalışıyor ve **birbirine yönlendirmiyor**. Google bunu iki ayrı site gibi görebiliyor, puan bölünüyor. Tek adrese toplayacağız: **www'lu olan**.

## Nereye gideceksin

👉 https://dash.cloudflare.com

## Adım adım

1. Linke git, giriş yap.
2. Açılan listede **dongelnakliyat.com** yazan kutuya tıkla.
3. Sol menüde **Rules** → altında **Redirect Rules** → **Create rule** (mavi buton).
4. Karşına şablon listesi çıkarsa, **"Redirect from Root to WWW"** şablonunu seç → alan adını kontrol et → **Deploy**. İşin bitti, 6. adıma geç.
5. Şablon çıkmazsa elle doldur — sırayla şunları yaz:

   **Rule name:** `root to www`

   **When incoming requests match** bölümünde **Wildcard pattern** seçeneğini seç:
   ```
   Request URL:  https://dongelnakliyat.com/*
   ```

   **Then** bölümü:
   ```
   Type:         Static  (veya "URL redirect")
   Target URL:   https://www.dongelnakliyat.com/${1}
   Status code:  301 - Permanent Redirect
   ```
   **Preserve query string** kutusunu **işaretle**.

6. **Deploy** butonuna bas.

## Test et (bunu mutlaka yap)

Tarayıcının adres çubuğuna şunu yaz ve entera bas:

```
dongelnakliyat.com/blog
```

Adres kendiliğinden `www.dongelnakliyat.com/blog` olarak değişiyorsa **tamam**. Değişmiyorsa bana söyle.

> Not: Bu işi site dosyalarından yapamıyorum. Cloudflare'de alan adı seviyesindeki yönlendirme sadece panelden kuruluyor. Panele girmemi istersen de yapabilirim ama hesap ayarı olduğu için her adımda onayını isterim — sen 5 dakikada bitirirsin.

---

# 2. Google İşletme Profili (40 dakika, tek oturumda)

## Neden

"istanbul evden eve nakliyat" yazınca en üstte reklamlar, hemen altında **3 firmalık harita kutusu** çıkıyor. O kutuya girmenin **tek yolu** bu profil. Site tek başına oraya giremez.

Ayrıca Search Console verisi şunu gösteriyor: 271 sayfamızın sadece 9'u Google'ın dizininde. Google siteyi "gerçek bir işletme" olarak henüz tanımadığı için ağır davranıyor. İşletme Profili bu güveni en hızlı kuran şey.

## Nereye gideceksin

👉 https://business.google.com/create

(çalışmazsa: https://www.google.com/business/ → sağ üstte **Şimdi yönetin**)

## Başlamadan önce masaya koy

- [ ] Profili yönetecek Google hesabı — **`mustafaagurman@gmail.com` kullan** (Search Console'da da bu hesap var, ikisi aynı olsun)
- [ ] **Vergi levhası** (videoda göstereceksin)
- [ ] **Araç** — üzerinde firma yazısı varsa çok iyi
- [ ] Telefonun şarjı ve 5 dakika sessiz zaman

## Adım adım — ne yazacaksın

Ekranlar sırayla gelir, aşağıdakileri **birebir** gir:

| Google ne sorar | Sen ne yazacaksın |
|---|---|
| İşletme adı | `Dönmar Nakliyat` |
| İşletme kategorisi | `Nakliyat şirketi` |
| Müşterilerin gelebileceği bir yer var mı? | **Hayır** |
| Hizmet verdiğin bölgeler | Aşağıdaki 15 ilçe |
| Telefon | `0538 861 41 10` |
| Web sitesi | `https://www.dongelnakliyat.com` |

### ⚠️ İşletme adına tek kelime ekleme

`Dönmar Nakliyat İstanbul Evden Eve` gibi bir isim Google'ın kuralını ihlal eder ve **profili askıya aldırır**. Anahtar kelime işini site yapıyor zaten.

### Hizmet bölgeleri — sadece bu 15'ini gir

```
Esenyurt · Küçükçekmece · Bahçelievler · Bağcılar · Beylikdüzü
Başakşehir · Avcılar · Pendik · Kartal · Maltepe
Ümraniye · Ataşehir · Kadıköy · Üsküdar · Şişli
```

39 ilçenin hepsini girme — sinyali seyreltir. Profil oturunca listeyi genişletiriz.

### Çalışma saatleri

Pazartesi–Pazar: `08:00 – 20:00`

### İşletme açıklaması

Profil açıldıktan sonra **Düzenle → Açıklama** kısmına şunu **olduğu gibi** yapıştır:

```
Dönmar Nakliyat, İstanbul genelinde evden eve nakliyat, ofis taşımacılığı,
şehirlerarası nakliyat, asansörlü taşımacılık, parça eşya taşıma ve gıda
taşımacılığı hizmeti veriyor. 10 yılı aşkın saha tecrübemizle çalışıyoruz.

Keşif ücretsizdir. Keşifte verdiğimiz fiyat yazılı sözleşmeye geçer ve orada
sabitlenir; iş uzadı ya da eşya fazla çıktı gerekçesiyle sonradan ek ücret
talep etmiyoruz. Taşeron ekip kullanmıyoruz, işi kendi aracımız ve sabit
kadromuzla yapıyoruz. Tüm taşımalar sigortalıdır, her iş için fatura
düzenlenir.

Paketleme malzemesi, mobilya montaj ve demontajı standart hizmetimize
dahildir. Ücretsiz keşif için 0538 861 41 10.
```

## Video doğrulaması — en kritik kısım

Hizmet bölgesi işletmelerinde Google genelde **video** istiyor. **Çekmeden önce bu bölümü sonuna kadar oku.**

**Kurallar**
- **Kesintisiz** çek, **en az 30 saniye**
- Hiç kesme, hiç düzenleme yok — beğenmezsen baştan çek
- Telefonla ve **profili açtığın Google hesabıyla giriş yapmışken** çek

**Çekim sırası — bu sırayla yürü, kamerayı hiç durdurma**

1. **Dışarıyı göster** — sokak, tabela, çevredeki bir bina (Google konumu buradan anlıyor)
2. **Yürüyerek araca git** — kesme yapma, yürürken çek
3. **Aracın dışını göster** — firma yazısı varsa yakın çek
4. **Araç kapısını aç, içini göster** — battaniye, streç, koli, kayış, ambalaj malzemesi
5. **Sonunda vergi levhasını** veya üzerinde işletme adı geçen bir belgeyi kameraya tut

**Araçta firma yazısı yoksa:** üniforma, fatura, kartvizit veya vergi levhası mutlaka net görünsün. İşletme adının fiziksel bir kanıtı ekranda olmalı.

> ⚠️ Üst üste başarısız denemeden sonra Google "başka doğrulama yolu yok" diyip destek hattına yönlendiriyor ve süreç haftalara yayılıyor. **İlk denemeyi aceleye getirme.** Yukarıdaki 5 adımı kafanda bir kez prova et, sonra kaydı başlat.

Doğrulama sonucu genelde **birkaç gün** içinde e-postayla geliyor.

## Onaylandıktan sonra bana ne göndereceksin

Profil → **Yorum iste** → çıkan `g.page/r/...` linkini kopyala, bana at.
O linkle QR kartını ve sitedeki yorumlar bölümünü ben hazırlarım.

Ayrıntılı versiyon: `pazarlama/ISLETME-PROFILI-ACILIS.md`

---

# 3. Fotoğraf çekimi (30 dakika)

## Neden

İki yerde birden lazım:
- **Sitede** 3 hizmet sayfasının görseli hâlâ geçici çizim (ofis taşımacılığı, şehirlerarası nakliyat, gıda taşımacılığı)
- **İşletme Profili** fotoğrafsız profilleri öne çıkarmıyor

Stok görsel işe yaramaz — Google gerçek fotoğrafı ayırt ediyor.

## Ne çekeceksin

Telefonla, **gündüz, doğal ışıkta**. Yatay çek (telefonu yan tut).

| Konu | Kaç kare |
|---|---|
| Araç dıştan, firma yazısı görünecek şekilde | 3 |
| Araç içi: battaniye, streç, koli, kayışlar | 2 |
| Ekip çalışırken: koltuk sarılırken, koli taşınırken | 4 |
| Asansörlü taşıma anı (varsa) | 2 |
| Ofis / işyeri taşıması (varsa) | 2 |
| Şehirlerarası yükleme, kapalı kasa dolu hali (varsa) | 2 |
| Soğuk zincir / gıda taşıma (varsa) | 2 |

**Yüz görünmesin** — ya arkadan çek ya da ekibe önceden söyle. Müşterinin evi/eşyası tanınacak şekilde çıkmasın.

## Nereye koyacaksın

Bilgisayarda şu klasörü aç ve içine at:

```
C:\Users\acemo\OneDrive\Belgeler\GitHub\dongelnakliyat\pazarlama\fotograflar
```

Klasörü senin için oluşturdum, hazır duruyor. İsim vermene gerek yok, olduğu gibi at.

Sonrasını ben yaparım: seçme, kırpma, sıkıştırma, webp'e çevirme, siteye yerleştirme, alt metin yazma.

---

# 4. Marka kayıtları (40 dakika)

## Neden

Google'da `dönmar nakliyat` yazınca hâlâ "dönmez nakliyat" diye düzeltiyor. Yani Google bu markayı henüz tanımıyor.

Google bir markanın gerçek olduğuna, **aynı bilgiyi birden fazla bağımsız kaynakta** görünce inanıyor. O bilgi şu üçlü:

## 📋 Her yere birebir bu bilgiyi gireceksin

```
İsim:     Dönmar Nakliyat
Telefon:  0538 861 41 10
Site:     https://www.dongelnakliyat.com
E-posta:  info@dongelnakliyat.com
Saatler:  Her gün 08:00 - 20:00
```

**Kural:** Tek bir harf, tek bir boşluk bile farklı olmayacak. Farklı numara = Google için ayrı firma.

## 4a. Bulurum kaydını düzelt (10 dk)

👉 https://www.bulurum.com

Orada şöyle bir kayıt var: **"DÖNMAR TAŞIMACILIK (İsa Döngel), Başakşehir, 0545 271 79 54"**

- **Bu senin işletmense:** kaydı sahiplen, adı `Dönmar Nakliyat`, telefonu `0538 861 41 10`, siteyi `www.dongelnakliyat.com` yap.
- **Senin değilse:** dokunma, bana haber ver.

## 4b. Yandex Business — ücretsiz, rakip az (15 dk)

👉 https://yandex.com.tr/sprav/add/

Türkiye'de Yandex Haritalar hatırı sayılır kullanılıyor ve nakliyat kategorisinde rekabet Google'a göre çok daha az. Ücretsiz.

1. Linke git, Yandex hesabıyla giriş yap (yoksa 1 dakikada açılıyor)
2. Firma adı: `Dönmar Nakliyat`
3. Faaliyet türü: `Nakliyat` / `Taşımacılık`
4. Yukarıdaki telefon ve site bilgisini gir
5. Doğrulama: telefona SMS gelir, kodu gir

## 4c. Instagram + Facebook (15 dk)

Takipçi için değil, **marka sinyali** için.

👉 https://www.instagram.com/accounts/emailsignup/
👉 https://www.facebook.com/pages/create

- Kullanıcı adı: `donmarnakliyat` (müsaitse)
- Görünen isim: `Dönmar Nakliyat`
- Biyografi:
  ```
  İstanbul geneli evden eve nakliyat · Sigortalı taşıma · Yazılı sabit fiyat
  ☎ 0538 861 41 10
  ```
- Web sitesi alanı: `https://www.dongelnakliyat.com`

**Sonrası:** Haftada 1 paylaşım yeter. Gerçek bir iş fotoğrafı + iki cümle. Slogan yok, stok görsel yok, 30 hashtag yok.

## Bitince bana ne göndereceksin

Açtığın hesapların adreslerini bana at (Instagram, Facebook, Yandex). Sitenin arka planındaki marka şemasına (`sameAs`) eklerim — Google "bu hesaplar aynı firmaya ait" diye okur.

---

# 5. Yorum toplama (2 numara bitince otomatik başlar)

Şimdilik yapacağın bir şey yok. Profil onaylanınca:

- Ben: QR kartı + WhatsApp mesaj şablonu + sitedeki yorumlar bölümünü hazırlarım
- Sen: iş bitiminde müşteriye tek mesaj atarsın

Ayrıntı: `pazarlama/YORUM-TOPLAMA.md`

> ❌ **Sahte yorum, tanıdıktan yorum, indirim karşılığı yorum yok.** Google bunları yakalıyor ve profili askıya alıyor; geri almak aylar sürüyor.

---

# Benim tarafım (senden bir şey istemez)

- Her sabah: Search Console ölçümü → 2 ilçe sayfası derinleştirme → günün içeriği → doğrulama → otomatik yayın
- **5 Eylül itibarıyla Search Console okunuyor** — artık gerçek sıralama verisi raporda var. Tek şart: tarayıcıda Google oturumun açık kalsın.
- Kalan ince sayfa: evden eve 31/39, asansörlü 39/39. Günde 2 tanesini derinleştiriyorum.
- Push "token" hatası verirse raporda yazarım; `TOKEN-KUR.bat` dosyasını tekrar çalıştırman yeter.

---

## Özet — şu sırayla yap

1. **Bugün:** Cloudflare yönlendirmesi (5 dk) → hemen kapanır
2. **Bu hafta sonu:** İşletme Profili + video (40 dk) → en büyük kazanç
3. **Bir iş gününde:** Fotoğraf çek, klasöre at (30 dk)
4. **Boş bir akşam:** Bulurum + Yandex + sosyal hesaplar (40 dk)
