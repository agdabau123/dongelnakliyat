# -*- coding: utf-8 -*-
import io, os, re, json, sys
from html.parser import HTMLParser
import xml.etree.ElementTree as ET

import glob as _glob
# Oturum yolu her calistirmada degistigi icin sabit yazilmaz; repo koku betigin konumundan bulunur.
B = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")
if not os.path.isdir(B):
    _c = _glob.glob("/sessions/*/mnt/dongelnakliyat/site")
    if _c: B = _c[0]
VOID = {"meta","link","img","br","hr","input","source","area","col","embed","track","wbr","base","param"}
SVG_SELF = {"path","circle","rect","line","polygon","polyline","ellipse","stop","use"}
hata = []

files = []
for r, d, fs in os.walk(B):
    for f in fs:
        if f.endswith(".html"):
            files.append(os.path.join(r, f))
files.sort()

class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.st=[]; s.bad=[]
    def handle_starttag(s,t,a):
        if t in VOID or t in SVG_SELF: return
        s.st.append(t)
    def handle_startendtag(s,t,a): pass
    def handle_endtag(s,t):
        if t in VOID or t in SVG_SELF: return
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st.pop()!=t: pass
            s.bad.append("ic-ice hatali: "+t)
        else: s.bad.append("fazladan kapanis: "+t)

sayfa_ici_anchor = {}
tum_linkler = []

for fp in files:
    rel = os.path.relpath(fp, B).replace("\\","/")
    h = io.open(fp, encoding="utf-8").read()

    # etiket dengesi
    p = P()
    try: p.feed(h)
    except Exception as e: hata.append("%s: parse hatasi %s" % (rel, e))
    if p.st: hata.append("%s: kapanmamis etiket %s" % (rel, p.st))
    if p.bad: hata.append("%s: %s" % (rel, p.bad[:3]))

    # tek H1
    n = len(re.findall(r"<h1[\s>]", h))
    if n != 1: hata.append("%s: H1 sayisi %d" % (rel, n))

    # JSON-LD
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: json.loads(m.group(1))
        except Exception as e: hata.append("%s: gecersiz JSON-LD (%s)" % (rel, e))

    # kalinti
    for kal in [u"Döngel", "donmarnakliyat"]:
        if kal in h: hata.append("%s: '%s' kalintisi" % (rel, kal))

    # anchor id envanteri
    sayfa_ici_anchor[rel] = set(re.findall(r'id="([^"]+)"', h))

    for href in re.findall(r'href="([^"]+)"', h):
        tum_linkler.append((rel, href))
    for src in re.findall(r'src="([^"]+)"', h):
        tum_linkler.append((rel, src))

BILINEN_EKSIK = {"images/ofis-tasimaciligi.jpg","images/sehirlerarasi-nakliyat.jpg","images/gida-tasimaciligi.jpg"}

def cozumle(rel, href):
    d = os.path.dirname(rel)
    return os.path.normpath(os.path.join(d, href)).replace("\\","/")

kirik = set()
for rel, href in tum_linkler:
    if href.startswith(("http","mailto:","tel:","#","data:","javascript:")): continue
    yol, _, frag = href.partition("#")
    yol = yol.split("?")[0]
    if not yol:
        continue
    hedef = cozumle(rel, yol)
    if hedef in BILINEN_EKSIK: continue
    kandidat = [hedef, hedef + ".html", hedef.rstrip("/") + "/index.html", hedef + "/index.html"]
    if hedef.endswith("/") or yol.endswith("/") or yol in ("./","../"):
        kandidat.append(hedef + "/index.html")
    var = any(os.path.exists(os.path.join(B,c)) for c in kandidat)
    if not var:
        kirik.add("%s -> %s" % (rel, href))
    elif frag:
        # hedef sayfada anchor var mi
        hp = None
        for c in kandidat:
            if os.path.exists(os.path.join(B,c)) and c.endswith(".html"):
                hp = c; break
        if hp and hp in sayfa_ici_anchor and frag not in sayfa_ici_anchor[hp]:
            kirik.add("%s -> %s (anchor yok)" % (rel, href))

# sayfa ici #anchor
for rel, href in tum_linkler:
    if href.startswith("#") and len(href) > 1:
        if href[1:] not in sayfa_ici_anchor.get(rel, set()):
            kirik.add("%s -> %s (anchor yok)" % (rel, href))

for k in sorted(kirik): hata.append("kirik link: " + k)

# ---- sitemap ----
sm = os.path.join(B, "sitemap.xml")
try:
    root = ET.parse(sm).getroot()
except Exception as e:
    hata.append("sitemap.xml gecersiz XML: %s" % e); root = None

if root is not None:
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    locs = [e.text for e in root.iter(ns+"loc")]
    smset = set()
    for l in locs:
        if not l.startswith("https://www.dongelnakliyat.com/"):
            hata.append("sitemap: www/https disi URL %s" % l)
        if l.endswith(".html"): hata.append("sitemap: .html uzantili URL %s" % l)
        path = l.replace("https://www.dongelnakliyat.com/","")
        smset.add(path if path else "index")
        f = "index.html" if path == "" else path + ".html"
        if not os.path.exists(os.path.join(B, f)):
            hata.append("sitemap: dosyasi yok -> %s" % l)
    HARIC = {"404.html","tesekkurler.html"}
    for fp in files:
        rel = os.path.relpath(fp, B).replace("\\","/")
        if rel in HARIC: continue
        key = "index" if rel == "index.html" else rel[:-5]
        if key not in smset:
            hata.append("sitemap'te yok: %s" % rel)
    print("sitemap URL:", len(locs), "| HTML dosya:", len(files))

