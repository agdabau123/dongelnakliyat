# Döngel Nakliyat

İstanbul geneli nakliyat ve lojistik web sitesi — https://www.dongelnakliyat.com

## Yapı
- `site/` — yayınlanan statik site (Cloudflare Pages çıktı klasörü)
  - 257 sayfa: 39 ilçe, 6 hizmet, 195 hizmet×ilçe kombinasyonu, blog, kurumsal sayfalar
  - `images/` — görseller
  - `sitemap.xml`, `robots.txt` — teknik SEO

## Yayınlama
`site` klasöründeki değişiklikler main dalına push edildiğinde Cloudflare Pages otomatik yayınlar.
