"""Sinh các trang con dùng chung giao diện trang chủ: /gioi-thieu/ và /kien-thuc/.
Lấy CSS, header, footer, nút nổi từ index.html nên đổi giao diện trang chủ rồi chạy lại là đồng bộ.
Chạy: python3 tools/trang_con.py
- Nội dung Giới thiệu: tools/gioi-thieu-noi-dung.html
- Bài kiến thức: tools/bai_viet.py (danh sách BAI)
"""
import os, re, json, datetime, html as H
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
SITE = "https://vietcuongnhan.com"
IDX = open(R + "index.html", encoding="utf-8").read()
# Mã đo lường (GA4, Meta Pixel) lấy từ trang chủ để mọi trang con dùng chung.
TRACK = IDX[IDX.index("<!-- Google tag"):IDX.index("<!-- /tracking -->")]  # GA4 + Meta Pixel
# Đếm lượt bấm Zalo / gọi điện trên trang con (trang chủ có sẵn đoạn này).
CLICK = '''<script>document.addEventListener("click", e => { const a = e.target.closest(\'a[href*="zalo.me"], a[href^="tel:"]\'); if (a) { try { gtag("event", a.href.includes("zalo") ? "click_zalo" : "click_call"); } catch {} try { fbq("track", "Contact"); } catch {} } });</script>'''

def cut(a, b, s=IDX, keep_b=True):
    i = s.index(a); j = s.index(b, i)
    return s[i:j + (len(b) if keep_b else 0)]

STYLE1 = cut("<style>body{margin:0}", "</style>")
FONTS = cut('<link rel="preconnect" href="https://fonts.googleapis.com">', 'display=swap">')
STYLE2 = IDX[IDX.index("<style>", IDX.index(FONTS)):]
STYLE2 = STYLE2[:STYLE2.index("</style>") + 8]
FOOTER = cut("<footer>", "</footer>")
FAB = cut('<div class="fab"', "</div>")
EXTRA_CSS = """<style>
.intro { padding-block: 44px 16px; display: grid; gap: 10px; }
.intro h1 { font-size: clamp(32px, 5.5vw, 48px); color: var(--emerald-2); }
.intro p { margin: 0; color: var(--muted); max-width: 64ch; }
.kchips { display: flex; flex-wrap: wrap; gap: 8px; padding-block: 8px 22px; }
.kchips .chip[aria-pressed="true"] { background: var(--emerald-2); border-color: var(--emerald-2); color: #fff; }
.posts { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 18px; padding-block: 0 56px; }
.post { display: grid; gap: 8px; align-content: start; text-decoration: none; color: inherit; background: var(--paper); border: 1px solid var(--line); border-top: 3px solid var(--logo-gold); border-radius: 12px; padding: 18px; }
.post h2 { font-size: 20px; color: var(--ink); }
.post p { margin: 0; color: var(--muted); font-size: 14px; }
.post .more { color: var(--emerald-2); font-weight: 700; font-size: 14px; }
.post:hover { border-color: var(--logo-gold); box-shadow: 0 10px 24px rgb(168 29 36 / .1); }
.article { max-width: 760px; margin: 0 auto; padding: 36px 20px 56px; }
.article .crumb { font-size: 13px; color: var(--muted); margin: 0 0 14px; }
.article .crumb a { color: var(--emerald-2); }
.article h1 { font-size: clamp(28px, 5vw, 42px); color: var(--emerald-2); margin-block: 6px 12px; }
.article .lede { font-size: 17px; color: var(--muted); margin: 0 0 24px; }
.article h2 { font-size: 24px; margin: 30px 0 10px; color: var(--ink); }
.article h3 { font-size: 18px; margin: 20px 0 6px; color: var(--emerald-2); }
.article p, .article li { max-width: 68ch; }
.article ol, .article ul { padding-left: 22px; display: grid; gap: 6px; }
.article a { color: var(--emerald-2); }
.article .note { border-left: 3px solid var(--logo-gold); background: var(--paper); padding: 14px 18px; border-radius: 0 10px 10px 0; color: var(--muted); font-size: 14px; margin-top: 30px; }
.article .tldr { background: var(--paper); border: 1px solid var(--line); border-radius: 12px; padding: 14px 18px; margin: 0 0 22px; }
.article .tldr b { color: var(--emerald-2); }
.article .tldr ul { margin: 8px 0 0; }
.article .meta { font-size: 13px; color: var(--muted); margin: -14px 0 20px; }
.article .cta { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 26px; }
.article table { width: 100%; border-collapse: collapse; margin: 14px 0; font-size: 14px; background: var(--paper); border: 1px solid var(--line); }
.article th, .article td { text-align: left; padding: 9px 12px; border-top: 1px solid var(--line); vertical-align: top; }
.article td.num { text-align: right; white-space: nowrap; }
.eyebrow { font-size: 12px; letter-spacing: .14em; text-transform: uppercase; color: var(--gold); font-weight: 700; margin: 0; }
</style>"""

