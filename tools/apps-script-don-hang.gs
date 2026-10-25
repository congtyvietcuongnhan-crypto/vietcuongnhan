/**
 * Cầu nối đơn hàng: website vietcuongnhan.com → Pancake POS (không qua Google Sheet).
 * Cần cầu nối này để API key Pancake nằm kín ở đây, không lộ trong code công khai của website.
 * Cài đặt:
 *   1. script.google.com → Dự án mới → dán toàn bộ file này.
 *   2. Cài đặt dự án (bánh răng) → Thuộc tính tập lệnh → thêm:
 *        POS_SHOP_ID = 101108492
 *        POS_API_KEY = <API key lấy trong Pancake POS: Cấu hình → Nâng cao → API>
 *   3. Triển khai → Tùy chọn triển khai mới → Loại: Ứng dụng web
 *        Thực thi với tư cách: Tôi · Ai có quyền truy cập: Bất kỳ ai → Triển khai → chép URL /exec gửi Claude.
 */
function doPost(e) {
  const p = (e && e.parameter) || {};
  if (p.website) return out("bot");                      // ô bẫy bot
  if (!p.name || !p.phone) return out("thiếu thông tin");
  try { return out(toPancake_(p)); } catch (err) { console.error(err); return out("LỖI: " + err); }
}

function toPancake_(p) {
  const props = PropertiesService.getScriptProperties();
  const shop = props.getProperty("POS_SHOP_ID"), key = props.getProperty("POS_API_KEY");
  if (!shop || !key) return "chưa cài API";
  const qty = Number(p.qty) || 1;
  const price = Number(p.price) || Math.round((Number(p.total) || 0) / qty); // đơn giá đúng như trên web
  const note = `[WEBSITE] ${p.product || ""} (${p.spec || ""}) x ${p.qty || 1} · Tạm tính ${Number(p.total || 0).toLocaleString("vi-VN")}đ` + (p.note ? ` · Ghi chú: ${p.note}` : "");
  const body = {
    bill_full_name: p.name,
    bill_phone_number: p.phone,
    shipping_address: { full_name: p.name, phone_number: p.phone, address: p.addr || "" },
    note: note,
    // Sản phẩm gửi dạng "thêm nhanh" (one_time_product): chỉ tên + giá theo web,
    // không gắn vào sản phẩm trong kho nên không đổi giá/tồn kho trên Pancake.
    items: [{
      one_time_product: true,
      quantity: Number(p.qty) || 1,
      discount_each_product: 0,
      is_bonus_product: false,
      is_discount_percent: false,
      is_wholesale: false,
      variation_info: { name: [p.product, p.spec].filter(Boolean).join(" - ") || "Sản phẩm website", retail_price: price }
    }],
    order_sources: -1,
    status: 0
  };
  const res = UrlFetchApp.fetch(`https://pos.pages.fm/api/v1/shops/${shop}/orders?api_key=${encodeURIComponent(key)}`, {
    method: "post", contentType: "application/json", payload: JSON.stringify(body), muteHttpExceptions: true
  });
  const code = res.getResponseCode(), txt = res.getContentText().slice(0, 300);
  if (code >= 300) throw code + " " + txt;
  try { const j = JSON.parse(txt); return "ok " + ((j.data && (j.data.id || j.data.display_id)) || ""); } catch (_) { return "ok"; }
}

function out(s) { return ContentService.createTextOutput(s); }
