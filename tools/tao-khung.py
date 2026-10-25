"""Tạo ảnh khung sản phẩm Việt Cường Nhân (900x900) theo kiểu phatlocnaturalfood.com.
Nền đỏ catalog, viền tròn vàng logo, tên + quy cách, huy hiệu cam kết, hotline.
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
RED_TOP, RED_BOT = (176, 30, 38), (110, 14, 20)
GOLD_A, GOLD_B = (194, 166, 50), (236, 216, 92)   # vàng logo
CREAM = (253, 246, 222)
HOTLINE = "0978 094 739"

def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def background():
    im = Image.new("RGB", (W, W))
    d = ImageDraw.Draw(im)
    for y in range(W):
        d.line([(0, y), (W, y)], fill=lerp(RED_TOP, RED_BOT, y / W))
    # vòm tối phía sau sản phẩm
    arch = Image.new("L", (W, W), 0)
    a = ImageDraw.Draw(arch)
    a.rounded_rectangle([150, 110, 750, 980], radius=300, fill=110)
    arch = arch.filter(ImageFilter.GaussianBlur(6))
    im.paste(Image.new("RGB", (W, W), (80, 8, 12)), (0, 0), arch)
    # sàn sân khấu
    fl = Image.new("L", (W, W), 0)
    ImageDraw.Draw(fl).ellipse([90, 760, 810, 900], fill=120)
    fl = fl.filter(ImageFilter.GaussianBlur(14))
    im.paste(Image.new("RGB", (W, W), (150, 22, 30)), (0, 0), fl)
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
    words, lines, cur = text.split(), [], ""
    for x in words:
        t = (cur + " " + x).strip()
        if d.textlength(t, font=f) <= w: cur = t
        else: lines.append(cur); cur = x
    lines.append(cur)
    return lines

def make(p, mark):
    im = background()
    d = ImageDraw.Draw(im)
    # nhãn gian hàng
    d.rounded_rectangle([300, 22, 600, 82], radius=14, fill=(255, 255, 255))
    m = mark.copy(); m.thumbnail((46, 46))
    im.paste(m, (318, 52 - m.height // 2), m)
    d.line([(376, 34), (376, 70)], fill=(220, 210, 200), width=2)
    d.text((392, 31), "GIAN HÀNG", font=font("Bold", 15), fill=(110, 30, 34))
    d.rounded_rectangle([390, 52, 520, 74], radius=11, fill=GOLD_A)
    d.text((455, 63), "CHÍNH HÃNG", font=font("Bold", 13), fill=(90, 20, 24), anchor="mm")
    # tên + quy cách
    name = p["name"].upper()
    f = fit_text(d, name, 780, 50)
    lines = [name] if d.textlength(name, font=f) <= 780 else wrap(d, name, 780, font("ExtraBold", 40))
    if len(lines) > 1: f = font("ExtraBold", 40)
    y = 120
    for ln in lines[:2]:
        d.text((W // 2, y), ln, font=f, fill=(255, 255, 255), anchor="mm")
        y += f.size + 8
    if p.get("spec"):
        d.text((W // 2, y + 4), p["spec"].upper(), font=font("SemiBold", 28), fill=(255, 236, 200), anchor="mm")
    # ảnh tròn viền vàng
    cy, size, thick = 540, 470, 18
    cx = 560
    src = Image.open(os.path.join(SP, p["img"])).convert("RGB")
    s = min(src.size); src = src.crop(((src.width - s) // 2, (src.height - s) // 2, (src.width + s) // 2, (src.height + s) // 2))
    inner = size - 2 * thick
    src = src.resize((inner, inner), Image.LANCZOS)
    mk = Image.new("L", (inner, inner), 0); ImageDraw.Draw(mk).ellipse([0, 0, inner - 1, inner - 1], fill=255)
    sh = Image.new("L", (W, W), 0); ImageDraw.Draw(sh).ellipse([cx - size // 2 + 6, cy - size // 2 + 22, cx + size // 2 + 6, cy + size // 2 + 22], fill=150)
    sh = sh.filter(ImageFilter.GaussianBlur(18)); im.paste(Image.new("RGB", (W, W), (40, 0, 4)), (0, 0), sh)
    im.paste(Image.new("RGB", (inner, inner), (255, 255, 255)), (cx - inner // 2, cy - inner // 2), mk)
    im.paste(src, (cx - inner // 2, cy - inner // 2), mk)
    ring, rm = gold_ring(size, thick)
    im.paste(ring, (cx - size // 2, cy - size // 2), rm)
    # huy hiệu cam kết
    bx, by, bw, bh = 40, 450, 250, 290
    d.rounded_rectangle([bx + 4, by + 8, bx + bw + 4, by + bh + 8], radius=18, fill=(70, 6, 10))
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=18, fill=CREAM, outline=GOLD_A, width=4)
    c = bx + bw // 2
    d.text((c, by + 36), "CAM KẾT", font=font("Bold", 22), fill=(110, 30, 34), anchor="mm")
    d.text((c, by + 72), "CHÍNH HÃNG", font=font("ExtraBold", 30), fill=(190, 30, 38), anchor="mm")
    for i, t in enumerate(["Chứng nhận HACCP", "Rõ nguồn gốc", "Giao toàn quốc"]):
        d.text((c, by + 118 + i * 30), t, font=font("SemiBold", 19), fill=(60, 30, 30), anchor="mm")
    d.text((c, by + 222), "Hotline", font=font("SemiBold", 18), fill=(110, 30, 34), anchor="mm")
    d.text((c, by + 254), HOTLINE, font=font("ExtraBold", 27), fill=(190, 30, 38), anchor="mm")
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