def header(active):
    items = [("../gioi-thieu/", "Giới thiệu", "gt"), ("../#san-pham", "Sản phẩm", ""), ("../chung-nhan/", "Chứng nhận &amp; Cam kết", "cn"),
             ("../kien-thuc/", "Kiến thức", "kt")]
    nav = "\n".join(f'      <a href="{h}"{" aria-current=\"page\"" if k == active and k else ""}>{t}</a>' for h, t, k in items)
    return f'''<header class="top">
  <div class="wrap">
    <a class="brand" href="../" aria-label="Việt Cường Nhân">
      <span class="mark"><img src="../mark.png" alt=""></span>
      <span><b>VIỆT CƯỜNG NHÂN</b><small>Excellence in Every Product</small></span>
    </a>
    <nav class="menu" id="menu" aria-label="Chính" onclick="if(event.target.closest('a')){{const h=this.closest('header');h.classList.remove('open');h.querySelector('.nav-t').setAttribute('aria-expanded','false')}}">
{nav}
    </nav>
    <button type="button" class="nav-t" aria-label="Mở menu" aria-expanded="false" aria-controls="menu" onclick="const h=this.closest('header');this.setAttribute('aria-expanded',h.classList.toggle('open'))"><span></span><span></span><span></span></button>
    <a class="btn btn-line" href="../#dat-hang">Liên hệ</a>
  </div>
</header>'''

def shell(path, title, desc, active, body, ld=None, og="website", script=""):
    url = f"{SITE}/{path}"
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (ld or []))
    return f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
{TRACK}<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{H.escape(title)} | Việt Cường Nhân</title>
<meta name="description" content="{H.escape(desc)}">
<link rel="canonical" href="{url}">
<link rel="icon" href="../mark.png">
<meta property="og:type" content="{og}">
<meta property="og:title" content="{H.escape(title)}">
<meta property="og:description" content="{H.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/logo.png">
{lds}{STYLE1}
{FONTS}
{STYLE2}
{EXTRA_CSS}
</head>
<body>
{header(active)}

{body}

{FOOTER}

{FAB}
{CLICK}
{script}
</body>
</html>
'''

LB = '''<dialog class="lb" id="lb" aria-label="Ảnh">
  <img id="lb-img" alt="">
  <div class="bar"><span id="lb-n"></span><button type="button" id="lb-x">Đóng</button></div>
</dialog>
<script>
const lb = document.getElementById("lb"), im = document.getElementById("lb-img");
document.addEventListener("click", e => { const b = e.target.closest("[data-doc]"); if (!b) return;
  const img = b.querySelector("img"); im.src = img.src.replace("/nho-", "/"); im.alt = img.alt; document.getElementById("lb-n").textContent = img.alt; lb.showModal(); });
document.getElementById("lb-x").onclick = () => lb.close();
lb.addEventListener("click", e => { if (e.target === lb) lb.close(); });
</script>'''

# Lightbox nhiều trang cho giấy chứng nhận và bản tự công bố (bấm Trước/Sau để lật trang).
LB_DOCS = '''<dialog class="lb" id="lb" aria-label="Giấy tờ">
  <img id="lb-img" alt="">
  <div class="bar"><button type="button" id="lb-prev">Trước</button><span id="lb-n"></span><button type="button" id="lb-next">Sau</button><button type="button" id="lb-x">Đóng</button></div>
