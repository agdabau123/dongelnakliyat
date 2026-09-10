# Mustafa'nın Yapacakları — adım adım

Son güncelleme: 10 Eylül 2026

> 📌 **İş almak için ne yapılmalı sorusunun cevabı ayrı dosyada:** `pazarlama/IS-ALMA-PLANI.md`
> Bu dosya siteyle ilgili teknik maddeleri tutuyor; iş alma kanalları (eski müşteri, İşletme Profili,
> Armut, Bulurum/Yandex, Ads) ve hazır mesaj şablonları orada.

Dört iş var. Kolaydan zora sıraladım. Her birinde **nereye gideceğin (link)**, **ne tıklayacağın** ve **ne yazacağın** yazıyor.
Bir maddeyi bitirince bana "1 bitti" de, gerisini ben devralırım.

| # | İş | Süre | Etki | Durum |
|---|---|---|---|---|
| 1 | Cloudflare www yönlendirmesi | 5 dk | Orta | ✅ **BİTTİ** — 5 Eylül |
| 2 | Google İşletme Profili | 40 dk | **En yüksek** | 🔴 **4 MÜKERRER KAYIT VAR** — önce temizlik |
| 3 | Fotoğraf çekimi | 30 dk | Yüksek | ⬜ |
| 4 | Marka kayıtları (rehber + sosyal) | 40 dk | Orta | ⬜ |
| 5 | Natro otomatik yenileme | — | Kritik | ✅ **ZATEN AÇIKMIŞ** — 10 Eylül'de teyit edildi |

---

# 5. Natro otomatik yenileme — ✅ KONTROL EDİLDİ, AÇIK (10 Eylül 2026)

Panele girip baktım. Her iki alan adında da durum şu:

| Alan adı | Bitiş | Otomatik yenileme |
|---|---|---|
| **dongelnakliyat.com** | 26 Ağustos 2027 | ✅ Aktif — kayıtlı karttan **20 Ağustos 2027**'de çekilecek |
| dongelnakliyat.xyz | 26 Ağustos 2027 | ✅ Aktif — aynı kart, aynı tarih |

Ödeme talimatı 26 Ağustos 2026'da, alan adını alırken sepette verilmiş. Yani yapılacak bir şey yoktu.
Yenileme, bitiş tarihinden **6 gün önce** deneniyor — sorun çıkarsa müdahale için pay var.

### Tek dikkat edilecek şey

Kayıtlı kartın son kullanma tarihi 2027 Ağustos'tan önce dolarsa çekim başarısız olur ve alan adı düşer.
**Kartı yenilediğinde Natro'daki kayıtlı kartı da güncelle.** Bunu 2027 Temmuz'a not düştüm, o dönemde
hatırlatacağım.

<details>
<summary>Eski talimat (artık gerekmiyor)</summary>

## Neden gerekiyordu

**9-10 Eylül'de site 20 saat kapalı kaldı.** Sebep: alan adı kayıt e-postasını 14 gün içinde
onaylamadığın için Natro alan adını ICANN kuralı gereği askıya aldı (`clientHold`). Onayladın, düzeldi.

O sorun tek seferlikti, bir daha çıkmaz. Ama **yenileme ayrı bir risk**: alan adı 26 Ağustos 2027'de
doluyor ve otomatik yenileme kapalıysa site aynı şekilde kapanır — üstelik o zaman geri almak
çok daha zor ve pahalı olur.

## Senden istediğim tek şey

👉 https://www.natro.com/musteri/default.asp adresine **Chrome'da giriş yap**, sonra bana "girdim" de.

Otomatik yenilemeyi açmayı ben hallederim. Giriş yapamıyorum çünkü şifre girmiyorum —
bu kural bende sabit, hesap şifrelerini görmem ve yazmam.

Kendin yapmak istersen: giriş → **Alan Adlarım** → `dongelnakliyat.com` → **Otomatik Yenileme: Açık**.
Kayıtlı ödeme yöntemi yoksa onu da eklemen gerekiyor, yoksa otomatik yenileme çalışmaz.

</details>

---

# 🔴 ÖNCELİK — 9 Eylül'de bulundu: 4 mükerrer İşletme Profili

