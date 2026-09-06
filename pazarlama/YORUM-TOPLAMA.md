# Dönmar Nakliyat — Google Yorum Toplama Sistemi

Hedef: **ayda 5-8 gerçek yorum.** Üç ayda 20 yorum, yerel aramada seni rakiplerin önüne taşır.

> ## 🎯 Eşik sandığımızdan düşük — 5 Eylül 2026 SERP incelemesi
>
> `istanbul evden eve nakliyat` harita kutusundaki üç firma:
>
> | Firma | Yorum |
> |---|---|
> | Altus Evden Eve | 4,9 · 142 yorum |
> | **Pera Nakliyat** | 5,0 · **10 yorum** |
> | Eyüpoğlu Taşımacılık | 5,0 · 32 yorum |
>
> **10 yorumla İstanbul geneli harita kutusunda ikinci sıra.** Yüzlerce yorum gerekmiyor.
> İlçe seviyesinde durum daha da iyi: `esenyurt evden eve nakliyat` kutusundaki üç firmanın hiçbirinde yorum sayısı bile görünmüyor.
>
> **20-30 gerçek yorum bizi oyunun içine sokar.** Bu, 4-5 ayda ulaşılabilir bir sayı.

---

## 📍 Durum: 5 Eylül 2026

| | |
|---|---|
| Profil | ✅ oluşturuldu — **Dönmar Nakliyat** |
| Ana kategori | ✅ Evden Eve Nakliyat |
| Doğrulama | ❌ **yapılmadı** — profil "HERKESE GÖRÜNÜR DEĞİL" |
| Yorum linki | ❌ **henüz yok** |

> **Doğrulanmamış profile yorum yazılamaz.** Profil Google'da yayında olmadığı için müşteri arasa bile bulamaz, yorum kutusu açılmaz. Link de doğrulamadan sonra üretiliyor.
>
> **Yani: video doğrulaması yapılmadan yorum toplama başlayamaz.** Sıradaki tek iş bu.

### Ara çözüm: Yandex'te hemen başlayabilirsin

Yandex Business **SMS ile doğruluyor, video istemiyor.** Kaydı açtığın gün yorum toplamaya başlayabilirsin ve Yandex Haritalar Türkiye'de ciddi kullanılıyor.

👉 https://yandex.com.tr/sprav/add/

Aynı WhatsApp şablonlarını Yandex linkiyle kullanabilirsin. Google doğrulanınca ikisini paralel yürütürüz.

---

## Doğrulandığı gün: yorum linkini nereden alacaksın

Google iki farklı link veriyor, ikisi de çalışır:

**1. Kısa link (tavsiye edilen)**
İşletme Profili → **Yorum iste** butonu → çıkan adres:
```
https://g.page/r/XXXXXXXXXXXX/review
```

**2. Uzun link (kalıcı, yedek)**
```
https://search.google.com/local/writereview?placeid=XXXXXXXXXXXX
```

Hangisini alırsan al **bana ilet** — QR kartını ve sitedeki yorumlar bölümünü aynı gün üretirim. QR üreteci hazır bekliyor: `pazarlama/qr-uret.py`

---

## Profil ayarları (referans — hepsi girildi ✅)

| Alan | Değer |
|---|---|
| İşletme adı | `Dönmar Nakliyat` — sonuna kelime **ekleme**, Google ceza veriyor |
| Kategori (ana) | `Evden Eve Nakliyat` |
| Ek kategori | `Nakliye Hizmeti` |
| İşletme türü | **Hizmet bölgesi işletmesi** — adres gizli |
| Hizmet bölgesi | İstanbul |
| Telefon | `0538 861 41 10` — sitedekiyle birebir |
| Web sitesi | `https://www.dongelnakliyat.com` |
| Çalışma saatleri | Her gün 09:00 - 21:00 |

### Video doğrulaması — ilk seferde geçmek için

Hizmet bölgesi işletmelerinde artık ağırlıklı olarak video doğrulama isteniyor. Kurallar:

- **Kesintisiz, en az 30 saniye**, düzenlenmemiş
- Telefonla ve **profili yöneteceğin Google hesabıyla giriş yapmışken** çek
- Ev/ofis adresinden çekebilirsin — sokak tabelası veya çevredeki bir yapıyı göster
- Sonra **araca geç**: üzerindeki yazıyı göster, kapısını aç, içindeki ekipmanı (battaniye, streç, kayış, asansör) göster
- Araçta yazı yoksa: üniforma, fatura, vergi levhası, kartvizit gibi işletme adının geçtiği bir belge göster
- Tek çekimde bitir, kesme yapma

> **Dikkat:** Üst üste başarısız denemeden sonra "Doğrulamak için başka yol yok" ekranı çıkabiliyor ve destek hattına düşüyorsun. İlk denemeden önce yukarıdakileri hazırla, aceleye getirme.

---

## Yorum isteme akışı

```
İş biter, eşya yerleşir, ödeme alınır
        ↓
Ekip başı YÜZ YÜZE ister        ← dönüşümün %80'i burada
        ↓
Aynı anda WhatsApp'tan link gönderilir
        ↓
Cevap yoksa 3 gün sonra TEK hatırlatma
```

### Ekip başı için konuşma metni

Çıkmadan hemen önce, müşteri memnun görünüyorken:

> "**[Ad] Bey / Hanım**, geçmiş olsun, umarım her şey istediğiniz gibi oldu.
> Bir ricam olacak — biz küçük bir firmayız, reklamdan çok tavsiyeyle iş alıyoruz.
> Memnun kaldıysanız Google'a iki satır yazabilir misiniz? Şimdi linki telefonunuza atıyorum, müsait olduğunuzda bakarsınız."

Kurallar:

- **Ödeme alındıktan sonra** iste, önce değil — baskı gibi durur
- Müşteri şikâyetliyse **isteme.** Önce sorunu çöz, yorum kendiliğinden gelir
- İsterken telefonu müşterinin eline verme, kendisi yazsın
- Reddederse üsteleme, "olsun, iyi günler" deyip geç

---

## WhatsApp şablonları

`[LINK]` yerine profil açıldıktan sonra alacağın kısa yorum linkini koy.
**Linki nereden alacaksın:** Google İşletme Profili → **Yorum İste** → çıkan `g.page/r/...` adresi.

### 1. Evden eve nakliyat

> Merhaba [Ad] Bey/Hanım, bugün taşınmanızı birlikte tamamladık. Yeni evinizde mutluluklar dileriz.
>
> Hizmetimizden memnun kaldıysanız Google'a kısa bir yorum bırakmanız bizim için çok değerli. Küçük bir firmayız, her yorum bize yeni müşteri kazandırıyor.
>
> 30 saniyenizi alır: [LINK]
>
> Teşekkürler,
> Dönmar Nakliyat · 0538 861 41 10

### 2. Asansörlü taşıma

> Merhaba [Ad] Bey/Hanım, bugünkü asansörlü taşımanız tamamlandı, geçmiş olsun.
>
> Ekibimizden ve asansör çalışmasından memnun kaldıysanız Google'a birkaç satır yazar mısınız? Özellikle **hangi semtten hangi semte** taşındığınızı yazarsanız, aynı bölgedeki komşularınız bizi daha kolay buluyor.
>
> [LINK]
>
> Dönmar Nakliyat · 0538 861 41 10

### 3. Ofis taşımacılığı

> Merhaba [Ad] Bey/Hanım, ofis taşımanız tamamlandı. Yeni yerinizde bol kazanç dileriz.
>
> Süreçten memnun kaldıysanız Google'a kısa bir değerlendirme bırakmanız bizim için çok kıymetli. Kurumsal müşteriler karar verirken en çok bu yorumlara bakıyor.
>
> [LINK]
>
> Dönmar Nakliyat · 0538 861 41 10

### 4. Şehirlerarası nakliyat

> Merhaba [Ad] Bey/Hanım, eşyalarınız [Şehir] adresine teslim edildi. Geçmiş olsun.
>
> Teslimattan memnun kaldıysanız Google'a kısa bir yorum bırakır mısınız? Şehirlerarası taşımada insanlar en çok "eşyalar sağlam gitti mi" diye merak ediyor — sizin yorumunuz onlara güven veriyor.
>
> [LINK]
>
> Dönmar Nakliyat · 0538 861 41 10