</dialog>
<script>
const pages = (n, c, t) => Array.from({length: c}, (_, i) => [`../ho-so/trang/${n}-${i + 1}.jpg`, `${t} (trang ${i + 1}/${c})`]);
const DOCS = {
  haccp: [["../ho-so/haccp-vn.jpg", "Chứng nhận HACCP, GKVN-0387-HC (tiếng Việt)"], ["../ho-so/haccp.jpg", "HACCP certificate, GKVN-0387-HC (English)"]],
  iso: [["../ho-so/iso22000-vn.jpg", "Chứng nhận ISO 22000:2018, GKVN-0387-FC (tiếng Việt)"], ["../ho-so/iso22000.jpg", "ISO 22000:2018 certificate, GKVN-0387-FC (English)"]],
  gmp: [["../ho-so/gmp.jpg", "Chứng nhận GMP, GKVN-0387-GMP"]],
  "yen-tho": pages("yen-tho", 5, "Bản tự công bố Tổ yến thô"),
  "yen-tinh-che": pages("yen-tinh-che", 5, "Bản tự công bố Tổ yến tinh chế"),
  "dong-trung": pages("dong-trung", 7, "Bản tự công bố Nấm đông trùng hạ thảo")
};
const lb = document.getElementById("lb"), lbImg = document.getElementById("lb-img"), prev = document.getElementById("lb-prev"), next = document.getElementById("lb-next");
let gal = [], gi = 0;
function lbShow() { lbImg.src = gal[gi][0]; lbImg.alt = gal[gi][1]; document.getElementById("lb-n").textContent = gal.length > 1 && !/trang \\d/.test(gal[gi][1]) ? `${gal[gi][1]} · ${gi + 1}/${gal.length}` : gal[gi][1]; prev.hidden = next.hidden = gal.length < 2; }
document.addEventListener("click", e => { const d = e.target.closest("[data-doc]"); if (d && DOCS[d.dataset.doc]) { gal = DOCS[d.dataset.doc]; gi = 0; lbShow(); lb.showModal(); } });
prev.onclick = () => { gi = (gi + gal.length - 1) % gal.length; lbShow(); };
next.onclick = () => { gi = (gi + 1) % gal.length; lbShow(); };
document.getElementById("lb-x").onclick = () => lb.close();
lb.addEventListener("click", e => { if (e.target === lb) lb.close(); });
</script>'''

def gioi_thieu():
    c = open(R + "tools/gioi-thieu-noi-dung.html", encoding="utf-8").read()
    c = c.replace('src="images/', 'src="../images/')
    c = c.replace('<div class="head"><div><div class="eyebrow">Về chúng tôi</div><h2>Giới thiệu Việt Cường Nhân</h2></div></div>',
                  '<div class="head"><div><div class="eyebrow">Về chúng tôi</div><h1 style="font-size:clamp(32px,5.5vw,48px);color:var(--emerald-2)">Giới thiệu Việt Cường Nhân</h1></div></div>')
    c += '''
<section class="block" style="padding-top:0">
  <div class="wrap" style="display:flex;flex-wrap:wrap;gap:10px">
    <a class="btn btn-gold" href="../#san-pham">Xem bảng giá sản phẩm</a>
    <a class="btn btn-line" href="../chung-nhan/">Xem chứng nhận HACCP, ISO 22000, GMP</a>
    <a class="btn btn-line" href="https://zalo.me/0978094739" target="_blank" rel="noopener">Nhắn Zalo 0978 094 739</a>
  </div>