İşletme Profili Yöneticisi'nde **tek profil değil, dört profil** var. Dördü de doğrulanmamış (%0 doğrulandı).
Google bir markayı, aynı bilgiyi birden fazla yerde tutarlı görünce tanıyor. Burada tam tersi var: dört kayıt,
dört farklı isim/kategori/saat. **"Google dönmar nakliyatı dönmez diye düzeltiyor" sorununun sebebi büyük
ihtimalle bu.** Doğrulamaya girmeden önce bunun temizlenmesi lazım — yoksa yanlış kaydı doğrulamış olursun.

| | İsim | Kategori | Bölge | Saat | Site |
|---|---|---|---|---|---|
| **A** | Döngel Nakliyat ❌ *(eski isim)* | Evden Eve Nakliyat | İstanbul | 08:00-20:00 ❌ | www ✓ |
| **B** | DönmarNakliyat ❌ *(bitişik)* | Lojistik Firması ❌ | **Bursa, Düzce +8** ❌ | 09:00-22:00 ❌ | **www'suz** ❌ |
| **C** | Dönmar Nakliyat ✓ | **Evden Eve Nakliyat ✓** | İstanbul ✓ | 09:00-**21:30** ⚠️ | www ✓ |
| **D** | Dönmar Nakliyat ✓ | Nakliyat Şirketi ⚠️ | İstanbul ✓ | **08:00-20:00** ❌ | www ✓ |

### Önerim: **C'yi tut, diğer üçünü kapat**

C zaten doğru isimde, doğru bölgede ve **birincil kategorisi zaten "Evden Eve Nakliyat"** —
yani listedeki "kategori ters" maddesi C için geçerli değilmiş, o madde D'yi tarif ediyormuş.
C'de düzeltilecek tek şey çalışma saati: **21:30 → 21:00** (site 09:00-21:00 diyor, birebir aynı olmalı).

### Sen ne yapacaksın

👉 https://business.google.com/locations

1. **A, B ve D**'yi tek tek aç → sağ üstteki üç nokta → **"İşletmeyi kaldır" / "Profili sil"**.
   Doğrulanmamış kayıtlar olduğu için silmek kolay, kimseye görünmüyorlar zaten.
2. **C'yi aç** → Profili düzenle → Çalışma saatleri → **09:00 - 21:00** yap.
3. Sonra **sadece C için** video doğrulamasına gir (adımlar aşağıda).

> ⚠️ Silme işini ben yapmıyorum: canlı işletme kaydını kalıcı silmek geri alınamıyor, bu senin kararın olmalı.
> Hangisinin silineceğinden emin değilsen bana sor, birlikte bakarız.

---

# 1. Cloudflare — www yönlendirmesi ✅ ÇÖZÜLDÜ (5 Eylül 2026)

Kural yayında ve **Active**: `Redirect from root to WWW [Template]`
`https://dongelnakliyat.com/*` → `https://www.dongelnakliyat.com/${1}` · **301** · query string korunuyor.

Test edildi, üçü de geçti:
- `dongelnakliyat.com/blog` → www'ya döndü ✅
- `dongelnakliyat.com/evden-eve-nakliyat-maltepe` → www'ya döndü ✅
- `dongelnakliyat.com/teklif-al?utm_source=test` → www'ya döndü, parametre korundu ✅

Artık site tek adreste toplandı. Bir daha dokunmana gerek yok.

<details>
<summary>Nasıl yapıldığı (kayıt için)</summary>

Cloudflare → dongelnakliyat.com → **Rules → Overview** → şablon listesi → **"Redirect from root to WWW"** kartı → *Create from template* → **Preserve query string** işaretle → **Deploy**.

⚠️ Listede birbirine çok benzeyen iki kart var. Doğru olanın açıklaması *"Always redirect HTTP requests from the root..."* diye başlar. *"...from the WWW subdomain"* diye başlayan kart tam tersini yapar.
</details>

<details>
<summary>Eski talimat (artık gerekmiyor)</summary>

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

> Not: Bu işi site dosyalarından yapamıyorum. Cloudflare'de alan adı seviyesindeki yönlendirme sadece panelden kuruluyor.

</details>

---

