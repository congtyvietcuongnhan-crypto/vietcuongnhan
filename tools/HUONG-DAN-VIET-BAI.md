# Hướng dẫn viết bài SEO cho vietcuongnhan.com

Mỗi ngày 2 bài: 7:00 và 13:00 (giờ Việt Nam), theo thứ tự trong `tools/lich-bai.json`.
Bài vừa đạt chuẩn Google (SEO) vừa dễ được ChatGPT, Gemini, Perplexity trích dẫn (GEO).

## 1. Cách đăng một bài

1. Lấy bài đầu tiên có `"trang_thai": "chua_viet"` trong `tools/lich-bai.json`.
2. Thêm 1 `dict(...)` vào **cuối** danh sách `BAI` trong `tools/bai_viet.py`. Các trường:
   - `slug`: lấy đúng `slug` trong lịch.
   - `cat`: `chuyen_muc` trong lịch.
   - `ngay`: ngày đăng thật (YYYY-MM-DD, giờ VN).
   - `tu_khoa`: từ khóa chính + 2–4 từ khóa phụ, cách nhau bằng dấu phẩy.
   - `h1`: tiêu đề, chứa từ khóa chính, dưới 65 ký tự. Có thể sửa nhẹ `tieu_de_lich` cho tự nhiên.
   - `desc`: mô tả meta 140–160 ký tự, có từ khóa chính và lợi ích cho người đọc.
   - `lede`: 1–2 câu mở đầu trả lời thẳng câu hỏi chính.
   - `tom_tat`: 3–5 ý ngắn (mỗi ý 1 câu, có số liệu cụ thể nếu có). Hiện thành khung "Tóm tắt nhanh" đầu bài, là phần AI hay trích nhất.
   - `body`: nội dung HTML (h2, h3, p, ul, ol, table). Dùng `li(<mã SP>)` và `ul(...)` để chèn sản phẩm kèm giá thật từ bảng giá.
   - `faq`: 3–5 cặp (câu hỏi, câu trả lời) đúng cách người dùng hỏi Google/ChatGPT.
3. Chạy `python3 tools/trang_con.py` (sinh trang bài, trang Kiến thức, sitemap.xml, llms.txt).
4. Kiểm tra: mở `kien-thuc/<slug>.html` xem HTML đúng, `xmllint --noout sitemap.xml`, mọi link nội bộ tồn tại.
5. Sửa `trang_thai` của bài trong lịch thành `"da_dang"`, thêm `"ngay_dang"` và `"url"`.
   Bài thêm ngoài lịch (bài kèm video, bài đặt riêng): thêm entry mới ở **cuối** lịch với `"trang_thai": "da_dang"` và **luôn** có `"ngoai_lich": true`; không thay thế chủ đề đã có trong lịch.
6. Nhánh `bai-<slug>`, commit, PR, merge squash (xem lịch chạy tự động).

## 2. Chuẩn SEO Google

- **Một từ khóa chính mỗi bài**, có trong: h1, `desc`, câu đầu `lede`, ít nhất một h2, và tự nhiên trong bài (không nhồi).
- **Độ dài 900–1.500 chữ**, đủ trả lời trọn ý định tìm kiếm (`y_dinh` trong lịch):
  - thông tin: giải thích rõ, có bước làm, bảng so sánh nếu hợp;
  - so sánh: luôn có bảng `<table>` so sánh các tiêu chí;
  - công thức: nguyên liệu (định lượng), các bước đánh số, thời gian, mẹo;
  - thương mại: bảng giá thật từ web, cách chọn, cách đặt hàng;
  - địa phương: địa chỉ xưởng, giờ làm, cách đến, số điện thoại.
- **Cấu trúc rõ**: h2 cho từng ý lớn, h3 cho ý con; đoạn văn ngắn 2–4 câu.
- **Link nội bộ**: 2–3 link tới bài kiến thức liên quan đã đăng (`<a href="cach-chung-yen-sao.html">`), 1 link về bảng giá `../#san-pham`. Khi bài mới liên quan rõ tới bài cũ, có thể thêm 1 link từ bài cũ sang bài mới.
- **E-E-A-T**: nói từ kinh nghiệm xưởng Việt Cường Nhân (từ 2009, nhà yến, xưởng nhặt lông, nhà máy nước yến, HACCP, ISO 22000, GMP). Dùng "ở xưởng chúng tôi…", "khách hay hỏi…" khi đúng sự thật.
- **Slug** không dấu, ngắn, có từ khóa (đã có sẵn trong lịch).

## 3. Chuẩn cho ChatGPT, Gemini, Perplexity (GEO)

- **Trả lời trước, giải thích sau**: câu đầu mỗi h2 là câu trả lời trọn vẹn, đứng riêng vẫn hiểu.
- **Câu có thông tin cụ thể**: số gam, số phút, số chén, giá, kích thước. Ví dụ: "100 g yến tinh chế chưng được khoảng 25–30 chén, mỗi chén 3–4 g."
- **Gọi tên thực thể đầy đủ**: "Việt Cường Nhân", "yến tinh chế 1 lớp sợi vừa", "nước yến VCN Nest 0.8gr", không viết tắt mơ hồ.
- **FAQ đúng câu người ta hỏi** ("Bà bầu ăn yến được không?", "100gr yến bao nhiêu tiền?"), trả lời 2–3 câu.
- **Bảng và danh sách** cho số liệu, so sánh: AI dễ đọc và trích.
- Trang tự có schema Article + FAQPage, `llms.txt` tự cập nhật, robots.txt cho phép bot AI.

## 4. Giá và sản phẩm

- Giá **chỉ** lấy từ bảng giá trong `index.html` qua `li()` / `gia()`; không gõ tay giá.
- Sản phẩm gợi ý trong lịch (`san_pham`) là mã trong bảng giá; chọn 2–4 mã hợp nội dung.
- Giá chưa gồm phí giao hàng. Mua sỉ, đại lý: mời nhắn Zalo 0978 094 739, **không** ghi mức chiết khấu.

## 5. Tuyệt đối không

- Viết công dụng chữa bệnh, "trị", "chữa", "phòng ngừa ung thư", hay so sánh với thuốc. Bài sức khỏe (bà bầu, trẻ em, người già) phải khuyên hỏi bác sĩ; không đưa liều dùng như thuốc.
- Bịa số liệu nghiên cứu, bịa nhận xét khách, bịa giải thưởng.
- Hứa chính sách chưa có (chỉ dùng nội dung ở trang chính sách).
- Sửa giá, trang chủ, sản phẩm, trang chính sách.
- Sao chép bài của web khác.

## 6. Làm bù khi lỡ lịch

Mốc đăng: 6:40 và 12:40 mỗi ngày từ 26/10/2026 (để bài lên web khoảng 7:00 và 13:00).
Số bài đáng lẽ đã đăng = số mốc đã qua tính đến giờ chạy.
Số bài đã đăng theo lịch = số entry có `"trang_thai": "da_dang"` và **không** có `"ngoai_lich": true`. Bài ngoài lịch (`"ngoai_lich": true`, ví dụ bài kèm video) **không** được tính, nên không làm lùi lịch.
Nếu số bài đã đăng theo lịch ít hơn số mốc đã qua: đăng bù theo thứ tự lịch (bài `chua_viet` đầu tiên), tối đa 3 bài mỗi lần chạy, mỗi bài một PR.
