# Danh sách bài kiến thức. Thêm bài mới: thêm 1 dict vào cuối BAI rồi chạy python3 tools/trang_con.py
# Quy tắc: giá lấy từ bảng giá index.html (hàm li/gia), không viết công dụng chữa bệnh, không bịa đánh giá.
import os, json, subprocess
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
_js = r'''const fs=require("fs");const h=fs.readFileSync(process.argv[1],"utf8");
const code=h.slice(h.indexOf("const P = ["),h.indexOf("const DIR ="));const c={};
new Function("ctx",code.replace(/\bconst (P|IMG|R|AN_XA_BONG|HET_HANG)\b/g,"var $1")+";ctx.P=P;").call(null,c);
process.stdout.write(JSON.stringify(c.P));'''
P = {p[0]: p for p in json.loads(subprocess.check_output(["node", "-e", _js, R + "index.html"]))}
vnd = lambda n: f"{n:,}".replace(",", ".") + "đ"
gia = lambda i: vnd(P[i][4])
def li(i, note=""):
    p = P[i]
    return f'    <li><a href="../#san-pham"><b>{p[2]}</b></a> ({p[3]}): {vnd(p[4])}.{(" " + note) if note else ""}</li>'
def ul(*rows): return "  <ul>\n" + "\n".join(rows) + "\n  </ul>"