# 2. Google İşletme Profili — 🔴 ÖNCE MÜKERRER TEMİZLİĞİ (yukarı bak)

> **9 Eylül notu:** Aşağıdaki tablo tek profil varsayımıyla yazılmıştı. Gerçekte dört kayıt var —
> yukarıdaki kırmızı bölüme bak. Aşağısı, tutulacak profil (C) için hâlâ geçerli.
> "Kategori ters" maddesi C'de **zaten düzelmiş**; C'de kalan tek düzeltme çalışma saati (21:30 → 21:00).

## Durum (5 Eylül 2026)

Profil oluşturuldu, şu an **"HERKESE GÖRÜNÜR DEĞİL"** — doğrulama yapılmadığı için Google'da yayında değil.

| Alan | Değer | |
|---|---|---|
| İşletme adı | Dönmar Nakliyat | ✅ |
| Çalışma saatleri | 09:00 – 21:00 | ✅ site ile birebir |
| Telefon | 0538 861 41 10 | ✅ |
| Web sitesi | https://www.dongelnakliyat.com | ✅ |
| Açıklama | 733 karakter, girildi | ✅ |
| Hizmet bölgesi | İstanbul, Türkiye | ✅ yeterli |
| Açılış tarihi | 1 Şubat 2019 (şirket kuruluşu) | ✅ |
| **Kategori** | Nakliye Hizmeti (birincil) + Evden Eve Nakliyat | ⚠️ **ters — düzeltilecek** |
| **Doğrulama** | yapılmadı (video) | ⬜ **kalan iş** |
| Fotoğraf | yok — gerçek fotoğraf bekleniyor | ⬜ |

> 📌 **10 Eylül:** Silme ve saat düzeltmesinin ekran ekran anlatımı ayrı dosyada:
> **`pazarlama/ISLETME-PROFILI-ADIM-ADIM.md`** — mağaza kodlarıyla birlikte, hangi menüde
> neye basılacağı yazılı. Aşağıdaki eski özet yerine onu kullan.

### Kalan iki iş

**a) Kategorileri yer değiştir (2 dk)**
`Evden Eve Nakliyat` **birincil** olmalı, `Nakliye Hizmeti` ek kategori olarak kalmalı.
Yerel aramada birincil kategori diğerlerinden kat kat ağır basar; hedefimiz "istanbul evden eve nakliyat" olduğu için birebir eşleşen kategori öne alınmalı.
Yol: **Profili düzenle → Hakkında → İşletme kategorisi**

**b) Video doğrulaması**
Ofiste ve araç yanındayken yapılacak. Adımlar aşağıda, aynen geçerli.

### 📌 Kayda geçsin: 2019 vs "10 yılı aşkın tecrübe"

Şirket **1 Şubat 2019**'da kuruldu, ama Mustafa işi daha eskiden beri yapıyor.
Sitedeki "10 Yılı Aşkın Tecrübe · İstanbul genelinde saha tecrübesi" ifadesi **şirketin yaşını değil saha tecrübesini** anlatıyor — doğru ve çelişki değil. Bu iki bilgiyi karıştırıp site metnini değiştirme.

---

## Neden

"istanbul evden eve nakliyat" yazınca en üstte reklamlar, hemen altında **3 firmalık harita kutusu** çıkıyor. O kutuya girmenin **tek yolu** bu profil. Site tek başına oraya giremez.

Ayrıca Search Console verisi şunu gösteriyor (7 Eylül 2026): 157 sayfanın 144'ü dizine eklendi — indeksleme sorunu büyük ölçüde çözüldü. Asıl sorun artık görünürlük: 28 günde 514 gösterim, **0 tıklama**, ortalama pozisyon 73,5. Yani Google sayfaları biliyor ama çok geriden gösteriyor. İlk sayfaya en yakın olduğumuz kelimelerde bile harita kutusu ekranın üstünü kapatıyor. İşletme Profili o kutuya girmenin tek yolu.

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

## 4a. Bulurum'a yeni kayıt aç (10 dk)

👉 https://www.bulurum.com

