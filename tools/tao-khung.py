"""Tạo ảnh khung sản phẩm Việt Cường Nhân (900x900) theo kiểu phatlocnaturalfood.com.
Nền vàng logo, chữ và viền tròn xanh logo, tên + quy cách, huy hiệu cam kết, hotline.
Chạy: python3 tools/tao-khung.py sp.json   (sp.json: [{id,name,spec,img}])
Ghi ra images/san-pham/khung/<id>.jpg và images/san-pham/nho/khung/<id>.webp
"""
import json, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SP = os.path.join(ROOT, "images", "san-pham")
F = "/usr/share/fonts/opentype/inter/"
def font(w, s): return ImageFont.truetype(F + f"Inter-{w}.otf", s)

W = 900
RED_TOP, RED_BOT = (247, 226, 120), (214, 172, 58)   # nền vàng logo
GOLD_A, GOLD_B = (42, 82, 169), (72, 143, 211)   # viền tròn xanh logo   # vàng logo
CREAM = (253, 246, 222)
HOTLINE = "0978 094 739"
TITLE = (42, 82, 169)   # xanh logo #2a52a9
BLUE_D = (24, 52, 120)   # vàng logo sáng cho tên sản phẩm

def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def background():
    im = Image.new("RGB", (W, W))
    d = ImageDraw.Draw(im)
    for y in range(W):
        d.line([(0, y), (W, y)], fill=lerp(RED_TOP, RED_BOT, y / W))
    # vòm tối phía sau sản phẩm
    arch = Image.new("L", (W, W), 0)
    a = ImageDraw.Draw(arch)
    a.rounded_rectangle([150, 110, 750, 980], radius=300, fill=90)
    arch = arch.filter(ImageFilter.GaussianBlur(6))
    im.paste(Image.new("RGB", (W, W), (200, 150, 40)), (0, 0), arch)
    # sàn sân khấu
    fl = Image.new("L", (W, W), 0)
    ImageDraw.Draw(fl).ellipse([90, 760, 810, 900], fill=120)
    fl = fl.filter(ImageFilter.GaussianBlur(14))
    im.paste(Image.new("RGB", (W, W), (190, 140, 36)), (0, 0), fl)
    return im

def gold_ring(size, thick):
    ring = Image.new("RGB", (size, size))
    d = ImageDraw.Draw(ring)
    for y in range(size):
        d.line([(0, y), (size, y)], fill=lerp(GOLD_B, GOLD_A, y / size))
    m = Image.new("L", (size, size), 0)
    md = ImageDraw.Draw(m)
    md.ellipse([0, 0, size - 1, size - 1], fill=255)
    md.ellipse([thick, thick, size - 1 - thick, size - 1 - thick], fill=0)
    return ring, m

def fit_text(d, text, w, start, weight="ExtraBold", minsize=30):
    s = start
    while s > minsize and d.textlength(text, font=font(weight, s)) > w:
        s -= 2
    return font(weight, s)

def wrap(d, text, w, f):
    # chia 2 dòng cân nhau
    words = text.split()
    best = None
    for i in range(1, len(words)):
        l1, l2 = " ".join(words[:i]), " ".join(words[i:])
        m = max(d.textlength(l1, font=f), d.textlength(l2, font=f))
        if best is None or m < best[0]: best = (m, [l1, l2])
    return best[1] if best else [text]