</section>'''
    ld = [{"@context": "https://schema.org", "@type": "AboutPage", "name": "Giới thiệu Việt Cường Nhân", "url": f"{SITE}/gioi-thieu/",
           "about": {"@type": "Organization", "name": "Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân", "foundingDate": "2009-06",
                     "url": SITE, "telephone": "+84978094739", "logo": f"{SITE}/logo.png"}}]
    os.makedirs(R + "gioi-thieu", exist_ok=True)
    open(R + "gioi-thieu/index.html", "w", encoding="utf-8").write(shell(
        "gioi-thieu/", "Giới thiệu công ty", "Việt Cường Nhân thành lập năm 2009: nhà yến, xưởng nhặt lông, xưởng tinh chế, nhà máy nước yến chưng, trang trại đông trùng hạ thảo và nha đam. Đạt HACCP, ISO 22000, GMP.",
        "gt", c, ld, script=LB))

def kien_thuc():
    import importlib.util
    spec = importlib.util.spec_from_file_location("bai_viet", R + "tools/bai_viet.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    os.makedirs(R + "kien-thuc", exist_ok=True)
    cats = []
    for b in m.BAI:
        if b["cat"] not in cats: cats.append(b["cat"])
        body = b["body"]
        lds = [{"@context": "https://schema.org", "@type": "Article", "headline": b["h1"], "description": b["desc"],
                "datePublished": b["ngay"], "dateModified": b.get("sua", b["ngay"]), "inLanguage": "vi",
                "keywords": b.get("tu_khoa", ""),
                "author": {"@type": "Organization", "name": "Việt Cường Nhân"},
                "publisher": {"@type": "Organization", "name": "Việt Cường Nhân", "logo": {"@type": "ImageObject", "url": f"{SITE}/logo.png"}},
                "mainEntityOfPage": f"{SITE}/kien-thuc/{b['slug']}.html"}]
        if b.get("faq"):
            lds.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in b["faq"]]})
            body += "\n  <h2>Câu hỏi thường gặp</h2>\n" + "\n".join(f"  <h3>{q}</h3>\n  <p>{a}</p>" for q, a in b["faq"])
        tldr = ("  <div class=\"tldr\"><b>Tóm tắt nhanh</b>\n  <ul>\n" + "\n".join(f"    <li>{t}</li>" for t in b["tom_tat"]) + "\n  </ul></div>\n") if b.get("tom_tat") else ""
        art = f'''<main class="article">
  <p class="crumb"><a href="./">Kiến thức</a> / {b["cat"]}</p>
  <p class="eyebrow">{b["cat"]}</p>
  <h1>{b["h1"]}</h1>
  <p class="lede">{b["lede"]}</p>
  <p class="meta">Việt Cường Nhân · Đăng {"/".join(reversed(b["ngay"].split("-")))}</p>
{tldr}{body}
  <p class="note">Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh. Người đang mang thai, có bệnh nền hoặc đang dùng thuốc nên hỏi ý kiến bác sĩ trước khi dùng.</p>
  <div class="cta">
    <a class="btn btn-gold" href="../#san-pham">Xem bảng giá</a>
    <a class="btn btn-line" href="https://zalo.me/0978094739" target="_blank" rel="noopener">Nhắn Zalo tư vấn</a>
    <a class="btn btn-line" href="./">Xem bài khác</a>
  </div>
</main>'''
        open(R + f"kien-thuc/{b['slug']}.html", "w", encoding="utf-8").write(
            shell(f"kien-thuc/{b['slug']}.html", b["h1"], b["desc"], "kt", art, lds, og="article"))
    slug = lambda c: re.sub(r"[^a-z0-9]+", "-", c.lower().translate(str.maketrans("àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ",
        "aaaaaaaaaaaaaaaaaeeeeeeeeeeeiiiiiooooooooooooooooouuuuuuuuuuuyyyyyd"))).strip("-")
    chips = '    <button class="chip" type="button" aria-pressed="true" data-cat="all">Tất cả</button>\n' + "\n".join(
        f'    <button class="chip" type="button" aria-pressed="false" data-cat="{slug(c)}">{c}</button>' for c in cats)
    posts = "\n".join(f'''    <a class="post" href="{b["slug"]}.html" data-cat="{slug(b["cat"])}">
      <span class="eyebrow">{b["cat"]}</span>
      <h2>{b["h1"]}</h2>
      <p>{b["desc"]}</p>
      <span class="more">Đọc bài →</span>
    </a>''' for b in reversed(m.BAI))
    body = f'''<main class="wrap">
  <div class="intro">
    <p class="eyebrow">Kiến thức</p>
    <h1>Góc kiến thức Việt Cường Nhân</h1>
    <p>Cách chọn, sơ chế, chưng và bảo quản yến sào, nước yến, đông trùng hạ thảo, táo đỏ, viết từ kinh nghiệm của xưởng yến và nhà máy Việt Cường Nhân.</p>
  </div>
  <div class="kchips" role="group" aria-label="Chuyên mục">
{chips}
  </div>
  <div class="posts" id="posts">
{posts}
  </div>
</main>'''
    script = '''<script>
