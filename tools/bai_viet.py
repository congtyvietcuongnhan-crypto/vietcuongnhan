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
]