> 📌 **Düzeltme (10 Eylül):** Daha önce buraya "Bulurum'daki kaydı düzelt" diye yazmıştım.
> **Yanlıştı.** Oradaki **"DÖNMAR TAŞIMACILIK (İsa Döngel), Başakşehir, 0545 271 79 54"** kaydı
> **bize ait değil** — Mustafa teyit etti, başka bir firma. **O kayda dokunma.**

Yapılacak şey: sıfırdan **kendi** kaydını açmak — `Dönmar Nakliyat`, `0538 861 41 10`,
`www.dongelnakliyat.com`, `info@dongelnakliyat.com`, `Her gün 09:00 - 21:00`.

**Not:** Piyasada aynı isimde başka bir nakliyat firması olması marka aramasında ayrışmayı
zorlaştırıyor. Bunun tek çözümü doğrulanmış İşletme Profili ve gerçek yorumlar; ayrıntısı
`pazarlama/IS-ALMA-PLANI.md` içinde.

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
- Kalan ince sayfa: evden eve **15/39**, asansörlü 39/39. Günde 2 tanesini derinleştiriyorum. Artık sırayı listeden değil **Search Console talebinden** belirliyorum: en çok gösterim alan ince sayfa öne geçiyor.
- Push "token" hatası verirse raporda yazarım; `TOKEN-KUR.bat` dosyasını tekrar çalıştırman yeter.

## Search Console — 9 Eylül ölçümü (son 28 gün)

151 sorgu · **565 gösterim · 0 tıklama · ort. pozisyon 73,7** · dizinde 144 sayfa (212 sayfa dizin dışı,
büyük bölümü 301'lediğimiz eski sayfalar).

**Kelime kümeleri — gösterim / ortalama pozisyon:**

| Küme | Sorgu | Gösterim | Ort. pozisyon |
|---|---|---|---|
| **parça eşya taşıma + ilçe** | 11 | **133** | **66,4** ← sorgu başına en verimli küme |
| evden eve + ilçe | 52 | 227 | 77,7 |
| fiyat / ücret / ne kadar | 31 | 92 | 70,2 |
| ofis taşımacılığı | 37 | 76 | 81,1 |
| asansörlü | 20 | 49 | 76,8 |
| **marka ("dönmar nakliyat")** | **0** | **0** | — ← marka hâlâ görünmez |

**İlk sayfaya en yakın 3 kelime:**
1. `nakliyeciler klima söker mi` — **pozisyon 10** (sitenin en iyi sırası; 9 Eylül'de başlık bu soruya göre düzeltildi)
2. `adalar asansörlü nakliyat` — pozisyon 37
3. `istanbul evden eve nakliyat fiyatlari` — pozisyon 40,5

### 📌 Kayda geçsin: parça eşya bulgusu

`parça eşya taşıma + ilçe` sorguları, sorgu başına en çok gösterimi alan küme (12,1 gösterim/sorgu;
evden evede bu 4,4). Bu sayfaları 4 Eylül'de kapı sayfası oldukları için 301'leyip kaldırmıştık —
karar doğruydu, ilçe×hizmet kapı sayfası üretmeye geri dönmüyoruz. Ama talep gerçek.
**Doğru cevap:** tek ve gerçekten iyi bir `hizmetler/parca-esya-tasima` sayfası + bölge hub'larındaki
`#parca-esya` bölümleri. Bunu yakın bir güne planlıyorum.

---

## Özet — şu sırayla yap

1. ~~Cloudflare yönlendirmesi~~ ✅ **bitti (5 Eylül)**
2. ~~Natro otomatik yenileme~~ ✅ **zaten açıkmış, teyit edildi (10 Eylül)**
3. **🔴 İlk iş (15 dk):** Mükerrer 3 profili sil (A, B, D), C'nin saatini 21:00 yap — en üstteki kırmızı bölüm
4. **Sonra (ofiste):** Sadece C için video doğrulaması
5. **Bir iş gününde:** Fotoğraf çek, klasöre at (30 dk)
6. **Boş bir akşam:** Bulurum + Yandex + sosyal hesaplar (40 dk)

> Not: 4. madde (marka kayıtları) mükerrer profiller silinmeden yapılırsa işe yaramaz — Google'a yine
> çelişkili sinyal gitmiş olur. Sıra önemli: önce temizlik, sonra doğrulama, sonra dış kayıtlar.