const chips = document.querySelectorAll(".kchips .chip"), posts = document.querySelectorAll(".post");
function show(cat) { posts.forEach(p => p.hidden = !(cat === "all" || p.dataset.cat === cat)); chips.forEach(c => c.setAttribute("aria-pressed", String(c.dataset.cat === cat))); }
chips.forEach(c => c.addEventListener("click", () => { show(c.dataset.cat); history.replaceState(null, "", c.dataset.cat === "all" ? "./" : "#" + c.dataset.cat); }));
const h = location.hash.slice(1); if (h && document.querySelector('.chip[data-cat="' + h + '"]')) show(h);
</script>'''
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Kiến thức yến sào, đông trùng hạ thảo", "url": f"{SITE}/kien-thuc/"}]
    open(R + "kien-thuc/index.html", "w", encoding="utf-8").write(shell(
        "kien-thuc/", "Kiến thức yến sào, đông trùng hạ thảo", "Bài viết của Việt Cường Nhân về cách chọn, chưng, bảo quản yến sào, nước yến, đông trùng hạ thảo và táo đỏ.",
        "kt", body, ld, script=script))
    return m.BAI

# Trang chính sách: /chinh-sach/doi-tra.html, van-chuyen.html, bao-mat.html
CS = [
    ("doi-tra", "Chính sách đổi trả và hoàn tiền", "Điều kiện, thời hạn và cách đổi trả, hoàn tiền khi mua yến sào, đông trùng hạ thảo và sản phẩm của Việt Cường Nhân.", """
  <h2>1. Trường hợp được đổi trả</h2>
  <ul>
    <li>Giao sai sản phẩm, sai quy cách hoặc thiếu hàng so với đơn đã xác nhận.</li>
    <li>Sản phẩm hư hỏng, móp vỡ do vận chuyển hoặc lỗi từ nhà sản xuất.</li>
    <li>Sản phẩm hết hạn sử dụng hoặc có dấu hiệu biến chất khi nhận.</li>
  </ul>
  <h2>2. Điều kiện</h2>
  <ul>
    <li>Báo cho Việt Cường Nhân trong vòng <b>03 ngày</b> kể từ khi nhận hàng, qua điện thoại hoặc Zalo 0978 094 739.</li>
    <li>Sản phẩm còn nguyên niêm phong, tem nhãn (trừ lỗi chỉ phát hiện được khi mở).</li>
    <li>Có hình ảnh hoặc video lúc mở hàng để đối chiếu.</li>
  </ul>
  <h2>3. Trường hợp không áp dụng</h2>
  <p>Vì là thực phẩm và mỹ phẩm, Việt Cường Nhân không nhận đổi trả sản phẩm đã mở niêm phong và sử dụng vì lý do khẩu vị, mùi hương hoặc không còn nhu cầu, trừ các trường hợp ở mục 1.</p>
  <h2>4. Cách thức và thời gian</h2>
  <ul>
    <li>Việt Cường Nhân chịu phí vận chuyển đổi trả cho các trường hợp ở mục 1.</li>
    <li>Khách chọn đổi sản phẩm mới cùng loại hoặc hoàn tiền.</li>
    <li>Hoàn tiền bằng chuyển khoản vào tài khoản khách cung cấp trong vòng <b>07 ngày làm việc</b> kể từ khi Việt Cường Nhân nhận lại hàng.</li>
  </ul>"""),
    ("van-chuyen", "Chính sách vận chuyển và kiểm hàng", "Phạm vi, thời gian, phí giao hàng và quyền kiểm hàng khi nhận sản phẩm Việt Cường Nhân.", """
  <h2>1. Phạm vi giao hàng</h2>
  <p>Giao hàng toàn quốc qua nhân viên Việt Cường Nhân (khu vực gần) hoặc đơn vị vận chuyển.</p>
  <h2>2. Thời gian dự kiến</h2>
  <ul>
    <li>TP. Hồ Chí Minh và khu vực lân cận: 1 đến 2 ngày làm việc.</li>
    <li>Các tỉnh, thành khác: 2 đến 5 ngày làm việc.</li>
  </ul>
  <p>Thời gian có thể kéo dài vào dịp lễ, Tết hoặc do thời tiết; nhân viên sẽ báo khách khi có thay đổi.</p>
  <h2>3. Phí giao hàng</h2>
  <p>Giá trên website chưa gồm phí giao hàng. Phí tính theo khu vực và khối lượng đơn, được báo cho khách khi gọi xác nhận đơn, trước khi giao. Chương trình miễn phí giao hàng (nếu có) được ghi rõ trên website.</p>
  <h2>4. Kiểm hàng khi nhận</h2>
  <ul>
    <li>Khách được kiểm tra bên ngoài kiện hàng, số lượng, loại sản phẩm và tình trạng niêm phong trước khi thanh toán.</li>
    <li>Nếu hàng sai, thiếu hoặc hư hỏng, khách có quyền từ chối nhận và báo ngay cho Việt Cường Nhân.</li>
    <li>Khách nên quay video khi mở hàng để làm căn cứ đổi trả theo <a href="doi-tra.html">chính sách đổi trả</a>.</li>
  </ul>"""),
    ("bao-mat", "Chính sách bảo mật thông tin cá nhân", "Việt Cường Nhân thu thập, sử dụng, lưu trữ và bảo vệ thông tin cá nhân của khách hàng khi đặt hàng trên vietcuongnhan.com như thế nào.", """
  <h2>1. Thông tin thu thập</h2>
  <p>Khi đặt hàng, khách cung cấp: họ tên, số điện thoại, địa chỉ giao hàng, sản phẩm đặt mua và ghi chú (nếu có). Website không yêu cầu tạo tài khoản và không thu thập thông tin thẻ thanh toán.</p>
  <h2>2. Mục đích sử dụng</h2>
  <ul>
    <li>Xác nhận và giao đơn hàng, chăm sóc khách hàng sau mua.</li>
    <li>Giải quyết đổi trả, khiếu nại.</li>
    <li>Thông báo chương trình ưu đãi, chỉ khi khách đồng ý.</li>
  </ul>
  <h2>3. Thời gian lưu trữ</h2>
  <p>Thông tin đơn hàng được lưu trong thời gian cần thiết để thực hiện giao dịch và theo quy định về lưu trữ chứng từ kế toán, hoặc đến khi khách yêu cầu xóa (nếu pháp luật cho phép).</p>
  <h2>4. Chia sẻ thông tin</h2>
  <p>Việt Cường Nhân không bán hay trao đổi thông tin khách hàng. Thông tin chỉ được cung cấp cho đơn vị vận chuyển (họ tên, số điện thoại, địa chỉ) để giao hàng, hoặc cho cơ quan nhà nước có thẩm quyền khi có yêu cầu theo quy định pháp luật.</p>
  <h2>5. Đơn vị thu thập và quản lý thông tin</h2>
  <p>Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân, trụ sở: Số 24/22 Khu phố Thống Nhất 1, Phường Dĩ An, TP. Hồ Chí Minh. Mã số doanh nghiệp: 3701518691. Hotline, Zalo 0978 094 739. Email: congtyvietcuongnhan@gmail.com.</p>
  <h2>6. Quyền của khách hàng</h2>
  <p>Khách có quyền yêu cầu xem, chỉnh sửa, xóa thông tin cá nhân hoặc rút lại sự đồng ý nhận tin ưu đãi bằng cách liên hệ số điện thoại hoặc email trên. Việt Cường Nhân phản hồi trong vòng 72 giờ.</p>
  <h2>7. Cam kết bảo mật</h2>
  <p>Thông tin đơn hàng được lưu trên hệ thống quản lý bán hàng có kiểm soát truy cập, chỉ nhân viên phụ trách đơn hàng được xem. Khi phát hiện sự cố lộ lọt thông tin, Việt Cường Nhân sẽ thông báo cho khách và cơ quan chức năng theo quy định.</p>"""),
]
CS_CSS = """<style>.policy-nav { display: flex; flex-wrap: wrap; gap: 6px 14px; font-size: 13px; margin: 0 0 24px; } .policy-nav a[aria-current] { color: var(--ink); font-weight: 600; text-decoration: none; } .updated { font-size: 13px; color: var(--muted); margin-top: 28px; }</style>"""

def chinh_sach():
    os.makedirs(R + "chinh-sach", exist_ok=True)
    for slug, h1, desc, body in CS:
        cur = ' aria-current="page"'
        nav = " ".join(f'<a href="{s}.html"{cur if s == slug else ""}>{t}</a>' for s, t, _, _ in CS)
        art = f"""{CS_CSS}
<main class="article">
  <p class="eyebrow">Chính sách</p>
  <h1>{h1}</h1>
  <nav class="policy-nav" aria-label="Chính sách">{nav}</nav>
{body}
  <p class="updated">Áp dụng từ ngày 25/10/2026. Mọi thắc mắc xin gọi hoặc nhắn Zalo 0978 094 739.</p>
</main>"""
        ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": h1, "url": f"{SITE}/chinh-sach/{slug}.html", "inLanguage": "vi"}]
        open(R + f"chinh-sach/{slug}.html", "w", encoding="utf-8").write(shell(f"chinh-sach/{slug}.html", h1, desc, "", art, ld))
    return [s for s, _, _, _ in CS]

def sitemap(bai, cs=()):
    today = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=7)).strftime("%Y-%m-%d")
    urls = [f"{SITE}/", f"{SITE}/gioi-thieu/", f"{SITE}/chung-nhan/", f"{SITE}/kien-thuc/"] + [f"{SITE}/kien-thuc/{b['slug']}.html" for b in bai] + [f"{SITE}/chinh-sach/{c}.html" for c in cs]
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    open(R + "sitemap.xml", "w", encoding="utf-8").write(x)

def chung_nhan():
    c = open(R + "tools/chung-nhan-noi-dung.html", encoding="utf-8").read()
    c += '''