BAI = [
dict(slug="cach-chung-yen-sao", cat="Yến sào", ngay="2026-10-25",
  h1="Cách chưng yến sào đường phèn tại nhà",
  desc="Hướng dẫn ngâm, làm sạch, chưng cách thủy và bảo quản yến sào đúng cách để sợi yến dai, không bị tan.",
  lede="Chưng cách thủy giữ sợi yến dai và trong. Đây là các bước xưởng Việt Cường Nhân vẫn hướng dẫn khách.",
  body="""  <h2>Chuẩn bị cho 1 chén</h2>
  <ul>
    <li>Khoảng 3 đến 5 g yến khô (yến tinh chế hoặc yến rút lông).</li>
    <li>150 đến 200 ml nước lọc, đường phèn tùy khẩu vị.</li>
    <li>Thố sứ có nắp và nồi để chưng cách thủy.</li>
  </ul>
  <h2>Các bước</h2>
  <ol>
    <li><b>Ngâm yến.</b> Yến tinh chế ngâm nước sạch 30 đến 60 phút cho nở mềm. Yến thô còn lông ngâm lâu hơn rồi nhặt lông bằng nhíp.</li>
    <li><b>Rửa và xé sợi.</b> Vớt yến, rửa nhẹ tay, xé sợi vừa ăn, để ráo.</li>
    <li><b>Chưng cách thủy.</b> Cho yến và nước vào thố, đậy nắp, đặt vào nồi nước sôi lăn tăn, chưng 20 đến 30 phút.</li>
    <li><b>Thêm đường phèn</b> trong 5 phút cuối, khuấy nhẹ cho tan.</li>
  </ol>
  <h2>Lưu ý</h2>
  <ul>
    <li>Không đun sôi sùng sục và không chưng quá lâu, sợi yến sẽ tan thành nước.</li>
    <li>Có thể chưng cùng táo đỏ, hạt sen, kỷ tử hoặc vài cọng đông trùng hạ thảo để đổi vị.</li>
  </ul>
  <h2>Bảo quản</h2>
  <ul>
    <li>Yến khô: hộp kín, nơi khô ráo, tránh nắng.</li>
    <li>Yến đã chưng: để nguội, đậy kín, cất ngăn mát và dùng trong vài ngày.</li>
  </ul>
  <h2>Yến phù hợp để chưng tại nhà</h2>
""" + ul(li(109), li(111), li(113, "Đã nhặt lông bằng tay, ngâm xong là chưng.")),
  faq=[("Ngâm yến bao lâu là đủ?", "Yến tinh chế khoảng 30 đến 60 phút; yến rút lông khô có thể lâu hơn một chút. Sợi nở mềm, tơi là được."),
       ("Một tuần nên ăn mấy lần?", "Nhiều gia đình dùng 2 đến 3 lần mỗi tuần, mỗi lần 3 đến 5 g yến khô. Người có bệnh nền nên hỏi bác sĩ.")]),

dict(slug="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau", cat="Yến sào", ngay="2026-10-25",
  h1="Yến thô, yến tinh chế và yến rút lông khác nhau thế nào?",
  desc="So sánh yến thô, yến tinh chế và yến rút lông: cách làm sạch, thời gian sơ chế, giá 100gr và nên chọn loại nào.",
  lede="Cùng là tổ yến, nhưng mức độ làm sạch khác nhau nên giá và công sơ chế ở nhà cũng khác.",
  body=f"""  <h2>Yến thô</h2>
  <p>Tổ yến lấy từ nhà yến, mới làm sạch sơ, còn lông và tạp chất. Giá mềm nhất nhưng phải tự ngâm, nhặt lông khá lâu.</p>
""" + ul(li(101), li(104)) + f"""
  <h2>Yến tinh chế</h2>
  <p>Đã ngâm và nhặt sạch lông tại xưởng, sau đó sấy khô và định hình. Về nhà chỉ cần ngâm và chưng.</p>
""" + ul(li(106), li(109), li(112)) + f"""
  <h2>Yến rút lông</h2>
  <p>Nhặt lông bằng tay trên tổ còn nguyên sợi, giữ sợi yến dài và dày hơn, nên giá cao nhất.</p>
""" + ul(li(113), li(114), li(116)) + """
  <h2>Nên chọn loại nào?</h2>
  <table><thead><tr><th>Nhu cầu</th><th>Gợi ý</th></tr></thead><tbody>
  <tr><td>Có thời gian, muốn giá tốt</td><td>Yến thô</td></tr>
  <tr><td>Dùng hằng ngày, tiện</td><td>Yến tinh chế 1 lớp sợi</td></tr>
  <tr><td>Biếu tặng, muốn sợi đẹp</td><td>Yến rút lông đắp tổ, định hình</td></tr>
  <tr><td>Nấu cháo, súp cho bé</td><td>Yến tinh chế vụn baby</td></tr>
  </tbody></table>""",
  faq=[("Yến thô có sạch không?", "Yến thô còn lông và tạp chất tự nhiên, cần ngâm và nhặt kỹ trước khi chưng."),
       ("Vì sao yến rút lông đắt hơn?", "Vì nhặt lông thủ công trên tổ nguyên sợi, tốn nhiều công hơn và giữ sợi yến dài, đẹp hơn.")]),

dict(slug="cach-chon-yen-sao-that", cat="Yến sào", ngay="2026-10-25",
  h1="Cách chọn mua yến sào thật, tránh hàng pha",
  desc="Các dấu hiệu nhận biết yến sào thật bằng mắt, khi ngâm và khi chưng, cùng giấy tờ nên hỏi người bán.",
  lede="Không có mẹo nào chắc chắn 100%, nhưng kết hợp nhiều dấu hiệu và giấy tờ sẽ giảm rủi ro mua phải hàng pha.",
  body="""  <h2>Nhìn bằng mắt</h2>
  <ul>
    <li>Sợi yến tự nhiên to nhỏ không đều, màu trắng ngà, không trắng tinh bất thường.</li>
    <li>Soi dưới đèn thấy sợi đan xen, không bóng nhựa.</li>
  </ul>
  <h2>Khi ngâm và chưng</h2>
  <ul>
    <li>Yến thật nở mềm, sợi tơi, nước ngâm không đục trắng hay có váng lạ.</li>
    <li>Chưng đúng thời gian sợi vẫn còn, có mùi tanh nhẹ đặc trưng của yến.</li>
  </ul>
  <h2>Giấy tờ nên hỏi</h2>
  <ul>
    <li>Bản tự công bố sản phẩm cho từng loại yến.</li>
    <li>Chứng nhận an toàn thực phẩm của cơ sở sản xuất như HACCP, ISO 22000, GMP.</li>
    <li>Địa chỉ xưởng, nhà máy có thể đến xem.</li>
  </ul>
  <p>Việt Cường Nhân công khai chứng nhận HACCP, ISO 22000:2018, GMP và bản tự công bố tổ yến thô, tổ yến tinh chế ngay trên <a href="../chung-nhan/">trang chủ</a>.</p>""",
  faq=[("Yến quá trắng có phải hàng tẩy?", "Yến tự nhiên thường trắng ngà; màu trắng tinh bất thường nên hỏi kỹ nguồn gốc."),
       ("Có nên mua yến giá rẻ hơn thị trường nhiều?", "Nên cẩn thận vì công nhặt lông chiếm phần lớn giá thành; giá thấp bất thường dễ là hàng pha.")]),

dict(slug="nuoc-yen-chung-san-cach-dung-bao-quan", cat="Nước yến", ngay="2026-10-25",
  h1="Nước yến chưng sẵn: chọn loại nào, dùng và bảo quản ra sao?",
  desc="Phân biệt nước yến chưng thủ công từ yến tươi và nước yến VCN Nest đóng hũ, cách dùng và bảo quản.",
  lede="Nước yến chưng sẵn tiện mang theo, biếu tặng. Việt Cường Nhân có hai dòng: chưng thủ công và VCN Nest đóng hũ tiệt trùng.",
  body=f"""  <h2>Nước yến chưng thủ công</h2>
  <p>Chưng từ yến tươi theo từng mẻ, lượng yến nhiều trong mỗi hũ.</p>
""" + ul(li(124), li(125)) + """
  <h2>Nước yến VCN Nest</h2>
  <p>Sản xuất trên dây chuyền tại nhà máy, đóng hũ tiệt trùng, ghi rõ lượng tổ yến thô mỗi hũ.</p>
""" + ul(li(126), li(127), li(129), li(135, "Có hộp, hợp để biếu.")) + """
  <h2>Cách dùng</h2>
  <ul>
    <li>Ngon nhất khi để mát. Lắc nhẹ trước khi mở.</li>
    <li>Đã mở nắp nên dùng hết trong ngày.</li>
  </ul>
  <h2>Bảo quản</h2>
  <ul>
    <li>Để nơi khô mát, tránh nắng trực tiếp; xem hạn dùng in trên hũ.</li>
  </ul>""",
  faq=[("Nước yến chưng sẵn có cần bảo quản lạnh?", "Hũ tiệt trùng chưa mở để nơi khô mát được; để lạnh trước khi uống sẽ ngon hơn. Đã mở nắp thì dùng hết trong ngày."),
       ("Mua sỉ nước yến thế nào?", "Liên hệ Zalo 0978 094 739 để được báo giá sỉ theo số lượng.")]),

dict(slug="cach-dung-dong-trung-ha-thao", cat="Đông trùng hạ thảo", ngay="2026-10-25",
  h1="Cách dùng nấm đông trùng hạ thảo sấy khô trong món ăn hằng ngày",
  desc="Gợi ý pha trà, nấu canh, chưng cùng yến với nấm đông trùng hạ thảo sấy; cách bảo quản và chọn loại cây, loại gãy.",
  lede="Nấm đông trùng hạ thảo do Việt Cường Nhân nuôi trồng, sấy khô, dùng được trong nhiều món quen thuộc.",
  body=f"""  <h2>Pha trà</h2>
  <p>Cho một nhúm nhỏ nấm vào ly, rót nước nóng khoảng 80 đến 90 độ, ủ 5 đến 10 phút. Uống xong có thể ăn luôn phần nấm.</p>
  <h2>Nấu canh, hầm</h2>
  <p>Thả nấm vào nồi canh gà, sườn, hạt sen trong 10 phút cuối để giữ màu cam và vị ngọt nhẹ.</p>
  <h2>Chưng cùng yến</h2>
  <p>Khi chưng yến, thêm vài cọng đông trùng ở 5 phút cuối cho đẹp màu.</p>
  <h2>Loại cây hay loại gãy?</h2>
""" + ul(li(136, "Cọng nguyên, đẹp, hợp biếu tặng."), li(138, "Cọng gãy, giá mềm, hợp nấu ăn hằng ngày."), li(140)) + """
  <h2>Bảo quản</h2>
  <ul><li>Để hũ kín, nơi khô mát; mở ra dùng xong đậy kín ngay để nấm không ẩm.</li></ul>""",
  faq=[("Mỗi lần dùng bao nhiêu?", "Thường dùng một nhúm nhỏ khoảng 1 đến 3 g nấm khô mỗi lần. Người có bệnh nền nên hỏi bác sĩ.")]),

dict(slug="tao-do-tan-cuong-cach-chon-va-mon-ngon", cat="Táo đỏ", ngay="2026-10-25",
  h1="Táo đỏ Tân Cương: cách chọn size và món ngon dễ làm",
  desc="Phân biệt táo đỏ Tân Cương size trung, size đại, thượng hạng; cách bảo quản và các món trà, chè, chưng yến.",
  lede="Táo đỏ Tân Cương được Việt Cường Nhân nhập khẩu và phân phối, chia theo số quả mỗi kg.",
  body=f"""  <h2>Chọn size theo nhu cầu</h2>
""" + ul(li(142), li(143), li(144), li(145)) + """
  <p>Quả càng ít mỗi kg thì quả càng to, cùi dày. Pha trà, nấu chè dùng size trung là đủ; biếu tặng chọn size đại hoặc thượng hạng.</p>
  <h2>Món ngon</h2>
  <ul>
    <li><b>Trà táo đỏ:</b> 4 đến 5 quả xẻ đôi, hãm nước sôi 10 phút, thêm vài kỷ tử.</li>
    <li><b>Chưng yến táo đỏ:</b> cho táo vào cùng yến khi chưng cách thủy.</li>
    <li><b>Chè táo đỏ hạt sen:</b> nấu hạt sen mềm rồi thêm táo đỏ, đường phèn.</li>
  </ul>
  <h2>Bảo quản</h2>
  <ul><li>Để túi kín nơi khô mát hoặc ngăn mát tủ lạnh để táo không bị ẩm.</li></ul>"""),

dict(slug="chung-nhan-haccp-iso-22000-gmp-la-gi", cat="Chứng nhận", ngay="2026-10-25",
  h1="HACCP, ISO 22000 và GMP nghĩa là gì khi mua yến sào?",
  desc="Giải thích ngắn gọn 3 chứng nhận an toàn thực phẩm HACCP, ISO 22000:2018, GMP và cách kiểm tra trên giấy chứng nhận.",
  lede="Ba chứng nhận này cho biết cơ sở sản xuất được đánh giá về quy trình an toàn thực phẩm, không phải lời quảng cáo công dụng.",
  body="""  <h2>HACCP</h2>
  <p>Hệ thống phân tích mối nguy và kiểm soát điểm tới hạn: xác định những bước có thể gây mất an toàn trong sản xuất và kiểm soát chúng.</p>
  <h2>ISO 22000:2018</h2>
  <p>Tiêu chuẩn quốc tế về hệ thống quản lý an toàn thực phẩm, bao trùm cả chuỗi từ nguyên liệu đến thành phẩm.</p>
  <h2>GMP</h2>
  <p>Thực hành sản xuất tốt: yêu cầu về nhà xưởng, vệ sinh, con người và thiết bị.</p>
  <h2>Kiểm tra trên giấy chứng nhận</h2>
  <ul>
    <li>Tên và địa chỉ cơ sở phải trùng với nơi sản xuất sản phẩm.</li>
    <li>Phạm vi chứng nhận có ghi đúng nhóm sản phẩm bạn mua.</li>
    <li>Số chứng nhận, tổ chức cấp và thời hạn hiệu lực còn hạn.</li>
  </ul>
  <p>Việt Cường Nhân đạt HACCP (GKVN-0387-HC), ISO 22000:2018 (GKVN-0387-FC) và GMP (GKVN-0387-GMP) do G-CERTI cấp. Xem bản scan đầy đủ tại <a href="../chung-nhan/">mục Chứng nhận</a>.</p>"""),

dict(slug="gia-yen-sao-bao-nhieu-tien", cat="Yến sào", ngay="2026-10-26",
  tu_khoa="giá yến sào, giá yến sào 100gr, bảng giá yến sào 2026, yến sào bao nhiêu tiền, giá tổ yến",
  h1="Giá yến sào bao nhiêu tiền 100gr? Bảng giá 2026",
  desc=f"Giá yến sào 100gr tại xưởng Việt Cường Nhân từ {gia(104)} (yến thô) đến {gia(116)} (rút lông khô). Bảng giá từng loại và cách chọn đúng nhu cầu.",
  lede=f"Giá yến sào 100gr tại xưởng Việt Cường Nhân hiện từ {gia(104)} với yến thô bể nứt nhẹ đến {gia(116)} với yến rút lông khô. Giá chênh nhau chủ yếu vì mức độ làm sạch, độ nguyên sợi và hình dáng tổ.",
  tom_tat=[f"Yến thô 100gr: từ {gia(104)} đến {gia(101)}, còn lông, phải tự nhặt trước khi chưng.",
           f"Yến tinh chế 100gr: từ {gia(106)} đến {gia(112)}, đã nhặt sạch lông, ngâm là chưng được.",
           f"Yến rút lông 100gr: từ {gia(113)} đến {gia(116)}, nhặt lông thủ công trên tổ nguyên sợi.",
           f"Nước yến chưng sẵn: từ {gia(126)}/hũ VCN Nest 0.3gr, hợp dùng thử hoặc mang theo.",
           "100gr yến khô chưng được khoảng 20–30 chén nếu mỗi chén dùng 3–5 g; giá trên web chưa gồm phí giao hàng."],
  body=f"""  <h2>Giá yến sào 100gr bao nhiêu tiền?</h2>
  <p>Giá yến sào 100gr dao động khoảng {gia(104)} đến {gia(116)} tùy loại, theo bảng giá đang niêm yết trên website Việt Cường Nhân. Cùng một khối lượng 100gr, loại càng sạch lông, càng nhiều sợi nguyên và càng giữ được dáng tổ thì giá càng cao.</p>
  <p>Ở xưởng chúng tôi, khách hay hỏi vì sao chênh nhau gần gấp ba. Câu trả lời nằm ở công làm sạch: một tổ yến thô phải ngâm, nhặt từng sợi lông bằng nhíp, sấy và định hình lại. Phần công này chiếm phần lớn giá của yến tinh chế và yến rút lông.</p>

  <h2>Bảng giá yến sào theo từng loại (100gr)</h2>
  <p>Bảng dưới lấy trực tiếp từ bảng giá trên trang chủ vietcuongnhan.com, giá chưa gồm phí giao hàng.</p>
  <table><thead><tr><th>Nhóm</th><th>Sản phẩm</th><th>Quy cách</th><th>Giá</th></tr></thead><tbody>
  <tr><td>Yến thô</td><td>{P[104][2]}</td><td>{P[104][3]}</td><td>{gia(104)}</td></tr>
  <tr><td>Yến thô</td><td>{P[101][2]}</td><td>{P[101][3]}</td><td>{gia(101)}</td></tr>
  <tr><td>Yến tinh chế</td><td>{P[106][2]}</td><td>{P[106][3]}</td><td>{gia(106)}</td></tr>
  <tr><td>Yến tinh chế</td><td>{P[109][2]}</td><td>{P[109][3]}</td><td>{gia(109)}</td></tr>
  <tr><td>Yến tinh chế</td><td>{P[112][2]}</td><td>{P[112][3]}</td><td>{gia(112)}</td></tr>
  <tr><td>Yến rút lông</td><td>{P[113][2]}</td><td>{P[113][3]}</td><td>{gia(113)}</td></tr>
  <tr><td>Yến rút lông</td><td>{P[116][2]}</td><td>{P[116][3]}</td><td>{gia(116)}</td></tr>
  </tbody></table>
  <p>Xem đủ các loại khác (chân tua, yến vụn baby, yến định hình, nước yến) tại <a href="../#san-pham">bảng giá sản phẩm</a>.</p>

  <h2>Vì sao giá yến sào chênh lệch nhiều?</h2>
  <p>Giá yến sào chênh lệch chủ yếu do 3 yếu tố: mức làm sạch, độ nguyên sợi và hình dáng thành phẩm.</p>
  <h3>1. Mức độ làm sạch</h3>
  <p>Yến thô mới làm sạch sơ, còn lông và tạp chất tự nhiên nên giá mềm nhất. Yến tinh chế và yến rút lông đã được nhặt sạch lông tại xưởng, về nhà chỉ cần ngâm rồi chưng. Chi tiết từng loại có ở bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>.</p>
  <h3>2. Độ nguyên sợi</h3>
  <p>Sợi yến càng dài, dày thì khi chưng càng dai và đẹp chén. Yến rút lông giữ được sợi dài vì nhặt lông ngay trên tổ, không ngâm tơi rồi ép lại. Yến vụn, sợi ngắn có giá thấp hơn nhưng phù hợp nấu cháo, súp.</p>
  <h3>3. Hình dáng và mục đích dùng</h3>
  <p>Tổ định hình đẹp, nguyên tai thường được chọn làm quà biếu nên giá cao hơn. Nếu chỉ dùng trong gia đình, loại 1 lớp sợi vừa đã đủ tiện và dễ chưng.</p>

  <h2>Nên mua yến sào giá bao nhiêu là hợp lý?</h2>
  <p>Mức giá hợp lý phụ thuộc vào việc bạn dùng hằng ngày, nấu cho bé hay biếu tặng. Bảng gợi ý dưới đây dựa trên những gì khách của Việt Cường Nhân hay chọn.</p>
  <table><thead><tr><th>Nhu cầu</th><th>Gợi ý</th><th>Giá 100gr</th></tr></thead><tbody>
  <tr><td>Có thời gian tự nhặt lông, muốn tiết kiệm</td><td>{P[104][2]}</td><td>{gia(104)}</td></tr>
  <tr><td>Nấu cháo, súp, chưng nhanh</td><td>{P[106][2]}</td><td>{gia(106)}</td></tr>
  <tr><td>Dùng đều trong gia đình</td><td>{P[109][2]}</td><td>{gia(109)}</td></tr>
  <tr><td>Biếu tặng, muốn sợi đẹp</td><td>{P[113][2]}</td><td>{gia(113)}</td></tr>
  <tr><td>Quà cao cấp</td><td>{P[116][2]}</td><td>{gia(116)}</td></tr>
  </tbody></table>
  <p>Một hộp 100gr chưng được khoảng 20 đến 30 chén nếu mỗi chén dùng 3 đến 5 g yến khô. Cách ngâm và chưng đúng để sợi không tan xem tại bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Giá rẻ bất thường có đáng lo không?</h2>
  <p>Có. Yến tinh chế được chào giá thấp hơn nhiều so với mặt bằng chung thì nên hỏi kỹ nguồn gốc, giấy tờ và cơ sở sản xuất. Việt Cường Nhân nuôi yến và làm sạch tại xưởng từ năm 2009, cơ sở đạt HACCP, ISO 22000:2018 và GMP. Cách tự kiểm tra khi mua có ở bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật</a>.</p>

  <h2>Nước yến chưng sẵn giá bao nhiêu?</h2>
  <p>Nếu chưa có thời gian chưng, nước yến hũ là lựa chọn tiện. Giá hiện tại trên website:</p>
""" + ul(li(126), li(127), li(124)) + """
  <h2>Cách đặt mua yến sào tại Việt Cường Nhân</h2>
  <ol>
    <li>Chọn sản phẩm trong <a href="../#san-pham">bảng giá</a> và điền form đặt hàng trên website.</li>
    <li>Nhân viên gọi lại xác nhận giá và phí giao hàng theo khu vực.</li>
    <li>Nhận hàng và kiểm tra theo <a href="../chinh-sach/van-chuyen.html">chính sách vận chuyển và kiểm hàng</a>.</li>
  </ol>
  <p>Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739 để được tư vấn.</p>""",
  faq=[("100gr yến sào bao nhiêu tiền?", f"Tại Việt Cường Nhân, 100gr yến sào có giá từ {gia(104)} (yến thô bể nứt nhẹ) đến {gia(116)} (yến rút lông khô). Loại dùng phổ biến trong gia đình là {P[109][2]} giá {gia(109)}."),
       ("Vì sao yến tinh chế đắt hơn yến thô?", "Vì yến tinh chế đã được ngâm, nhặt sạch lông bằng tay, sấy và định hình tại xưởng. Phần công làm sạch này mất nhiều thời gian, đổi lại người mua chỉ cần ngâm và chưng."),
       ("1 lạng yến chưng được bao nhiêu chén?", "1 lạng (100gr) yến khô chưng được khoảng 20 đến 30 chén, tùy mỗi chén dùng 3 hay 5 g yến."),
       ("Giá yến sào trên web đã gồm phí giao hàng chưa?", "Chưa. Phí giao tính theo khu vực và khối lượng đơn, nhân viên sẽ báo khi gọi xác nhận đơn."),
       ("Mua sỉ yến sào giá thế nào?", "Giá sỉ và đại lý tùy số lượng, vui lòng nhắn Zalo 0978 094 739 để được báo giá.")]),

dict(slug="yen-sao-loai-nao-tot", cat="Yến sào", ngay="2026-10-26",
  tu_khoa="yến sào loại nào tốt, nên mua yến sào loại nào, chọn yến sào, yến tinh chế hay yến thô, yến sào biếu tặng",
  h1="Yến sào loại nào tốt? Chọn theo nhu cầu và ngân sách",
  desc=f"Yến sào loại nào tốt? Không có loại tốt nhất cho mọi người. Cách chọn yến thô, tinh chế, rút lông hay nước yến theo nhu cầu, thời gian và ngân sách.",
  lede=f"Yến sào loại nào tốt tùy vào việc bạn dùng để làm gì: dùng hằng ngày thì yến tinh chế 1 lớp sợi vừa ({gia(109)}/100gr) là cân bằng nhất, biếu tặng thì yến rút lông, còn muốn tiết kiệm và có thời gian thì yến thô. Cả ba đều là tổ yến, khác nhau ở mức làm sạch và độ nguyên sợi.",
  tom_tat=[f"Dùng hằng ngày trong gia đình: {P[109][2]}, {gia(109)}/100gr, đã sạch lông, ngâm 30–60 phút là chưng.",
           f"Muốn tiết kiệm, có thời gian nhặt lông: {P[104][2]}, {gia(104)}/100gr.",
           f"Nấu cháo, súp cho cả nhà: {P[107][2]}, {gia(107)}/100gr, sợi vụn nhưng nở nhanh.",
           f"Biếu tặng: {P[113][2]} {gia(113)} hoặc {P[114][2]} {gia(114)}/100gr, sợi dài, tổ đẹp.",
           f"Không có thời gian chưng: nước yến hũ, từ {gia(126)}/hũ VCN Nest 0.3gr."],
  body=f"""  <h2>Yến sào loại nào tốt nhất?</h2>
  <p>Không có một loại yến sào tốt nhất cho mọi người; loại tốt là loại hợp với nhu cầu, thời gian sơ chế và ngân sách của bạn. Ở xưởng Việt Cường Nhân, cùng một mẻ tổ yến từ nhà yến được chia thành nhiều loại: yến thô để nguyên lông, yến tinh chế đã nhặt sạch, yến rút lông giữ sợi dài và nước yến chưng sẵn.</p>
  <p>Khách hay hỏi "loại đắt nhất có phải tốt nhất không". Giá cao chủ yếu vì tốn công làm sạch và giữ dáng tổ đẹp, không có nghĩa là loại rẻ hơn kém an toàn. Điều quan trọng hơn là nguồn gốc rõ ràng và cơ sở làm sạch đạt chuẩn.</p>

  <h2>So sánh các loại yến sào phổ biến</h2>
  <p>Bảng dưới so sánh 5 loại yến sào theo cách làm sạch, công sơ chế ở nhà và mục đích phù hợp. Giá lấy từ bảng giá trên vietcuongnhan.com, chưa gồm phí giao hàng.</p>
  <table><thead><tr><th>Loại</th><th>Đặc điểm</th><th>Sơ chế ở nhà</th><th>Hợp với</th><th>Giá 100gr</th></tr></thead><tbody>
  <tr><td>{P[104][2]}</td><td>Còn lông, tạp chất tự nhiên</td><td>Ngâm, nhặt lông bằng nhíp khá lâu</td><td>Người có thời gian, muốn tiết kiệm</td><td>{gia(104)}</td></tr>
  <tr><td>{P[107][2]}</td><td>Sạch lông, sợi vụn ngắn</td><td>Ngâm nhanh, nở nhanh</td><td>Nấu cháo, súp</td><td>{gia(107)}</td></tr>
  <tr><td>{P[109][2]}</td><td>Sạch lông, sợi vừa, định hình 1 lớp</td><td>Ngâm 30–60 phút rồi chưng</td><td>Dùng đều trong gia đình</td><td>{gia(109)}</td></tr>
  <tr><td>{P[113][2]}</td><td>Nhặt lông trên tổ, sợi dài</td><td>Ngâm rồi chưng</td><td>Biếu tặng, thích sợi dai</td><td>{gia(113)}</td></tr>
  <tr><td>{P[114][2]}</td><td>Rút lông, giữ dáng tổ đẹp</td><td>Ngâm rồi chưng</td><td>Quà biếu trang trọng</td><td>{gia(114)}</td></tr>
  </tbody></table>
  <p>Giải thích chi tiết sự khác nhau giữa các nhóm có ở bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>.</p>

  <h2>Chọn yến sào theo nhu cầu</h2>
  <p>Cách nhanh nhất để chọn đúng loại yến sào là trả lời ba câu hỏi: ai dùng, dùng thế nào và có bao nhiêu thời gian sơ chế.</p>
  <h3>Dùng hằng ngày trong gia đình</h3>
  <p>Yến tinh chế 1 lớp sợi vừa là lựa chọn cân bằng nhất cho gia đình. Yến đã được nhặt sạch lông tại xưởng, mỗi lần chỉ cần ngâm khoảng 30 đến 60 phút rồi chưng cách thủy, sợi vẫn dai và đẹp chén.</p>
""" + ul(li(109), li(111, "Tai nhỏ, dễ chia phần cho từng lần chưng.")) + f"""
  <h3>Muốn tiết kiệm và có thời gian</h3>
  <p>Yến thô có giá mềm nhất nhưng còn lông, phải tự ngâm và nhặt bằng nhíp trước khi chưng. Loại này hợp với người đã quen sơ chế yến hoặc mua với số lượng lớn để dùng dần.</p>
""" + ul(li(104), li(101, "Ít lông hơn, đỡ công nhặt.")) + f"""
  <h3>Nấu cháo, súp hoặc món cho bé</h3>
  <p>Yến tinh chế vụn có sợi ngắn nên giá thấp hơn yến sợi, nhưng nở nhanh và dễ hòa vào cháo, súp. Với món cho trẻ nhỏ, nên hỏi ý kiến bác sĩ về độ tuổi bắt đầu và lượng dùng phù hợp.</p>
""" + ul(li(107), li(106)) + f"""
  <h3>Biếu tặng</h3>
  <p>Yến rút lông được chọn làm quà nhiều nhất vì sợi dài, tổ nguyên dáng và hộp đẹp. Yến rút lông định hình giữ hình tổ rõ hơn, phù hợp quà trang trọng.</p>
""" + ul(li(113), li(114)) + f"""
  <h3>Không có thời gian chưng</h3>
  <p>Nước yến chưng sẵn là lựa chọn tiện nhất: mở nắp dùng ngay, mang theo đi làm hay đi xa. Nước yến chưng thủ công dùng yến tươi, còn dòng VCN Nest sản xuất tại nhà máy nước yến của Việt Cường Nhân.</p>
""" + ul(li(124), li(126), li(127)) + f"""
  <p>Cách dùng và bảo quản nước yến có ở bài <a href="nuoc-yen-chung-san-cach-dung-bao-quan.html">nước yến chưng sẵn: cách dùng và bảo quản</a>.</p>

  <h2>Dấu hiệu yến sào tốt khi mua</h2>
  <p>Yến sào tốt có sợi yến không đều tự nhiên, màu trắng ngà, khi ngâm nở dần và vẫn giữ sợi, có nguồn gốc và giấy tờ cơ sở sản xuất rõ ràng. Không nên chỉ dựa vào một dấu hiệu, mà kết hợp nhiều cách kiểm tra.</p>
  <ul>
    <li><b>Nhìn:</b> sợi to nhỏ đan xen, không trắng tinh bất thường, không bóng như nhựa.</li>
    <li><b>Ngâm:</b> yến nở mềm, sợi tơi, nước ngâm không đục bất thường.</li>
    <li><b>Chưng:</b> sợi dai, không tan hết thành nước khi chưng đúng thời gian 20–30 phút.</li>
    <li><b>Giấy tờ:</b> hỏi người bán tên cơ sở sản xuất, chứng nhận an toàn thực phẩm còn hạn.</li>
  </ul>
  <p>Chi tiết từng bước kiểm tra xem tại bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>. Việt Cường Nhân nuôi yến và làm sạch tại xưởng từ năm 2009, cơ sở đạt HACCP, ISO 22000:2018 và GMP; ý nghĩa các chứng nhận này có ở bài <a href="chung-nhan-haccp-iso-22000-gmp-la-gi.html">HACCP, ISO 22000 và GMP nghĩa là gì</a>.</p>

  <h2>Mua bao nhiêu là vừa?</h2>
  <p>Hộp 100gr yến khô là quy cách phổ biến nhất, chưng được khoảng 20 đến 30 chén nếu mỗi chén dùng 3 đến 5 g. Gia đình dùng 2 đến 3 lần mỗi tuần thường dùng hết một hộp trong vài tháng; bảo quản yến khô trong hộp kín, nơi khô ráo. So sánh giá đầy đủ các loại xem tại bài <a href="gia-yen-sao-bao-nhieu-tien.html">giá yến sào bao nhiêu tiền 100gr</a>.</p>

  <h2>Đặt mua yến sào tại Việt Cường Nhân</h2>
  <ol>
    <li>Chọn loại yến trong <a href="../#san-pham">bảng giá sản phẩm</a> và điền form đặt hàng.</li>
    <li>Nhân viên gọi lại xác nhận đơn, phí giao hàng theo khu vực.</li>
    <li>Nhận và kiểm hàng theo <a href="../chinh-sach/van-chuyen.html">chính sách vận chuyển và kiểm hàng</a>.</li>
  </ol>
  <p>Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739 để được tư vấn.</p>""",
  faq=[("Yến sào loại nào tốt nhất?", f"Không có loại tốt nhất cho mọi người. Dùng hằng ngày nên chọn {P[109][2]} ({gia(109)}/100gr), biếu tặng chọn yến rút lông, muốn tiết kiệm và có thời gian thì chọn yến thô."),
       ("Nên mua yến thô hay yến tinh chế?", "Nếu có thời gian ngâm và nhặt lông thì yến thô tiết kiệm hơn. Nếu muốn tiện, ngâm xong là chưng, nên chọn yến tinh chế đã nhặt sạch lông tại xưởng."),
       ("Yến sào đắt nhất có phải tốt nhất không?", "Không hẳn. Giá cao chủ yếu do công làm sạch, độ dài sợi và dáng tổ đẹp. Quan trọng hơn là nguồn gốc rõ ràng và cơ sở sản xuất đạt chuẩn an toàn thực phẩm."),
       ("Mua yến sào biếu nên chọn loại nào?", f"Thường chọn {P[113][2]} ({gia(113)}/100gr) hoặc {P[114][2]} ({gia(114)}/100gr) vì sợi dài và tổ nguyên dáng đẹp."),
       ("Yến vụn có kém hơn yến sợi không?", "Yến vụn là tổ yến sạch lông nhưng sợi ngắn hơn, nên giá thấp hơn. Loại này hợp nấu cháo, súp vì nở nhanh và dễ hòa vào món ăn.")]),
dict(slug="100gr-yen-chung-duoc-bao-nhieu-chen", cat="Yến sào", ngay="2026-10-27",
  tu_khoa="100gr yến chưng được bao nhiêu chén, 1 chén yến bao nhiêu gram, 100gr yến ăn được bao lâu, định lượng chưng yến",
  h1="100gr yến chưng được bao nhiêu chén, dùng được bao lâu?",
  desc="100gr yến chưng được bao nhiêu chén? Khoảng 20–30 chén nếu mỗi chén 3–5 g yến khô. Bảng định lượng, số tuần dùng và chi phí mỗi chén theo từng loại yến.",
  lede="100gr yến tinh chế chưng được khoảng 20 đến 30 chén, vì mỗi chén thường dùng 3 đến 5 g yến khô với 150 đến 200 ml nước. Nếu ăn 2 đến 3 lần mỗi tuần, một hộp 100gr dùng được khoảng 2 đến 3 tháng.",
  tom_tat=["100gr yến tinh chế chưng được khoảng 20–30 chén, mỗi chén 3–5 g yến khô.",
           "Mỗi chén dùng 150–200 ml nước, chưng cách thủy 20–30 phút.",
           "Ăn 2–3 lần mỗi tuần, mỗi lần 4 g: một hộp 100gr dùng khoảng 8–12 tuần.",
           f"Với {P[109][2]} ({gia(109)}/100gr), mỗi chén 4 g tốn khoảng {vnd(int(round(P[109][4]*4/100, -3)))} tiền yến.",
           "Yến thô còn lông nên sau khi nhặt sạch sẽ ra ít chén hơn yến tinh chế cùng khối lượng."],
  body=f"""  <h2>100gr yến chưng được bao nhiêu chén?</h2>
  <p>100gr yến tinh chế chưng được khoảng 20 đến 30 chén, tùy mỗi chén bạn dùng bao nhiêu gam yến khô. Mức phổ biến ở các gia đình là 3 đến 5 g yến khô cho một chén khoảng 150 đến 200 ml.</p>
  <p>Ở xưởng Việt Cường Nhân, câu khách hay hỏi nhất sau giá là "một hộp 100gr ăn được mấy lần". Con số chính xác phụ thuộc vào loại yến, độ đặc bạn thích và người dùng là ai, nên bảng dưới tính sẵn cho từng mức.</p>
  <table><thead><tr><th>Yến khô mỗi chén</th><th>Số chén từ 100gr</th><th>Độ đặc</th><th>Thường dùng cho</th></tr></thead><tbody>
  <tr><td>3 g</td><td>khoảng 33 chén</td><td>Loãng, nhiều nước</td><td>Người mới ăn, trẻ lớn (hỏi bác sĩ trước)</td></tr>
  <tr><td>4 g</td><td>25 chén</td><td>Vừa</td><td>Dùng đều trong gia đình</td></tr>
  <tr><td>5 g</td><td>20 chén</td><td>Đặc, nhiều sợi</td><td>Người thích chén yến đặc sợi</td></tr>
  </tbody></table>
  <p>Cách cân nhanh không cần cân điện tử: một tai yến tinh chế 1 lớp loại 18–20 tai/100gr nặng khoảng 5 g, đủ cho một chén đặc hoặc chia đôi cho hai chén loãng.</p>

  <h2>1 chén yến bao nhiêu gram yến khô và bao nhiêu nước?</h2>
  <p>Một chén yến chuẩn thường dùng 3 đến 5 g yến khô và 150 đến 200 ml nước lọc. Yến khô khi ngâm sẽ hút nước và nở ra nhiều lần, nên lượng yến khô nhìn ít nhưng chén yến sau khi chưng vẫn đầy sợi.</p>
  <ul>
    <li><b>Yến khô:</b> 3–5 g cho người lớn.</li>
    <li><b>Nước:</b> 150–200 ml; muốn sệt thì giảm nước, muốn thanh thì tăng nước.</li>
    <li><b>Đường phèn:</b> tùy khẩu vị, cho vào 5 phút cuối.</li>
    <li><b>Thời gian:</b> ngâm 30–60 phút, chưng cách thủy 20–30 phút.</li>
  </ul>
  <p>Các bước chi tiết có ở bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>. Trẻ nhỏ, phụ nữ mang thai, người lớn tuổi hoặc người có bệnh nền nên hỏi bác sĩ về lượng dùng phù hợp.</p>

  <h2>100gr yến ăn được bao lâu?</h2>
  <p>Nếu dùng 2 đến 3 lần mỗi tuần, mỗi lần 4 g, một hộp 100gr yến dùng được khoảng 8 đến 12 tuần, tức 2 đến 3 tháng cho một người. Thời gian ngắn lại nếu cả nhà cùng ăn hoặc dùng mỗi ngày.</p>
  <table><thead><tr><th>Cách dùng (4 g/chén)</th><th>Chén mỗi tuần</th><th>100gr dùng được</th></tr></thead><tbody>
  <tr><td>1 người, 2 lần/tuần</td><td>2</td><td>khoảng 12 tuần</td></tr>
  <tr><td>1 người, 3 lần/tuần</td><td>3</td><td>khoảng 8 tuần</td></tr>
  <tr><td>2 người, 3 lần/tuần</td><td>6</td><td>khoảng 4 tuần</td></tr>
  <tr><td>1 người, mỗi ngày</td><td>7</td><td>khoảng 3,5 tuần</td></tr>
  </tbody></table>
  <p>Yến khô bảo quản trong hộp kín, nơi khô ráo, tránh nắng nên mua hộp 100gr để dùng dần là hợp lý. Yến đã chưng thì để nguội, đậy kín, cất ngăn mát và dùng trong vài ngày; không nên chưng một lần quá nhiều.</p>

  <h2>Số chén khác nhau theo loại yến</h2>
  <p>Cùng 100gr, yến tinh chế và yến rút lông cho số chén gần như nhau, còn yến thô cho ít chén hơn vì một phần khối lượng là lông và tạp chất bị nhặt bỏ khi sơ chế. Độ dài sợi chủ yếu ảnh hưởng đến cảm giác ăn và độ đẹp chén, không làm thay đổi nhiều số chén.</p>
  <table><thead><tr><th>Loại yến</th><th>Sơ chế</th><th>Số chén từ 100gr (4 g/chén)</th><th>Giá 100gr</th></tr></thead><tbody>
  <tr><td>{P[104][2]}</td><td>Ngâm và nhặt lông bằng nhíp</td><td>Ít hơn 25 chén, tùy lượng lông</td><td>{gia(104)}</td></tr>
  <tr><td>{P[106][2]}</td><td>Ngâm nhanh, sợi vụn</td><td>khoảng 25 chén</td><td>{gia(106)}</td></tr>
  <tr><td>{P[109][2]}</td><td>Ngâm 30–60 phút rồi chưng</td><td>khoảng 25 chén</td><td>{gia(109)}</td></tr>
  <tr><td>{P[113][2]}</td><td>Ngâm rồi chưng, sợi dài</td><td>khoảng 25 chén</td><td>{gia(113)}</td></tr>
  </tbody></table>
  <p>Sự khác nhau giữa các nhóm yến được giải thích ở bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>.</p>

  <h2>Mỗi chén yến tốn bao nhiêu tiền?</h2>
  <p>Chi phí tiền yến cho mỗi chén bằng giá hộp 100gr chia cho số chén. Với mức 4 g mỗi chén (25 chén/100gr), chi phí ước tính theo bảng giá hiện tại của Việt Cường Nhân như sau, chưa tính đường phèn và nguyên liệu chưng kèm:</p>
  <ul>
    <li>{P[106][2]}: khoảng {vnd(int(round(P[106][4]/25, -3)))} mỗi chén.</li>
    <li>{P[109][2]}: khoảng {vnd(int(round(P[109][4]/25, -3)))} mỗi chén.</li>
    <li>{P[113][2]}: khoảng {vnd(int(round(P[113][4]/25, -3)))} mỗi chén.</li>
  </ul>
  <p>Nếu không có thời gian chưng, nước yến hũ là lựa chọn khác: {P[124][2]} giá {gia(124)}/{P[124][3].lower()}. Bảng giá đầy đủ các loại xem tại bài <a href="gia-yen-sao-bao-nhieu-tien.html">giá yến sào bao nhiêu tiền 100gr</a>.</p>

  <h2>Mẹo chia yến để dùng đều cả hộp</h2>
  <ol>
    <li><b>Chia phần ngay khi mở hộp:</b> tách yến thành các phần 4 g, để trong túi hoặc hộp nhỏ kín.</li>
    <li><b>Chọn yến dạng tai nhỏ</b> nếu muốn khỏi cân: mỗi tai là một phần định sẵn.</li>
    <li><b>Chưng vừa đủ ăn trong 2–3 ngày</b>, cất ngăn mát, tránh chưng cả tuần một lần.</li>
    <li><b>Ghi ngày mở hộp</b> để biết tốc độ dùng và lần sau mua bao nhiêu cho đủ.</li>
  </ol>

  <h2>Yến phù hợp để chưng tại nhà</h2>
  <p>Chưa biết chọn loại nào, xem bài <a href="yen-sao-loai-nao-tot.html">yến sào loại nào tốt</a>. Các loại yến đã nhặt sạch lông tại xưởng Việt Cường Nhân, ngâm xong là chưng:</p>
""" + ul(li(109, "Sợi vừa, dùng đều trong gia đình."), li(111, "Tai nhỏ khoảng 5 g, khỏi cần cân."), li(106, "Hợp nấu cháo, súp."), li(113, "Sợi dài, hợp biếu tặng.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>, giá chưa gồm phí giao hàng. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739 để được tư vấn.</p>""",
  faq=[("100gr yến chưng được bao nhiêu chén?", "Khoảng 20 đến 30 chén. Mỗi chén thường dùng 3 đến 5 g yến khô; dùng 4 g mỗi chén thì 100gr được 25 chén."),
       ("1 chén yến cần bao nhiêu gram yến khô?", "Thường 3 đến 5 g yến khô với 150 đến 200 ml nước. Trẻ nhỏ, phụ nữ mang thai hoặc người có bệnh nền nên hỏi bác sĩ về lượng phù hợp."),
       ("100gr yến ăn được bao lâu?", "Một người ăn 2 đến 3 lần mỗi tuần, mỗi lần 4 g thì 100gr dùng khoảng 8 đến 12 tuần. Cả nhà cùng ăn thì hết nhanh hơn."),
       ("Yến thô 100gr chưng được bao nhiêu chén?", "Ít hơn yến tinh chế cùng khối lượng, vì phần lông và tạp chất bị nhặt bỏ khi sơ chế. Số chén cụ thể tùy lượng lông của từng tổ."),
       ("Yến đã chưng để được bao lâu?", "Để nguội, đậy kín, cất ngăn mát và dùng trong vài ngày. Nên chưng vừa đủ ăn trong 2 đến 3 ngày thay vì chưng cả tuần.")]),
dict(slug="an-yen-luc-nao-tot-nhat", cat="Yến sào", ngay="2026-10-27",
  tu_khoa="ăn yến lúc nào tốt nhất, ăn yến buổi sáng hay buổi tối, uống nước yến lúc nào, ăn yến trước hay sau bữa ăn",
  h1="Ăn yến lúc nào trong ngày là hợp lý?",
  desc="Ăn yến lúc nào tốt nhất? Gợi ý thời điểm dùng yến chưng và nước yến hũ trong ngày: sáng, giữa buổi hay tối, trước hay sau bữa ăn, kèm lưu ý cho từng người.",
  lede="Không có một giờ duy nhất bắt buộc phải ăn yến. Nhiều gia đình chọn buổi sáng lúc bụng còn nhẹ hoặc buổi tối trước khi ngủ khoảng 1 tiếng, cách bữa ăn chính 30 đến 60 phút, và quan trọng hơn là dùng đều đặn.",
  tom_tat=["Thời điểm phổ biến: buổi sáng sau khi thức dậy, hoặc buổi tối trước khi ngủ khoảng 1 tiếng.",
           "Nên ăn cách bữa ăn chính 30–60 phút, không ăn ngay khi vừa no.",
           "Dùng đều 2–3 lần mỗi tuần, mỗi lần 3–5 g yến khô, quan trọng hơn chọn đúng giờ.",
           f"Bận rộn thì dùng nước yến hũ chưng sẵn, ví dụ {P[126][2]} giá {gia(126)}/hũ.",
           "Trẻ nhỏ, phụ nữ mang thai, người có bệnh nền nên hỏi bác sĩ về thời điểm và lượng dùng."],
  body=f"""  <h2>Ăn yến lúc nào tốt nhất?</h2>
  <p>Thời điểm ăn yến hợp lý nhất là lúc bạn có thể dùng đều đặn mỗi tuần: buổi sáng khi bụng còn nhẹ hoặc buổi tối trước khi đi ngủ khoảng 1 tiếng. Yến là thực phẩm, không có giờ "uống thuốc" cố định, nên hãy chọn khung giờ hợp nếp sinh hoạt của gia đình.</p>
  <p>Ở xưởng Việt Cường Nhân, khách hay hỏi "ăn sáng hay ăn tối mới tốt". Câu trả lời ngắn: cả hai đều được, miễn là không ăn ngay sau bữa no và giữ thói quen dùng đều.</p>
  <table><thead><tr><th>Thời điểm</th><th>Phù hợp với</th><th>Lưu ý</th></tr></thead><tbody>
  <tr><td>Sáng, sau khi thức dậy</td><td>Người dậy sớm, muốn bắt đầu ngày với món nhẹ</td><td>Ăn trước bữa sáng chính khoảng 30 phút</td></tr>
  <tr><td>Giữa buổi (10h hoặc 15h)</td><td>Dân văn phòng, dùng nước yến hũ</td><td>Thay cho món ăn vặt, không ăn sát bữa trưa</td></tr>
  <tr><td>Tối, trước khi ngủ khoảng 1 tiếng</td><td>Người bận ban ngày, cả nhà ăn cùng</td><td>Chén nhỏ, ít đường; không ăn quá khuya</td></tr>
  </tbody></table>

  <h2>Ăn yến buổi sáng hay buổi tối?</h2>
  <p>Ăn yến buổi sáng hay buổi tối đều được; khác nhau chủ yếu ở sự tiện lợi. Buổi sáng hợp với người có thời gian chuẩn bị từ tối hôm trước, buổi tối hợp với gia đình muốn ăn chung sau giờ làm.</p>
  <ul>
    <li><b>Buổi sáng:</b> chưng sẵn từ tối, sáng hâm ấm cách thủy vài phút là dùng được.</li>
    <li><b>Buổi tối:</b> chưng xong ăn ấm; nên dùng chén nhỏ, ít đường phèn để bụng nhẹ trước khi ngủ.</li>
    <li><b>Không nên:</b> ăn yến thay hẳn bữa chính, hoặc ăn quá khuya ngay trước khi nằm.</li>
  </ul>

  <h2>Ăn yến trước hay sau bữa ăn?</h2>
  <p>Nên ăn yến khi bụng không quá no, tức là trước bữa ăn chính khoảng 30 phút hoặc sau bữa ăn khoảng 1 tiếng. Ăn ngay sau bữa no dễ gây cảm giác đầy bụng và khó ăn hết chén.</p>
  <p>Một chén yến chuẩn dùng 3 đến 5 g yến khô với 150 đến 200 ml nước. Cách tính số chén từ một hộp có ở bài <a href="100gr-yen-chung-duoc-bao-nhieu-chen.html">100gr yến chưng được bao nhiêu chén</a>.</p>

  <h2>Nước yến hũ uống lúc nào?</h2>
  <p>Nước yến hũ chưng sẵn uống được bất cứ lúc nào trong ngày, tiện nhất là giữa buổi sáng hoặc giữa buổi chiều thay cho món ăn vặt. Hũ chưa mở để nơi khô mát; mở nắp rồi thì nên uống hết trong ngày.</p>
""" + ul(li(126, "Hũ nhỏ, tiện mang đi làm."), li(124, "Chưng thủ công từ yến tươi.")) + f"""
  <p>Cách bảo quản và chọn loại nước yến xem thêm ở bài <a href="nuoc-yen-chung-san-cach-dung-bao-quan.html">nước yến chưng sẵn: chọn loại nào, dùng và bảo quản ra sao</a>.</p>

  <h2>Lưu ý theo từng người dùng</h2>
  <ul>
    <li><b>Người lớn khỏe mạnh:</b> 2 đến 3 lần mỗi tuần, mỗi lần 3 đến 5 g yến khô, vào sáng hoặc tối đều được.</li>
    <li><b>Người lớn tuổi:</b> chưng loãng hơn, dùng chén nhỏ, ăn ấm vào buổi sáng hoặc đầu giờ tối.</li>
    <li><b>Trẻ nhỏ, phụ nữ mang thai, người có bệnh nền hoặc đang dùng thuốc:</b> hỏi bác sĩ trước về việc có nên dùng, thời điểm và lượng dùng.</li>
    <li><b>Người ăn kiêng đường:</b> chưng yến không đường hoặc rất ít đường phèn.</li>
  </ul>

  <h2>Mẹo để ăn yến đều đặn</h2>
  <ol>
    <li><b>Chọn một khung giờ cố định</b> trong tuần, ví dụ sáng thứ Hai, Tư, Sáu.</li>
    <li><b>Chưng sẵn cho 2 đến 3 ngày</b>, để nguội, đậy kín, cất ngăn mát và hâm ấm khi ăn.</li>
    <li><b>Chia yến khô thành phần 4 g</b> ngay khi mở hộp để khỏi cân mỗi lần.</li>
    <li><b>Ngày bận</b> thì thay bằng một hũ nước yến chưng sẵn.</li>
  </ol>
  <p>Các bước ngâm và chưng xem ở bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Yến phù hợp để dùng hằng tuần</h2>
""" + ul(li(109, "Sợi vừa, ngâm xong là chưng."), li(126), li(124)) + """
  <p>Chưa biết chọn loại nào, xem bài <a href="yen-sao-loai-nao-tot.html">yến sào loại nào tốt</a> hoặc <a href="../#san-pham">bảng giá sản phẩm</a> (giá chưa gồm phí giao hàng). Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Ăn yến lúc nào tốt nhất trong ngày?", "Buổi sáng khi bụng còn nhẹ hoặc buổi tối trước khi ngủ khoảng 1 tiếng đều được. Quan trọng là dùng đều 2 đến 3 lần mỗi tuần và không ăn ngay sau bữa no."),
       ("Ăn yến buổi tối có được không?", "Được. Nên ăn trước khi ngủ khoảng 1 tiếng, dùng chén nhỏ và ít đường phèn, không ăn quá khuya."),
       ("Nên ăn yến trước hay sau bữa ăn?", "Trước bữa ăn chính khoảng 30 phút hoặc sau bữa ăn khoảng 1 tiếng, khi bụng không quá no."),
       ("Nước yến hũ uống lúc nào?", "Uống lúc nào trong ngày cũng được, tiện nhất là giữa buổi sáng hoặc giữa buổi chiều. Hũ đã mở nên uống hết trong ngày."),
       ("Bà bầu và trẻ nhỏ ăn yến lúc nào?", "Nên hỏi bác sĩ trước về việc có nên dùng, thời điểm và lượng dùng phù hợp với từng người.")]),
dict(slug="nam-dong-trung-ha-thao-tiem-ga-ac", cat="Đông trùng hạ thảo", ngay="2026-10-28",
  tu_khoa="nấm đông trùng hạ thảo tiềm gà ác, gà ác tiềm đông trùng hạ thảo, cách nấu gà ác tiềm, gà ác hầm táo đỏ hạt sen",
  h1="Nấm đông trùng hạ thảo tiềm gà ác: cách nấu tại nhà",
  desc="Cách nấu nấm đông trùng hạ thảo tiềm gà ác với táo đỏ, hạt sen, kỷ tử: nguyên liệu, 6 bước làm, thời gian hầm và mẹo giữ nước dùng trong, ngọt thanh.",
  lede="Nấm đông trùng hạ thảo tiềm gà ác là món hầm gồm gà ác, đông trùng hạ thảo sấy khô, táo đỏ, hạt sen, kỷ tử và vài lát sâm, nấu lửa nhỏ khoảng 1 tiếng cho nước dùng vàng trong, ngọt thanh. Món này làm được bằng nồi thường hoặc nồi áp suất, chỉ cần 6 bước.",
  video=dict(yt="vFkUoRGhTMo", ten="Nấm đông trùng hạ thảo tiềm gà ác – cách nấu tại nhà", ngay="2026-10-28", thoi_luong="PT1M12S"),
  tom_tat=["Nguyên liệu cho 3–4 người: 1 con gà ác 400–500 g, 5–10 g nấm đông trùng hạ thảo sấy khô, 6–8 quả táo đỏ, 30 g hạt sen, 1 muỗng kỷ tử, 2–3 lát sâm.",
           "Gà ác chần sơ 2–3 phút cho sạch, rồi hầm với khoảng 1–1,2 lít nước.",
           "Táo đỏ và kỷ tử cho vào khi nước sôi; đông trùng hạ thảo cho sau, hầm lửa nhỏ thêm 30–40 phút.",
           "Tổng thời gian khoảng 60–75 phút với nồi thường, 25–30 phút với nồi áp suất.",
           f"Nấm đông trùng hạ thảo tại Việt Cường Nhân: loại gãy {gia(138)}/100gr, loại cây {gia(136)}/100gr; táo đỏ Tân Cương hộp 350gr từ {gia(147)}."],
  body=f"""  <h2>Nguyên liệu nấm đông trùng hạ thảo tiềm gà ác</h2>
  <p>Một nồi nấm đông trùng hạ thảo tiềm gà ác cho 3–4 người cần 1 con gà ác nhỏ và một ít dược liệu khô quen thuộc. Gà ác (gà đen) thịt chắc, xương nhỏ nên hầm lâu không bị bở.</p>
  <table><thead><tr><th>Nguyên liệu</th><th>Định lượng</th><th>Ghi chú</th></tr></thead><tbody>
  <tr><td>Gà ác</td><td>1 con, 400–500 g</td><td>Để nguyên con hoặc chặt đôi</td></tr>
  <tr><td>Nấm đông trùng hạ thảo sấy khô</td><td>5–10 g</td><td>Loại gãy dùng nấu ăn là đủ</td></tr>
  <tr><td>Táo đỏ</td><td>6–8 quả</td><td>Rửa sạch, có thể khứa nhẹ</td></tr>
  <tr><td>Hạt sen</td><td>30 g</td><td>Hạt sen khô nên ngâm trước 1–2 tiếng</td></tr>
  <tr><td>Kỷ tử</td><td>1 muỗng canh</td><td>Rửa nhanh, cho vào cuối</td></tr>
  <tr><td>Sâm</td><td>2–3 lát mỏng</td><td>Không bắt buộc</td></tr>
  <tr><td>Nước, muối</td><td>1–1,2 lít nước, muối vừa ăn</td><td>Có thể thay bằng nước dùng gà</td></tr>
  </tbody></table>

  <h2>Cách nấu nấm đông trùng hạ thảo tiềm gà ác (6 bước)</h2>
  <p>Cách nấu gà ác tiềm đông trùng hạ thảo gồm 6 bước: chần gà, hầm gà, thêm táo đỏ và kỷ tử, thêm đông trùng, gắp gà ra bát và hoàn thiện. Video ở đầu bài làm đúng theo các bước này.</p>
  <ol>
    <li><b>Chần sơ gà ác.</b> Cho gà vào nồi nước sôi 2–3 phút, vớt ra rửa lại nước sạch để nước dùng trong, không hôi.</li>
    <li><b>Hầm gà.</b> Cho gà vào nồi hoặc thố, đổ 1–1,2 lít nước, thêm hạt sen đã ngâm, đun sôi rồi hạ lửa nhỏ.</li>
    <li><b>Thêm táo đỏ, kỷ tử.</b> Khi nước sôi lại, thả táo đỏ để nước ngọt thanh, thêm kỷ tử và vài lát sâm.</li>
    <li><b>Cho nấm đông trùng hạ thảo.</b> Thả đông trùng vào, giữ lửa nhỏ liu riu, hầm thêm 30–40 phút cho gà mềm, ngấm vị.</li>
    <li><b>Gắp gà ra bát lớn.</b> Nêm muối vừa ăn, gắp gà ra bát hoặc thố.</li>
    <li><b>Hoàn thiện.</b> Xếp hạt sen, táo đỏ, đông trùng lên trên, chan nước dùng nóng là ăn được.</li>
  </ol>

  <h2>Thời gian hầm bao lâu?</h2>
  <p>Gà ác tiềm đông trùng hạ thảo hầm tổng khoảng 60–75 phút với nồi thường, hoặc 25–30 phút với nồi áp suất. Nếu dùng nồi áp suất, nên cho đông trùng và kỷ tử sau khi xả van, đun sôi lại 5–10 phút để nấm giữ màu cam, không bị nát.</p>
  <ul>
    <li><b>Chưng cách thủy trong thố:</b> khoảng 1,5–2 tiếng, nước dùng trong nhất.</li>
    <li><b>Nồi thường:</b> 60–75 phút, lửa nhỏ, hớt bọt khi sôi.</li>
    <li><b>Nồi áp suất:</b> 25–30 phút, tiện cho ngày bận.</li>
  </ul>

  <h2>Mẹo để món tiềm ngon, nước dùng trong</h2>
  <ul>
    <li>Luôn chần gà trước và hớt bọt khi nước sôi lần đầu.</li>
    <li>Không cho đông trùng quá sớm; cho ở nửa sau thời gian hầm để nấm giữ màu và độ giòn nhẹ.</li>
    <li>Táo đỏ khứa nhẹ vỏ để ra vị ngọt nhanh hơn, nhờ vậy bớt nêm đường.</li>
    <li>Nêm nhạt, để vị ngọt tự nhiên của gà và táo đỏ.</li>
  </ul>
  <p>Các cách dùng khác của đông trùng (pha trà, nấu canh, chưng cùng yến) có ở bài <a href="cach-dung-dong-trung-ha-thao.html">cách dùng nấm đông trùng hạ thảo sấy khô</a>. Cách chọn táo đỏ theo size xem bài <a href="tao-do-tan-cuong-cach-chon-va-mon-ngon.html">táo đỏ Tân Cương: cách chọn size và món ngon</a>.</p>

  <h2>Chọn đông trùng hạ thảo và táo đỏ cho món tiềm</h2>
  <p>Để nấu ăn trong gia đình, nấm đông trùng hạ thảo loại gãy là lựa chọn tiết kiệm vì vị như loại cây, chỉ khác cọng ngắn. Loại cây cọng nguyên đẹp hơn, hợp khi nấu đãi khách hoặc biếu tặng. Giá dưới đây lấy từ bảng giá website Việt Cường Nhân, chưa gồm phí giao hàng.</p>
""" + ul(li(138, "Hợp nấu tiềm, nấu canh hằng ngày."), li(136, "Cọng nguyên, đẹp, hợp đãi khách, biếu tặng."), li(140), li(146, "Quả to, cùi dày, hợp món hầm."), li(145)) + """
  <p>Cần thêm kỷ tử, sâm hoặc hạt sen để nấu cùng, anh chị nhắn Zalo 0978 094 739 để Việt Cường Nhân báo hàng có sẵn. Xem toàn bộ <a href="../#san-pham">bảng giá sản phẩm</a> để đặt hàng.</p>""",
  faq=[("Gà ác tiềm đông trùng hạ thảo nấu bao lâu?", "Khoảng 60–75 phút với nồi thường, 25–30 phút với nồi áp suất, hoặc 1,5–2 tiếng nếu chưng cách thủy trong thố."),
       ("Nấu gà ác tiềm cần bao nhiêu đông trùng hạ thảo?", "Một con gà ác 400–500 g dùng khoảng 5–10 g nấm đông trùng hạ thảo sấy khô là vừa cho 3–4 người."),
       ("Khi nào cho đông trùng hạ thảo vào nồi?", "Cho ở nửa sau thời gian hầm, khoảng 30–40 phút trước khi tắt bếp, để nấm giữ màu cam và không bị nát."),
       ("Dùng loại đông trùng nào để nấu tiềm?", "Loại gãy đủ cho nấu ăn hằng ngày và giá mềm hơn; loại cây cọng nguyên hợp khi đãi khách hoặc biếu tặng."),
       ("Có thể thay gà ác bằng gà ta không?", "Được. Gà ta thịt to hơn nên tăng nước và thời gian hầm thêm khoảng 15–20 phút.")]),
dict(slug="yen-sao-binh-duong-di-an-mua-o-dau", cat="Yến sào", ngay="2026-10-29",
  tu_khoa="yến sào Dĩ An Bình Dương, mua yến sào ở Dĩ An, yến sào Bình Dương, xưởng yến sào Dĩ An, cửa hàng yến sào Tân Đông Hiệp",
  h1="Mua yến sào ở Dĩ An, Bình Dương cũ: địa chỉ xưởng",
  desc="Mua yến sào Dĩ An Bình Dương ở đâu? Địa chỉ nhà máy, cơ sở đóng gói Việt Cường Nhân tại Tân Đông Hiệp, Đông Hòa, cách đặt hàng, giao nhận và bảng giá.",
  lede="Ở Dĩ An (Bình Dương cũ, nay thuộc TP. Hồ Chí Minh), bạn có thể mua yến sào trực tiếp tại xưởng Việt Cường Nhân: nhà máy ở 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp và cơ sở đóng gói ở 261-263 Võ Thị Sáu, Phường Đông Hòa. Nên gọi hoặc nhắn Zalo 0978 094 739 trước khi đến để được hẹn giờ và chuẩn bị sẵn hàng.",
  tom_tat=["Việt Cường Nhân thành lập năm 2009, trụ sở tại Phường Dĩ An, xưởng tinh chế yến đầu tiên hoạt động ở Dĩ An từ năm 2019.",
           "Nhà máy: 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp; cơ sở đóng gói: 261-263 Võ Thị Sáu, KP. Tây A, Phường Đông Hòa, TP. Hồ Chí Minh.",
           "Gọi hoặc nhắn Zalo 0978 094 739 trước khi đến để hẹn giờ; đặt online thì giao TP. Hồ Chí Minh và khu vực lân cận trong 1–2 ngày làm việc.",
           f"Giá tham khảo: {P[109][2]} {gia(109)}/100gr, {P[101][2]} {gia(101)}/100gr, {P[124][2]} {gia(124)}/hũ.",
           "Xưởng đạt HACCP, ISO 22000:2018 và GMP; giá trên web chưa gồm phí giao hàng."],
  body=f"""  <h2>Mua yến sào ở Dĩ An, Bình Dương ở đâu?</h2>
  <p>Người ở Dĩ An có thể mua yến sào ngay tại xưởng của Việt Cường Nhân, doanh nghiệp yến sào có trụ sở và nhà máy trong khu vực Dĩ An (trước đây thuộc tỉnh Bình Dương, nay thuộc TP. Hồ Chí Minh). Mua tại xưởng giúp bạn xem tận mắt sợi yến, hỏi trực tiếp cách sơ chế và nhận hàng trong ngày.</p>
  <p>Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân thành lập tháng 6 năm 2009. Năm 2019, công ty đưa vào hoạt động xưởng tinh chế yến sào đầu tiên tại Dĩ An; đến năm 2022 xây thêm nhà máy nước yến chưng sẵn. Vì vậy yến bán ở đây là hàng xưởng tự làm sạch, đóng gói, không qua nhiều khâu trung gian.</p>

  <h2>Địa chỉ xưởng yến sào Việt Cường Nhân tại Dĩ An</h2>
  <p>Việt Cường Nhân có 3 địa điểm trong khu vực Dĩ An cũ, đều dùng chung số điện thoại và Zalo 0978 094 739. Sau khi sắp xếp lại đơn vị hành chính, các địa chỉ được ghi theo phường mới thuộc TP. Hồ Chí Minh.</p>
  <table><thead><tr><th>Địa điểm</th><th>Địa chỉ</th><th>Ghi chú</th></tr></thead><tbody>
  <tr><td>Nhà máy</td><td>511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp, TP. Hồ Chí Minh</td><td>Nơi sản xuất yến tinh chế, nước yến chưng</td></tr>
  <tr><td>Cơ sở đóng gói</td><td>261-263 Võ Thị Sáu, KP. Tây A, Phường Đông Hòa, TP. Hồ Chí Minh</td><td>Đóng gói, chuẩn bị đơn hàng</td></tr>
  <tr><td>Trụ sở công ty</td><td>Số 24/22 Khu phố Thống Nhất 1, Phường Dĩ An, TP. Hồ Chí Minh</td><td>Trụ sở đăng ký kinh doanh, MST 3701518691</td></tr>
  </tbody></table>
  <p>Khi tìm trên bản đồ, bạn có thể gõ cả tên phường mới lẫn tên cũ (Tân Đông Hiệp, Đông Hòa thuộc Dĩ An, Bình Dương) để ra đúng vị trí.</p>

  <h3>Nên gọi trước khi đến</h3>
  <p>Hãy gọi hoặc nhắn Zalo 0978 094 739 trước khi ghé để được hẹn giờ, báo địa điểm phù hợp và chuẩn bị sẵn loại yến bạn cần. Xưởng là nơi sản xuất, nên hẹn trước giúp bạn không phải chờ và có người tư vấn trực tiếp.</p>

  <h2>Mua yến tại xưởng có gì khác mua online?</h2>
  <p>Mua tại xưởng Dĩ An phù hợp khi bạn muốn xem sợi yến trước khi chọn; mua online phù hợp khi bạn đã biết loại cần mua và muốn giao tận nhà. Giá sản phẩm lấy theo cùng một bảng giá trên website.</p>
  <table><thead><tr><th>Tiêu chí</th><th>Đến xưởng</th><th>Đặt online</th></tr></thead><tbody>
  <tr><td>Xem sợi yến</td><td>Xem tận tay, so sánh nhiều loại</td><td>Xem ảnh, hỏi thêm qua Zalo</td></tr>
  <tr><td>Nhận hàng</td><td>Nhận ngay khi đến</td><td>TP. Hồ Chí Minh và lân cận 1–2 ngày làm việc</td></tr>
  <tr><td>Phí giao hàng</td><td>Không phát sinh</td><td>Tính theo khu vực, báo khi xác nhận đơn</td></tr>
  <tr><td>Tư vấn</td><td>Hỏi trực tiếp cách ngâm, chưng</td><td>Qua điện thoại, Zalo</td></tr>
  </tbody></table>
  <p>Theo <a href="../chinh-sach/van-chuyen.html">chính sách vận chuyển</a>, khu vực gần có thể được giao bởi nhân viên Việt Cường Nhân, và khách được kiểm tra kiện hàng trước khi thanh toán.</p>

  <h2>Các loại yến sào bán tại xưởng Dĩ An</h2>
  <p>Xưởng Việt Cường Nhân bán đủ ba nhóm: yến thô còn lông, yến tinh chế đã nhặt sạch lông và nước yến chưng sẵn đóng hũ. Ở xưởng chúng tôi, khách mua dùng trong gia đình thường chọn yến tinh chế 1 lớp sợi vừa, khách có thời gian tự nhặt lông chọn yến thô, còn người bận rộn chọn nước yến hũ.</p>
""" + ul(li(109, "Đã nhặt sạch lông, ngâm xong là chưng."), li(101, "Còn lông, cần ngâm và nhặt tại nhà."), li(124, "Chưng sẵn, mở nắp là dùng.")) + f"""
  <p>Sự khác nhau giữa các nhóm yến được giải thích ở bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>. Bảng giá đầy đủ các loại xem tại bài <a href="gia-yen-sao-bao-nhieu-tien.html">giá yến sào bao nhiêu tiền 100gr</a> hoặc <a href="../#san-pham">bảng giá sản phẩm</a>.</p>

  <h2>Kiểm tra gì khi mua yến sào ở Dĩ An?</h2>
  <p>Dù mua ở đâu, bạn nên xem sợi yến, nhãn mác và giấy tờ của cơ sở sản xuất. Đây là những điểm khách đến xưởng hay hỏi:</p>
  <ol>
    <li><b>Xem sợi yến:</b> sợi tự nhiên to nhỏ không đều, màu trắng ngà, không bóng nhựa.</li>
    <li><b>Hỏi nguồn gốc:</b> yến từ nhà yến nào, làm sạch ở đâu. Việt Cường Nhân có nhà yến tại Gò Công Tây (Tiền Giang cũ), Bình Thuận và các xưởng nhặt lông tại Lâm Đồng.</li>
    <li><b>Xem chứng nhận:</b> HACCP, ISO 22000:2018, GMP và hồ sơ tự công bố sản phẩm, có thể xem trên <a href="../chung-nhan/">trang chứng nhận</a>.</li>
    <li><b>Xem nhãn:</b> tên sản phẩm, khối lượng, ngày sản xuất, hạn dùng, thông tin cơ sở sản xuất.</li>
  </ol>
  <p>Các dấu hiệu chi tiết hơn có ở bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>. Ý nghĩa từng chứng nhận xem ở bài <a href="chung-nhan-haccp-iso-22000-gmp-la-gi.html">HACCP, ISO 22000 và GMP nghĩa là gì</a>.</p>

  <h2>Cách đặt yến sào giao tận nhà ở Dĩ An</h2>
  <p>Cách nhanh nhất là đặt trên website hoặc nhắn Zalo 0978 094 739, nhân viên sẽ gọi xác nhận đơn và báo phí giao trước khi giao.</p>
  <ol>
    <li>Chọn sản phẩm ở <a href="../#san-pham">bảng giá</a> và điền thông tin đặt hàng.</li>
    <li>Nhân viên Việt Cường Nhân gọi xác nhận, báo phí giao hàng theo khu vực.</li>
    <li>Nhận hàng, kiểm tra bên ngoài kiện, số lượng và niêm phong trước khi thanh toán.</li>
    <li>Nên quay video lúc mở hàng để làm căn cứ theo <a href="../chinh-sach/doi-tra.html">chính sách đổi trả</a>.</li>
  </ol>
  <p>Nhận yến về, bạn có thể làm theo bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý ở Dĩ An và khu vực lân cận: nhắn Zalo 0978 094 739 để được tư vấn.</p>""",
  faq=[("Mua yến sào ở Dĩ An, Bình Dương ở đâu?", "Có thể mua tại xưởng Việt Cường Nhân: nhà máy 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp hoặc cơ sở đóng gói 261-263 Võ Thị Sáu, Phường Đông Hòa, TP. Hồ Chí Minh. Nên gọi hoặc nhắn Zalo 0978 094 739 trước khi đến."),
       ("Có được đến xưởng xem yến trước khi mua không?", "Được, bạn nên gọi hoặc nhắn Zalo 0978 094 739 trước để hẹn giờ và địa điểm, nhân viên sẽ chuẩn bị sẵn các loại yến để bạn xem."),
       ("Đặt yến online giao về Dĩ An mất bao lâu?", "Theo chính sách vận chuyển của Việt Cường Nhân, TP. Hồ Chí Minh và khu vực lân cận nhận hàng trong 1 đến 2 ngày làm việc. Phí giao được báo khi gọi xác nhận đơn."),
       ("Yến sào ở xưởng Dĩ An giá bao nhiêu?", f"Ví dụ {P[109][2]} giá {gia(109)}/100gr, {P[101][2]} giá {gia(101)}/100gr. Giá chưa gồm phí giao hàng, bảng giá đầy đủ có trên website."),
       ("Muốn mua sỉ yến sào ở Bình Dương thì liên hệ ai?", "Nhắn Zalo 0978 094 739 để được Việt Cường Nhân tư vấn mua số lượng lớn, mua sỉ hoặc làm đại lý.")]),
dict(slug="chan-yen-chan-tua-la-gi", cat="Yến sào", ngay="2026-10-31",
  tu_khoa="chân yến là gì, chân tua yến, chân yến có tốt không, giá chân yến 100gr, cách chưng chân yến",
  h1="Chân yến là gì? Chân tua yến có nên mua không?",
  desc="Chân yến là gì? Chân yến (chân tua) là phần gốc tổ bám vào xà nhà yến, sợi dày và dai. Cách phân biệt, cách ngâm chưng, giá 100gr và ai nên mua.",
  lede="Chân yến là phần gốc của tổ yến bám chặt vào xà gỗ trong nhà yến, còn gọi là chân tua hay chân tổ. Phần này đặc, sợi dày và dai hơn thân tổ, nên cần ngâm và chưng lâu hơn; hợp với người thích ăn sợi dai, giòn.",
  tom_tat=["Chân yến (chân tua) là phần gốc tổ bám vào xà nhà yến, sợi đặc, dày và cứng hơn thân tổ.",
           "Chân yến cần ngâm khoảng 2–3 tiếng và chưng cách thủy khoảng 30–40 phút, lâu hơn yến tinh chế thường.",
           f"Giá tham khảo tại Việt Cường Nhân: {P[118][2]} {gia(118)}/100gr, {P[119][2]} {gia(119)}/100gr, {P[105][2]} {gia(105)}/100gr.",
           "Chân yến khác yến sợi chủ yếu ở kết cấu khi ăn (dai, giòn) và cách sơ chế; không có căn cứ để nói bổ hơn hay kém hơn.",
           "Hợp với người thích sợi dai, có thời gian ngâm chưng; trẻ nhỏ, người lớn tuổi khó nhai nên chọn yến sợi mềm hoặc yến vụn."],
  body=f"""  <h2>Chân yến là gì?</h2>
  <p>Chân yến là phần gốc của tổ yến, nơi tổ dính chặt vào xà gỗ trong nhà yến. Khi làm tổ, chim yến nhả nhiều lớp nước dãi chồng lên nhau ở phần này để tổ bám chắc, nên chân tổ đặc, dày và cứng hơn hẳn phần thân và miệng tổ.</p>
  <p>Trong nghề yến, phần chân thường được tách riêng khi làm sạch và định hình tổ. Người bán gọi bằng nhiều tên: <b>chân yến</b>, <b>chân tổ</b>, <b>chân tua</b> (vì phần chân sau khi tách có dạng tua, khối nhỏ). Còn <b>chân rìa</b> là phần chân và rìa tổ được gom lại khi chưa nhặt lông.</p>
  <p>Ở xưởng Việt Cường Nhân, khách hay hỏi "chân yến có phải yến vụn không". Không phải: yến vụn là sợi ngắn rơi ra trong lúc nhặt lông, còn chân yến là khối đặc ở gốc tổ, hai loại khác nhau về hình dạng lẫn cách nấu.</p>

  <h2>Chân yến khác yến sợi và yến vụn thế nào?</h2>
  <p>Chân yến khác yến sợi và yến vụn chủ yếu ở kết cấu, thời gian sơ chế và món phù hợp. Bảng dưới so sánh ba loại đều đã nhặt sạch lông tại xưởng.</p>
  <table><thead><tr><th>Tiêu chí</th><th>Chân tua sạch</th><th>Yến tinh chế sợi</th><th>Yến tinh chế vụn</th></tr></thead><tbody>
  <tr><td>Phần của tổ</td><td>Gốc tổ bám vào xà</td><td>Thân tổ, sợi dài vừa</td><td>Sợi ngắn rơi ra khi làm sạch</td></tr>
  <tr><td>Hình dạng</td><td>Khối nhỏ, đặc, dày</td><td>Tai yến, sợi đan đều</td><td>Sợi vụn, mảnh nhỏ</td></tr>
  <tr><td>Thời gian ngâm</td><td>Khoảng 2–3 tiếng</td><td>Khoảng 30–60 phút</td><td>Khoảng 15–20 phút</td></tr>
  <tr><td>Thời gian chưng</td><td>Khoảng 30–40 phút</td><td>Khoảng 20–30 phút</td><td>Khoảng 10–15 phút</td></tr>
  <tr><td>Khi ăn</td><td>Dai, giòn sần sật</td><td>Mềm, sợi rõ</td><td>Mềm, hòa vào món</td></tr>
  <tr><td>Hợp món</td><td>Chưng đường phèn, chè, hầm</td><td>Chưng hằng ngày, biếu tặng</td><td>Cháo, súp, chưng sữa</td></tr>
  <tr><td>Giá 100gr</td><td>{gia(119)} – {gia(118)}</td><td>{gia(109)}</td><td>{gia(107)}</td></tr>
  </tbody></table>
  <p>Thời gian ngâm và chưng trong bảng là mức tham khảo; tổ khô, cứng hơn thì ngâm lâu hơn. Sự khác nhau giữa yến thô, yến tinh chế và yến rút lông xem ở bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>.</p>

  <h2>Chân yến có tốt không, có nên mua không?</h2>
  <p>Chân yến vẫn là tổ yến, chỉ khác phần của tổ, nên nên mua hay không tùy vào khẩu vị và thời gian sơ chế của bạn. Không có căn cứ để nói chân yến bổ hơn hay kém hơn yến sợi; điểm khác rõ nhất là cảm giác ăn dai, giòn và cần nấu lâu hơn.</p>
  <h3>Nên chọn chân yến khi</h3>
  <ul>
    <li>Bạn thích chén yến có sợi dai, giòn, nhai được, không bị tan.</li>
    <li>Bạn hay nấu chè, hầm hoặc chưng lâu, cần loại yến chịu nhiệt tốt.</li>
    <li>Bạn có thời gian ngâm từ sáng để chiều chưng, hoặc ngâm buổi tối để sáng hôm sau chưng.</li>
  </ul>
  <h3>Nên chọn loại khác khi</h3>
  <ul>
    <li>Bạn cần nấu nhanh: chọn yến tinh chế sợi, ngâm 30–60 phút là chưng được.</li>
    <li>Nấu cho trẻ nhỏ hoặc người lớn tuổi khó nhai: chọn yến sợi mềm hoặc yến vụn, chưng mềm.</li>
    <li>Mua để biếu, cần hình thức đẹp: chọn yến rút lông hoặc yến tinh chế dạng tai.</li>
  </ul>

  <h2>Vì sao chân yến sạch giá cao hơn yến tinh chế thường?</h2>
  <p>Chân tua sạch có giá cao hơn yến tinh chế 1 lớp sợi vừa vì mỗi tổ chỉ có một phần chân nhỏ, và phần này cứng, đặc nên làm sạch tốn công hơn. Chân yến bám vào xà gỗ dễ dính mùn gỗ, cát và lông ở các kẽ, thợ phải ngâm và nhặt kỹ từng khối.</p>
  <p>Chân rìa thô thì giá mềm hơn chân tua sạch vì chưa làm sạch, khi mua về bạn phải tự ngâm, nhặt lông và tạp chất. Giá dưới đây lấy từ bảng giá website Việt Cường Nhân, chưa gồm phí giao hàng:</p>
""" + ul(li(118, "Khối chân đều, đã nhặt sạch lông tại xưởng."), li(119, "Đã nhặt sạch lông, khối nhỏ hơn loại 1."), li(105, "Còn lông và tạp chất, cần tự làm sạch.")) + f"""
  <p>Muốn so sánh với các loại yến khác, xem bài <a href="gia-yen-sao-bao-nhieu-tien.html">giá yến sào bao nhiêu tiền 100gr</a>.</p>

  <h2>Cách ngâm và chưng chân yến tại nhà</h2>
  <p>Chân yến cần ngâm lâu hơn và chưng lâu hơn yến sợi, vì phần gốc tổ đặc và cứng. Một chén dùng khoảng 3–5 g chân yến khô với 150–200 ml nước, giống mức chưng yến thường.</p>
  <ol>
    <li><b>Ngâm:</b> ngâm chân yến trong nước sạch khoảng 2–3 tiếng, đến khi khối yến mềm và tơi ra. Có thể ngâm trong ngăn mát nếu để lâu hơn.</li>
    <li><b>Xé tơi:</b> dùng tay xé khối chân thành sợi nhỏ; phần nào còn cứng thì ngâm thêm.</li>
    <li><b>Kiểm tra:</b> với chân rìa thô, đặt yến lên đĩa trắng, dùng nhíp nhặt lông và mùn gỗ còn sót.</li>
    <li><b>Chưng cách thủy:</b> cho yến và nước vào thố, đậy nắp, chưng lửa nhỏ khoảng 30–40 phút.</li>
    <li><b>Nêm:</b> thêm đường phèn trong 5 phút cuối. Có thể chưng cùng táo đỏ, hạt sen hoặc vài sợi đông trùng hạ thảo.</li>
  </ol>
  <p>Các bước chưng cơ bản có ở bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>. Tính số chén từ một hộp xem bài <a href="100gr-yen-chung-duoc-bao-nhieu-chen.html">100gr yến chưng được bao nhiêu chén</a>.</p>

  <h2>Cách nhận biết chân yến thật</h2>
  <p>Chân yến thật có màu trắng ngà đến vàng nhạt, khối đặc nhưng nhìn kỹ vẫn thấy sợi yến xếp lớp, khi ngâm nở mềm và tơi thành sợi. Nên cẩn thận với chân yến trắng tinh bất thường, bóng như nhựa hoặc ngâm lâu vẫn không tơi.</p>
  <ul>
    <li><b>Nhìn:</b> các lớp sợi chồng lên nhau, to nhỏ không đều.</li>
    <li><b>Ngâm:</b> nước ngâm trong, không có váng lạ; khối yến mềm dần và xé được thành sợi.</li>
    <li><b>Chưng:</b> sợi vẫn còn, dai, có mùi tanh nhẹ đặc trưng của yến.</li>
    <li><b>Nguồn gốc:</b> hỏi rõ cơ sở làm sạch, xem chứng nhận an toàn thực phẩm và bản tự công bố sản phẩm.</li>
  </ul>
  <p>Các dấu hiệu chung xem thêm ở bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>.</p>

  <h2>Mua chân yến ở Việt Cường Nhân</h2>
  <p>Việt Cường Nhân làm yến từ năm 2009, có nhà yến và xưởng nhặt lông riêng, nhà máy đạt HACCP, ISO 22000:2018 và GMP. Chân tua sạch được tách và nhặt lông tại xưởng, về nhà chỉ cần ngâm và chưng. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>, giá chưa gồm phí giao hàng. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739 để được tư vấn.</p>""",
  faq=[("Chân yến là gì?", "Chân yến (chân tua, chân tổ) là phần gốc của tổ yến bám vào xà gỗ trong nhà yến. Phần này có nhiều lớp nước dãi chồng lên nhau nên đặc, dày và dai hơn thân tổ."),
       ("Chân yến có tốt hơn yến sợi không?", "Chân yến và yến sợi đều là tổ yến, khác nhau ở phần của tổ và kết cấu khi ăn. Không có căn cứ để nói loại nào bổ hơn; chọn theo khẩu vị và thời gian sơ chế."),
       ("Chân yến ngâm bao lâu?", "Khoảng 2–3 tiếng, đến khi khối yến mềm và xé tơi được. Sau đó chưng cách thủy khoảng 30–40 phút."),
       ("Chân yến giá bao nhiêu 100gr?", f"Tại Việt Cường Nhân, {P[118][2]} giá {gia(118)}/100gr, {P[119][2]} giá {gia(119)}/100gr và {P[105][2]} giá {gia(105)}/100gr, chưa gồm phí giao hàng."),
       ("Chân tua và chân rìa khác nhau thế nào?", "Chân tua sạch là phần chân tổ đã nhặt sạch lông tại xưởng, ngâm xong là chưng. Chân rìa thô là phần chân và rìa tổ chưa làm sạch, phải tự ngâm và nhặt lông.")]),
dict(slug="yen-vun-baby-la-gi", cat="Yến sào", ngay="2026-10-31",
  tu_khoa="yến vụn, yến vụn baby là gì, yến vụn nấu món gì, yến vụn đắp tổ, giá yến vụn 100gr",
  h1="Yến vụn baby là gì, dùng làm món gì?",
  desc="Yến vụn baby là gì? Là sợi yến ngắn, nhỏ đã nhặt sạch lông, nở nhanh, hợp nấu cháo, súp, chưng sữa. Cách ngâm, chưng, món ngon và giá yến vụn 100gr.",
  lede="Yến vụn baby là những sợi yến ngắn, nhỏ rơi ra trong lúc làm sạch và định hình tổ yến, đã được nhặt sạch lông. Yến vụn nở nhanh, mềm, dễ hòa vào món ăn nên hợp nấu cháo, súp, chưng sữa, và có giá mềm hơn yến sợi.",
  tom_tat=["Yến vụn là sợi yến ngắn, nhỏ tách ra khi làm sạch và định hình tổ; vẫn là tổ yến, đã nhặt sạch lông.",
           "Yến vụn chỉ cần ngâm khoảng 15–20 phút và chưng khoảng 10–15 phút; chưng lâu dễ tan.",
           "Hợp nấu cháo yến, súp gà yến, yến chưng sữa tươi, chè và yến chưng táo đỏ.",
           f"Giá tham khảo tại Việt Cường Nhân: {P[107][2]} và {P[106][2]} cùng giá {gia(107)}/100gr.",
           f"Muốn tiện hơn có {P[120][2]} chia sẵn từng viên: {gia(120)}/10 gói, {gia(121)}/10 hũ."],
  body=f"""  <h2>Yến vụn baby là gì?</h2>
  <p>Yến vụn baby là phần sợi yến ngắn và nhỏ tách ra trong quá trình ngâm, nhặt lông và định hình tổ yến. Sau khi gom lại, yến vụn cũng được nhặt sạch lông và sấy khô như yến sợi, nên về bản chất vẫn là tổ yến, chỉ khác độ dài sợi.</p>
  <p>Chữ "baby" là cách gọi trong nghề để chỉ loại vụn có sợi rất nhỏ, mịn. Ở xưởng Việt Cường Nhân, khi thợ nhặt lông và tạo hình tai yến, những sợi quá ngắn không đắp được vào tổ sẽ được gom riêng thành yến vụn.</p>
  <h3>Các dạng yến vụn thường gặp</h3>
  <ul>
    <li><b>Yến vụn baby:</b> sợi nhỏ, rời, nở nhanh, dễ chia lượng ít.</li>
    <li><b>Yến vụn đắp tổ:</b> sợi vụn được đắp lại thành dạng tai tổ, dễ lấy từng phần, nhìn gọn hơn.</li>
    <li><b>Viên yến baby:</b> yến vụn ép thành viên tròn, chia sẵn từng gói hoặc hũ, mỗi lần dùng một viên.</li>
  </ul>

  <h2>Yến vụn có tốt không, khác yến sợi thế nào?</h2>
  <p>Yến vụn và yến sợi đều là tổ yến đã làm sạch; điểm khác chính là độ dài sợi, cảm giác khi ăn và giá. Sợi dài không làm chén yến "bổ" hơn, nó chủ yếu tạo cảm giác dai và chén yến đẹp hơn.</p>
  <table><thead><tr><th>Tiêu chí</th><th>Yến tinh chế vụn</th><th>Yến tinh chế 1 lớp sợi vừa</th></tr></thead><tbody>
  <tr><td>Sợi yến</td><td>Ngắn, nhỏ, rời</td><td>Dài vừa, đan thành tai</td></tr>
  <tr><td>Ngâm</td><td>Khoảng 15–20 phút</td><td>Khoảng 30–60 phút</td></tr>
  <tr><td>Chưng cách thủy</td><td>Khoảng 10–15 phút</td><td>Khoảng 20–30 phút</td></tr>
  <tr><td>Khi ăn</td><td>Mềm, hòa vào món</td><td>Sợi rõ, hơi dai</td></tr>
  <tr><td>Hợp món</td><td>Cháo, súp, chưng sữa, chè</td><td>Chưng đường phèn, biếu tặng</td></tr>
  <tr><td>Giá 100gr</td><td>{gia(107)}</td><td>{gia(109)}</td></tr>
  </tbody></table>
  <p>Vì nở nhanh và mềm, yến vụn thường được chọn để nấu cho trẻ nhỏ và người lớn tuổi. Trẻ nhỏ, phụ nữ mang thai, người có bệnh nền nên hỏi bác sĩ trước khi dùng. Muốn hiểu thêm các nhóm yến, xem bài <a href="yen-sao-loai-nao-tot.html">yến sào loại nào tốt</a>.</p>

  <h2>Yến vụn nấu món gì ngon?</h2>
  <p>Yến vụn hợp nhất với các món nấu nhừ hoặc có nước dùng, vì sợi nhỏ hòa đều vào món và không cần chưng lâu. Dưới đây là năm món nhiều gia đình hay làm với yến vụn.</p>
  <table><thead><tr><th>Món</th><th>Yến khô</th><th>Cách cho yến</th></tr></thead><tbody>
  <tr><td>Cháo yến thịt bằm</td><td>2–3 g cho 1 chén</td><td>Cho yến đã ngâm vào cháo chín, nấu thêm 5–7 phút</td></tr>
  <tr><td>Súp gà yến</td><td>3–4 g cho 2 chén</td><td>Thêm yến vào nồi súp ở 10 phút cuối</td></tr>
  <tr><td>Yến chưng sữa tươi</td><td>3 g cho 1 chén</td><td>Chưng yến với nước 10 phút, tắt bếp rồi mới cho sữa</td></tr>
  <tr><td>Yến chưng táo đỏ</td><td>3–4 g cho 1 chén</td><td>Chưng cùng táo đỏ cắt lát 10–15 phút</td></tr>
  <tr><td>Chè hạt sen yến</td><td>4 g cho 2 chén</td><td>Nấu hạt sen mềm, cho yến vào 10 phút cuối</td></tr>
  </tbody></table>
  <h3>Cách nấu cháo yến thịt bằm (1 chén)</h3>
  <ol>
    <li>Ngâm 2–3 g yến vụn trong nước sạch khoảng 15–20 phút, vớt ra để ráo.</li>
    <li>Nấu 30 g gạo với khoảng 400 ml nước thành cháo nhừ.</li>
    <li>Cho khoảng 30 g thịt nạc bằm vào, khuấy tan, nấu chín.</li>
    <li>Cho yến vào, nấu nhỏ lửa thêm 5–7 phút, nêm nhạt vừa ăn rồi tắt bếp.</li>
  </ol>
  <p>Với món ngọt, có thể chưng cùng táo đỏ Tân Cương; cách chọn size táo xem ở bài <a href="tao-do-tan-cuong-cach-chon-va-mon-ngon.html">táo đỏ Tân Cương: cách chọn size và món ngon</a>.</p>

  <h2>Cách ngâm và chưng yến vụn không bị tan</h2>
  <p>Yến vụn sợi nhỏ nên chỉ cần ngâm ngắn và chưng ngắn; ngâm hoặc chưng quá lâu là nguyên nhân chính khiến yến vụn tan thành nước. Mỗi chén yến chưng đường phèn dùng khoảng 3–4 g yến vụn với 150–200 ml nước.</p>
  <ol>
    <li><b>Ngâm:</b> 15–20 phút trong nước sạch, đến khi sợi nở mềm.</li>
    <li><b>Lọc:</b> đổ yến qua rây lưới nhỏ để không trôi mất sợi, rửa nhẹ tay.</li>
    <li><b>Chưng:</b> cho yến và nước vào thố, chưng cách thủy lửa nhỏ 10–15 phút.</li>
    <li><b>Nêm:</b> thêm đường phèn ở 3–5 phút cuối.</li>
  </ol>
  <p>Các bước chưng chung xem ở bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>; số chén từ một hộp xem bài <a href="100gr-yen-chung-duoc-bao-nhieu-chen.html">100gr yến chưng được bao nhiêu chén</a>.</p>

  <h2>Giá yến vụn 100gr và nên chọn loại nào</h2>
  <p>Yến vụn có giá thấp hơn yến tinh chế dạng sợi vì sợi ngắn, không định hình được tổ đẹp. Giá dưới đây lấy từ bảng giá website Việt Cường Nhân, chưa gồm phí giao hàng:</p>
""" + ul(li(107, "Sợi nhỏ, rời, dễ chia lượng ít để nấu cháo, súp."), li(106, "Vụn được đắp thành tai, lấy từng phần gọn hơn."), li(120, "Mỗi viên một lần dùng, đóng gói."), li(121, "Mỗi viên một lần dùng, đóng hũ.")) + f"""
  <ul>
    <li><b>Nấu cháo, súp hằng ngày:</b> {P[107][2]}.</li>
    <li><b>Muốn dễ lấy, dễ bảo quản:</b> {P[106][2]}.</li>
    <li><b>Bận rộn, không muốn cân:</b> {P[120][2]}, thành phần ghi trên bao bì.</li>
  </ul>

  <h2>Bảo quản yến vụn</h2>
  <p>Yến vụn khô bảo quản trong hộp hoặc túi kín, nơi khô ráo, tránh nắng; sau mỗi lần lấy cần đậy kín ngay vì sợi nhỏ dễ hút ẩm. Yến đã chưng hoặc cháo yến nên ăn trong ngày; nếu còn thừa thì để nguội, đậy kín, cất ngăn mát.</p>
  <p>Việt Cường Nhân làm yến từ năm 2009, xưởng đạt HACCP, ISO 22000:2018 và GMP; yến vụn được gom và nhặt lông cùng quy trình với yến sợi. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Yến vụn là gì?", "Yến vụn là những sợi yến ngắn, nhỏ tách ra khi ngâm, nhặt lông và định hình tổ yến. Yến vụn vẫn là tổ yến, được nhặt sạch lông và sấy khô như yến sợi."),
       ("Yến vụn có tốt bằng yến sợi không?", "Yến vụn và yến sợi đều là tổ yến đã làm sạch, khác nhau chủ yếu ở độ dài sợi và cảm giác khi ăn. Sợi dài cho chén yến đẹp và dai hơn, còn yến vụn mềm, nở nhanh, hợp nấu cháo, súp."),
       ("Yến vụn ngâm bao lâu?", "Khoảng 15–20 phút là sợi nở mềm. Sau đó chưng cách thủy khoảng 10–15 phút; chưng lâu hơn yến dễ bị tan."),
       ("Yến vụn nấu món gì?", "Hợp nấu cháo yến, súp gà yến, yến chưng sữa tươi, yến chưng táo đỏ và chè hạt sen yến."),
       ("Yến vụn baby giá bao nhiêu?", f"Tại Việt Cường Nhân, {P[107][2]} giá {gia(107)}/100gr, chưa gồm phí giao hàng. {P[120][2]} giá {gia(120)}/10 gói.")]),
dict(slug="yen-chung-tao-do-hat-sen", cat="Món ngon", ngay="2026-10-31",
  tu_khoa="yến chưng táo đỏ hạt sen, cách chưng yến táo đỏ hạt sen, yến chưng hạt sen, tỉ lệ yến táo đỏ hạt sen",
  h1="Cách làm yến chưng táo đỏ hạt sen thơm ngon",
  desc="Cách làm yến chưng táo đỏ hạt sen tại nhà: định lượng cho 2 chén, cách sơ chế hạt sen không đắng, các bước chưng khoảng 45 phút và mẹo giữ sợi yến không tan.",
  lede="Yến chưng táo đỏ hạt sen mất khoảng 45 phút trên bếp (chưa tính thời gian ngâm): nấu hạt sen cho mềm trước, rồi chưng cách thủy cùng yến và táo đỏ khoảng 20–25 phút, thêm đường phèn ở 5 phút cuối. Cho 2 chén cần khoảng 8 g yến khô, 30 g hạt sen và 4–6 quả táo đỏ.",
  tom_tat=["Định lượng 2 chén: 8 g yến khô, 30 g hạt sen, 4–6 quả táo đỏ, 400 ml nước, 20–30 g đường phèn.",
           "Hạt sen nấu mềm trước khoảng 20 phút vì chín lâu hơn yến; nhớ bỏ tim sen để không đắng.",
           "Chưng cách thủy yến cùng hạt sen và táo đỏ khoảng 20–25 phút, đường phèn cho ở 5 phút cuối.",
           "Không đun sôi mạnh và không chưng quá 30 phút sau khi cho yến để sợi yến không tan.",
           f"Nguyên liệu tại Việt Cường Nhân: {P[109][2]} {gia(109)}/100gr, {P[145][2]} {gia(145)}/hộp 350gr."],
  body=f"""  <h2>Nguyên liệu yến chưng táo đỏ hạt sen (2 chén)</h2>
  <p>Một mẻ yến chưng táo đỏ hạt sen cho 2 chén cần 8 g yến khô, 30 g hạt sen, 4–6 quả táo đỏ, 400 ml nước và đường phèn tùy khẩu vị. Đây là định lượng xưởng Việt Cường Nhân hay gợi ý cho khách mới chưng lần đầu.</p>
  <table><thead><tr><th>Nguyên liệu</th><th>Định lượng</th><th>Ghi chú</th></tr></thead><tbody>
  <tr><td>Yến tinh chế khô</td><td>8 g (khoảng 4 g mỗi chén)</td><td>Yến sợi hoặc yến vụn đều được</td></tr>
  <tr><td>Hạt sen</td><td>30 g khô hoặc 50 g tươi</td><td>Đã bỏ tim</td></tr>
  <tr><td>Táo đỏ</td><td>4–6 quả</td><td>Rửa sạch, cắt lát, bỏ hạt</td></tr>
  <tr><td>Nước lọc</td><td>400 ml</td><td>Muốn sệt thì giảm còn 300 ml</td></tr>
  <tr><td>Đường phèn</td><td>20–30 g</td><td>Tùy khẩu vị, có thể bỏ</td></tr>
  <tr><td>Gừng (tùy chọn)</td><td>1–2 lát mỏng</td><td>Giảm mùi tanh nhẹ của yến</td></tr>
  </tbody></table>
  <p>Dụng cụ: 2 thố sứ có nắp hoặc 1 thố lớn, nồi để chưng cách thủy, rây lưới nhỏ.</p>

  <h2>Sơ chế nguyên liệu</h2>
  <h3>Ngâm yến</h3>
  <p>Yến tinh chế 1 lớp sợi ngâm nước sạch 30–60 phút đến khi sợi nở mềm; yến vụn chỉ cần 15–20 phút. Vớt yến qua rây, xé tơi theo thớ sợi, để ráo. Nếu dùng chân yến thì ngâm lâu hơn, khoảng 2–3 tiếng, xem bài <a href="chan-yen-chan-tua-la-gi.html">chân yến là gì</a>.</p>
  <h3>Sơ chế hạt sen</h3>
  <p>Hạt sen khô ngâm nước khoảng 2 tiếng cho mềm, hạt sen tươi chỉ cần rửa sạch. Dùng tăm đẩy bỏ tim sen màu xanh ở giữa hạt, vì tim sen có vị đắng.</p>
  <h3>Sơ chế táo đỏ</h3>
  <p>Rửa táo đỏ, ngâm nước ấm 10 phút cho mềm vỏ, cắt lát mỏng và bỏ hạt để táo ra vị ngọt nhanh hơn. Cách chọn size táo xem bài <a href="tao-do-tan-cuong-cach-chon-va-mon-ngon.html">táo đỏ Tân Cương: cách chọn size và món ngon</a>.</p>

  <h2>Cách chưng yến táo đỏ hạt sen từng bước</h2>
  <p>Nguyên tắc chính: nấu hạt sen chín trước, sau đó mới chưng cùng yến, vì hạt sen cần thời gian lâu hơn yến rất nhiều. Tổng thời gian trên bếp khoảng 45 phút.</p>
  <ol>
    <li><b>Nấu hạt sen (20 phút):</b> cho hạt sen vào nồi cùng 400 ml nước, nấu lửa vừa khoảng 20 phút đến khi bóp nhẹ thấy bở mềm. Giữ lại phần nước nấu sen.</li>
    <li><b>Cho vào thố:</b> chia yến đã ngâm, hạt sen, táo đỏ và nước nấu sen vào thố, thêm lát gừng nếu dùng. Nước ngập yến khoảng 1–2 đốt ngón tay.</li>
    <li><b>Chưng cách thủy (20–25 phút):</b> đậy nắp thố, đặt vào nồi nước đang sôi lăn tăn, mực nước ngoài thố khoảng nửa thân thố. Giữ lửa nhỏ.</li>
    <li><b>Thêm đường phèn (5 phút cuối):</b> mở nắp, cho đường phèn, khuấy nhẹ đến khi tan rồi đậy lại.</li>
    <li><b>Tắt bếp:</b> vớt bỏ gừng, để thố nghỉ vài phút. Ăn ấm hoặc để nguội rồi cất ngăn mát.</li>
  </ol>
  <p>Chén yến đạt khi sợi yến trong, mềm nhưng còn dai, hạt sen bở, táo đỏ mềm và nước có vị ngọt thanh. Các bước chưng yến cơ bản có ở bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Mẹo để yến chưng táo đỏ hạt sen ngon hơn</h2>
  <ul>
    <li><b>Không đun sôi mạnh:</b> nước sôi sùng sục làm sợi yến tan; chỉ giữ lửa nhỏ lăn tăn.</li>
    <li><b>Không chưng quá lâu:</b> sau khi cho yến vào, tối đa khoảng 30 phút là đủ.</li>
    <li><b>Đường phèn cho sau cùng:</b> dễ nếm và điều chỉnh độ ngọt theo khẩu vị.</li>
    <li><b>Táo đỏ cắt lát:</b> giúp nước chưng có màu vàng nhạt, ngọt tự nhiên, nên có thể giảm đường.</li>
    <li><b>Thêm kỷ tử:</b> 8–10 hạt cho vào ở 5 phút cuối để giữ màu đỏ đẹp.</li>
    <li><b>Ít đường cho người ăn kiêng:</b> có thể bỏ đường phèn, dùng vị ngọt của táo đỏ.</li>
  </ul>

  <h2>Biến tấu khác với yến chưng hạt sen</h2>
  <table><thead><tr><th>Món</th><th>Thay đổi so với công thức gốc</th></tr></thead><tbody>
  <tr><td>Yến chưng hạt sen long nhãn</td><td>Bỏ táo đỏ, thêm 10–15 g long nhãn ở 10 phút cuối</td></tr>
  <tr><td>Yến chưng táo đỏ kỷ tử</td><td>Bỏ hạt sen, thêm 8–10 hạt kỷ tử, chưng 20 phút</td></tr>
  <tr><td>Yến chưng hạt sen đông trùng</td><td>Thêm vài sợi đông trùng hạ thảo khô ở 5 phút cuối</td></tr>
  <tr><td>Chè hạt sen yến</td><td>Nấu hạt sen với nhiều nước hơn, cho yến vào 10 phút cuối</td></tr>
  </tbody></table>

  <h2>Bảo quản yến chưng táo đỏ hạt sen</h2>
  <p>Yến chưng xong nên để nguội, đậy kín và cất ngăn mát, dùng trong vài ngày; khi ăn có thể hâm cách thủy vài phút hoặc ăn mát. Nên chưng vừa đủ cho 2–3 ngày thay vì chưng một lần quá nhiều. Lượng dùng mỗi tuần và số chén từ một hộp yến xem bài <a href="100gr-yen-chung-duoc-bao-nhieu-chen.html">100gr yến chưng được bao nhiêu chén</a>. Trẻ nhỏ, phụ nữ mang thai, người có bệnh nền nên hỏi bác sĩ trước khi dùng.</p>

  <h2>Nguyên liệu chưng yến tại Việt Cường Nhân</h2>
  <p>Yến tinh chế của Việt Cường Nhân đã nhặt sạch lông tại xưởng, ngâm xong là chưng; táo đỏ Tân Cương chia theo size. Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(109, "Sợi vừa, hợp chưng hằng ngày."), li(107, "Nở nhanh, chưng 10–15 phút."), li(145, "Đủ cho nhiều mẻ chưng."), li(142, "Mua dùng lâu, tiết kiệm hơn.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Yến chưng táo đỏ hạt sen chưng bao lâu?", "Nấu hạt sen mềm trước khoảng 20 phút, sau đó chưng cách thủy cùng yến và táo đỏ khoảng 20–25 phút. Tổng thời gian trên bếp khoảng 45 phút."),
       ("Tỉ lệ yến, táo đỏ, hạt sen thế nào?", "Cho 2 chén dùng khoảng 8 g yến khô, 30 g hạt sen khô, 4–6 quả táo đỏ và 400 ml nước, đường phèn 20–30 g tùy khẩu vị."),
       ("Vì sao yến chưng hạt sen bị đắng?", "Thường do chưa bỏ tim sen. Hãy dùng tăm đẩy bỏ phần tim màu xanh ở giữa hạt trước khi nấu."),
       ("Có cho hạt sen và yến vào chưng cùng lúc được không?", "Không nên, vì hạt sen chín lâu hơn yến. Nếu chưng cùng lúc đến khi sen mềm thì sợi yến dễ bị tan; nên nấu sen trước."),
       ("Yến chưng táo đỏ hạt sen để được bao lâu?", "Để nguội, đậy kín, cất ngăn mát và dùng trong vài ngày. Nên chưng vừa đủ ăn trong 2–3 ngày.")]),
dict(slug="yen-chung-dong-trung-ha-thao", cat="Món ngon", ngay="2026-10-31",
  tu_khoa="yến chưng đông trùng hạ thảo, cách chưng yến với đông trùng hạ thảo, tỉ lệ yến và đông trùng, yến chưng đông trùng táo đỏ",
  h1="Yến chưng đông trùng hạ thảo: cách làm và tỉ lệ",
  desc="Yến chưng đông trùng hạ thảo làm thế nào? Tỉ lệ 4 g yến khô với 1 g đông trùng sấy cho 1 chén, các bước chưng cách thủy 20–30 phút và mẹo giữ màu nấm.",
  lede="Yến chưng đông trùng hạ thảo dùng tỉ lệ phổ biến khoảng 4 g yến khô với 1 g nấm đông trùng hạ thảo sấy khô (khoảng 10–15 sợi) cho một chén 150–200 ml. Chưng yến cách thủy 20–30 phút, cho đông trùng và đường phèn vào ở 5–10 phút cuối để nấm giữ màu cam đẹp.",
  tom_tat=["Tỉ lệ 1 chén: 4 g yến khô, khoảng 1 g đông trùng hạ thảo sấy (10–15 sợi), 150–200 ml nước.",
           "Chưng cách thủy tổng 20–30 phút; đông trùng cho vào 5–10 phút cuối để giữ màu cam và không nát.",
           "Có thể thêm 2–3 quả táo đỏ cắt lát để nước chưng ngọt tự nhiên, giảm đường phèn.",
           "Đông trùng loại gãy hợp chưng hằng ngày; loại cây cọng nguyên đẹp hơn khi đãi khách, biếu tặng.",
           f"Giá tham khảo: {P[109][2]} {gia(109)}/100gr, {P[140][2]} {gia(140)}/hũ, {P[138][2]} {gia(138)}/100gr."],
  body=f"""  <h2>Tỉ lệ yến chưng đông trùng hạ thảo</h2>
  <p>Tỉ lệ yến chưng đông trùng hạ thảo dễ dùng nhất là 4 g yến khô với khoảng 1 g nấm đông trùng hạ thảo sấy khô cho mỗi chén. Đông trùng chỉ đóng vai trò thêm màu và vị ngọt nhẹ, nên không cần cho nhiều.</p>
  <table><thead><tr><th>Số chén</th><th>Yến khô</th><th>Đông trùng hạ thảo sấy</th><th>Nước</th><th>Đường phèn</th></tr></thead><tbody>
  <tr><td>1 chén</td><td>4 g</td><td>khoảng 1 g (10–15 sợi)</td><td>150–200 ml</td><td>10–15 g</td></tr>
  <tr><td>2 chén</td><td>8 g</td><td>khoảng 2 g</td><td>300–400 ml</td><td>20–30 g</td></tr>
  <tr><td>4 chén</td><td>16 g</td><td>khoảng 3–4 g</td><td>600–800 ml</td><td>40–50 g</td></tr>
  </tbody></table>
  <p>Nếu dùng đông trùng tươi thay cho loại sấy, cần lượng nhiều hơn vì đông trùng tươi còn nước; cho một nhúm nhỏ và điều chỉnh theo màu nước chưng. Số chén từ một hộp yến 100gr xem ở bài <a href="100gr-yen-chung-duoc-bao-nhieu-chen.html">100gr yến chưng được bao nhiêu chén</a>.</p>

  <h2>Nguyên liệu và dụng cụ</h2>
  <ul>
    <li><b>Yến tinh chế:</b> 4 g mỗi chén. Yến 1 lớp sợi vừa cho sợi rõ; yến vụn nở nhanh, chưng ngắn hơn.</li>
    <li><b>Nấm đông trùng hạ thảo sấy khô:</b> khoảng 1 g mỗi chén.</li>
    <li><b>Đường phèn:</b> 10–15 g mỗi chén, tùy khẩu vị; có thể bỏ.</li>
    <li><b>Táo đỏ (tùy chọn):</b> 2–3 quả mỗi chén, cắt lát bỏ hạt.</li>
    <li><b>Dụng cụ:</b> thố sứ có nắp, nồi chưng cách thủy, rây lưới nhỏ.</li>
  </ul>

  <h2>Cách chưng yến với đông trùng hạ thảo từng bước</h2>
  <p>Chưng yến trước, đông trùng sau: yến cần 20–30 phút để mềm, còn nấm đông trùng sấy chỉ cần 5–10 phút để nở và ra màu. Cho đông trùng từ đầu sẽ làm nấm nhạt màu và dễ nát.</p>
  <ol>
    <li><b>Ngâm yến:</b> yến tinh chế sợi ngâm 30–60 phút, yến vụn 15–20 phút. Vớt qua rây, xé tơi, để ráo.</li>
    <li><b>Rửa đông trùng:</b> tráng nhanh nấm đông trùng sấy qua nước sạch, không ngâm lâu để giữ màu và vị.</li>
    <li><b>Chưng yến:</b> cho yến và nước vào thố (thêm táo đỏ nếu dùng), đậy nắp, chưng cách thủy lửa nhỏ khoảng 15–20 phút.</li>
    <li><b>Thêm đông trùng:</b> mở nắp, cho đông trùng vào, chưng tiếp 5–10 phút đến khi sợi nấm nở và nước chuyển màu vàng cam nhạt.</li>
    <li><b>Nêm đường phèn:</b> cho đường phèn ở 3–5 phút cuối, khuấy nhẹ cho tan rồi tắt bếp.</li>
  </ol>
  <p>Chén yến đạt khi sợi yến trong, mềm mà còn dai, sợi đông trùng giữ màu cam và nước có vị ngọt thanh. Các bước chưng yến cơ bản xem bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Biến tấu yến chưng đông trùng hạ thảo</h2>
  <table><thead><tr><th>Món</th><th>Thêm gì</th><th>Lưu ý</th></tr></thead><tbody>
  <tr><td>Yến chưng đông trùng táo đỏ</td><td>2–3 quả táo đỏ cắt lát mỗi chén</td><td>Cho táo từ đầu, giảm đường phèn</td></tr>
  <tr><td>Yến chưng đông trùng hạt sen</td><td>15 g hạt sen đã nấu mềm mỗi chén</td><td>Nấu sen trước khoảng 20 phút</td></tr>
  <tr><td>Yến chưng đông trùng kỷ tử</td><td>8–10 hạt kỷ tử</td><td>Cho cùng lúc với đông trùng</td></tr>
  <tr><td>Yến chưng đông trùng không đường</td><td>Bỏ đường phèn, thêm táo đỏ</td><td>Hợp người ăn kiêng đường</td></tr>
  </tbody></table>
  <p>Cách làm sen trước rồi mới chưng yến có ở bài <a href="yen-chung-tao-do-hat-sen.html">cách làm yến chưng táo đỏ hạt sen</a>. Đông trùng còn dùng được trong món mặn như <a href="nam-dong-trung-ha-thao-tiem-ga-ac.html">nấm đông trùng hạ thảo tiềm gà ác</a>.</p>

  <h2>Mẹo giữ màu đông trùng và sợi yến không tan</h2>
  <ul>
    <li><b>Cho đông trùng sau cùng:</b> 5–10 phút cuối là đủ để nấm nở, giữ màu cam tươi.</li>
    <li><b>Lửa nhỏ lăn tăn:</b> nước sôi mạnh làm sợi yến tan và đông trùng nát.</li>
    <li><b>Không chưng quá 30 phút</b> tính từ lúc cho yến vào thố.</li>
    <li><b>Đậy kín nắp thố</b> để hơi nước không nhỏ vào làm loãng chén yến.</li>
    <li><b>Ăn cả sợi đông trùng</b> sau khi chưng, sợi mềm và có vị ngọt nhẹ.</li>
  </ul>

  <h2>Nên chọn đông trùng loại cây hay loại gãy để chưng yến?</h2>
  <p>Để chưng yến hằng ngày, đông trùng loại gãy là đủ vì vị như loại cây, chỉ khác sợi ngắn hơn. Loại cây cọng nguyên đẹp hơn, hợp chưng đãi khách hoặc làm quà. Hũ 10gr tiện để thử hoặc dùng dần cho vài chục chén. Cách dùng đông trùng trong các món khác xem bài <a href="cach-dung-dong-trung-ha-thao.html">cách dùng nấm đông trùng hạ thảo sấy khô</a>.</p>
""" + ul(li(138, "Sợi gãy, giá mềm, hợp chưng hằng ngày."), li(136, "Cọng nguyên, đẹp, hợp đãi khách."), li(140, "Hũ nhỏ, tiện dùng thử."), li(109, "Yến đã nhặt sạch lông, ngâm xong là chưng.")) + """

  <h2>Bảo quản và lưu ý khi dùng</h2>
  <p>Yến chưng đông trùng hạ thảo nên để nguội, đậy kín, cất ngăn mát và dùng trong vài ngày. Đông trùng sấy khô chưa dùng thì để hũ kín, nơi khô mát, đậy nắp ngay sau mỗi lần lấy để nấm không hút ẩm. Đây là món ăn, không thay thế thuốc; trẻ nhỏ, phụ nữ mang thai, người có bệnh nền hoặc đang dùng thuốc nên hỏi bác sĩ trước khi dùng đông trùng hạ thảo.</p>
  <p>Việt Cường Nhân làm yến từ năm 2009, có xưởng nhặt lông và nhà máy đạt HACCP, ISO 22000:2018, GMP; nấm đông trùng hạ thảo do Việt Cường Nhân nuôi trồng và sấy khô. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>, giá chưa gồm phí giao hàng. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Chưng yến với đông trùng hạ thảo tỉ lệ bao nhiêu?", "Mỗi chén khoảng 4 g yến khô với 1 g nấm đông trùng hạ thảo sấy (khoảng 10–15 sợi) và 150–200 ml nước."),
       ("Khi nào cho đông trùng hạ thảo vào yến?", "Cho ở 5–10 phút cuối khi chưng. Cho từ đầu nấm dễ nhạt màu và nát."),
       ("Yến chưng đông trùng hạ thảo chưng bao lâu?", "Tổng khoảng 20–30 phút cách thủy với lửa nhỏ: chưng yến 15–20 phút, sau đó thêm đông trùng chưng tiếp 5–10 phút."),
       ("Có cần ngâm đông trùng hạ thảo trước khi chưng không?", "Không cần ngâm lâu. Chỉ tráng nhanh qua nước sạch rồi cho vào thố ở cuối thời gian chưng."),
       ("Dùng đông trùng loại nào để chưng yến?", "Loại gãy đủ cho chưng hằng ngày và giá mềm hơn; loại cây cọng nguyên hợp khi đãi khách hoặc biếu tặng.")]),
dict(slug="chao-yen-cho-be", cat="Món ngon", ngay="2026-10-31",
  tu_khoa="cháo yến cho bé, cách nấu cháo yến cho bé, cháo yến cho bé ăn dặm, cháo yến thịt bằm cho bé, cháo yến bí đỏ",
  h1="Cháo yến cho bé: cách nấu và lưu ý theo độ tuổi",
  desc="Cách nấu cháo yến cho bé từ yến vụn: nguyên liệu 1 chén nhỏ, các bước nấu, 4 món dễ làm và lưu ý theo độ tuổi. Nên hỏi bác sĩ nhi trước khi cho bé ăn.",
  lede="Cháo yến cho bé nấu đơn giản: nấu cháo thật nhừ, cho yến vụn đã ngâm mềm vào ở 5–7 phút cuối, nêm thật nhạt. Trước khi cho bé ăn yến lần đầu, cha mẹ nên hỏi bác sĩ nhi về độ tuổi và lượng phù hợp, rồi bắt đầu với lượng rất nhỏ để theo dõi.",
  tom_tat=["Hỏi bác sĩ nhi trước khi cho bé ăn yến lần đầu, nhất là bé dưới 1 tuổi hoặc có cơ địa dị ứng.",
           "Dùng yến vụn hoặc yến tinh chế đã nhặt sạch lông, ngâm 15–20 phút, nấu cùng cháo 5–7 phút cuối.",
           "Lần đầu chỉ cho lượng rất nhỏ, ăn vào buổi sáng để dễ theo dõi biểu hiện lạ trong ngày.",
           "Cháo cho bé nêm thật nhạt, không thêm đường phèn nhiều, không dùng chung với nhiều món mới cùng lúc.",
           f"{P[107][2]} giá {gia(107)}/100gr tại Việt Cường Nhân, sợi nhỏ, nở nhanh, hợp nấu cháo."],
  body=f"""  <h2>Bé mấy tuổi thì nên ăn cháo yến?</h2>
  <p>Không có một độ tuổi chung áp dụng cho mọi bé; thời điểm cho bé ăn yến nên được bác sĩ nhi tư vấn dựa trên sức khỏe, cơ địa và quá trình ăn dặm của bé. Nhiều gia đình chờ đến khi bé đã ăn dặm quen với nhiều loại thực phẩm mới bắt đầu thử yến.</p>
  <p>Ở xưởng Việt Cường Nhân, câu cha mẹ hay hỏi nhất là "bé nhà em ăn yến được chưa". Chúng tôi là cơ sở sản xuất thực phẩm, không phải bác sĩ, nên luôn khuyên cha mẹ hỏi bác sĩ nhi trước, sau đó mới chọn loại yến và cách nấu phù hợp.</p>
  <table><thead><tr><th>Giai đoạn</th><th>Gợi ý chung</th><th>Kết cấu cháo</th></tr></thead><tbody>
  <tr><td>Bé mới ăn dặm, dưới 1 tuổi</td><td>Không tự ý cho ăn; hỏi bác sĩ nhi trước</td><td>Theo hướng dẫn của bác sĩ</td></tr>
  <tr><td>Bé đã ăn dặm quen, được bác sĩ đồng ý</td><td>Thử lượng rất nhỏ, mỗi lần một món mới</td><td>Cháo nấu nhừ, yến vụn xé thật nhỏ</td></tr>
  <tr><td>Bé lớn, đã nhai tốt</td><td>Có thể kết hợp thịt, rau củ quen thuộc</td><td>Cháo hạt, sợi yến ngắn</td></tr>
  </tbody></table>
  <p>Nếu bé có tiền sử dị ứng thực phẩm, chàm, hen hoặc đang điều trị bệnh, cha mẹ càng cần hỏi bác sĩ trước khi cho bé thử bất kỳ thực phẩm mới nào, kể cả yến.</p>

  <h2>Chọn loại yến nấu cháo cho bé</h2>
  <p>Yến vụn đã nhặt sạch lông là lựa chọn tiện nhất để nấu cháo cho bé, vì sợi nhỏ, nở nhanh và hòa đều vào cháo. Không nên dùng yến thô còn lông cho bé nếu không có thời gian nhặt thật kỹ.</p>
  <ul>
    <li><b>Yến tinh chế vụn baby:</b> sợi nhỏ, dễ chia lượng ít, ngâm 15–20 phút.</li>
    <li><b>Yến tinh chế vụn đắp tổ:</b> vụn được đắp thành tai, lấy từng phần gọn.</li>
    <li><b>Tránh:</b> chân yến (sợi dai, cứng) và yến thô chưa làm sạch.</li>
  </ul>
  <p>Yến vụn là gì và khác yến sợi thế nào, xem bài <a href="yen-vun-baby-la-gi.html">yến vụn baby là gì, dùng làm món gì</a>.</p>

  <h2>Cách nấu cháo yến cho bé (1 chén nhỏ)</h2>
  <p>Cách nấu cháo yến cho bé gồm 3 phần: nấu cháo nhừ, sơ chế yến, rồi cho yến vào cháo ở cuối. Lượng yến trong công thức dưới đây là lượng nhỏ để nấu một chén; lượng cho từng bé nên theo tư vấn của bác sĩ.</p>
  <h3>Nguyên liệu</h3>
  <ul>
    <li>Khoảng 20 g gạo tẻ (hoặc cháo trắng nấu sẵn).</li>
    <li>Khoảng 300 ml nước hoặc nước dùng rau củ không nêm.</li>
    <li>Một lượng nhỏ yến vụn, khoảng 1 g yến khô.</li>
    <li>Rau củ hoặc thịt bé đã ăn quen (tùy chọn).</li>
  </ul>
  <h3>Các bước</h3>
  <ol>
    <li><b>Nấu cháo:</b> vo gạo, nấu với nước lửa nhỏ khoảng 30–40 phút đến khi hạt nở bung. Bé nhỏ thì rây hoặc xay mịn.</li>
    <li><b>Ngâm yến:</b> ngâm yến vụn trong nước sạch 15–20 phút, đổ qua rây lưới nhỏ, kiểm tra lại dưới đèn xem còn sợi lông nào không.</li>
    <li><b>Xé nhỏ:</b> dùng tay xé sợi yến thật nhỏ hoặc băm nhuyễn để bé dễ nuốt.</li>
    <li><b>Cho yến vào cháo:</b> khi cháo đã nhừ, cho yến vào, khuấy đều, nấu lửa nhỏ thêm 5–7 phút.</li>
    <li><b>Để nguội bớt:</b> nêm rất nhạt hoặc không nêm, để nguội đến độ ấm vừa rồi cho bé ăn.</li>
  </ol>

  <h2>4 món cháo yến cho bé dễ làm</h2>
  <p>Khi bé đã ăn quen cháo yến và từng nguyên liệu kèm theo, có thể đổi món bằng các loại rau củ, thịt bé đã ăn không có vấn đề gì. Mỗi lần chỉ thêm một nguyên liệu mới.</p>
  <table><thead><tr><th>Món</th><th>Nguyên liệu thêm</th><th>Cách làm</th></tr></thead><tbody>
  <tr><td>Cháo yến bí đỏ</td><td>30 g bí đỏ</td><td>Hấp chín, nghiền mịn, khuấy vào cháo trước khi cho yến</td></tr>
  <tr><td>Cháo yến cà rốt</td><td>20 g cà rốt</td><td>Luộc mềm, nghiền, cho vào cháo cùng lúc với yến</td></tr>
  <tr><td>Cháo yến thịt gà</td><td>20 g ức gà</td><td>Băm nhuyễn, nấu chín kỹ trong cháo rồi mới cho yến</td></tr>
  <tr><td>Cháo yến hạt sen</td><td>10 g hạt sen bỏ tim</td><td>Nấu sen thật nhừ, nghiền, khuấy vào cháo</td></tr>
  </tbody></table>
  <p>Cách sơ chế hạt sen để không bị đắng có ở bài <a href="yen-chung-tao-do-hat-sen.html">cách làm yến chưng táo đỏ hạt sen</a>.</p>

  <h2>Lưu ý an toàn khi nấu cháo yến cho bé</h2>
  <p>Điều quan trọng nhất khi cho bé ăn yến là bắt đầu thật ít, theo dõi kỹ và hỏi bác sĩ khi có thắc mắc. Các lưu ý dưới đây là kinh nghiệm chung về chế biến thực phẩm cho trẻ, không thay thế tư vấn y tế.</p>
  <ul>
    <li><b>Lần đầu ăn buổi sáng:</b> để dễ theo dõi bé trong ngày; không thử cùng lúc nhiều món mới.</li>
    <li><b>Theo dõi biểu hiện lạ:</b> nếu bé nổi mẩn, ngứa, nôn, tiêu chảy, quấy khác thường thì ngưng cho ăn; nếu bé khó thở, sưng môi mặt thì đưa bé đi cơ sở y tế ngay.</li>
    <li><b>Nhặt lông thật kỹ:</b> kể cả yến tinh chế, nên kiểm tra lại dưới đèn trước khi nấu.</li>
    <li><b>Nấu chín, ăn ngay:</b> cháo nấu xong nên cho bé ăn trong bữa, không để cháo qua đêm ở nhiệt độ phòng.</li>
    <li><b>Nêm nhạt:</b> không thêm muối, nước mắm, đường phèn nhiều vào cháo của bé.</li>
    <li><b>Không thay bữa chính:</b> cháo yến là một món trong thực đơn đa dạng, không thay sữa và các nhóm thực phẩm khác.</li>
  </ul>

  <h2>Bảo quản yến vụn để nấu cháo cho bé</h2>
  <p>Yến vụn khô cất trong hộp kín, nơi khô ráo, tránh nắng; đậy kín ngay sau khi lấy vì sợi nhỏ dễ hút ẩm. Có thể chia sẵn yến thành các phần nhỏ trong túi kín để mỗi lần nấu lấy một phần, đỡ phải mở hộp nhiều lần.</p>
  <p>Yến vụn của Việt Cường Nhân được nhặt lông tại xưởng, nhà máy đạt HACCP, ISO 22000:2018 và GMP. Giá dưới đây lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(107, "Sợi nhỏ, rời, dễ chia lượng ít."), li(106, "Vụn đắp thành tai, lấy từng phần gọn.")) + """
  <p>Cách chọn yến có nguồn gốc rõ ràng xem bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a> hoặc nhắn Zalo 0978 094 739 để được tư vấn chọn loại yến.</p>""",
  faq=[("Bé mấy tuổi ăn được cháo yến?", "Không có một độ tuổi chung cho mọi bé. Cha mẹ nên hỏi bác sĩ nhi trước; nhiều gia đình chờ bé ăn dặm quen với nhiều loại thực phẩm rồi mới thử yến."),
       ("Nấu cháo yến cho bé dùng loại yến nào?", "Nên dùng yến vụn hoặc yến tinh chế đã nhặt sạch lông, sợi nhỏ, nở nhanh và dễ hòa vào cháo. Tránh chân yến và yến thô chưa làm sạch."),
       ("Cho yến vào cháo lúc nào?", "Khi cháo đã nấu nhừ, cho yến đã ngâm mềm vào và nấu lửa nhỏ thêm 5–7 phút."),
       ("Bé ăn cháo yến bao nhiêu là đủ?", "Lượng phù hợp tùy từng bé, nên hỏi bác sĩ nhi. Lần đầu chỉ nên cho lượng rất nhỏ và theo dõi bé trong ngày."),
       ("Bé ăn yến bị nổi mẩn thì làm sao?", "Ngưng cho bé ăn và hỏi bác sĩ. Nếu bé khó thở, sưng môi, sưng mặt hoặc nôn nhiều thì đưa bé đến cơ sở y tế ngay.")]),
dict(slug="ba-bau-an-yen-duoc-khong", cat="Yến sào", ngay="2026-10-31",
  tu_khoa="bà bầu ăn yến, bà bầu ăn yến được không, bà bầu ăn yến lúc nào, mẹ bầu ăn yến chưng, bà bầu uống nước yến",
  h1="Bà bầu ăn yến được không? Lưu ý khi dùng",
  desc="Bà bầu ăn yến được không? Yến sào là thực phẩm, nhiều mẹ bầu vẫn dùng nhưng nên hỏi bác sĩ trước. Lưu ý chọn yến, cách chưng ít đường, khi nào cần thận trọng.",
  lede="Bà bầu ăn yến là chuyện nhiều gia đình quan tâm: yến sào là một thực phẩm, nhiều mẹ bầu vẫn dùng như một món ăn trong chế độ ăn đa dạng. Tuy vậy mỗi thai kỳ khác nhau, nên mẹ bầu cần hỏi bác sĩ sản khoa trước khi dùng, nhất là khi có tiểu đường thai kỳ, dị ứng hoặc bệnh nền.",
  tom_tat=["Yến sào là thực phẩm, không phải thuốc; bà bầu nên hỏi bác sĩ sản khoa trước khi đưa yến vào thực đơn.",
           "Mẹ bầu có tiểu đường thai kỳ, dị ứng thực phẩm hoặc bệnh nền cần đặc biệt hỏi ý kiến bác sĩ.",
           "Chọn yến có nguồn gốc rõ ràng, đã làm sạch, chưng chín kỹ và nêm ít đường phèn.",
           "Lần đầu dùng lượng nhỏ, không ăn thay bữa chính, ngưng ngay nếu thấy biểu hiện bất thường.",
           f"Nước yến hũ tiện cho mẹ bầu đi làm, ví dụ {P[124][2]} giá {gia(124)}/hũ; nên xem thành phần đường trên nhãn."],
  body=f"""  <h2>Bà bầu ăn yến được không?</h2>
  <p>Bà bầu ăn yến được hay không nên do bác sĩ theo dõi thai kỳ trả lời cho từng người, vì sức khỏe mỗi mẹ bầu khác nhau. Về bản chất, yến sào là một loại thực phẩm, và nhiều mẹ bầu vẫn dùng yến chưng như một món ăn bên cạnh các bữa chính.</p>
  <p>Ở xưởng Việt Cường Nhân, mẹ bầu và người nhà hay hỏi "bầu mấy tháng ăn yến được" hoặc "mỗi tuần ăn mấy lần". Chúng tôi là cơ sở sản xuất thực phẩm, không đưa ra lời khuyên y khoa, nên luôn khuyên mẹ bầu mang câu hỏi này đến bác sĩ trong lần khám thai, sau đó chọn loại yến và cách chưng phù hợp.</p>
  <p>Bài viết này không nói về công dụng của yến với thai kỳ. Yến sào không phải là thuốc và không thay thế chế độ ăn, thuốc bổ hay chỉ định của bác sĩ.</p>

  <h2>Khi nào bà bầu cần hỏi kỹ bác sĩ trước khi ăn yến?</h2>
  <p>Mọi mẹ bầu đều nên hỏi bác sĩ trước, nhưng các trường hợp dưới đây cần đặc biệt thận trọng và chỉ dùng khi bác sĩ đồng ý.</p>
  <table><thead><tr><th>Trường hợp</th><th>Vì sao cần hỏi bác sĩ</th></tr></thead><tbody>
  <tr><td>Tiểu đường thai kỳ hoặc đường huyết cao</td><td>Yến chưng và nước yến thường có đường; cần kiểm soát lượng đường trong khẩu phần</td></tr>
  <tr><td>Có tiền sử dị ứng thực phẩm</td><td>Bất kỳ thực phẩm mới nào cũng có thể gây dị ứng ở người có cơ địa nhạy cảm</td></tr>
  <tr><td>Thai kỳ có nguy cơ, đang điều trị</td><td>Chế độ ăn cần theo chỉ định riêng của bác sĩ</td></tr>
  <tr><td>Ốm nghén nặng, khó tiêu</td><td>Cần chọn thời điểm và món ăn hợp với tình trạng tiêu hóa</td></tr>
  <tr><td>Đang dùng thuốc, thực phẩm bổ sung</td><td>Bác sĩ cần biết toàn bộ những gì mẹ bầu đang dùng</td></tr>
  </tbody></table>

  <h2>Bà bầu ăn yến lúc nào?</h2>
  <p>Nếu bác sĩ đồng ý, mẹ bầu có thể ăn yến vào lúc thấy dễ chịu nhất trong ngày, thường là giữa buổi sáng hoặc giữa buổi chiều, cách bữa chính khoảng 1 tiếng. Tránh ăn khi bụng quá no hoặc lúc đang buồn nôn.</p>
  <ul>
    <li><b>Giữa buổi:</b> khoảng 9–10 giờ sáng hoặc 15–16 giờ chiều, như một bữa phụ nhẹ.</li>
    <li><b>Buổi tối:</b> nếu ăn tối, nên dùng chén nhỏ, ít đường và cách giờ ngủ khoảng 1 tiếng.</li>
    <li><b>Ba tháng đầu:</b> nhiều mẹ bầu bị nghén, nên hỏi bác sĩ về thời điểm bắt đầu và chọn lúc ít nghén nhất.</li>
  </ul>
  <p>Thời điểm ăn yến chung cho người lớn xem thêm ở bài <a href="an-yen-luc-nao-tot-nhat.html">ăn yến lúc nào trong ngày là hợp lý</a>.</p>

  <h2>Lưu ý khi bà bầu ăn yến</h2>
  <p>Những lưu ý dưới đây là kinh nghiệm chung về chọn và chế biến thực phẩm, giúp mẹ bầu dùng yến an toàn hơn sau khi đã hỏi bác sĩ.</p>
  <ol>
    <li><b>Chọn yến có nguồn gốc rõ ràng:</b> mua của cơ sở có địa chỉ sản xuất, chứng nhận an toàn thực phẩm và bản tự công bố sản phẩm.</li>
    <li><b>Chọn yến đã làm sạch:</b> yến tinh chế đã nhặt lông tại xưởng giúp mẹ bầu đỡ mất công ngâm, nhặt lâu.</li>
    <li><b>Chưng chín kỹ:</b> chưng cách thủy đủ thời gian, ăn khi còn ấm hoặc để ngăn mát và dùng sớm.</li>
    <li><b>Ít đường:</b> nêm ít đường phèn hoặc dùng vị ngọt tự nhiên của táo đỏ; với nước yến hũ, đọc thành phần đường trên nhãn.</li>
    <li><b>Bắt đầu lượng nhỏ:</b> lần đầu dùng chén nhỏ, theo dõi cơ thể; ngưng và hỏi bác sĩ nếu thấy ngứa, nổi mẩn, khó chịu.</li>
    <li><b>Không thay bữa chính:</b> yến chỉ là một món trong thực đơn, mẹ bầu vẫn cần đủ các nhóm thực phẩm theo hướng dẫn của bác sĩ.</li>
    <li><b>Không kết hợp tùy tiện:</b> tránh tự ý chưng yến cùng các vị thuốc bắc, thảo dược khi chưa hỏi bác sĩ.</li>
  </ol>

  <h2>Cách chưng yến cho bà bầu ít đường</h2>
  <p>Cách đơn giản nhất là chưng yến cách thủy với táo đỏ hoặc hạt sen, dùng rất ít hoặc không dùng đường phèn. Một chén thường dùng 3–5 g yến khô với 150–200 ml nước; lượng phù hợp cho mẹ bầu nên hỏi bác sĩ.</p>
  <ol>
    <li>Ngâm yến tinh chế 30–60 phút, vớt qua rây, xé tơi.</li>
    <li>Cho yến, 2–3 quả táo đỏ cắt lát và nước vào thố.</li>
    <li>Chưng cách thủy lửa nhỏ 20–30 phút, đậy kín nắp.</li>
    <li>Nếm thử; chỉ thêm chút đường phèn ở 5 phút cuối nếu cần.</li>
  </ol>
  <p>Công thức chi tiết với hạt sen có ở bài <a href="yen-chung-tao-do-hat-sen.html">cách làm yến chưng táo đỏ hạt sen</a>; các bước chưng cơ bản xem bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Chọn yến chưng tại nhà hay nước yến hũ?</h2>
  <p>Yến chưng tại nhà giúp mẹ bầu tự kiểm soát lượng đường và nguyên liệu; nước yến hũ chưng sẵn tiện mang đi làm nhưng cần đọc kỹ thành phần trên nhãn.</p>
  <table><thead><tr><th>Tiêu chí</th><th>Yến tự chưng</th><th>Nước yến hũ</th></tr></thead><tbody>
  <tr><td>Kiểm soát đường</td><td>Tự quyết định, có thể không đường</td><td>Theo công thức nhà sản xuất, xem nhãn</td></tr>
  <tr><td>Thời gian</td><td>Ngâm và chưng khoảng 1–1,5 tiếng</td><td>Mở nắp là dùng</td></tr>
  <tr><td>Bảo quản</td><td>Ngăn mát, dùng trong vài ngày</td><td>Hũ chưa mở để nơi khô mát; mở rồi dùng trong ngày</td></tr>
  </tbody></table>
""" + ul(li(109, "Đã nhặt sạch lông, ngâm xong là chưng."), li(124, "Chưng sẵn từ yến tươi, xem thành phần trên nhãn.")) + """
  <p>Cách chọn yến thật và các giấy tờ nên hỏi người bán xem bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>. Việt Cường Nhân làm yến từ năm 2009, nhà máy đạt HACCP, ISO 22000:2018 và GMP. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>, giá chưa gồm phí giao hàng; cần tư vấn chọn loại yến, nhắn Zalo 0978 094 739.</p>""",
  faq=[("Bà bầu ăn yến được không?", "Yến sào là một thực phẩm và nhiều mẹ bầu vẫn dùng như một món ăn. Tuy vậy mỗi thai kỳ khác nhau, nên mẹ bầu cần hỏi bác sĩ sản khoa trước khi dùng."),
       ("Bà bầu 3 tháng đầu ăn yến được không?", "Ba tháng đầu là giai đoạn nhiều mẹ bầu bị nghén và cần theo dõi kỹ. Mẹ bầu nên hỏi bác sĩ về việc có nên dùng và thời điểm bắt đầu."),
       ("Bà bầu ăn yến lúc nào?", "Nếu bác sĩ đồng ý, có thể ăn giữa buổi sáng hoặc giữa buổi chiều, cách bữa chính khoảng 1 tiếng, tránh lúc đang buồn nôn hoặc quá no."),
       ("Bà bầu bị tiểu đường thai kỳ có ăn yến được không?", "Cần hỏi bác sĩ trước. Nếu được đồng ý, nên chưng yến không đường hoặc rất ít đường và đọc kỹ thành phần đường của nước yến hũ."),
       ("Bà bầu uống nước yến hũ được không?", "Nên hỏi bác sĩ trước và đọc thành phần trên nhãn, nhất là lượng đường. Hũ đã mở nên dùng hết trong ngày.")]),
dict(slug="cach-lam-sach-yen-tho", cat="Yến sào", ngay="2026-10-31",
  tu_khoa="cách làm sạch yến thô, cách nhặt lông yến thô tại nhà, sơ chế yến thô, ngâm yến thô bao lâu",
  h1="Cách làm sạch yến thô tại nhà: 5 bước (có video)",
  desc="Cách làm sạch yến thô tại nhà qua 5 bước: ngâm nở mềm, xé tơi theo thớ, lọc qua rây, nhặt lông bằng nhíp trên nền trắng, xả lại nước sạch. Kèm video và mẹo.",
  lede="Cách làm sạch yến thô tại nhà gồm 5 bước: ngâm nước sạch đến khi tổ nở mềm, xé tơi nhẹ tay theo thớ sợi, lọc qua rây cho bụi và lông nổi lên, đặt trên nền trắng dùng nhíp nhặt từng sợi lông, rồi xả lại nước sạch và để ráo. Sau đó yến đã sạch có thể chưng cách thủy cùng hạt sen, đường phèn.",
  tom_tat=["5 bước: ngâm nở mềm, xé tơi theo thớ sợi, lọc qua rây, nhặt lông bằng nhíp trên nền trắng, xả lại nước sạch.",
           "Nhặt lông bằng nhíp là khâu lâu nhất; thời gian tùy lượng lông của từng tổ.",
           "Chỉ dùng nước sạch, không dùng nước nóng hay hóa chất để làm sạch yến.",
           "Yến sạch đem chưng cách thủy cùng hạt sen, đường phèn là có chén yến sợi dai, thơm nhẹ.",
           f"Không có thời gian thì chọn yến tinh chế đã làm sạch sẵn, ví dụ {P[109][2]} {gia(109)}/100gr."],
  video=dict(yt="Shx390T-45g", ten="5 bước làm sạch yến thô tại nhà", ngay="2026-10-30"),
  cac_buoc=[("Ngâm nước sạch", "Ngâm tổ yến thô trong nước sạch đến khi tổ nở mềm."),
            ("Xé tơi theo thớ sợi", "Xé tơi tổ yến nhẹ tay theo thớ sợi để lông và bụi lộ ra."),
            ("Lọc qua rây", "Lọc yến qua rây trong nước cho bụi và lông nổi lên rồi gạn bỏ."),
            ("Nhặt lông bằng nhíp", "Đặt yến trên nền trắng, dùng nhíp nhặt từng sợi lông còn sót."),
            ("Xả lại nước sạch", "Xả yến lại bằng nước sạch, để ráo rồi đem chưng.")],
  body=f"""  <h2>Cách làm sạch yến thô tại nhà: 5 bước</h2>
  <p>Làm sạch yến thô tại nhà chỉ cần nước sạch, một cái rây, một cái nhíp và nền trắng để dễ thấy lông. Đây cũng là 5 bước trong video hướng dẫn của Việt Cường Nhân ở đầu bài.</p>
  <ol>
    <li><b>Ngâm nước sạch đến khi tổ nở mềm.</b> Cho tổ yến thô vào tô nước sạch ở nhiệt độ thường, ngâm đến khi tổ mềm, các sợi tách nhẹ ra. Yến thô thường cần ngâm lâu hơn yến tinh chế; phần chân tổ đặc nên mềm chậm nhất.</li>
    <li><b>Xé tơi nhẹ tay theo thớ sợi.</b> Dùng tay tách tổ theo chiều thớ sợi thành từng mảng nhỏ. Xé nhẹ để sợi yến không bị đứt vụn, đồng thời lông và bụi kẹt bên trong lộ ra.</li>
    <li><b>Lọc qua rây cho bụi và lông nổi lên.</b> Đặt yến vào rây lưới nhỏ, nhúng trong tô nước sạch và lắc nhẹ. Bụi, lông nhẹ nổi lên mặt nước hoặc trôi ra; thay nước vài lần đến khi nước trong.</li>
    <li><b>Đặt trên nền trắng, dùng nhíp nhặt từng sợi lông.</b> Trải từng ít yến lên đĩa trắng hoặc khay trắng có chút nước, dùng nhíp đầu nhọn nhặt từng sợi lông nhỏ còn bám. Đây là khâu lâu nhất và cần kiên nhẫn.</li>
    <li><b>Xả lại nước sạch, để ráo.</b> Cho yến đã nhặt lông vào rây, xả lại bằng nước sạch, để ráo nước. Yến lúc này sẵn sàng để chưng.</li>
  </ol>

  <h2>Dụng cụ cần chuẩn bị</h2>
  <p>Dụng cụ làm sạch yến thô đều là đồ có sẵn trong bếp, quan trọng nhất là nhíp tốt và đủ ánh sáng.</p>
  <table><thead><tr><th>Dụng cụ</th><th>Dùng để</th><th>Lưu ý</th></tr></thead><tbody>
  <tr><td>Tô hoặc thau sạch</td><td>Ngâm yến</td><td>Đủ rộng để tổ nở ra</td></tr>
  <tr><td>Rây lưới nhỏ</td><td>Lọc bụi, lông, giữ sợi yến</td><td>Lưới mịn để không trôi sợi vụn</td></tr>
  <tr><td>Nhíp đầu nhọn</td><td>Nhặt từng sợi lông</td><td>Đầu nhíp khít, không gỉ</td></tr>
  <tr><td>Đĩa hoặc khay màu trắng</td><td>Làm nền để thấy lông đen</td><td>Đổ chút nước để sợi yến tơi ra</td></tr>
  <tr><td>Đèn sáng</td><td>Soi lông nhỏ</td><td>Ngồi nơi sáng, ánh sáng trắng</td></tr>
  </tbody></table>

  <h2>Ngâm yến thô bao lâu là đủ?</h2>
  <p>Ngâm yến thô đến khi tổ nở mềm và xé tơi được là đủ, không có một con số cố định cho mọi tổ. Tổ khô, dày hoặc có nhiều phần chân sẽ cần ngâm lâu hơn tổ mỏng.</p>
  <ul>
    <li>Dùng nước sạch ở nhiệt độ thường, không dùng nước nóng vì sợi yến dễ bị nhũn và tan khi chưng.</li>
    <li>Nếu cần ngâm lâu, có thể để tô yến trong ngăn mát tủ lạnh.</li>
    <li>Phần chân tổ đặc, có thể tách riêng và ngâm thêm; xem bài <a href="chan-yen-chan-tua-la-gi.html">chân yến là gì</a>.</li>
  </ul>

  <h2>Mẹo nhặt lông yến nhanh và sạch hơn</h2>
  <p>Nhặt lông nhanh hơn khi chia yến thành từng phần nhỏ và làm trên nền trắng có nước, vì sợi yến tơi ra còn lông đen nổi rõ.</p>
  <ul>
    <li><b>Làm từng ít một:</b> mỗi lần chỉ trải một nhúm nhỏ lên đĩa, nhặt xong mới lấy tiếp.</li>
    <li><b>Đĩa có chút nước:</b> sợi yến xòe ra, lông nhỏ dễ thấy và dễ gắp hơn.</li>
    <li><b>Chấm nhíp vào nước:</b> lông dính vào nhíp được rửa ngay, không rơi lại vào yến.</li>
    <li><b>Kiểm tra lần cuối:</b> sau khi xả nước, soi lại dưới đèn một lượt.</li>
    <li><b>Ngồi thoải mái:</b> khâu này tốn thời gian, nên chọn lúc rảnh như buổi tối.</li>
  </ul>

  <h2>Những lỗi thường gặp khi làm sạch yến thô</h2>
  <ul>
    <li><b>Ngâm nước nóng:</b> làm sợi yến mềm nhũn, khi chưng dễ tan.</li>
    <li><b>Vò mạnh tay:</b> sợi yến đứt vụn, trôi qua rây.</li>
    <li><b>Dùng hóa chất, chất tẩy:</b> tuyệt đối không dùng; chỉ cần nước sạch và nhíp.</li>
    <li><b>Bỏ qua bước xả cuối:</b> bụi nhỏ còn sót có thể làm nước chưng bị đục.</li>
  </ul>

  <h2>Sau khi làm sạch: chưng yến cùng hạt sen, đường phèn</h2>
  <p>Yến thô đã làm sạch được chưng giống yến tinh chế: chưng cách thủy lửa nhỏ, thêm hạt sen đã nấu mềm và đường phèn ở cuối. Một chén thường dùng 3–5 g yến khô với 150–200 ml nước.</p>
  <p>Công thức chi tiết có ở bài <a href="yen-chung-tao-do-hat-sen.html">cách làm yến chưng táo đỏ hạt sen</a> và <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>. Lưu ý yến thô sau khi nhặt lông sẽ hao hụt một phần khối lượng, nên số chén ít hơn yến tinh chế cùng khối lượng, xem bài <a href="100gr-yen-chung-duoc-bao-nhieu-chen.html">100gr yến chưng được bao nhiêu chén</a>.</p>

  <h2>Không có thời gian? Chọn yến tinh chế đã làm sạch sẵn</h2>
  <p>Nếu không có thời gian ngâm và nhặt lông, yến tinh chế đã được làm sạch sẵn tại xưởng là lựa chọn tiện hơn: chỉ cần ngâm rồi chưng. Yến thô hợp với người có thời gian và muốn tự tay làm sạch.</p>
  <table><thead><tr><th>Tiêu chí</th><th>Yến thô</th><th>Yến tinh chế</th></tr></thead><tbody>
  <tr><td>Lông, tạp chất</td><td>Còn, phải tự nhặt</td><td>Đã nhặt sạch tại xưởng</td></tr>
  <tr><td>Công sơ chế tại nhà</td><td>5 bước, nhặt lông lâu</td><td>Ngâm 30–60 phút rồi chưng</td></tr>
  <tr><td>Giá 100gr</td><td>{gia(104)} – {gia(101)}</td><td>{gia(109)} (1 lớp sợi vừa)</td></tr>
  </tbody></table>
""" + ul(li(101, "Ít lông, dễ làm sạch hơn."), li(104, "Giá mềm, cần nhặt lông kỹ."), li(109, "Đã nhặt sạch lông, ngâm xong là chưng.")) + """
  <p>Xem cả quá trình từ tổ yến thô đến chén yến ở bài <a href="cach-chung-yen-tho-hat-sen.html">cách chưng yến thô: từ tổ yến đến chén yến hạt sen</a>. Muốn so sánh kỹ các loại, xem bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>, giá chưa gồm phí giao hàng. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Làm sạch yến thô tại nhà như thế nào?", "Gồm 5 bước: ngâm nước sạch đến khi tổ nở mềm, xé tơi nhẹ tay theo thớ sợi, lọc qua rây cho bụi và lông nổi lên, đặt trên nền trắng dùng nhíp nhặt từng sợi lông, rồi xả lại nước sạch và để ráo."),
       ("Ngâm yến thô bao lâu?", "Ngâm đến khi tổ nở mềm và xé tơi được; tổ dày hoặc nhiều phần chân cần lâu hơn. Dùng nước sạch nhiệt độ thường, không dùng nước nóng."),
       ("Nhặt lông yến thô bằng gì?", "Dùng nhíp đầu nhọn, đặt yến trên đĩa hoặc khay trắng có chút nước dưới đèn sáng để dễ thấy và gắp từng sợi lông."),
       ("Có nên dùng hóa chất để làm sạch yến nhanh hơn không?", "Không. Chỉ cần nước sạch, rây và nhíp; không dùng hóa chất hay chất tẩy cho thực phẩm."),
       ("Không có thời gian nhặt lông thì mua loại nào?", "Chọn yến tinh chế đã được nhặt sạch lông tại xưởng, về nhà chỉ cần ngâm 30–60 phút rồi chưng.")]),
