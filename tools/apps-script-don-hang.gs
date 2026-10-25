/**
 * Nhận đơn từ website vietcuongnhan.com → ghi vào Google Sheet + tạo đơn trên Pancake POS.
 * Cài đặt (anh Việt tự làm, không gửi API key cho ai):
 *   1. Tạo Google Sheet "Đơn hàng website Việt Cường Nhân" → Tiện ích mở rộng → Apps Script → dán toàn bộ file này.
 *   2. Cài đặt dự án (bánh răng) → Thuộc tính tập lệnh → thêm:
 *        POS_SHOP_ID = 101108492
 *        POS_API_KEY = <API key lấy trong Pancake POS: Cấu hình → Nâng cao → API>
 *   3. Triển khai → Tùy chọn triển khai mới → Loại: Ứng dụng web
 *        Thực thi với tư cách: Tôi · Ai có quyền truy cập: Bất kỳ ai → Triển khai → chép URL /exec gửi Claude.
 */
const HEADERS = ["Thời gian", "Họ tên", "SĐT", "Địa chỉ", "Sản phẩm", "Quy cách", "SL", "Tạm tính", "Ghi chú", "Pancake"];

function doPost(e) {
  const p = (e && e.parameter) || {};
  if (p.website) return out("bot");                      // ô bẫy bot
  if (!p.name || !p.phone) return out("thiếu thông tin");
  const sh = sheet_();
  const row = [new Date(), p.name, "'" + p.phone, p.addr || "", p.product || "", p.spec || "", p.qty || 1, Number(p.total) || 0, p.note || ""];
  let pos = "";
  try { pos = toPancake_(p); } catch (err) { pos = "LỖI: " + err; }
  sh.appendRow(row.concat([pos]));
  return out("ok");
}

function toPancake_(p) {
  const props = PropertiesService.getScriptProperties();
  const shop = props.getProperty("POS_SHOP_ID"), key = props.getProperty("POS_API_KEY");
  if (!shop || !key) return "chưa cài API";
  const note = `[WEBSITE] ${p.product || ""} (${p.spec || ""}) x ${p.qty || 1} · Tạm tính ${Number(p.total || 0).toLocaleString("vi-VN")}đ` + (p.note ? ` · Ghi chú: ${p.note}` : "");
  const body = {
    bill_full_name: p.name,
    bill_phone_number: p.phone,
    shipping_address: { full_name: p.name, phone_number: p.phone, address: p.addr || "" },
    note: note,
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

function sheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getSheetByName("Đơn") || ss.insertSheet("Đơn");
  if (sh.getLastRow() === 0) sh.appendRow(HEADERS);
  return sh;
}
function out(s) { return ContentService.createTextOutput(s); }