def make(p, mark):
    im = background()
    d = ImageDraw.Draw(im)
    # nhãn gian hàng
    d.rounded_rectangle([300, 22, 600, 82], radius=14, fill=(255, 255, 255))
    m = mark.copy(); m.thumbnail((46, 46))
    im.paste(m, (318, 52 - m.height // 2), m)
    d.line([(376, 34), (376, 70)], fill=(220, 210, 200), width=2)
    d.text((392, 31), "GIAN HÀNG", font=font("Bold", 15), fill=BLUE_D)
    d.rounded_rectangle([390, 52, 520, 74], radius=11, fill=(214, 172, 58))
    d.text((455, 63), "CHÍNH HÃNG", font=font("Bold", 13), fill=BLUE_D, anchor="mm")
    # tên + quy cách
    name = p["name"].upper()
    f = fit_text(d, name, 820, 62)
    lines = [name] if f.size >= 44 else wrap(d, name, 820, font("ExtraBold", 50))
    if len(lines) > 1:
        f = font("ExtraBold", 50)
        while max(d.textlength(l, font=f) for l in lines) > 820: f = font("ExtraBold", f.size - 2)
    y = 128
    for ln in lines[:2]:
        d.text((W // 2 + 2, y + 3), ln, font=f, fill=(255, 246, 210), anchor="mm")
        d.text((W // 2, y), ln, font=f, fill=TITLE, anchor="mm")
        y += f.size + 8
    if p.get("spec"):
        d.text((W // 2, y + 4), p["spec"].upper(), font=font("Bold", 30), fill=BLUE_D, anchor="mm")
    # ảnh tròn viền vàng
    cy, size, thick = 540, 470, 18
    cx = 560
    src = Image.open(os.path.join(SP, p["img"])).convert("RGB")
    s = min(src.size); src = src.crop(((src.width - s) // 2, (src.height - s) // 2, (src.width + s) // 2, (src.height + s) // 2))
    inner = size - 2 * thick
    src = src.resize((inner, inner), Image.LANCZOS)
    mk = Image.new("L", (inner, inner), 0); ImageDraw.Draw(mk).ellipse([0, 0, inner - 1, inner - 1], fill=255)
    sh = Image.new("L", (W, W), 0); ImageDraw.Draw(sh).ellipse([cx - size // 2 + 6, cy - size // 2 + 22, cx + size // 2 + 6, cy + size // 2 + 22], fill=150)
    sh = sh.filter(ImageFilter.GaussianBlur(18)); im.paste(Image.new("RGB", (W, W), (120, 80, 10)), (0, 0), sh)
    im.paste(Image.new("RGB", (inner, inner), (255, 255, 255)), (cx - inner // 2, cy - inner // 2), mk)
    im.paste(src, (cx - inner // 2, cy - inner // 2), mk)
    ring, rm = gold_ring(size, thick)
    im.paste(ring, (cx - size // 2, cy - size // 2), rm)
    # huy hiệu cam kết
    bx, by, bw, bh = 40, 450, 250, 290
    d.rounded_rectangle([bx + 4, by + 8, bx + bw + 4, by + bh + 8], radius=18, fill=(150, 105, 25))
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=18, fill=CREAM, outline=GOLD_A, width=4)
    c = bx + bw // 2
    d.text((c, by + 36), "CAM KẾT", font=font("Bold", 22), fill=BLUE_D, anchor="mm")
    d.text((c, by + 72), "CHÍNH HÃNG", font=font("ExtraBold", 30), fill=TITLE, anchor="mm")
    for i, t in enumerate(["Chứng nhận HACCP", "Rõ nguồn gốc", "Giao toàn quốc"]):
        d.text((c, by + 118 + i * 30), t, font=font("SemiBold", 19), fill=BLUE_D, anchor="mm")
    d.text((c, by + 222), "Hotline", font=font("SemiBold", 18), fill=BLUE_D, anchor="mm")
    d.text((c, by + 254), HOTLINE, font=font("ExtraBold", 27), fill=TITLE, anchor="mm")
    return im

def main():
    items = json.load(open(sys.argv[1], encoding="utf-8"))
    mark = Image.open(os.path.join(ROOT, "mark.png")).convert("RGBA")
    os.makedirs(os.path.join(SP, "khung"), exist_ok=True)
    os.makedirs(os.path.join(SP, "nho", "khung"), exist_ok=True)
    n = 0
    for p in items:
        if not p.get("img"): continue
        im = make(p, mark)
        im.save(os.path.join(SP, "khung", f"{p['id']}.webp"), "WEBP", quality=82)
        t = im.resize((480, 480), Image.LANCZOS)
        t.save(os.path.join(SP, "nho", "khung", f"{p['id']}.webp"), "WEBP", quality=78)
        n += 1
    print("đã tạo", n, "khung")

if __name__ == "__main__":
    main()