### 5. Parça eşya taşıma

> Merhaba [Ad] Bey/Hanım, taşımanız tamamlandı, teşekkür ederiz.
>
> Küçük bir ricamız var: memnun kaldıysanız Google'a iki satır yorum bırakabilir misiniz? Bizim gibi küçük firmalar için bu yorumlar reklamdan daha değerli.
>
> [LINK]
>
> Dönmar Nakliyat · 0538 861 41 10

### 6. Hatırlatma (3 gün sonra, sadece bir kez)

> Merhaba [Ad] Bey/Hanım, rahatsız etmeyeyim — geçen günkü taşınmanızla ilgili yorum linkini tekrar bırakıyorum, unutulmuş olabilir diye.
>
> [LINK]
>
> Memnun kalmadığınız bir şey olduysa lütfen bana yazın, çözelim.
>
> Dönmar Nakliyat

> Son cümle önemli: memnuniyetsiz müşteriyi kamuya değil sana yönlendirir.

---

## Yasak listesi

Bunlar profili askıya aldırır veya Reklam Kurulu cezasına yol açar:

- ❌ Kendi hesaplarından veya tanıdıklardan yorum yazdırmak
- ❌ İndirim, hediye, çekiliş karşılığı yorum istemek — Google politikası ihlali
- ❌ Sadece memnun müşteriyi filtreleyip diğerlerini engellemek ("review gating")
- ❌ Yorum satın almak
- ❌ Kısa sürede çok sayıda yorum toplamak — doğal hız ayda 5-8

Sahte yorum Türkiye'de Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği kapsamında açıkça yasak. Reklam Kurulu 2026'nın ilk 7 ayında bu tür uygulamalara 218 milyon TL ceza kesti.

---

## Gelen yorumları yönet

- **Her yoruma 24 saat içinde cevap yaz.** Google bunu aktiflik sinyali sayıyor
- Cevapta semt ve hizmet adı geçir: *"Moda'daki taşınmanızda bizi tercih ettiğiniz için teşekkürler"* — arama eşleşmesine yarıyor
- Olumsuz yoruma savunmacı cevap verme. Kabul et, çözüm öner, telefon numaranı bırak. Potansiyel müşteri en çok **buna** bakıyor
- Ayda bir profile 2-3 iş fotoğrafı yükle

---

## Sırada ne var

Profil doğrulanıp yorum linkini aldığında **aynı gün** üretilecekler — hepsi hazır, sadece link bekliyor:

- [ ] **Yazdırılabilir QR kart** — araca, faturaya, müşteriye verilecek kartvizit boyutu.
      Üreteç hazır: `python3 pazarlama/qr-uret.py "https://g.page/r/.../review"`
- [ ] **Sitede müşteri yorumları bölümü** — gerçek yorumlarla dolacak, `Review` şemalı
- [ ] **Teşekkürler sayfasına yorum çağrısı** — form gönderen müşteri zaten sıcak

### ⚠️ Neden sitede şimdi yorum bölümü açmıyoruz

Boş bir "Müşteri Yorumları" sayfası ince içeriktir, faydadan çok zarar verir.
Daha önemlisi: **gerçek yorum yokken `aggregateRating` şeması eklemek yapılandırılmış veri ihlalidir** ve Google'dan manuel işlem yedirir. Yıldız işareti kazanmak için uydurma puan koymak, en hızlı ceza yollarından biri.

İlk 3-5 gerçek yorum geldiğinde ikisini de kurarız.

---

## Gerçekçi takvim

| Ay | Hedef | Toplam |
|---|---|---|
| Doğrulama ayı | 3-5 yorum | 5 |
| +1 ay | 5-8 | 12 |
| +2 ay | 5-8 | 19 |
| +3 ay | 5-8 | **25-30** |

Bu tempoda 4. ayın sonunda Pera Nakliyat'ın (10 yorum) üzerine, Eyüpoğlu'nun (32) yanına çıkarız.

**Hız sınırı önemli:** ayda 15-20 yorum doğal görünmez, Google filtreler. Yavaş ve düzenli, hızlı ve dalgalıdan iyidir.