# ---- canonical / og:url ----
for fp in files:
    rel = os.path.relpath(fp, B).replace("\\","/")
    if rel in {"404.html","tesekkurler.html"}: continue
    h = io.open(fp, encoding="utf-8").read()
    c = re.search(r'<link rel="canonical" href="([^"]+)"', h)
    o = re.search(r'<meta property="og:url" content="([^"]+)"', h)
    if not c: hata.append("%s: canonical yok" % rel); continue
    beklenen = "https://www.dongelnakliyat.com/" + ("" if rel=="index.html" else rel[:-5])
    if c.group(1).rstrip("/") != beklenen.rstrip("/"):
        hata.append("%s: canonical hatali %s" % (rel, c.group(1)))
    if o and o.group(1).rstrip("/") != beklenen.rstrip("/"):
        hata.append("%s: og:url hatali %s" % (rel, o.group(1)))

# ---- mukerrer title/meta ----
from collections import defaultdict
t_map, d_map = defaultdict(list), defaultdict(list)
for fp in files:
    rel = os.path.relpath(fp, B).replace("\\","/")
    h = io.open(fp, encoding="utf-8").read()
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
    if t: t_map[t.group(1)].append(rel)
    if d: d_map[d.group(1)].append(rel)
for k, v in t_map.items():
    if len(v) > 1: hata.append("mukerrer title (%d): %s" % (len(v), v[:3]))
for k, v in d_map.items():
    if len(v) > 1: hata.append("mukerrer meta (%d): %s" % (len(v), v[:3]))

# ---- sablon kopyalama kalintisi: yan formda yanlis ilce adi ----
ILCELER = [u"Adalar", u"Arnavutköy", u"Ataşehir", u"Avcılar", u"Bağcılar", u"Bahçelievler",
  u"Bakırköy", u"Başakşehir", u"Bayrampaşa", u"Beşiktaş", u"Beykoz", u"Beylikdüzü", u"Beyoğlu",
  u"Büyükçekmece", u"Çatalca", u"Çekmeköy", u"Esenler", u"Esenyurt", u"Eyüpsultan", u"Fatih",
  u"Gaziosmanpaşa", u"Güngören", u"Kadıköy", u"Kağıthane", u"Kartal", u"Küçükçekmece", u"Maltepe",
  u"Pendik", u"Sancaktepe", u"Sarıyer", u"Şile", u"Silivri", u"Şişli", u"Sultanbeyli",
  u"Sultangazi", u"Tuzla", u"Ümraniye", u"Üsküdar", u"Zeytinburnu"]
SLUG = {u"Arnavutköy":"arnavutkoy", u"Ataşehir":"atasehir", u"Avcılar":"avcilar",
  u"Bağcılar":"bagcilar", u"Bahçelievler":"bahcelievler", u"Bakırköy":"bakirkoy",
  u"Başakşehir":"basaksehir", u"Bayrampaşa":"bayrampasa", u"Beşiktaş":"besiktas",
  u"Beylikdüzü":"beylikduzu", u"Beyoğlu":"beyoglu", u"Büyükçekmece":"buyukcekmece",
  u"Çatalca":"catalca", u"Çekmeköy":"cekmekoy", u"Eyüpsultan":"eyupsultan",
  u"Gaziosmanpaşa":"gaziosmanpasa", u"Güngören":"gungoren", u"Kadıköy":"kadikoy",
  u"Kağıthane":"kagithane", u"Küçükçekmece":"kucukcekmece", u"Sarıyer":"sariyer",
  u"Şile":"sile", u"Şişli":"sisli", u"Ümraniye":"umraniye", u"Üsküdar":"uskudar"}
for fp in files:
    rel = os.path.relpath(fp, B).replace("\\", "/")
    h = io.open(fp, encoding="utf-8").read()
    m = re.search(r'<div class="teklif">\s*<h3>.*?</svg>\s*(.*?)</h3>', h, re.S)
    if not m: continue
    baslik = m.group(1)
    for ad in ILCELER:
        if ad in baslik:
            slug = SLUG.get(ad, ad.lower())
            if slug not in rel:
                hata.append("%s: yan formda yanlis ilce adi '%s' (sablon kopyalama kalintisi)" % (rel, ad))
            break

# ---- _redirects + yasak dosyalar ----
if not os.path.exists(os.path.join(B,"_redirects")): hata.append("_redirects dosyasi YOK")
for pref in ("ofis-tasimaciligi-","parca-esya-tasima-","sehirlerarasi-nakliyat-"):
    bad = [f for f in os.listdir(B) if f.startswith(pref) and f.endswith(".html")]
    if bad: hata.append("olmamasi gereken dosyalar: %s" % bad[:5])

print("\n=== SONUC ===")
if hata:
    print("HATA SAYISI:", len(hata))
    for x in hata[:60]: print(" -", x)
    sys.exit(1)
print("TEMIZ - hata yok")
