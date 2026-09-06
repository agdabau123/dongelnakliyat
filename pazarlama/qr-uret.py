# -*- coding: utf-8 -*-
"""
Dönmar Nakliyat — Google yorum QR kartı üreteci.

Kullanım:
    pip install qrcode pillow
    python3 qr-uret.py "https://g.page/r/XXXXXXXX/review"

Üretilenler (bu klasöre):
    yorum-qr.png       — sadece QR, 1000x1000 (dijital paylaşım için)
    yorum-karti.png    — baskıya hazır kart, 85x55 mm @ 300 dpi (kartvizit boyutu)
"""
import sys, os

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_H
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Once kur:  pip install qrcode pillow")

if len(sys.argv) < 2:
    sys.exit(__doc__)

LINK = sys.argv[1].strip()
if "g.page" not in LINK and "writereview" not in LINK:
    print("UYARI: bu bir Google yorum linkine benzemiyor ->", LINK)

BURADA = os.path.dirname(os.path.abspath(__file__))
LACI = (15, 53, 64)      # --lac
TURUNCU = (214, 122, 42)

# ---------- 1) sade QR ----------
qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=20, border=2)
qr.add_data(LINK)
qr.make(fit=True)
img = qr.make_image(fill_color=LACI, back_color="white").convert("RGB")
img = img.resize((1000, 1000), Image.LANCZOS)
img.save(os.path.join(BURADA, "yorum-qr.png"))

# ---------- 2) baskiya hazir kart ----------
# 85 x 55 mm @ 300 dpi
W, H = 1004, 650
kart = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(kart)

d.rectangle([0, 0, W, 14], fill=TURUNCU)

def yazitipi(boyut, kalin=False):
    adaylar = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if kalin
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if kalin else "C:/Windows/Fonts/arial.ttf",
    ]
    for y in adaylar:
        if os.path.exists(y):
            return ImageFont.truetype(y, boyut)
    return ImageFont.load_default()

qr_boy = 300
qr_img = img.resize((qr_boy, qr_boy), Image.LANCZOS)
kart.paste(qr_img, (W - qr_boy - 60, (H - qr_boy) // 2 + 10))

x = 60
d.text((x, 70),  "Dönmar Nakliyat", font=yazitipi(46, True), fill=LACI)
d.text((x, 140), "Memnun kaldıysanız", font=yazitipi(30), fill=(70, 100, 110))
d.text((x, 182), "iki satır yazar mısınız?", font=yazitipi(30), fill=(70, 100, 110))
d.text((x, 260), "Kodu telefonunuzun", font=yazitipi(25), fill=(120, 140, 148))
d.text((x, 296), "kamerasına tutmanız yeterli.", font=yazitipi(25), fill=(120, 140, 148))
d.text((x, 380), "0538 861 41 10", font=yazitipi(38, True), fill=TURUNCU)
d.text((x, 440), "www.dongelnakliyat.com", font=yazitipi(26), fill=(70, 100, 110))
d.text((x, 500), "Sigortalı taşıma · Yazılı sabit fiyat", font=yazitipi(22), fill=(120, 140, 148))
d.text((x, 534), "Kendi araç ve ekibimiz · Ücretsiz keşif", font=yazitipi(22), fill=(120, 140, 148))

kart.save(os.path.join(BURADA, "yorum-karti.png"), dpi=(300, 300))

print("Tamam:")
print("  ", os.path.join(BURADA, "yorum-qr.png"))
print("  ", os.path.join(BURADA, "yorum-karti.png"), "(85x55 mm, 300 dpi)")
print("Link:", LINK)
