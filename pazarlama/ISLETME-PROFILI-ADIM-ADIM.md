# İşletme Profili — Adım Adım Temizlik ve Düzeltme

Hazırlanma: 10 Eylül 2026 · Süre: 15-20 dk (video doğrulaması hariç)

Bu dosyayı 10 Eylül'de panelinde gezip **kendi ekranından** hazırladım. Aşağıdaki her şeyi
orada bizzat gördüm, tahmin yok.

---

## Neden yapıyoruz

Panelinde **tek profil değil, dört profil** var. Dördü de doğrulanmamış (%0 doğrulandı).
Google bir markayı, aynı bilgiyi tutarlı gördüğünde tanıyor. Burada tam tersi var: dört kayıt,
dört farklı isim ve kategori. Search Console'da marka aramasında **0 gösterimimiz** olmasının
muhtemel sebebi bu.

Yanlış olanı doğrulamamak için önce temizlik, sonra doğrulama.

---

# BÖLÜM 1 — Hangisi silinecek, hangisi kalacak

👉 https://business.google.com/locations

Karşına **4 satırlık bir liste** çıkacak. İsimler birbirine benziyor, bu yüzden
**işletme adına değil, soldaki "Mağaza kodu" sütununa bak.** Karıştırma ihtimalini sıfırlar.

| Mağaza kodu | İşletme adı | Bölge | NE YAPACAKSIN |
|---|---|---|---|
| `05219574286274898789` | Döngel Nakliyat | İstanbul | 🔴 **SİL** |
| `01139537662710523817` | DönmarNakliyat | Bursa, Düzce +8 | 🔴 **SİL** |
| `13508379437280358707` | Dönmar Nakliyat | İstanbul | 🟢 **TUT — buna dokunma** |
| `17175691592224202295` | Dönmar Nakliyat | İstanbul | 🔴 **SİL** |

### Neden `13508379437280358707` kalıyor

Bu profili tek tek açıp içine baktım. Doğru olan bu:

| | Bu profilde | Olması gereken |
|---|---|---|
| İsim | Dönmar Nakliyat | ✅ doğru |
| **Kategori** | **Evden Eve Nakliyat** | ✅ doğru — hedef kelimemizle birebir |
| Hizmet bölgesi | İstanbul, Türkiye | ✅ doğru |
| Telefon | 0538 861 41 10 | ✅ doğru |
| Web sitesi | https://www.dongelnakliyat.com/ | ✅ doğru |
| Çalışma saati | 09:00-**21:30** | ⚠️ sitede 21:00 yazıyor, düzeltilecek |

Diğer üçünde ya isim yanlış (Döngel / bitişik yazılmış DönmarNakliyat), ya bölge yanlış (Bursa-Düzce),
ya da kategori zayıf (Nakliyat Şirketi).

---

# BÖLÜM 2 — Silme işlemi (satır satır)

Üç kaydı **tek tek** sileceksin. Aynı anda birden fazlasını seçme, karıştırma riski var.

### Adım 1
Silinecek satırın **en solundaki kutucuğu** işaretle. (Mağaza kodunun solunda.)

### Adım 2
Kutucuğu işaretler işaretlemez üstte **mavi bir şerit** belirir:
`1 işletme seçildi` yazar, sağ tarafında **"İşlem"** diye bir düğme vardır.

### Adım 3
**"İşlem"** düğmesine bas. Açılan menüde şunlar çıkar:

```
İndir:
   İşletme Girişleri
   Analizler

Google güncellemeleri:
   Kabul et
   Sil              ← ❌ BU DEĞİL
İşletmeyi aktar

Şu şekilde işaretle:
   Açık
   Geçici olarak kapalı
   Tamamen kapalı    ← ❌ BU DA DEĞİL

İşletmeyi kaldır     ← ✅ BU
```

### Adım 4
**En alttaki "İşletmeyi kaldır"** seçeneğine bas. Onay isterse onayla.

### Adım 5
Diğer iki kayıt için 1-4 arasını tekrarla.

## ⚠️ İki tuzak — buraya dikkat

**1. "Sil" ile "İşletmeyi kaldır" aynı şey değil.**
Menünün ortasındaki **"Sil"**, *Google güncellemeleri* başlığının altında ve Google'ın önerdiği
değişiklikleri reddetmeye yarıyor. İşletmeyi silmiyor. Sen **en alttaki "İşletmeyi kaldır"**ı istiyorsun.

**2. "Tamamen kapalı" işaretleme.**
Bu, işletmeyi silmiyor — "bu firma kapandı" diye etiketliyor. Google'da "KALICI OLARAK KAPALI"
yazısıyla görünür kalır ki bu istediğimizin tam tersi. Kullanma.