dict(slug="cach-chung-yen-tho-hat-sen", cat="Món ngon", ngay="2026-10-31",
  tu_khoa="chưng yến thô, cách chưng yến thô với hạt sen, từ tổ yến thô đến chén yến chưng, sơ chế tổ yến thô",
  h1="Cách chưng yến thô: từ tổ yến đến chén yến hạt sen",
  desc="Cách chưng yến thô từ A đến Z: ngâm, xé tơi, lọc rây, nhặt lông bằng nhíp, xả sạch rồi chưng cách thủy cùng hạt sen, đường phèn. Kèm video, định lượng 2 chén.",
  lede="Chưng yến thô cần làm sạch trước rồi mới chưng: ngâm cho tổ nở mềm, xé tơi, lọc qua rây cho bụi trôi đi, nhặt từng sợi lông nhỏ bằng nhíp, xả lại nước sạch, sau đó chưng cách thủy cùng hạt sen và đường phèn. Kết quả là chén yến sợi dai, thơm nhẹ.",
  tom_tat=["Quy trình: ngâm nở mềm, xé tơi, lọc rây, nhặt lông bằng nhíp, xả nước sạch, chưng cách thủy cùng hạt sen, đường phèn.",
           "Nhặt từng sợi lông nhỏ bằng nhíp là khâu lâu nhất của cả quá trình.",
           "Định lượng 2 chén: 8 g yến đã làm sạch (tính theo yến khô), 30 g hạt sen, 400 ml nước, 20–30 g đường phèn.",
           "Hạt sen nấu mềm trước khoảng 20 phút, sau đó chưng cùng yến khoảng 20–25 phút, đường phèn cho ở 5 phút cuối.",
           f"Nhà bận có yến tinh chế ({P[109][2]} {gia(109)}/100gr) và yến chưng sẵn ({P[124][2]} {gia(124)}/hũ)."],
  video=dict(yt="2FkERIYAkR8", ten="Từ tổ yến thô đến chén yến chưng hạt sen", ngay="2026-10-31"),
  cac_buoc=[("Ngâm tổ yến", "Ngâm tổ yến thô trong nước sạch cho tổ nở mềm."),
            ("Xé tơi", "Xé tơi tổ yến nhẹ tay theo thớ sợi."),
            ("Lọc qua rây", "Lọc yến qua rây trong nước sạch cho bụi trôi đi."),
            ("Nhặt lông bằng nhíp", "Nhặt từng sợi lông nhỏ bằng nhíp; đây là khâu lâu nhất."),
            ("Xả lại nước sạch", "Xả yến lại bằng nước sạch và để ráo."),
            ("Chưng cách thủy cùng hạt sen", "Chưng yến cách thủy cùng hạt sen đã nấu mềm, thêm đường phèn ở 5 phút cuối.")],
  body=f"""  <h2>Cách chưng yến thô gồm những bước nào?</h2>
  <p>Cách chưng yến thô gồm hai phần: làm sạch tổ yến (5 bước) và chưng cách thủy cùng hạt sen, đường phèn. Video ở đầu bài quay lại toàn bộ quá trình từ tổ yến thô đến chén yến chưng hạt sen.</p>
  <table><thead><tr><th>Giai đoạn</th><th>Việc cần làm</th><th>Ghi chú</th></tr></thead><tbody>
  <tr><td>1. Ngâm</td><td>Ngâm nước sạch cho tổ nở mềm</td><td>Nước nhiệt độ thường</td></tr>
  <tr><td>2. Xé tơi</td><td>Tách tổ nhẹ tay theo thớ sợi</td><td>Không vò mạnh</td></tr>
  <tr><td>3. Lọc rây</td><td>Lọc qua rây cho bụi trôi đi</td><td>Thay nước đến khi trong</td></tr>
  <tr><td>4. Nhặt lông</td><td>Dùng nhíp nhặt từng sợi lông nhỏ</td><td>Khâu lâu nhất</td></tr>
  <tr><td>5. Xả sạch</td><td>Xả lại nước sạch, để ráo</td><td>Soi lại dưới đèn</td></tr>
  <tr><td>6. Chưng</td><td>Chưng cách thủy cùng hạt sen, đường phèn</td><td>Lửa nhỏ, khoảng 20–25 phút</td></tr>
  </tbody></table>

  <h2>Làm sạch tổ yến thô trước khi chưng</h2>
  <p>Tổ yến thô còn lông và bụi tự nhiên từ nhà yến, nên bắt buộc phải làm sạch trước khi chưng. Năm bước làm sạch được hướng dẫn chi tiết, kèm mẹo nhặt lông nhanh, ở bài <a href="cach-lam-sach-yen-tho.html">cách làm sạch yến thô tại nhà: 5 bước</a>.</p>
  <ol>
    <li><b>Ngâm cho tổ nở mềm:</b> ngâm tổ trong nước sạch đến khi các sợi tách nhẹ ra.</li>
    <li><b>Xé tơi:</b> tách tổ theo thớ sợi thành mảng nhỏ để lông, bụi lộ ra.</li>
    <li><b>Lọc qua rây cho bụi trôi đi:</b> nhúng rây trong tô nước sạch, lắc nhẹ, thay nước vài lần.</li>
    <li><b>Nhặt từng sợi lông nhỏ bằng nhíp:</b> trải yến trên đĩa trắng có chút nước, gắp từng sợi lông.</li>
    <li><b>Xả lại nước sạch:</b> cho yến vào rây, xả nước, để ráo.</li>
  </ol>
  <h3>Vì sao nhặt lông là khâu lâu nhất?</h3>
  <p>Lông yến rất nhỏ, bám xen giữa các sợi tổ, nên phải gắp từng sợi bằng nhíp chứ không thể rửa trôi hết. Ở các xưởng nhặt lông của Việt Cường Nhân, khâu này cũng làm thủ công bằng nhíp, và đây là lý do yến tinh chế đã nhặt sạch lông có giá cao hơn yến thô cùng khối lượng.</p>

  <h2>Chưng yến thô cùng hạt sen, đường phèn (2 chén)</h2>
  <p>Sau khi làm sạch, yến thô được chưng như yến tinh chế: nấu hạt sen mềm trước, rồi chưng cách thủy cùng yến khoảng 20–25 phút, thêm đường phèn ở 5 phút cuối.</p>
  <h3>Nguyên liệu</h3>
  <ul>
    <li>Yến đã làm sạch: khoảng 8 g tính theo yến khô (khoảng 4 g mỗi chén).</li>
    <li>Hạt sen: 30 g hạt khô (ngâm khoảng 2 tiếng) hoặc 50 g hạt tươi, đã bỏ tim.</li>
    <li>Nước lọc: 400 ml.</li>
    <li>Đường phèn: 20–30 g, tùy khẩu vị.</li>
  </ul>
  <h3>Các bước chưng</h3>
  <ol>
    <li><b>Nấu hạt sen:</b> nấu hạt sen với 400 ml nước khoảng 20 phút đến khi bở mềm, giữ lại nước nấu.</li>
    <li><b>Cho vào thố:</b> chia yến đã làm sạch, hạt sen và nước nấu sen vào thố, đậy nắp.</li>
    <li><b>Chưng cách thủy:</b> đặt thố vào nồi nước sôi lăn tăn, lửa nhỏ, chưng khoảng 20–25 phút.</li>
    <li><b>Thêm đường phèn:</b> cho đường phèn ở 5 phút cuối, khuấy nhẹ cho tan rồi tắt bếp.</li>
  </ol>
  <p>Chén yến đạt khi sợi yến trong, dai, thơm nhẹ mùi yến, hạt sen bở và nước ngọt thanh. Muốn thêm táo đỏ, xem công thức <a href="yen-chung-tao-do-hat-sen.html">yến chưng táo đỏ hạt sen</a>; các bước chưng cơ bản ở bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Mẹo để chén yến từ tổ thô sợi dai, thơm</h2>
  <ul>
    <li><b>Không ngâm nước nóng:</b> sợi yến dễ nhũn, khi chưng dễ tan.</li>
    <li><b>Xé theo thớ sợi:</b> giữ sợi dài, chén yến có độ dai.</li>
    <li><b>Lửa nhỏ, đậy kín:</b> nước sôi mạnh làm sợi tan, nước đọng nhỏ vào làm loãng chén yến.</li>
    <li><b>Không chưng quá lâu:</b> tối đa khoảng 30 phút tính từ lúc cho yến vào thố.</li>
    <li><b>Phần chân tổ:</b> đặc và cứng hơn, có thể ngâm lâu hơn; xem bài <a href="chan-yen-chan-tua-la-gi.html">chân yến là gì</a>.</li>
  </ul>

  <h2>Nhà bận rộn: chọn yến tinh chế hoặc yến chưng sẵn</h2>
  <p>Nếu không có thời gian làm sạch tổ yến thô, có hai lựa chọn tiện hơn: yến tinh chế đã nhặt sạch lông tại xưởng (chỉ cần ngâm rồi chưng) và nước yến chưng sẵn (mở nắp là dùng).</p>
  <table><thead><tr><th>Lựa chọn</th><th>Công làm tại nhà</th><th>Phù hợp</th></tr></thead><tbody>
  <tr><td>Yến thô</td><td>Ngâm, nhặt lông, chưng</td><td>Người có thời gian, muốn tự tay làm</td></tr>
  <tr><td>Yến tinh chế</td><td>Ngâm 30–60 phút rồi chưng</td><td>Gia đình chưng yến hằng tuần</td></tr>
  <tr><td>Yến chưng sẵn</td><td>Không cần nấu</td><td>Người đi làm, mang theo, biếu</td></tr>
  </tbody></table>
  <p>Giá lấy từ bảng giá website Việt Cường Nhân, chưa gồm phí giao hàng:</p>
""" + ul(li(101, "Yến thô ít lông, tự làm sạch tại nhà."), li(109, "Đã nhặt sạch lông, ngâm xong là chưng."), li(124, "Chưng sẵn từ yến tươi."), li(126, "Hũ nhỏ, tiện mang đi.")) + """
  <p>So sánh kỹ các loại yến xem bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>. Việt Cường Nhân làm yến từ năm 2009, có nhà yến, xưởng nhặt lông và nhà máy đạt HACCP, ISO 22000:2018, GMP. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>; mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Yến thô có chưng trực tiếp được không?", "Không nên. Yến thô còn lông và bụi tự nhiên, cần ngâm, xé tơi, lọc rây, nhặt lông bằng nhíp và xả lại nước sạch trước khi chưng."),
       ("Chưng yến thô với hạt sen bao lâu?", "Nấu hạt sen mềm trước khoảng 20 phút, sau đó chưng cách thủy cùng yến đã làm sạch khoảng 20–25 phút, thêm đường phèn ở 5 phút cuối."),
       ("Khâu nào lâu nhất khi chưng yến thô?", "Nhặt từng sợi lông nhỏ bằng nhíp là khâu lâu nhất, vì lông bám xen giữa các sợi tổ và phải gắp thủ công."),
       ("Chưng yến thô cần bao nhiêu hạt sen?", "Cho 2 chén dùng khoảng 8 g yến (tính theo yến khô), 30 g hạt sen khô đã bỏ tim và 400 ml nước."),
       ("Không có thời gian làm sạch yến thô thì nên mua gì?", "Chọn yến tinh chế đã nhặt sạch lông tại xưởng, hoặc nước yến chưng sẵn đóng hũ, mở nắp là dùng.")]),
dict(slug="tre-may-tuoi-an-duoc-yen", cat="Yến sào", ngay="2026-10-31",
  tu_khoa="trẻ mấy tuổi ăn được yến, bé mấy tuổi ăn yến được, trẻ em ăn yến, cho bé ăn yến lần đầu, trẻ uống nước yến được không",
  h1="Trẻ mấy tuổi ăn được yến sào? Lưu ý cho cha mẹ",
  desc="Trẻ mấy tuổi ăn được yến? Không có một mốc chung cho mọi bé, cha mẹ nên hỏi bác sĩ nhi trước. Cách cho bé thử lần đầu, chọn loại yến, dấu hiệu dị ứng cần lưu ý.",
  lede="Trẻ mấy tuổi ăn được yến là câu hỏi không có một mốc chung cho mọi bé: thời điểm phù hợp tùy sức khỏe, cơ địa và quá trình ăn dặm của từng trẻ, nên cha mẹ cần hỏi bác sĩ nhi trước. Nhiều gia đình chờ đến khi bé đã ăn dặm quen với nhiều loại thực phẩm, thường sau 1 tuổi, rồi mới cho thử một lượng rất nhỏ.",
  tom_tat=["Không có độ tuổi chung cho mọi trẻ; cha mẹ nên hỏi bác sĩ nhi trước khi cho bé ăn yến lần đầu.",
           "Bé dưới 1 tuổi, bé có cơ địa dị ứng, chàm, hen hoặc đang điều trị bệnh càng cần ý kiến bác sĩ.",
           "Lần đầu chỉ cho lượng rất nhỏ, vào buổi sáng, không thử cùng lúc với món mới khác để dễ theo dõi.",
           "Ngưng cho ăn nếu bé nổi mẩn, ngứa, nôn, tiêu chảy; đưa đi cơ sở y tế ngay nếu bé khó thở, sưng môi mặt.",
           f"Yến vụn đã nhặt sạch lông dễ nấu cho trẻ, ví dụ {P[106][2]} giá {gia(106)}/100gr tại Việt Cường Nhân."],
  body=f"""  <h2>Trẻ mấy tuổi ăn được yến?</h2>
  <p>Không có một độ tuổi áp dụng cho mọi trẻ; bé nào ăn yến được và từ khi nào nên do bác sĩ nhi tư vấn dựa trên sức khỏe, cơ địa và quá trình ăn dặm của bé. Yến sào là một thực phẩm, nên cách tiếp cận giống khi cho bé làm quen bất kỳ thực phẩm mới nào: hỏi bác sĩ, thử ít, theo dõi kỹ.</p>
  <p>Ở xưởng Việt Cường Nhân, nhiều cha mẹ hỏi "bé nhà em mấy tháng thì ăn yến được". Chúng tôi là cơ sở sản xuất thực phẩm, không phải bác sĩ, nên không đưa ra mốc tuổi hay lượng dùng cho trẻ. Điều chúng tôi chia sẻ được là cách chọn yến sạch, cách sơ chế và những lưu ý chung khi cho bé thử thực phẩm mới.</p>
  <table><thead><tr><th>Tình huống</th><th>Cha mẹ nên làm gì</th></tr></thead><tbody>
  <tr><td>Bé dưới 1 tuổi, đang ăn dặm giai đoạn đầu</td><td>Không tự ý cho ăn yến; hỏi bác sĩ nhi trước</td></tr>
  <tr><td>Bé đã ăn dặm quen nhiều loại thực phẩm</td><td>Hỏi bác sĩ; nếu được đồng ý, thử lượng rất nhỏ trong cháo</td></tr>
  <tr><td>Bé có cơ địa dị ứng, chàm, hen</td><td>Cần ý kiến bác sĩ trước khi thử bất kỳ thực phẩm mới nào</td></tr>
  <tr><td>Bé đang ốm, đang điều trị hoặc dùng thuốc</td><td>Hỏi bác sĩ đang điều trị cho bé</td></tr>
  <tr><td>Bé lớn, đã ăn yến nhiều lần không có vấn đề</td><td>Dùng như một món trong thực đơn đa dạng, không thay bữa chính</td></tr>
  </tbody></table>

  <h2>Vì sao cần hỏi bác sĩ trước khi cho trẻ ăn yến?</h2>
  <p>Cần hỏi bác sĩ vì hệ tiêu hóa và cơ địa của trẻ nhỏ khác người lớn, và như mọi thực phẩm giàu đạm, yến có thể không hợp với một số bé. Bác sĩ nhi theo dõi bé qua các lần khám nên đánh giá được bé đã sẵn sàng hay chưa.</p>
  <ul>
    <li><b>Dị ứng thực phẩm:</b> bất kỳ thực phẩm mới nào cũng có thể gây dị ứng ở trẻ có cơ địa nhạy cảm.</li>
    <li><b>Giai đoạn ăn dặm:</b> bé cần làm quen lần lượt từng nhóm thực phẩm cơ bản trước.</li>
    <li><b>Đường và gia vị:</b> yến chưng, nước yến hũ thường có đường, không hợp với trẻ nhỏ nếu bác sĩ khuyên hạn chế.</li>
  </ul>
  <p>Khi đi khám, cha mẹ có thể hỏi bác sĩ: bé đã ăn yến được chưa, nên bắt đầu với món gì, bao lâu cho ăn một lần, và cần theo dõi dấu hiệu gì.</p>

  <h2>Cho bé ăn yến lần đầu thế nào?</h2>
  <p>Nếu bác sĩ đồng ý, lần đầu nên cho bé ăn một lượng rất nhỏ yến nấu chín kỹ trong món bé đã quen, như cháo, rồi theo dõi bé trong ngày. Không nên cho bé thử yến cùng lúc với một món mới khác.</p>
  <ol>
    <li><b>Chọn yến sạch:</b> yến tinh chế hoặc yến vụn đã nhặt sạch lông, có nguồn gốc rõ ràng.</li>
    <li><b>Sơ chế kỹ:</b> ngâm yến vụn 15–20 phút, lọc qua rây, soi dưới đèn để nhặt sợi lông còn sót.</li>
    <li><b>Nấu chín, xé nhỏ:</b> xé sợi yến thật nhỏ, nấu cùng cháo đã nhừ thêm 5–7 phút.</li>
    <li><b>Thử vào buổi sáng:</b> để cả ngày có thể quan sát bé.</li>
    <li><b>Theo dõi 2–3 ngày:</b> chưa thêm món mới nào khác trong thời gian này để dễ nhận biết nếu có phản ứng.</li>
  </ol>
  <p>Công thức chi tiết và các món cháo đổi vị xem bài <a href="chao-yen-cho-be.html">cháo yến cho bé: cách nấu và lưu ý theo độ tuổi</a>.</p>

  <h2>Dấu hiệu dị ứng cần lưu ý khi trẻ ăn yến</h2>
  <p>Sau khi bé ăn yến, nếu thấy biểu hiện bất thường thì ngưng cho ăn và hỏi bác sĩ; các dấu hiệu nặng cần đưa bé đi cơ sở y tế ngay. Đây là lưu ý chung cho mọi thực phẩm mới, không riêng yến sào.</p>
  <table><thead><tr><th>Biểu hiện</th><th>Cha mẹ nên làm gì</th></tr></thead><tbody>
  <tr><td>Nổi mẩn đỏ, ngứa, quấy khóc khác thường</td><td>Ngưng cho ăn, liên hệ bác sĩ</td></tr>
  <tr><td>Nôn, tiêu chảy, đau bụng</td><td>Ngưng cho ăn, theo dõi và hỏi bác sĩ</td></tr>
  <tr><td>Khó thở, thở rít, sưng môi, sưng mặt, lừ đừ</td><td>Đưa bé đến cơ sở y tế ngay</td></tr>
  </tbody></table>

  <h2>Trẻ em ăn yến loại nào, nấu món gì?</h2>
  <p>Với trẻ nhỏ, yến vụn đã nhặt sạch lông là loại dễ dùng nhất vì sợi nhỏ, nở nhanh, hòa đều vào cháo và súp. Không nên dùng chân yến (sợi dai, cứng) hay yến thô chưa làm sạch cho bé.</p>
  <ul>
    <li><b>Bé nhỏ:</b> cháo nấu nhừ, sợi yến xé hoặc băm thật nhỏ, nêm nhạt.</li>
    <li><b>Bé lớn hơn, nhai tốt:</b> cháo hạt, súp gà yến, yến chưng táo đỏ ít đường.</li>
    <li><b>Hạn chế đường:</b> chưng yến cho trẻ nên ít hoặc không đường phèn, dùng vị ngọt của táo đỏ.</li>
  </ul>
  <p>Yến vụn là gì, khác yến sợi thế nào xem bài <a href="yen-vun-baby-la-gi.html">yến vụn baby là gì, dùng làm món gì</a>.</p>

  <h2>Trẻ uống nước yến hũ được không?</h2>
  <p>Nước yến hũ chưng sẵn thường có đường, nên cha mẹ cần đọc thành phần trên nhãn và hỏi bác sĩ trước khi cho trẻ uống, nhất là trẻ nhỏ. Với trẻ nhỏ, yến tự nấu tại nhà giúp cha mẹ chủ động hơn về lượng đường và cách chế biến.</p>
  <p>Cách dùng và bảo quản nước yến xem bài <a href="nuoc-yen-chung-san-cach-dung-bao-quan.html">nước yến chưng sẵn: chọn loại nào, dùng và bảo quản ra sao</a>.</p>

  <h2>Chọn yến sạch cho trẻ</h2>
  <p>Khi mua yến cho trẻ, nên chọn cơ sở có địa chỉ sản xuất, chứng nhận an toàn thực phẩm và bản tự công bố sản phẩm; các dấu hiệu chọn yến thật xem bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>. Việt Cường Nhân làm yến từ năm 2009, yến được nhặt lông tại xưởng, nhà máy đạt HACCP, ISO 22000:2018 và GMP. Giá dưới đây lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(107, "Sợi nhỏ, rời, dễ chia lượng ít để nấu cháo."), li(106, "Vụn đắp thành tai, lấy từng phần gọn."), li(124, "Chưng sẵn; đọc thành phần đường trên nhãn trước khi cho trẻ dùng.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>, hoặc nhắn Zalo 0978 094 739 để được tư vấn chọn loại yến.</p>""",
  faq=[("Trẻ mấy tuổi ăn được yến?", "Không có một độ tuổi chung cho mọi trẻ. Cha mẹ nên hỏi bác sĩ nhi; nhiều gia đình chờ bé ăn dặm quen với nhiều loại thực phẩm, thường sau 1 tuổi, rồi mới cho thử."),
       ("Trẻ dưới 1 tuổi ăn yến được không?", "Không nên tự ý cho bé dưới 1 tuổi ăn yến. Hãy hỏi bác sĩ nhi trước, vì bé còn trong giai đoạn làm quen các nhóm thực phẩm cơ bản."),
       ("Cho bé ăn yến lần đầu cần lưu ý gì?", "Cho lượng rất nhỏ yến nấu chín trong món bé đã quen, ăn vào buổi sáng, không thử cùng lúc với món mới khác và theo dõi bé 2–3 ngày."),
       ("Trẻ ăn yến bao nhiêu là đủ?", "Lượng phù hợp tùy từng bé, cha mẹ nên hỏi bác sĩ nhi. Việt Cường Nhân không đưa ra lượng dùng cho trẻ."),
       ("Trẻ ăn yến bị dị ứng có biểu hiện gì?", "Có thể nổi mẩn, ngứa, nôn, tiêu chảy hoặc quấy khác thường; khi đó ngưng cho ăn và hỏi bác sĩ. Nếu bé khó thở, sưng môi mặt thì đưa đến cơ sở y tế ngay.")]),
dict(slug="nguoi-gia-an-yen-the-nao", cat="Yến sào", ngay="2026-11-01",
  tu_khoa="người già ăn yến, người lớn tuổi ăn yến, người già ăn yến lúc nào, cách chưng yến cho người già, người già uống nước yến",
  h1="Người già ăn yến thế nào cho hợp? Lưu ý khi dùng",
  desc="Người già ăn yến thế nào cho hợp? Cách chọn yến sợi mềm, chưng loãng ít đường, ăn lúc nào trong ngày, và khi nào người lớn tuổi có bệnh nền nên hỏi bác sĩ trước.",
  lede="Người già ăn yến hợp nhất khi yến được chưng mềm, loãng, ít đường và dùng chén nhỏ vào lúc bụng nhẹ, như giữa buổi sáng hoặc đầu giờ tối. Yến sào là thực phẩm, không phải thuốc; người lớn tuổi có bệnh nền như tiểu đường, bệnh thận hoặc đang dùng thuốc nên hỏi bác sĩ trước khi đưa yến vào thực đơn.",
  tom_tat=["Yến sào là thực phẩm, không thay thế thuốc hay chế độ ăn bác sĩ chỉ định cho người lớn tuổi.",
           "Người có tiểu đường, bệnh thận, dị ứng hoặc đang dùng thuốc nên hỏi bác sĩ trước khi dùng yến.",
           "Chọn yến tinh chế sợi vừa hoặc yến vụn, chưng mềm với nhiều nước hơn (khoảng 200 ml cho mỗi chén) và ít đường phèn.",
           "Dùng chén nhỏ, ăn ấm vào giữa buổi sáng hoặc đầu giờ tối, cách bữa chính khoảng 1 tiếng.",
           f"Ông bà ngại nấu có thể dùng nước yến chưng sẵn, ví dụ {P[124][2]} giá {gia(124)}/hũ; nên đọc thành phần đường trên nhãn."],
  body=f"""  <h2>Người già ăn yến được không?</h2>
  <p>Người già ăn yến được như một món ăn trong bữa ăn đa dạng, miễn là yến được chọn sạch, chưng mềm và phù hợp với tình trạng sức khỏe của từng người. Yến sào là thực phẩm, không phải thuốc, nên không thay thế thuốc men hay chế độ ăn mà bác sĩ đã dặn.</p>
  <p>Ở xưởng Việt Cường Nhân, con cháu hay hỏi "mua yến cho ông bà thì chọn loại nào, chưng thế nào". Câu trả lời ngắn: chọn yến đã nhặt sạch lông, chưng loãng và mềm, ít đường, chén nhỏ; còn ông bà có bệnh nền thì nên hỏi bác sĩ trước.</p>

  <h2>Khi nào người lớn tuổi nên hỏi bác sĩ trước khi ăn yến?</h2>
  <p>Người lớn tuổi có bệnh mạn tính hoặc đang dùng thuốc nên hỏi bác sĩ trước, vì chế độ ăn của họ thường cần điều chỉnh riêng. Bảng dưới là các trường hợp thường gặp.</p>
  <table><thead><tr><th>Tình trạng</th><th>Vì sao nên hỏi bác sĩ</th></tr></thead><tbody>
  <tr><td>Tiểu đường, đường huyết cao</td><td>Yến chưng và nước yến hũ thường có đường; cần kiểm soát lượng đường trong khẩu phần</td></tr>
  <tr><td>Bệnh thận, cần hạn chế đạm</td><td>Yến là thực phẩm giàu đạm; bác sĩ sẽ cho biết khẩu phần đạm phù hợp</td></tr>
  <tr><td>Có tiền sử dị ứng thực phẩm</td><td>Bất kỳ thực phẩm mới nào cũng có thể gây dị ứng ở người có cơ địa nhạy cảm</td></tr>
  <tr><td>Đang dùng nhiều loại thuốc</td><td>Bác sĩ cần biết toàn bộ những gì người bệnh đang ăn uống, dùng thêm</td></tr>
  <tr><td>Khó nuốt, đang ốm, mới phẫu thuật</td><td>Cần chọn kết cấu món ăn và thời điểm phù hợp</td></tr>
  </tbody></table>

  <h2>Chọn loại yến nào cho người già?</h2>
  <p>Người già nên dùng yến đã nhặt sạch lông, sợi vừa hoặc sợi vụn, vì dễ chưng mềm và dễ nhai, nuốt. Tránh chân yến (sợi dai, cứng) với người răng yếu, và tránh yến thô nếu không có người nhặt lông kỹ.</p>
  <table><thead><tr><th>Loại yến</th><th>Kết cấu khi chưng</th><th>Hợp với</th></tr></thead><tbody>
  <tr><td>Yến tinh chế 1 lớp sợi vừa</td><td>Mềm, sợi rõ</td><td>Người còn nhai tốt, ăn yến chưng đường phèn</td></tr>
  <tr><td>Yến tinh chế vụn</td><td>Rất mềm, hòa vào món</td><td>Người răng yếu, nấu cháo, súp</td></tr>
  <tr><td>Chân yến</td><td>Dai, giòn</td><td>Không hợp người răng yếu</td></tr>
  <tr><td>Nước yến chưng sẵn</td><td>Lỏng, mở nắp là dùng</td><td>Người ngại nấu, cần tiện</td></tr>
  </tbody></table>
  <p>Khác nhau giữa các nhóm yến xem bài <a href="yen-sao-loai-nao-tot.html">yến sào loại nào tốt</a>; yến vụn xem bài <a href="yen-vun-baby-la-gi.html">yến vụn baby là gì</a>.</p>

  <h2>Cách chưng yến cho người già mềm, ít đường</h2>
  <p>Chưng yến cho người già nên dùng nhiều nước hơn bình thường, chưng đủ mềm và giảm đường phèn. Một chén thường dùng 3–5 g yến khô; với người lớn tuổi, nhiều gia đình chưng loãng hơn với khoảng 200 ml nước.</p>
  <ol>
    <li><b>Ngâm yến:</b> yến tinh chế sợi 30–60 phút, yến vụn 15–20 phút; vớt qua rây, xé tơi nhỏ.</li>
    <li><b>Cho vào thố:</b> yến với khoảng 200 ml nước, thêm 2–3 lát táo đỏ hoặc vài hạt sen đã nấu mềm nếu thích.</li>
    <li><b>Chưng cách thủy:</b> lửa nhỏ, đậy kín, khoảng 25–30 phút để sợi yến mềm.</li>
    <li><b>Nêm nhẹ:</b> rất ít đường phèn ở 5 phút cuối, hoặc bỏ hẳn đường và dùng vị ngọt tự nhiên của táo đỏ.</li>
    <li><b>Ăn ấm:</b> để nguội bớt đến độ ấm vừa rồi mới dùng.</li>
  </ol>
  <p>Các bước chưng cơ bản có ở bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>; công thức có hạt sen xem bài <a href="yen-chung-tao-do-hat-sen.html">cách làm yến chưng táo đỏ hạt sen</a>.</p>

  <h2>Người già ăn yến lúc nào?</h2>
  <p>Người lớn tuổi có thể ăn yến vào lúc bụng nhẹ, thường là giữa buổi sáng hoặc đầu giờ tối, cách bữa chính khoảng 1 tiếng. Không nên ăn quá khuya ngay trước khi ngủ hoặc ăn khi vừa no.</p>
  <ul>
    <li><b>Giữa buổi sáng (khoảng 9–10 giờ):</b> thay cho bữa phụ, ăn ấm.</li>
    <li><b>Đầu giờ tối:</b> chén nhỏ, ít đường, cách giờ ngủ ít nhất 1 tiếng.</li>
    <li><b>Đều đặn hơn là nhiều:</b> dùng chén nhỏ vài lần mỗi tuần dễ duy trì hơn ăn nhiều một lúc.</li>
  </ul>
  <p>Gợi ý thời điểm chung cho người lớn xem bài <a href="an-yen-luc-nao-tot-nhat.html">ăn yến lúc nào trong ngày là hợp lý</a>.</p>

  <h2>Món yến dễ ăn cho người lớn tuổi</h2>
  <table><thead><tr><th>Món</th><th>Cách làm ngắn</th><th>Lưu ý</th></tr></thead><tbody>
  <tr><td>Yến chưng táo đỏ ít đường</td><td>Chưng yến với táo đỏ cắt lát 25–30 phút</td><td>Có thể bỏ đường phèn</td></tr>
  <tr><td>Cháo yến thịt bằm</td><td>Cho yến vụn vào cháo nhừ, nấu thêm 5–7 phút</td><td>Hợp người răng yếu</td></tr>
  <tr><td>Súp gà yến</td><td>Thêm yến vào nồi súp 10 phút cuối</td><td>Nêm nhạt, ít muối</td></tr>
  <tr><td>Yến chưng hạt sen</td><td>Nấu hạt sen mềm trước rồi chưng cùng yến</td><td>Nhớ bỏ tim sen</td></tr>
  </tbody></table>

  <h2>Lưu ý khi người già ăn yến</h2>
  <ul>
    <li><b>Bắt đầu chén nhỏ:</b> lần đầu dùng ít, theo dõi; ngưng và hỏi bác sĩ nếu thấy ngứa, nổi mẩn, khó chịu bụng.</li>
    <li><b>Không thay bữa chính:</b> yến chỉ là một món, ông bà vẫn cần đủ cơm, rau, thịt cá theo hướng dẫn của bác sĩ.</li>
    <li><b>Không ngưng thuốc:</b> ăn yến không thay cho thuốc đang dùng.</li>
    <li><b>Ít đường, ít muối:</b> nhất là với người có tiểu đường, huyết áp cao.</li>
    <li><b>Không tự ý chưng với thuốc bắc:</b> hỏi bác sĩ trước khi kết hợp yến với thảo dược.</li>
    <li><b>Bảo quản đúng:</b> yến đã chưng để nguội, đậy kín, cất ngăn mát và dùng trong vài ngày.</li>
  </ul>

  <h2>Yến chưng tại nhà hay nước yến hũ cho ông bà?</h2>
  <p>Yến chưng tại nhà giúp con cháu chủ động lượng đường và độ mềm; nước yến chưng sẵn tiện cho ông bà ở một mình hoặc ngại nấu, nhưng nên đọc thành phần trên nhãn. Giá dưới đây lấy từ bảng giá website Việt Cường Nhân, chưa gồm phí giao hàng:</p>
""" + ul(li(109, "Đã nhặt sạch lông, ngâm xong là chưng."), li(124, "Chưng sẵn từ yến tươi, hũ nhỏ."), li(125, "Hũ lớn, hợp gia đình dùng chung.")) + """
  <p>Cách dùng và bảo quản nước yến xem bài <a href="nuoc-yen-chung-san-cach-dung-bao-quan.html">nước yến chưng sẵn: chọn loại nào, dùng và bảo quản ra sao</a>. Việt Cường Nhân làm yến từ năm 2009, có xưởng nhặt lông và nhà máy đạt HACCP, ISO 22000:2018, GMP. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>; mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Người già ăn yến được không?", "Được, như một món ăn trong bữa ăn đa dạng. Người lớn tuổi có bệnh nền như tiểu đường, bệnh thận hoặc đang dùng thuốc nên hỏi bác sĩ trước."),
       ("Người già nên ăn yến loại nào?", "Yến tinh chế sợi vừa hoặc yến vụn đã nhặt sạch lông, vì dễ chưng mềm và dễ nuốt. Người răng yếu nên tránh chân yến vì sợi dai, cứng."),
       ("Người già ăn yến lúc nào?", "Giữa buổi sáng hoặc đầu giờ tối, cách bữa chính khoảng 1 tiếng, dùng chén nhỏ và ăn ấm. Không nên ăn quá khuya."),
       ("Người bị tiểu đường ăn yến được không?", "Cần hỏi bác sĩ trước. Nếu được đồng ý, nên chưng yến không đường hoặc rất ít đường và đọc kỹ thành phần đường của nước yến hũ."),
       ("Chưng yến cho người già thế nào?", "Dùng 3–5 g yến khô với khoảng 200 ml nước, chưng cách thủy lửa nhỏ 25–30 phút cho mềm, nêm rất ít đường phèn hoặc dùng táo đỏ để có vị ngọt.")]),
]