<section class="block" style="padding-top:0">
  <div class="wrap" style="display:flex;flex-wrap:wrap;gap:10px">
    <a class="btn btn-gold" href="../#san-pham">Xem bảng giá sản phẩm</a>
    <a class="btn btn-line" href="../gioi-thieu/">Giới thiệu công ty</a>
    <a class="btn btn-line" href="https://zalo.me/0978094739" target="_blank" rel="noopener">Nhắn Zalo 0978 094 739</a>
  </div>
</section>'''
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": "Chứng nhận & Cam kết Việt Cường Nhân", "url": f"{SITE}/chung-nhan/",
           "about": {"@type": "Organization", "name": "Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân", "url": SITE}}]
    os.makedirs(R + "chung-nhan", exist_ok=True)
    open(R + "chung-nhan/index.html", "w", encoding="utf-8").write(shell(
        "chung-nhan/", "Chứng nhận & Cam kết", "Việt Cường Nhân đạt HACCP, ISO 22000:2018 và GMP (G-CERTI); bản tự công bố tổ yến thô, tổ yến tinh chế, nấm đông trùng hạ thảo. Xem bản scan giấy chứng nhận.",
        "cn", c, ld, script=LB_DOCS))

def llms(bai):
    """llms.txt: bản tóm tắt cho ChatGPT, Perplexity, Gemini đọc nhanh thông tin công ty và bài viết."""
    t = f"""# Việt Cường Nhân (vietcuongnhan.com)

> Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân (MST 3701518691), thành lập năm 2009 tại Dĩ An, TP. Hồ Chí Minh. Tự sản xuất và bán yến sào (tổ yến thô, yến tinh chế, yến rút lông, nước yến chưng hũ VCN Nest), nấm đông trùng hạ thảo, táo đỏ Tân Cương, thạch nha đam. Đạt HACCP, ISO 22000:2018, GMP. Thương hiệu yến Đỗ Thị Toán.

- Hotline, Zalo: 0978 094 739 · Email: congtyvietcuongnhan@gmail.com
- Nhà máy: 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp, TP. Hồ Chí Minh
- Cơ sở đóng gói: 261-263 Võ Thị Sáu, KP. Tây A, Phường Đông Hòa, TP. Hồ Chí Minh
- Bảng giá đầy đủ, đặt hàng: {SITE}/#san-pham (giá chưa gồm phí giao hàng)

## Trang chính
- [Giới thiệu công ty]({SITE}/gioi-thieu/): lịch sử, nhà yến, xưởng, nhà máy
- [Chứng nhận]({SITE}/chung-nhan/): HACCP, ISO 22000, GMP, tự công bố sản phẩm
- [Chính sách đổi trả]({SITE}/chinh-sach/doi-tra.html) · [Vận chuyển]({SITE}/chinh-sach/van-chuyen.html) · [Bảo mật]({SITE}/chinh-sach/bao-mat.html)

## Kiến thức
""" + "\n".join(f"- [{b['h1']}]({SITE}/kien-thuc/{b['slug']}.html): {b['desc']}" for b in reversed(bai)) + "\n"
    open(R + "llms.txt", "w", encoding="utf-8").write(t)

if __name__ == "__main__":
    gioi_thieu()
    chung_nhan()
    bai = kien_thuc()
    cs = chinh_sach()
    sitemap(bai, cs)
    llms(bai)
    print("gioi-thieu + kien-thuc:", len(bai), "bài")