## Yanlışlıkla `13508379437280358707`'yi silersen

Silme geri alınamıyor. O yüzden **her seferinde mağaza kodunu okuyup öyle işaretle.**
Yine de olursa panikleme, haber ver — kalan profillerden birini düzeltip devam ederiz,
sadece birkaç dakika kaybederiz.

---

# BÖLÜM 3 — Kalan profilin saatini düzelt (2 dk)

Silme bitince listede tek kayıt kalacak: `13508379437280358707`.

### Adım 1
Listeden o kaydın **adına** tıkla. Profil ekranı açılır.

### Adım 2
Üstte bir sıra ikon göreceksin:
`Profili düzenle` · `Yorumları oku` · `Fotoğraflar` · `Duyurular` · `Performans` · `Reklam verin`

**En soldaki "Profili düzenle"** (kalem ikonu) üzerine bas.

### Adım 3
Açılan pencerede **"Çalışma saatleri"** bölümünü bul.

### Adım 4
Kapanış saatini **21:30 → 21:00** yap. Pazartesi'den Pazar'a **yedi günün hepsi** aynı olmalı:

```
Her gün: 09:00 - 21:00
```

### Adım 5
**Kaydet.**

> Neden önemli: Google yerel sıralamada bilgi tutarlılığına bakıyor. Sitede 09:00-21:00,
> profilde 09:00-21:30 yazması küçük ama gereksiz bir çelişki. Sitedeki saati değiştirme —
> 158 sayfada ve şemada 21:00 yazıyor, doğru olan o.

---

# BÖLÜM 4 — Video doğrulaması (ofiste, araç yanında)

Temizlik bitmeden buna başlama. Yanlış profili doğrularsan geri almak çok daha zor.

Profil ekranında kırmızı uyarı ve **"Doğrulama yapın"** düğmesi var. Ona bastığında Google
doğrulama yöntemini soracak; hizmet bölgesi işletmelerinde genelde **video** istiyor.

## Kurallar

- **Kesintisiz** çek, **en az 30 saniye**
- Hiç durdurma, hiç kesme, hiç düzenleme yok — beğenmezsen baştan çek
- Telefonla ve **profili açtığın Google hesabıyla giriş yapmışken** çek

## Çekim sırası — bu sırayla yürü, kamerayı hiç durdurma

1. **Dışarıyı göster** — sokak, tabela, çevredeki bir bina
   *(Google konumu buradan anlıyor, atlama)*
2. **Yürüyerek araca git** — kesme yapma, yürürken çekmeye devam et
3. **Aracın dışını göster** — üzerinde firma yazısı varsa yakın çek
4. **Araç kapısını aç, içini göster** — battaniye, streç, koli, kayış, ambalaj malzemesi
5. **Sonunda vergi levhasını** veya üzerinde işletme adı geçen bir belgeyi kameraya tut

**Araçta firma yazısı yoksa:** üniforma, fatura, kartvizit veya vergi levhası mutlaka net görünsün.
İşletme adının fiziksel bir kanıtı ekranda olmalı.

> ⚠️ Üst üste başarısız denemeden sonra Google "başka doğrulama yolu yok" deyip destek hattına
> yönlendiriyor ve süreç haftalara yayılıyor. **İlk denemeyi aceleye getirme.** Yukarıdaki beş adımı
> kafanda bir kez prova et, sonra kaydı başlat.

Sonuç genelde birkaç gün içinde e-postayla geliyor.

---

# BÖLÜM 5 — Onaylandıktan sonra bana ne göndereceksin

Profil → **Yorum iste** → çıkan `g.page/r/...` linkini kopyala, bana at.

O linkle şunları ben hazırlarım:
- Müşteriye atılacak WhatsApp yorum isteme şablonu
- Araçta ve kartvizitte kullanılacak QR kartı
- Sitedeki yorumlar bölümü

> ❌ **Sahte yorum, tanıdıktan yorum, indirim karşılığı yorum yok.** Google bunları yakalıyor ve
> profili askıya alıyor; geri almak aylar sürüyor. Gerçek müşteriden gerçek yorum, başka yolu yok.

---

# Özet — sırayla

1. ⬜ `05219574286274898789` (Döngel Nakliyat) → İşletmeyi kaldır
2. ⬜ `01139537662710523817` (DönmarNakliyat, Bursa) → İşletmeyi kaldır
3. ⬜ `17175691592224202295` (Dönmar Nakliyat) → İşletmeyi kaldır
4. ⬜ `13508379437280358707` → çalışma saati 21:30 → **21:00**
5. ⬜ Aynı profil için video doğrulaması
6. ⬜ Onay gelince yorum linkini bana at

Takıldığın adımda ekran görüntüsü at, oradan devam ederiz.
