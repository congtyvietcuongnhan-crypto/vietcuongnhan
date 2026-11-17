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
  desc="Người già ăn yến thế nào cho hợp? Cách chọn yến sợi mềm, chưng loãng ít đường, ăn lúc nào trong ngày và khi nào người có bệnh nền nên hỏi bác sĩ trước.",
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
dict(slug="bao-quan-yen-sao", cat="Yến sào", ngay="2026-11-01",
  tu_khoa="bảo quản yến sào, bảo quản yến chưng, yến sào để được bao lâu, bảo quản yến khô, yến bị ẩm mốc",
  h1="Cách bảo quản yến sào khô và yến đã chưng",
  desc="Cách bảo quản yến sào đúng: yến khô để hộp kín nơi khô mát, yến đã ngâm và đã chưng cất ngăn mát, dùng trong vài ngày. Dấu hiệu yến bị ẩm mốc, hỏng cần bỏ.",
  lede="Bảo quản yến sào khô đúng cách là để trong hộp hoặc túi kín, nơi khô ráo, thoáng mát, tránh nắng và hơi ẩm; yến đã ngâm hoặc đã chưng thì phải cất ngăn mát tủ lạnh và dùng trong vài ngày. Yến có mùi chua, mốc, nhớt hoặc đổi màu bất thường thì nên bỏ.",
  tom_tat=["Yến khô: hộp hoặc túi kín, nơi khô ráo, thoáng mát, tránh nắng; xem hạn dùng in trên bao bì.",
           "Yến đã ngâm nở nhưng chưa chưng: để ráo, đậy kín, cất ngăn mát và chưng sớm trong ngày.",
           "Yến đã chưng: để nguội, chia hũ nhỏ đậy kín, cất ngăn mát và dùng trong vài ngày.",
           "Nước yến hũ chưa mở để nơi khô mát; đã mở nắp thì dùng hết trong ngày.",
           "Bỏ yến nếu có mùi chua, mốc, đốm lạ, sợi nhớt hoặc đổi màu bất thường."],
  body=f"""  <h2>Bảo quản yến sào khô thế nào?</h2>
  <p>Yến sào khô bảo quản tốt nhất trong hộp hoặc túi kín, đặt nơi khô ráo, thoáng mát, tránh ánh nắng trực tiếp và hơi ẩm. Kẻ thù lớn nhất của yến khô là độ ẩm: yến hút ẩm sẽ mềm, dễ mốc và có mùi lạ.</p>
  <ul>
    <li><b>Giữ hộp gốc:</b> hộp yến của nhà sản xuất thường có túi hút ẩm; mở ra lấy xong thì đóng kín ngay.</li>
    <li><b>Hộp kín khí:</b> nếu hộp gốc không kín, chuyển yến sang hũ thủy tinh hoặc hộp nhựa thực phẩm có nắp khít.</li>
    <li><b>Tránh nơi nóng ẩm:</b> không để gần bếp, bồn rửa, cửa sổ nắng chiếu hay trong xe hơi.</li>
    <li><b>Dùng tay khô, dụng cụ khô:</b> lấy yến bằng tay sạch, khô để không đưa hơi nước vào hộp.</li>
    <li><b>Xem hạn dùng:</b> thời hạn sử dụng in trên bao bì là mốc nên theo.</li>
  </ul>
  <h3>Có nên để yến khô trong tủ lạnh?</h3>
  <p>Yến khô đóng kín không cần để tủ lạnh nếu nhà khô thoáng. Ở nơi nồm ẩm, có thể cho yến vào hộp kín khí rồi đặt ngăn mát; khi lấy ra nên để hộp về nhiệt độ phòng rồi mới mở nắp, tránh hơi nước đọng lên sợi yến. Mở tủ, lấy yến rồi cất lại nhiều lần trong ngày dễ làm yến bị ẩm hơn.</p>

  <h2>Bảng bảo quản yến theo từng dạng</h2>
  <p>Mỗi dạng yến có cách bảo quản khác nhau: yến càng nhiều nước thì càng phải giữ lạnh và dùng sớm.</p>
  <table><thead><tr><th>Dạng yến</th><th>Cách bảo quản</th><th>Nên dùng trong</th></tr></thead><tbody>
  <tr><td>Yến khô (thô, tinh chế, rút lông)</td><td>Hộp kín, nơi khô ráo, thoáng mát, tránh nắng</td><td>Theo hạn dùng trên bao bì</td></tr>
  <tr><td>Yến đã ngâm, chưa chưng</td><td>Để ráo, hộp kín, ngăn mát tủ lạnh</td><td>Chưng sớm trong ngày</td></tr>
  <tr><td>Yến đã chưng</td><td>Để nguội, hũ nhỏ đậy kín, ngăn mát</td><td>Vài ngày</td></tr>
  <tr><td>Nước yến hũ chưa mở</td><td>Nơi khô mát, tránh nắng</td><td>Theo hạn dùng trên hũ</td></tr>
  <tr><td>Nước yến hũ đã mở nắp</td><td>Đậy lại, ngăn mát</td><td>Trong ngày</td></tr>
  </tbody></table>

  <h2>Bảo quản yến đã chưng</h2>
  <p>Yến đã chưng cần để nguội, chia vào hũ nhỏ đậy kín, cất ngăn mát tủ lạnh và dùng trong vài ngày. Không để yến chưng ở nhiệt độ phòng qua đêm.</p>
  <ol>
    <li><b>Để nguội tự nhiên:</b> để yến chưng nguội đến nhiệt độ phòng, đậy hờ để không bị bụi.</li>
    <li><b>Chia hũ nhỏ:</b> mỗi hũ đủ một lần ăn, để không phải mở nắp và múc nhiều lần từ một hũ lớn.</li>
    <li><b>Đậy kín, cất ngăn mát:</b> hũ thủy tinh có nắp khít giúp yến không lẫn mùi thức ăn khác trong tủ.</li>
    <li><b>Dùng muỗng sạch:</b> không dùng muỗng đã ăn để múc lại vào hũ.</li>
    <li><b>Hâm lại nhẹ:</b> muốn ăn ấm thì hâm cách thủy vài phút, không đun sôi lại nhiều lần.</li>
  </ol>
  <p>Mẹo hay nhất là chưng vừa đủ ăn trong 2–3 ngày thay vì chưng cả tuần một lần. Cách tính lượng yến cho từng mẻ xem bài <a href="100gr-yen-chung-duoc-bao-nhieu-chen.html">100gr yến chưng được bao nhiêu chén</a>; các bước chưng xem bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>
  <h3>Có nên để yến chưng ngăn đá?</h3>
  <p>Ở xưởng Việt Cường Nhân, chúng tôi khuyên nên chưng vừa đủ ăn và để ngăn mát thay vì cấp đông, vì sợi yến sau khi rã đông thường mềm hơn và dễ tan. Nếu buộc phải cấp đông, nên chia hũ nhỏ, rã đông trong ngăn mát và dùng ngay sau khi rã.</p>

  <h2>Bảo quản yến đã ngâm nhưng chưa chưng</h2>
  <p>Yến đã ngâm nở chứa nhiều nước nên hỏng nhanh hơn yến khô nhiều; tốt nhất là ngâm vừa đủ và chưng ngay. Nếu chưa kịp chưng, vớt yến để ráo, cho vào hộp kín, cất ngăn mát và chưng sớm trong ngày.</p>
  <ul>
    <li>Không ngâm sẵn cả hộp yến để dùng dần.</li>
    <li>Không để yến đã ngâm ở nhiệt độ phòng nhiều giờ, nhất là ngày nóng.</li>
    <li>Yến thô đang nhặt lông dở có thể để trong tô nước, đậy kín, đặt ngăn mát; xem bài <a href="cach-lam-sach-yen-tho.html">cách làm sạch yến thô tại nhà</a>.</li>
  </ul>

  <h2>Dấu hiệu yến bị ẩm, mốc, hỏng</h2>
  <p>Yến khô hoặc yến chưng có mùi chua, mùi mốc, đốm xanh đen, sợi nhớt hoặc màu lạ thì nên bỏ, không cố rửa lại để dùng. Yến tự nhiên chỉ có mùi tanh nhẹ đặc trưng.</p>
  <table><thead><tr><th>Dạng yến</th><th>Dấu hiệu nên bỏ</th></tr></thead><tbody>
  <tr><td>Yến khô</td><td>Sợi mềm ẩm, có đốm mốc, mùi mốc hoặc mùi hôi lạ, chuyển màu bất thường</td></tr>
  <tr><td>Yến đã ngâm</td><td>Nước ngâm đục, có bọt, mùi chua; sợi nhớt</td></tr>
  <tr><td>Yến đã chưng</td><td>Mùi chua, vị lạ, nước đục hoặc có váng, sợi nhũn nhớt</td></tr>
  <tr><td>Nước yến hũ</td><td>Nắp phồng, hũ hở, mùi vị lạ, quá hạn dùng</td></tr>
  </tbody></table>
  <p>Yến khô có màu ngà vàng không đồng đều là bình thường với yến tự nhiên; màu trắng tinh bất thường mới là điều nên hỏi kỹ. Xem thêm bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>.</p>

  <h2>Bảo quản nước yến hũ</h2>
  <p>Nước yến hũ tiệt trùng chưa mở nắp để nơi khô mát, tránh nắng, theo hạn dùng in trên hũ; để lạnh trước khi uống sẽ ngon hơn. Đã mở nắp thì nên uống hết trong ngày. Chi tiết xem bài <a href="nuoc-yen-chung-san-cach-dung-bao-quan.html">nước yến chưng sẵn: chọn loại nào, dùng và bảo quản ra sao</a>.</p>

  <h2>Mẹo mua và chia yến để bảo quản dễ hơn</h2>
  <ul>
    <li><b>Mua vừa đủ dùng:</b> một hộp 100gr đủ cho một người dùng khoảng 2–3 tháng nếu ăn 2–3 lần mỗi tuần.</li>
    <li><b>Chia phần khi mở hộp:</b> tách yến thành phần 4 g trong túi zip nhỏ, mỗi lần lấy một túi, hộp lớn ít bị mở.</li>
    <li><b>Ghi ngày mở hộp</b> lên nắp để biết yến đã mở bao lâu.</li>
    <li><b>Yến biếu tặng:</b> giữ nguyên hộp, dặn người nhận cất nơi khô mát.</li>
  </ul>
  <p>Yến của Việt Cường Nhân được sấy khô và đóng hộp tại xưởng đạt HACCP, ISO 22000:2018 và GMP, có ghi ngày sản xuất và hạn dùng trên bao bì. Giá dưới đây lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(109, "Dùng hằng ngày, ngâm xong là chưng."), li(113, "Sợi dài, hộp đẹp, hợp biếu tặng."), li(124, "Chưng sẵn, mở nắp là dùng.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Yến sào khô để được bao lâu?", "Yến khô đóng kín, để nơi khô ráo, thoáng mát dùng được theo hạn sử dụng in trên bao bì. Sau khi mở hộp nên đóng kín ngay và dùng dần."),
       ("Yến đã chưng để được bao lâu?", "Để nguội, chia hũ nhỏ đậy kín, cất ngăn mát và dùng trong vài ngày. Không để yến chưng ở nhiệt độ phòng qua đêm."),
       ("Có nên để yến khô trong tủ lạnh không?", "Không bắt buộc nếu nhà khô thoáng. Ở nơi nồm ẩm có thể để yến trong hộp kín khí ở ngăn mát, và để hộp về nhiệt độ phòng rồi mới mở nắp."),
       ("Làm sao biết yến bị hỏng?", "Yến có mùi chua, mùi mốc, đốm lạ, sợi nhớt hoặc nước đục, có váng thì nên bỏ. Yến tự nhiên chỉ có mùi tanh nhẹ đặc trưng."),
       ("Yến đã ngâm mà chưa chưng thì làm sao?", "Vớt yến để ráo, cho vào hộp kín, cất ngăn mát và chưng sớm trong ngày. Tốt nhất chỉ ngâm vừa đủ lượng định chưng.")]),
dict(slug="nuoc-yen-hu-uong-luc-nao", cat="Nước yến", ngay="2026-11-02",
  tu_khoa="nước yến uống lúc nào, nước yến hũ uống lúc nào, mỗi ngày uống mấy hũ nước yến, uống nước yến buổi tối được không, nước yến uống lạnh hay nóng",
  h1="Nước yến uống lúc nào, mỗi ngày mấy hũ là vừa?",
  desc="Nước yến uống lúc nào trong ngày? Gợi ý thời điểm uống nước yến hũ, mỗi lần một hũ như bữa phụ, uống lạnh hay ấm, lưu ý đường và cách bảo quản hũ đã mở.",
  lede="Nước yến uống lúc nào cũng được vì đây là thực phẩm, nhưng tiện và dễ chịu nhất là giữa buổi sáng hoặc giữa buổi chiều, cách bữa chính khoảng 1 tiếng. Nhiều người dùng mỗi lần một hũ như một bữa phụ nhẹ; người có bệnh nền, trẻ nhỏ và phụ nữ mang thai nên hỏi bác sĩ trước.",
  tom_tat=["Thời điểm tiện nhất: giữa buổi sáng (9–10 giờ) hoặc giữa buổi chiều (15–16 giờ), cách bữa chính khoảng 1 tiếng.",
           "Nhiều người dùng mỗi lần 1 hũ như một bữa phụ; nước yến không thay bữa chính hay thuốc.",
           "Uống lạnh ngon hơn; muốn uống ấm thì ngâm cả hũ vào nước ấm vài phút, không đun sôi.",
           "Nước yến hũ thường có đường: người tiểu đường, ăn kiêng nên đọc nhãn và hỏi bác sĩ.",
           f"Giá tham khảo: {P[126][2]} {gia(126)}/hũ, {P[127][2]} {gia(127)}/hũ, {P[124][2]} {gia(124)}/hũ."],
  body=f"""  <h2>Nước yến uống lúc nào trong ngày?</h2>
  <p>Nước yến hũ uống được vào bất cứ lúc nào trong ngày; thời điểm phổ biến nhất là giữa buổi sáng hoặc giữa buổi chiều, thay cho món ăn vặt. Vì là thực phẩm chưng sẵn, nước yến không có "giờ uống" bắt buộc như thuốc, nên hãy chọn lúc hợp nếp sinh hoạt của bạn.</p>
  <p>Ở xưởng Việt Cường Nhân, khách mua nước yến hay hỏi "uống sáng hay tối mới tốt". Câu trả lời ngắn: lúc nào bụng không quá no và bạn thấy tiện là được; quan trọng hơn là chọn loại hũ phù hợp và không uống thay bữa chính.</p>
  <table><thead><tr><th>Thời điểm</th><th>Hợp với</th><th>Lưu ý</th></tr></thead><tbody>
  <tr><td>Sáng, trước bữa sáng khoảng 30 phút</td><td>Người dậy sớm, muốn món nhẹ đầu ngày</td><td>Không uống thay bữa sáng</td></tr>
  <tr><td>Giữa buổi sáng (9–10 giờ)</td><td>Dân văn phòng, học sinh lớn</td><td>Thay món ăn vặt, mang theo tiện</td></tr>
  <tr><td>Giữa buổi chiều (15–16 giờ)</td><td>Người làm việc cả ngày</td><td>Cách bữa tối ít nhất 1 tiếng</td></tr>
  <tr><td>Buổi tối, trước khi ngủ khoảng 1 tiếng</td><td>Người bận ban ngày</td><td>Chọn hũ nhỏ, không uống quá khuya</td></tr>
  </tbody></table>

  <h2>Uống nước yến trước hay sau bữa ăn?</h2>
  <p>Nên uống nước yến khi bụng không quá no: trước bữa chính khoảng 30 phút hoặc sau bữa ăn khoảng 1 tiếng. Uống ngay sau bữa no dễ thấy đầy bụng và ngán.</p>
  <p>Thời điểm ăn yến chưng tại nhà cũng theo nguyên tắc tương tự, xem bài <a href="an-yen-luc-nao-tot-nhat.html">ăn yến lúc nào trong ngày là hợp lý</a>.</p>

  <h2>Uống nước yến buổi tối được không?</h2>
  <p>Uống nước yến buổi tối được, miễn là trước khi ngủ khoảng 1 tiếng và chọn hũ nhỏ. Nước yến hũ thường có đường, nên uống quá khuya ngay trước khi nằm không phải thói quen tốt, nhất là với người đang kiểm soát đường.</p>

  <h2>Mỗi ngày uống mấy hũ nước yến?</h2>
  <p>Nhiều người dùng mỗi lần 1 hũ như một bữa phụ, vài lần trong tuần hoặc mỗi ngày tùy thói quen. Nước yến là thực phẩm, không có "liều" cố định; điều cần để ý là tổng lượng đường trong ngày và không dùng nước yến thay các bữa ăn đủ chất.</p>
  <ul>
    <li><b>Người lớn khỏe mạnh:</b> dùng 1 hũ mỗi lần như món ăn phụ, đọc thành phần đường trên nhãn.</li>
    <li><b>Người tiểu đường, đang ăn kiêng đường:</b> hỏi bác sĩ trước; có thể tự chưng yến không đường tại nhà để chủ động hơn.</li>
    <li><b>Trẻ nhỏ, phụ nữ mang thai, người có bệnh nền hoặc đang dùng thuốc:</b> hỏi bác sĩ trước khi dùng. Xem thêm bài <a href="ba-bau-an-yen-duoc-khong.html">bà bầu ăn yến được không</a> và <a href="tre-may-tuoi-an-duoc-yen.html">trẻ mấy tuổi ăn được yến</a>.</li>
    <li><b>Người lớn tuổi:</b> chọn hũ nhỏ, uống mát hoặc ấm nhẹ; xem bài <a href="nguoi-gia-an-yen-the-nao.html">người già ăn yến thế nào cho hợp</a>.</li>
  </ul>

  <h2>Nước yến uống lạnh hay nóng?</h2>
  <p>Nước yến hũ ngon nhất khi uống mát, sau khi để ngăn mát tủ lạnh vài tiếng. Muốn uống ấm, ngâm nguyên hũ còn đậy nắp vào tô nước ấm vài phút; không đun sôi hay cho vào lò vi sóng nguyên hũ.</p>
  <ol>
    <li>Lắc nhẹ hũ trước khi mở để sợi yến và nước hòa đều.</li>
    <li>Mở nắp, uống trực tiếp hoặc đổ ra chén, dùng muỗng ăn phần sợi yến.</li>
    <li>Có thể thêm vài viên đá hoặc vài quả táo đỏ ngâm mềm nếu thích.</li>
  </ol>

  <h2>Chọn loại nước yến hũ nào?</h2>
  <p>Việt Cường Nhân có hai dòng nước yến: nước yến chưng thủ công từ yến tươi theo từng mẻ, và nước yến VCN Nest sản xuất trên dây chuyền tại nhà máy, đóng hũ tiệt trùng, ghi rõ lượng tổ yến thô mỗi hũ. Giá dưới đây lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(126, "Hũ nhỏ, giá mềm, hợp dùng hằng ngày."), li(127, "Lượng yến nhiều hơn loại 0.3gr."), li(129, "Lốc 6 hũ, tiện để sẵn trong tủ lạnh."), li(124, "Chưng thủ công từ yến tươi.")) + f"""
  <table><thead><tr><th>Nhu cầu</th><th>Gợi ý</th></tr></thead><tbody>
  <tr><td>Uống hằng ngày, mang đi làm</td><td>{P[126][2]}</td></tr>
  <tr><td>Muốn nhiều yến hơn trong mỗi hũ</td><td>{P[127][2]}</td></tr>
  <tr><td>Thích yến chưng kiểu nhà làm</td><td>{P[124][2]}</td></tr>
  <tr><td>Để sẵn cho cả nhà</td><td>Lốc 6 hoặc lốc 10 hũ</td></tr>
  </tbody></table>

  <h2>Bảo quản nước yến hũ</h2>
  <p>Hũ chưa mở để nơi khô mát, tránh nắng, theo hạn dùng in trên hũ; đã mở nắp thì nên uống hết trong ngày. Bỏ hũ nếu nắp phồng, hũ hở, có mùi vị lạ hoặc quá hạn. Chi tiết xem bài <a href="nuoc-yen-chung-san-cach-dung-bao-quan.html">nước yến chưng sẵn: chọn loại nào, dùng và bảo quản ra sao</a> và <a href="bao-quan-yen-sao.html">cách bảo quản yến sào khô và yến đã chưng</a>.</p>
  <p>Việt Cường Nhân làm yến từ năm 2009, xây nhà máy nước yến chưng sẵn năm 2022 và đạt chứng nhận HACCP, ISO 22000:2018, GMP. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Nước yến uống lúc nào tốt nhất?", "Lúc nào trong ngày cũng được; tiện nhất là giữa buổi sáng hoặc giữa buổi chiều, cách bữa chính khoảng 1 tiếng, khi bụng không quá no."),
       ("Mỗi ngày uống mấy hũ nước yến?", "Nhiều người dùng mỗi lần 1 hũ như một bữa phụ. Nước yến là thực phẩm, không có liều cố định; nên để ý lượng đường và không uống thay bữa chính."),
       ("Uống nước yến buổi tối có được không?", "Được, nên uống trước khi ngủ khoảng 1 tiếng và chọn hũ nhỏ, không uống quá khuya."),
       ("Nước yến uống lạnh hay nóng?", "Uống mát ngon hơn. Muốn uống ấm thì ngâm nguyên hũ còn đậy nắp vào nước ấm vài phút, không đun sôi."),
       ("Người tiểu đường uống nước yến được không?", "Nên hỏi bác sĩ trước và đọc thành phần đường trên nhãn. Có thể tự chưng yến không đường tại nhà để chủ động lượng đường.")]),
dict(slug="nuoc-yen-hu-va-yen-to-chung", cat="Nước yến", ngay="2026-11-02",
  tu_khoa="nước yến hũ hay yến tổ, nên mua nước yến hay yến tổ, so sánh nước yến hũ và yến tự chưng, yến chưng sẵn hay yến khô",
  h1="Nước yến hũ hay yến tổ tự chưng: chọn cái nào?",
  desc="Nước yến hũ hay yến tổ tự chưng tốt hơn cho bạn? So sánh lượng yến, công chuẩn bị, chi phí mỗi lần dùng, đường, bảo quản và gợi ý chọn theo từng nhu cầu.",
  lede="Nước yến hũ hay yến tổ tự chưng không có lựa chọn nào hơn hẳn: nước yến hũ tiện, mở nắp là dùng; yến tổ tự chưng cho lượng yến mỗi chén nhiều hơn và bạn chủ động được lượng đường, nhưng mất công ngâm và chưng. Người bận rộn hợp nước yến hũ, gia đình có thời gian hợp yến tổ.",
  tom_tat=["Nước yến hũ: mở nắp là dùng, tiện mang đi, hợp người bận rộn và làm quà.",
           "Yến tổ tự chưng: mỗi chén thường dùng 3–5 g yến khô, nhiều yến hơn hũ VCN Nest ghi 0.3–0.8 g tổ yến thô mỗi hũ.",
           f"Chi phí tham khảo: {P[126][2]} {gia(126)}/hũ; chén tự chưng 4 g {P[109][2]} khoảng {vnd(int(round(P[109][4]*4/100, -3)))} tiền yến.",
           "Tự chưng chủ động được đường; nước yến hũ cần đọc thành phần đường trên nhãn.",
           "Nhiều gia đình kết hợp: chưng yến tổ cuối tuần, ngày bận dùng nước yến hũ."],
  body=f"""  <h2>Nước yến hũ hay yến tổ: khác nhau ở đâu?</h2>
  <p>Nước yến hũ và yến tổ tự chưng khác nhau chủ yếu ở sự tiện lợi, lượng yến trong mỗi lần dùng, chi phí và khả năng tự điều chỉnh đường. Cả hai đều là thực phẩm từ tổ yến, chọn loại nào tùy thời gian và nhu cầu của gia đình bạn.</p>
  <p>Ở xưởng Việt Cường Nhân, chúng tôi làm cả hai: yến tinh chế nhặt lông tại xưởng và nước yến chưng sẵn từ nhà máy xây năm 2022. Câu khách hay hỏi nhất là "mua hũ cho tiện hay mua yến về chưng", và bảng dưới là cách chúng tôi thường giải thích.</p>
  <table><thead><tr><th>Tiêu chí</th><th>Nước yến hũ</th><th>Yến tổ tự chưng</th></tr></thead><tbody>
  <tr><td>Chuẩn bị</td><td>Mở nắp là dùng</td><td>Ngâm 30–60 phút, chưng cách thủy 20–30 phút</td></tr>
  <tr><td>Lượng yến mỗi lần</td><td>Theo nhãn: VCN Nest 0.3 g hoặc 0.8 g tổ yến thô mỗi hũ; hũ thủ công 12 g hoặc 36 g yến tươi</td><td>Thường 3–5 g yến khô mỗi chén</td></tr>
  <tr><td>Đường</td><td>Theo công thức nhà sản xuất, xem nhãn</td><td>Tự quyết định, có thể không đường</td></tr>
  <tr><td>Chi phí mỗi lần</td><td>Từ {gia(126)}/hũ</td><td>Khoảng {vnd(int(round(P[109][4]*4/100, -3)))} tiền yến cho chén 4 g (yến tinh chế 1 lớp sợi vừa)</td></tr>
  <tr><td>Bảo quản</td><td>Hũ chưa mở để nơi khô mát theo hạn dùng; mở rồi dùng trong ngày</td><td>Yến khô để hộp kín lâu dài; yến đã chưng để ngăn mát, dùng trong vài ngày</td></tr>
  <tr><td>Mang đi</td><td>Rất tiện</td><td>Cần hũ đựng và giữ lạnh</td></tr>
  <tr><td>Biếu tặng</td><td>Lốc hũ có hộp, gọn đẹp</td><td>Hộp yến rút lông, yến tinh chế</td></tr>
  </tbody></table>

  <h2>Khi nào nên chọn nước yến hũ?</h2>
  <p>Nên chọn nước yến hũ khi bạn không có thời gian ngâm, chưng, cần mang theo đi làm, đi học, đi xa hoặc cần một món quà gọn đẹp. Nước yến hũ cũng hợp với người mới thử yến, chưa muốn mua cả hộp yến khô.</p>
  <ul>
    <li>Người đi làm, ăn trưa ở văn phòng.</li>
    <li>Ông bà ở một mình, ngại bếp núc.</li>
    <li>Biếu tặng, thăm hỏi, cần quà mở ra dùng được ngay.</li>
    <li>Dự trữ vài hũ trong tủ lạnh cho ngày bận.</li>
  </ul>
""" + ul(li(126, "Hũ nhỏ, giá mềm, dùng hằng ngày."), li(127, "Nhiều yến hơn loại 0.3gr."), li(124, "Chưng thủ công từ yến tươi.")) + f"""
  <p>Cách uống và thời điểm hợp lý xem bài <a href="nuoc-yen-hu-uong-luc-nao.html">nước yến uống lúc nào, mỗi ngày mấy hũ là vừa</a>.</p>

  <h2>Khi nào nên chọn yến tổ tự chưng?</h2>
  <p>Nên chọn yến tổ tự chưng khi gia đình có thời gian, muốn mỗi chén có nhiều sợi yến, muốn tự kiểm soát lượng đường hoặc muốn biến tấu với hạt sen, táo đỏ, đông trùng hạ thảo. Tính theo lượng yến, tự chưng thường tiết kiệm hơn.</p>
  <ul>
    <li>Gia đình nhiều người cùng ăn yến hằng tuần.</li>
    <li>Người cần ăn ít hoặc không đường, theo lời dặn của bác sĩ.</li>
    <li>Người thích chén yến đặc sợi, dai.</li>
    <li>Người muốn nấu cháo yến, súp yến cho cả nhà.</li>
  </ul>
""" + ul(li(109, "Đã nhặt sạch lông, ngâm xong là chưng."), li(107, "Nở nhanh, hợp nấu cháo, súp.")) + f"""
  <p>Các bước chưng xem bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>; một hộp chưng được bao nhiêu chén xem bài <a href="100gr-yen-chung-duoc-bao-nhieu-chen.html">100gr yến chưng được bao nhiêu chén</a>.</p>

  <h2>So sánh chi phí: nước yến hũ và yến tự chưng</h2>
  <p>Tính theo mỗi lần dùng, một hũ VCN Nest nhỏ có giá thấp hơn một chén yến tự chưng 4 g; nhưng tính theo lượng yến, yến tự chưng cho nhiều yến hơn trên cùng số tiền. Bảng dưới tính từ bảng giá website Việt Cường Nhân, chưa gồm đường phèn, nguyên liệu chưng kèm và phí giao hàng.</p>
  <table><thead><tr><th>Lựa chọn</th><th>Lượng yến ghi nhận</th><th>Giá mỗi lần dùng</th></tr></thead><tbody>
  <tr><td>{P[126][2]}</td><td>0.3 g tổ yến thô/hũ</td><td>{gia(126)}</td></tr>
  <tr><td>{P[127][2]}</td><td>0.8 g tổ yến thô/hũ</td><td>{gia(127)}</td></tr>
  <tr><td>{P[124][2]}</td><td>12 g yến tươi/hũ 70ml</td><td>{gia(124)}</td></tr>
  <tr><td>Chén tự chưng, {P[107][2]}</td><td>4 g yến khô/chén</td><td>khoảng {vnd(int(round(P[107][4]*4/100, -3)))}</td></tr>
  <tr><td>Chén tự chưng, {P[109][2]}</td><td>4 g yến khô/chén</td><td>khoảng {vnd(int(round(P[109][4]*4/100, -3)))}</td></tr>
  </tbody></table>
  <p>Lưu ý: "yến tươi" (đã ngâm nở) và "yến khô" là hai cách tính khác nhau, nên không so trực tiếp số gam của hũ chưng thủ công với chén tự chưng. Bảng giá đầy đủ xem bài <a href="gia-yen-sao-bao-nhieu-tien.html">giá yến sào bao nhiêu tiền 100gr</a>.</p>

  <h2>Kết hợp cả hai cho tiện</h2>
  <p>Nhiều gia đình kết hợp: cuối tuần chưng một mẻ yến tổ đủ ăn 2–3 ngày, những ngày bận thì dùng nước yến hũ để trong tủ lạnh. Cách này vừa giữ được thói quen dùng yến đều, vừa không phải chưng mỗi ngày.</p>
  <ol>
    <li>Chủ nhật: ngâm và chưng yến tổ cho 2–3 ngày đầu tuần, cất ngăn mát.</li>
    <li>Giữa tuần: dùng nước yến hũ mang đi làm.</li>
    <li>Chia yến khô thành phần 4 g ngay khi mở hộp để lần chưng sau nhanh hơn.</li>
  </ol>

  <h2>Lưu ý chung khi dùng yến</h2>
  <ul>
    <li>Yến là thực phẩm, không thay bữa chính hay thuốc.</li>
    <li>Trẻ nhỏ, phụ nữ mang thai, người có bệnh nền hoặc đang dùng thuốc nên hỏi bác sĩ trước khi dùng.</li>
    <li>Người tiểu đường nên đọc thành phần đường của nước yến hũ hoặc tự chưng yến không đường.</li>
    <li>Bảo quản đúng cách: xem bài <a href="bao-quan-yen-sao.html">cách bảo quản yến sào khô và yến đã chưng</a>.</li>
  </ul>
  <p>Việt Cường Nhân làm yến từ năm 2009, đạt HACCP, ISO 22000:2018 và GMP. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>, giá chưa gồm phí giao hàng. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Nên mua nước yến hũ hay yến tổ?", "Bận rộn, cần mang đi hoặc làm quà thì chọn nước yến hũ. Có thời gian, muốn nhiều sợi yến và tự kiểm soát đường thì chọn yến tổ tự chưng."),
       ("Nước yến hũ có nhiều yến bằng yến tự chưng không?", "Thường ít hơn. Hũ VCN Nest ghi 0.3 g hoặc 0.8 g tổ yến thô mỗi hũ, còn một chén tự chưng thường dùng 3–5 g yến khô."),
       ("Yến tự chưng có rẻ hơn nước yến hũ không?", "Tính theo lượng yến thì tự chưng thường tiết kiệm hơn. Tính theo mỗi lần dùng, hũ VCN Nest nhỏ có giá thấp hơn một chén tự chưng 4 g."),
       ("Người tiểu đường nên chọn nước yến hũ hay tự chưng?", "Nên hỏi bác sĩ trước. Tự chưng giúp chủ động không dùng đường; với nước yến hũ cần đọc kỹ thành phần đường trên nhãn."),
       ("Mua yến biếu nên chọn loại nào?", "Lốc nước yến có hộp gọn, mở ra dùng ngay; hộp yến rút lông hoặc yến tinh chế hợp khi người nhận quen tự chưng.")]),
dict(slug="qua-tet-yen-sao", cat="Quà tặng", ngay="2026-11-03",
  tu_khoa="quà Tết yến sào, hộp quà Tết yến sào, giỏ quà Tết yến sào, quà biếu Tết yến sào theo ngân sách, quà Tết 2027",
  h1="Quà Tết yến sào: chọn hộp quà biếu theo ngân sách",
  desc="Chọn quà Tết yến sào theo ngân sách: dưới 500 nghìn, 500 nghìn – 1 triệu, 1–2 triệu và trên 2 triệu. Bảng giá giỏ, hộp quà Tết 2027 Việt Cường Nhân, cách đặt.",
  lede=f"Chọn quà Tết yến sào dễ nhất là chọn theo ngân sách trước, rồi theo người nhận: dưới 500 nghìn có túi, hộp yến hũ; từ 500 nghìn đến 2 triệu có nhiều hộp, giỏ, khay quà; trên 2 triệu là giỏ, khay quà cao cấp. Bộ quà Tết 2027 của Việt Cường Nhân có giá từ {gia(358)} đến {gia(301)}, giá bán lẻ đã gồm VAT.",
  tom_tat=["Chọn theo ngân sách trước: dưới 500 nghìn, 500 nghìn – 1 triệu, 1–2 triệu, trên 2 triệu.",
           f"Bộ quà Tết 2027 của Việt Cường Nhân có giá từ {gia(358)} ({P[358][2]}) đến {gia(301)} ({P[301][2]}).",
           "Người nhận quen tự chưng yến: chọn hộp có yến khô; người bận rộn, người lớn tuổi ở xa: chọn quà yến hũ chưng sẵn.",
           f"Muốn tự phối quà: lốc yến hũ có hộp như {P[135][2]} {gia(135)}, hoặc 100gr {P[114][2]} {gia(114)}.",
           "Đặt sớm trước Tết để có hàng và giao kịp; đặt số lượng lớn cho công ty nhắn Zalo 0978 094 739."],
  body=f"""  <h2>Quà Tết yến sào nên chọn thế nào?</h2>
  <p>Quà Tết yến sào nên chọn theo ba câu hỏi: ngân sách bao nhiêu, người nhận là ai, và họ có quen tự chưng yến hay không. Trả lời xong ba câu này thì danh sách quà thu hẹp chỉ còn vài lựa chọn.</p>
  <p>Ở Việt Cường Nhân, mùa Tết khách hay hỏi "khoảng một triệu thì biếu gì cho đẹp". Bộ quà Tết 2027 của chúng tôi được chia sẵn theo dạng túi, hộp, giỏ, khay và hộp gỗ; giá bán lẻ trên website đã gồm VAT, chưa gồm phí giao hàng.</p>
  <table><thead><tr><th>Người nhận</th><th>Gợi ý dạng quà</th></tr></thead><tbody>
  <tr><td>Ông bà, cha mẹ</td><td>Hộp, giỏ có yến hũ chưng sẵn, dễ dùng</td></tr>
  <tr><td>Họ hàng, bạn bè thân</td><td>Túi hoặc hộp quà tầm trung</td></tr>
  <tr><td>Đối tác, sếp, khách hàng</td><td>Hộp gỗ, giỏ hoặc khay quà cao cấp</td></tr>
  <tr><td>Người quen tự chưng yến</td><td>Hộp yến khô (yến tinh chế, yến rút lông)</td></tr>
  <tr><td>Nhân viên, quà số lượng nhiều</td><td>Túi, hộp yến hũ giá vừa phải, đồng bộ</td></tr>
  </tbody></table>

  <h2>Quà Tết yến sào dưới 500 nghìn</h2>
  <p>Dưới 500 nghìn có các túi, hộp và giỏ yến hũ gọn nhẹ, hợp biếu họ hàng, bạn bè hoặc làm quà cho nhân viên. Giá lấy từ bảng giá website Việt Cường Nhân:</p>
""" + ul(li(358), li(359), li(357), li(348), li(349)) + f"""

  <h2>Quà Tết yến sào từ 500 nghìn đến 1 triệu</h2>
  <p>Tầm giá 500 nghìn đến 1 triệu có nhiều lựa chọn nhất, hợp biếu cha mẹ, thầy cô, người thân. Một số hộp, túi, giỏ tiêu biểu:</p>
""" + ul(li(347), li(340), li(335), li(325), li(323)) + f"""

  <h2>Quà Tết yến sào từ 1 đến 2 triệu</h2>
  <p>Từ 1 đến 2 triệu là tầm giá thường được chọn để biếu đối tác, cấp trên hoặc người lớn tuổi trong gia đình, với dạng hộp gỗ, giỏ và khay quà trang trọng hơn.</p>
""" + ul(li(320), li(318), li(316), li(312), li(309), li(306)) + f"""

  <h2>Quà Tết yến sào cao cấp trên 2 triệu</h2>
  <p>Trên 2 triệu là các giỏ, khay và hộp quà cao cấp nhất trong bộ quà Tết 2027, hợp biếu đối tác quan trọng.</p>
""" + ul(li(305), li(304), li(301)) + f"""
  <p>Ảnh từng giỏ, hộp có trong <a href="../#san-pham">bảng giá sản phẩm</a>; cần hỏi rõ trong hộp có gì, nhắn Zalo 0978 094 739.</p>

  <h2>Tự phối quà Tết từ yến khô và yến hũ</h2>
  <p>Nếu muốn quà theo ý mình, có thể chọn yến khô hoặc lốc yến hũ có hộp. Cách này hợp khi bạn biết rõ người nhận thích tự chưng hay thích loại chưng sẵn.</p>
  <table><thead><tr><th>Sản phẩm</th><th>Quy cách</th><th>Giá</th><th>Hợp với</th></tr></thead><tbody>
  <tr><td>{P[133][2]}</td><td>{P[133][3]}</td><td>{gia(133)}</td><td>Quà gọn, người bận rộn</td></tr>
  <tr><td>{P[135][2]}</td><td>{P[135][3]}</td><td>{gia(135)}</td><td>Gia đình đông người</td></tr>
  <tr><td>{P[110][2]}</td><td>{P[110][3]}</td><td>{gia(110)}</td><td>Người quen tự chưng yến</td></tr>
  <tr><td>{P[114][2]}</td><td>{P[114][3]}</td><td>{gia(114)}</td><td>Biếu trang trọng, tổ nguyên dáng</td></tr>
  </tbody></table>
  <p>Khác nhau giữa yến tinh chế và yến rút lông xem bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>. Nên biếu yến hũ hay yến khô, xem bài <a href="nuoc-yen-hu-va-yen-to-chung.html">nước yến hũ hay yến tổ tự chưng: chọn cái nào</a>.</p>

  <h2>Kinh nghiệm chọn quà Tết yến sào</h2>
  <ol>
    <li><b>Xem hạn dùng:</b> quà biếu thường được để dành qua Tết, nên chọn sản phẩm còn hạn dài và dặn người nhận cất nơi khô mát.</li>
    <li><b>Xem nguồn gốc:</b> chọn nơi bán có địa chỉ sản xuất, chứng nhận an toàn thực phẩm; xem bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật</a>.</li>
    <li><b>Hợp người nhận:</b> người lớn tuổi ở xa hợp yến hũ chưng sẵn; người có bệnh nền hoặc đang mang thai nên được khuyên hỏi bác sĩ trước khi dùng.</li>
    <li><b>Đặt sớm:</b> dịp sát Tết lượng đơn tăng và thời gian giao có thể kéo dài theo <a href="../chinh-sach/van-chuyen.html">chính sách vận chuyển</a>.</li>
    <li><b>Kiểm tra khi nhận:</b> xem kiện hàng, số lượng, niêm phong trước khi thanh toán.</li>
  </ol>
  <p>Cách bảo quản yến sau khi nhận quà xem bài <a href="bao-quan-yen-sao.html">cách bảo quản yến sào khô và yến đã chưng</a>.</p>

  <h2>Cách đặt quà Tết yến sào tại Việt Cường Nhân</h2>
  <p>Đặt quà Tết qua <a href="../#san-pham">bảng giá sản phẩm</a> trên website hoặc nhắn Zalo 0978 094 739; nhân viên sẽ gọi xác nhận đơn và báo phí giao hàng trước khi giao. Muốn xem quà tận nơi, gọi hoặc nhắn Zalo hẹn trước rồi ghé xưởng ở Dĩ An, xem địa chỉ trong bài <a href="yen-sao-binh-duong-di-an-mua-o-dau.html">mua yến sào ở Dĩ An, Bình Dương cũ</a>.</p>
  <p>Việt Cường Nhân làm yến từ năm 2009, có nhà yến, xưởng nhặt lông và nhà máy nước yến, đạt HACCP, ISO 22000:2018 và GMP. Công ty, cơ quan cần đặt quà Tết số lượng lớn hoặc mua sỉ: nhắn Zalo 0978 094 739 để được tư vấn.</p>""",
  faq=[("Quà Tết yến sào giá bao nhiêu?", f"Bộ quà Tết 2027 của Việt Cường Nhân có giá từ {gia(358)} đến {gia(301)}, giá bán lẻ đã gồm VAT, chưa gồm phí giao hàng."),
       ("Biếu Tết 1 triệu nên chọn quà yến sào nào?", f"Tầm 1 triệu có các hộp, giỏ như {P[320][2]} ({gia(320)}) hoặc {P[323][2]} ({gia(323)}). Xem thêm trong bảng giá để chọn theo người nhận."),
       ("Nên biếu yến hũ hay yến khô dịp Tết?", "Người nhận bận rộn hoặc lớn tuổi ở xa hợp yến hũ chưng sẵn; người quen tự chưng yến hợp yến khô như yến tinh chế, yến rút lông."),
       ("Đặt quà Tết yến sào số lượng lớn cho công ty thế nào?", "Nhắn Zalo 0978 094 739 để Việt Cường Nhân tư vấn mẫu quà, số lượng và thời gian giao."),
       ("Trong hộp quà Tết có những gì?", "Mỗi hộp, giỏ có ảnh trong bảng giá trên website. Để biết chính xác thành phần, nhắn Zalo 0978 094 739.")]),
dict(slug="qua-tang-doanh-nghiep-yen-sao", cat="Quà tặng", ngay="2026-11-03",
  tu_khoa="quà tặng doanh nghiệp yến sào, đặt quà tặng doanh nghiệp, quà tặng đối tác yến sào, quà tặng nhân viên yến sào, quà Tết doanh nghiệp",
  h1="Quà tặng doanh nghiệp yến sào: quy trình đặt và lưu ý",
  desc="Quà tặng doanh nghiệp yến sào: chọn mẫu theo đối tượng và ngân sách, quy trình 6 bước đặt số lượng lớn, nên đặt trước bao lâu và cần kiểm tra gì khi nhận.",
  lede="Đặt quà tặng doanh nghiệp yến sào nên làm theo thứ tự: xác định đối tượng nhận và ngân sách mỗi phần quà, chọn mẫu, chốt số lượng và lịch giao, rồi kiểm tra hàng khi nhận. Với Việt Cường Nhân, doanh nghiệp nhắn Zalo 0978 094 739 để được tư vấn mẫu quà, số lượng và báo giá theo đơn.",
  tom_tat=["Quy trình 6 bước: xác định đối tượng và ngân sách, chọn mẫu, xem hàng mẫu, chốt đơn, giao hàng, kiểm tra khi nhận.",
           "Quà nhân viên thường chọn yến hũ gọn, đồng bộ; quà đối tác chọn hộp gỗ, giỏ, khay hoặc yến khô cao cấp.",
           f"Ví dụ giá lẻ: {P[131][2]} ({P[131][3]}) {gia(131)}, {P[135][2]} ({P[135][3]}) {gia(135)}, {P[110][2]} {gia(110)}/100gr.",
           "Đơn số lượng lớn nên đặt sớm, nhất là mùa Tết, để có đủ hàng và thời gian giao.",
           "Báo giá cho đơn doanh nghiệp, mua sỉ: nhắn Zalo 0978 094 739."],
  body=f"""  <h2>Vì sao doanh nghiệp chọn yến sào làm quà tặng?</h2>
  <p>Yến sào là món quà phổ biến trong các dịp Tết, tri ân khách hàng, kỷ niệm thành lập hay chúc mừng đối tác, vì đây là thực phẩm quen thuộc với người Việt, dùng được cho cả gia đình người nhận và có nhiều mức giá để chọn. Với doanh nghiệp, yến còn dễ đồng bộ: cùng một mẫu quà có thể tặng hàng chục, hàng trăm người.</p>
  <p>Việt Cường Nhân làm yến từ năm 2009, có nhà yến, xưởng nhặt lông và nhà máy nước yến tại Dĩ An, đạt HACCP, ISO 22000:2018 và GMP. Với khách doanh nghiệp, chúng tôi thường tư vấn trực tiếp qua Zalo để chọn mẫu phù hợp với ngân sách và số lượng.</p>

  <h2>Chọn quà tặng doanh nghiệp yến sào theo đối tượng</h2>
  <p>Cách chọn nhanh nhất là chia người nhận thành nhóm, mỗi nhóm một mẫu quà và một mức ngân sách. Bảng dưới là gợi ý dạng quà theo từng nhóm.</p>
  <table><thead><tr><th>Đối tượng nhận</th><th>Gợi ý dạng quà</th><th>Lý do</th></tr></thead><tbody>
  <tr><td>Nhân viên</td><td>Lốc yến hũ, túi hoặc hộp quà giá vừa</td><td>Gọn, đồng bộ, dễ phát tận tay</td></tr>
  <tr><td>Khách hàng thân thiết</td><td>Lốc yến hũ có hộp, hộp quà tầm trung</td><td>Mở ra dùng ngay, hình thức đẹp</td></tr>
  <tr><td>Đối tác, lãnh đạo</td><td>Hộp gỗ, giỏ, khay quà; yến tinh chế, yến rút lông</td><td>Trang trọng, giá trị cao</td></tr>
  <tr><td>Người nhận quen tự chưng yến</td><td>Hộp yến khô 100gr</td><td>Chủ động cách chưng, dùng dần</td></tr>
  </tbody></table>

  <h2>Một số mẫu quà tham khảo</h2>
  <p>Giá dưới đây là giá lẻ lấy từ bảng giá website Việt Cường Nhân, chưa gồm phí giao hàng; đơn doanh nghiệp được báo giá riêng theo số lượng qua Zalo.</p>
  <h3>Yến hũ chưng sẵn</h3>
""" + ul(li(131, "Hợp quà nhân viên, khách hàng."), li(133, "Có hộp, gọn đẹp."), li(135, "Có hộp, hợp quà khách hàng, đối tác.")) + """
  <h3>Yến khô</h3>
""" + ul(li(110, "Tai yến đều, người nhận tự chưng."), li(114, "Tổ nguyên dáng, hợp quà trang trọng.")) + """
  <h3>Quà Tết dạng hộp, giỏ, khay</h3>
""" + ul(li(358), li(323), li(306), li(305)) + f"""
  <p>Danh sách quà Tết theo từng mức giá xem bài <a href="qua-tet-yen-sao.html">quà Tết yến sào: chọn hộp quà biếu theo ngân sách</a>. Nên tặng yến hũ hay yến khô, xem bài <a href="nuoc-yen-hu-va-yen-to-chung.html">nước yến hũ hay yến tổ tự chưng</a>.</p>

  <h2>Quy trình đặt quà tặng doanh nghiệp yến sào</h2>
  <p>Quy trình đặt quà doanh nghiệp tại Việt Cường Nhân gồm 6 bước, bắt đầu bằng việc nhắn Zalo 0978 094 739 với thông tin cơ bản về đơn hàng.</p>
  <ol>
    <li><b>Gửi thông tin:</b> dịp tặng, số lượng dự kiến, ngân sách mỗi phần quà, ngày cần nhận hàng, địa điểm giao.</li>
    <li><b>Nhận tư vấn mẫu:</b> nhân viên gợi ý mẫu quà phù hợp và báo giá theo số lượng.</li>
    <li><b>Xem hàng mẫu:</b> xem ảnh, hoặc hẹn trước để đến xưởng ở Dĩ An xem tận nơi.</li>
    <li><b>Chốt đơn:</b> thống nhất mẫu, số lượng, giá, thời gian và cách giao, các yêu cầu đi kèm.</li>
    <li><b>Giao hàng:</b> giao theo lịch đã thống nhất; phí giao tính theo khu vực, báo khi xác nhận đơn.</li>
    <li><b>Kiểm tra khi nhận:</b> kiểm tra số lượng, kiện hàng, niêm phong và hạn dùng trước khi ký nhận.</li>
  </ol>
  <p>Các yêu cầu riêng như hóa đơn, thiệp kèm quà hay đóng gói theo yêu cầu, doanh nghiệp vui lòng hỏi trực tiếp khi trao đổi đơn để được xác nhận có làm được hay không.</p>

  <h2>Nên đặt quà doanh nghiệp trước bao lâu?</h2>
  <p>Đơn quà số lượng lớn nên đặt càng sớm càng tốt, nhất là quà Tết, vì sát Tết lượng đơn tăng và thời gian giao có thể kéo dài. Đặt sớm giúp doanh nghiệp có thời gian xem mẫu, chốt danh sách người nhận và chủ động lịch phát quà.</p>
  <table><thead><tr><th>Việc cần làm</th><th>Gợi ý thời điểm</th></tr></thead><tbody>
  <tr><td>Chốt ngân sách và danh sách người nhận</td><td>Trước tiên, càng sớm càng tốt</td></tr>
  <tr><td>Nhắn Zalo, xem mẫu, nhận báo giá</td><td>Ngay sau khi có danh sách</td></tr>
  <tr><td>Chốt đơn</td><td>Đủ sớm trước ngày cần nhận để kịp chuẩn bị</td></tr>
  <tr><td>Nhận hàng</td><td>Vài ngày trước ngày phát quà để kịp kiểm tra</td></tr>
  </tbody></table>
  <p>Thời gian giao theo khu vực xem <a href="../chinh-sach/van-chuyen.html">chính sách vận chuyển</a>.</p>

  <h2>Lưu ý khi chọn quà tặng doanh nghiệp yến sào</h2>
  <ul>
    <li><b>Hạn dùng:</b> quà thường được người nhận để dành, nên chọn sản phẩm còn hạn dài.</li>
    <li><b>Nguồn gốc rõ ràng:</b> chọn đơn vị có địa chỉ sản xuất, chứng nhận an toàn thực phẩm; xem bài <a href="chung-nhan-haccp-iso-22000-gmp-la-gi.html">HACCP, ISO 22000 và GMP nghĩa là gì</a>.</li>
    <li><b>Đồng bộ trong từng nhóm:</b> người cùng cấp nên nhận cùng mẫu để tránh so sánh.</li>
    <li><b>Hướng dẫn kèm theo:</b> có thể kèm lời nhắn cách bảo quản; xem bài <a href="bao-quan-yen-sao.html">cách bảo quản yến sào</a>.</li>
    <li><b>Lời chúc đơn giản:</b> yến là thực phẩm, không nên viết công dụng như thuốc trên thiệp; người có bệnh nền nên hỏi bác sĩ trước khi dùng.</li>
  </ul>

  <h2>Thông tin liên hệ đặt quà doanh nghiệp</h2>
  <p>Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân, MST 3701518691. Nhà máy: 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp; cơ sở đóng gói: 261-263 Võ Thị Sáu, Phường Đông Hòa, TP. Hồ Chí Minh. Xem đường đến xưởng trong bài <a href="yen-sao-binh-duong-di-an-mua-o-dau.html">mua yến sào ở Dĩ An, Bình Dương cũ</a>.</p>
  <p>Đặt quà doanh nghiệp, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739 để được tư vấn và báo giá. Xem toàn bộ mẫu trong <a href="../#san-pham">bảng giá sản phẩm</a>.</p>""",
  faq=[("Đặt quà tặng doanh nghiệp yến sào ở đâu?", "Có thể đặt tại Việt Cường Nhân bằng cách nhắn Zalo 0978 094 739 với dịp tặng, số lượng, ngân sách và ngày cần nhận để được tư vấn mẫu và báo giá."),
       ("Quà tặng nhân viên bằng yến sào nên chọn loại nào?", f"Thường chọn lốc yến hũ hoặc túi, hộp quà giá vừa vì gọn và đồng bộ, ví dụ {P[131][2]} ({P[131][3]}) giá lẻ {gia(131)}."),
       ("Quà tặng đối tác bằng yến sào nên chọn gì?", "Hộp gỗ, giỏ, khay quà hoặc hộp yến khô cao cấp như yến tinh chế, yến rút lông, tùy ngân sách."),
       ("Đặt số lượng lớn có giá riêng không?", "Đơn doanh nghiệp và mua sỉ được báo giá riêng theo số lượng. Nhắn Zalo 0978 094 739 để nhận báo giá."),
       ("Nên đặt quà Tết doanh nghiệp trước bao lâu?", "Nên đặt càng sớm càng tốt, vì sát Tết lượng đơn tăng và thời gian giao có thể kéo dài. Nên nhận hàng vài ngày trước ngày phát quà để kịp kiểm tra.")]),
dict(slug="yen-nha-va-yen-dao", cat="Yến sào", ngay="2026-11-04",
  tu_khoa="yến nhà và yến đảo, yến nhà là gì, yến đảo là gì, yến đảo có tốt hơn yến nhà không, phân biệt yến nhà và yến đảo",
  h1="Yến nhà và yến đảo khác nhau thế nào?",
  desc="Yến nhà và yến đảo khác nhau thế nào? So sánh nơi làm tổ, cách khai thác, hình dạng tổ, độ sạch, sản lượng và giá, kèm cách chọn yến nhà có nguồn gốc rõ ràng.",
  lede="Yến nhà và yến đảo đều là tổ của chim yến, khác nhau chủ yếu ở nơi làm tổ: yến nhà làm tổ trong nhà yến do con người xây, còn yến đảo làm tổ trên vách hang đá ở các đảo ven biển. Vì vậy hai loại khác nhau về cách khai thác, hình dạng tổ, độ sạch, sản lượng và giá; phần lớn yến sào bán trên thị trường hiện nay là yến nhà.",
  tom_tat=["Yến nhà: tổ làm trong nhà yến do con người xây, khai thác chủ động, tổ tương đối đều, ít tạp chất hơn.",
           "Yến đảo: tổ làm trên vách hang đá ở đảo ven biển, khai thác khó và theo mùa, sản lượng ít nên giá cao hơn nhiều.",
           "Không có căn cứ rõ ràng để nói loại nào bổ hơn; khác biệt chính là nguồn gốc, hình dạng tổ, công sơ chế và giá.",
           "Yến đảo hiếm và dễ bị giả mạo tên gọi, nên cần mua nơi có nguồn gốc và giấy tờ rõ ràng.",
           f"Yến của Việt Cường Nhân là yến nhà, ví dụ {P[101][2]} {gia(101)}/100gr, {P[109][2]} {gia(109)}/100gr."],
  body=f"""  <h2>Yến nhà là gì?</h2>
  <p>Yến nhà là tổ yến do chim yến làm trong nhà yến, tức những ngôi nhà được con người xây và thiết kế riêng để dẫn dụ chim yến về làm tổ. Bên trong nhà yến có các xà gỗ để chim bám tổ, được giữ độ ẩm, nhiệt độ và độ tối phù hợp.</p>
  <p>Việt Cường Nhân có nhà yến tại Gò Công Tây (Tiền Giang cũ) và Bình Thuận, cùng các xưởng nhặt lông tại Lâm Đồng. Tổ yến từ nhà yến được thu hoạch, rồi đưa về xưởng làm sạch, nhặt lông và sấy khô thành yến tinh chế, yến rút lông.</p>

  <h2>Yến đảo là gì?</h2>
  <p>Yến đảo là tổ yến do chim yến làm tự nhiên trên vách các hang đá ở đảo và vùng ven biển. Việc khai thác yến đảo khó khăn vì hang đá cao, hiểm trở, thường chỉ làm vào một số thời điểm trong năm và phải tuân theo quy định quản lý của nơi khai thác.</p>
  <p>Vì sản lượng ít và khai thác vất vả, yến đảo có giá cao hơn yến nhà nhiều lần và không phổ biến trên thị trường bán lẻ.</p>

  <h2>So sánh yến nhà và yến đảo</h2>
  <p>Yến nhà và yến đảo khác nhau rõ nhất ở nơi làm tổ, cách khai thác, hình dạng tổ và giá. Bảng dưới tóm tắt các tiêu chí chính.</p>
  <table><thead><tr><th>Tiêu chí</th><th>Yến nhà</th><th>Yến đảo</th></tr></thead><tbody>
  <tr><td>Nơi làm tổ</td><td>Xà gỗ trong nhà yến do con người xây</td><td>Vách hang đá tự nhiên ở đảo, ven biển</td></tr>
  <tr><td>Khai thác</td><td>Chủ động, an toàn hơn</td><td>Khó, hiểm trở, theo mùa</td></tr>
  <tr><td>Hình dạng tổ</td><td>Tương đối đều, hình chén, chân tổ bám xà gỗ</td><td>Kém đều, chân tổ bám vào đá</td></tr>
  <tr><td>Tạp chất</td><td>Có lông, bụi, cần làm sạch</td><td>Thường lẫn nhiều tạp chất từ vách đá hơn</td></tr>
  <tr><td>Sản lượng</td><td>Chiếm phần lớn yến sào trên thị trường</td><td>Ít, hiếm</td></tr>
  <tr><td>Giá</td><td>Phổ biến, nhiều mức giá</td><td>Cao hơn nhiều lần</td></tr>
  <tr><td>Dễ kiểm tra nguồn gốc</td><td>Có thể hỏi nhà yến, xưởng sản xuất</td><td>Khó kiểm chứng nếu không mua đúng kênh</td></tr>
  </tbody></table>

  <h2>Yến đảo có tốt hơn yến nhà không?</h2>
  <p>Không có căn cứ rõ ràng để khẳng định yến đảo bổ hơn yến nhà. Cả hai đều là tổ yến; điểm khác lớn nhất là nơi làm tổ, sự hiếm có và giá, nên chọn loại nào chủ yếu tùy ngân sách và mục đích dùng.</p>
  <p>Với nhu cầu dùng hằng tuần trong gia đình, yến nhà đã làm sạch là lựa chọn phổ biến vì dễ mua, giá hợp lý và có thể hỏi rõ nhà yến, xưởng sơ chế. Yến đảo thường được chọn khi người mua muốn một món quà hiếm và chấp nhận giá cao.</p>

  <h2>Cẩn thận khi mua hàng gắn tên "yến đảo"</h2>
  <p>Vì yến đảo hiếm và đắt, trên thị trường có hàng được gọi là "yến đảo" nhưng không rõ nguồn gốc. Trước khi mua, nên kiểm tra những điểm sau:</p>
  <ul>
    <li>Người bán có cho biết rõ nơi khai thác và đơn vị cung cấp không.</li>
    <li>Sản phẩm có nhãn, bản tự công bố, thông tin cơ sở sản xuất không.</li>
    <li>Giá có hợp lý với độ hiếm của yến đảo không; yến đảo giá rẻ bất thường cần hỏi kỹ.</li>
    <li>Sợi yến khi ngâm có nở tơi, nước ngâm không đục, không có mùi lạ.</li>
  </ul>
  <p>Các dấu hiệu chung xem bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>.</p>

  <h2>Chọn yến nhà thế nào cho đúng nhu cầu?</h2>
  <p>Với yến nhà, điều quan trọng hơn chuyện "nhà hay đảo" là mức độ làm sạch và dạng sợi. Yến thô còn lông, giá mềm nhưng phải tự nhặt; yến tinh chế đã nhặt sạch lông, ngâm xong là chưng; yến rút lông giữ sợi dài, tổ đẹp, hợp biếu tặng.</p>
""" + ul(li(101, "Yến nhà, ít lông, tự làm sạch tại nhà."), li(109, "Yến nhà đã nhặt sạch lông, ngâm xong là chưng."), li(113, "Sợi dài, hợp biếu tặng.")) + """
  <p>So sánh chi tiết các nhóm yến xem bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>; cách làm sạch yến thô xem bài <a href="cach-lam-sach-yen-tho.html">cách làm sạch yến thô tại nhà: 5 bước</a>. Chọn theo ngân sách xem bài <a href="yen-sao-loai-nao-tot.html">yến sào loại nào tốt</a>.</p>

  <h2>Yến nhà của Việt Cường Nhân</h2>
  <p>Việt Cường Nhân làm yến từ năm 2009, có nhà yến riêng, xưởng nhặt lông và nhà máy đạt HACCP, ISO 22000:2018 và GMP, có bản tự công bố tổ yến thô và tổ yến tinh chế trên <a href="../chung-nhan/">trang chứng nhận</a>. Giá trên website chưa gồm phí giao hàng; đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Yến nhà và yến đảo khác nhau thế nào?", "Yến nhà làm tổ trong nhà yến do con người xây, còn yến đảo làm tổ trên vách hang đá ở đảo, ven biển. Hai loại khác nhau về cách khai thác, hình dạng tổ, sản lượng và giá."),
       ("Yến đảo có bổ hơn yến nhà không?", "Không có căn cứ rõ ràng để khẳng định yến đảo bổ hơn. Khác biệt chính là nguồn gốc, độ hiếm và giá."),
       ("Vì sao yến đảo đắt hơn yến nhà?", "Vì yến đảo khai thác khó, hiểm trở, theo mùa và sản lượng ít, trong khi yến nhà được khai thác chủ động từ nhà yến."),
       ("Yến bán trên thị trường chủ yếu là loại nào?", "Phần lớn yến sào bán lẻ hiện nay là yến nhà, vì sản lượng nhiều hơn và giá phổ biến hơn yến đảo."),
       ("Yến của Việt Cường Nhân là yến nhà hay yến đảo?", "Là yến nhà, từ nhà yến của Việt Cường Nhân tại Gò Công Tây (Tiền Giang cũ) và Bình Thuận, được làm sạch tại xưởng.")]),
dict(slug="yen-trang-yen-hong-huyet-yen", cat="Yến sào", ngay="2026-11-04",
  tu_khoa="huyết yến, yến trắng yến hồng huyết yến, huyết yến là gì, huyết yến có phải máu chim yến không, cách nhận biết huyết yến nhuộm màu",
  h1="Yến trắng, yến hồng, huyết yến khác nhau ra sao?",
  desc="Huyết yến là gì, có phải máu chim yến không? So sánh yến trắng, yến hồng và huyết yến về màu sắc, nguồn gốc màu, độ hiếm, giá và cách tránh hàng nhuộm màu.",
  lede="Huyết yến là tổ yến có màu đỏ cam, không phải do chim yến nhả máu như nhiều người vẫn nghĩ; màu của tổ yến chủ yếu chịu ảnh hưởng của môi trường nơi tổ được làm. Yến trắng là loại phổ biến nhất, còn yến hồng và huyết yến hiếm hơn nên giá cao hơn, và cũng là nhóm dễ bị làm giả bằng cách nhuộm màu.",
  tom_tat=["Yến trắng (trắng ngà) phổ biến nhất; yến hồng có màu hồng cam nhạt; huyết yến có màu đỏ cam đậm hơn.",
           "Huyết yến không phải máu chim yến; màu tổ chủ yếu do môi trường nơi làm tổ, như vách đá, độ ẩm và khoáng chất.",
           "Không có căn cứ rõ ràng để nói yến màu bổ hơn yến trắng; khác biệt chính là màu sắc, độ hiếm và giá.",
           "Yến màu dễ bị nhuộm: nước ngâm ra màu đỏ, màu loang không đều hoặc giá rẻ bất thường là dấu hiệu cần hỏi kỹ.",
           f"Việt Cường Nhân bán yến trắng, ví dụ {P[109][2]} {gia(109)}/100gr và {P[112][2]} {gia(112)}/100gr."],
  body=f"""  <h2>Huyết yến là gì?</h2>
  <p>Huyết yến là tên gọi tổ yến có màu đỏ cam đến đỏ đậm. Dù tên có chữ "huyết", đây không phải tổ yến có máu của chim yến: chim yến làm tổ bằng nước dãi, và màu của tổ chủ yếu chịu ảnh hưởng từ môi trường nơi tổ được làm và thời gian tổ ở đó.</p>
  <p>Ở xưởng Việt Cường Nhân, khách hay hỏi "huyết yến có phải chim yến kiệt sức nhả ra máu không". Đó là cách hiểu phổ biến nhưng không đúng. Tổ yến màu đỏ hiếm gặp, nên được gọi tên riêng và có giá cao.</p>

  <h2>Yến trắng, yến hồng và huyết yến khác nhau thế nào?</h2>
  <p>Ba loại khác nhau chủ yếu ở màu sắc, độ hiếm và giá; cả ba đều là tổ yến. Bảng dưới so sánh các tiêu chí chính.</p>
  <table><thead><tr><th>Tiêu chí</th><th>Yến trắng</th><th>Yến hồng</th><th>Huyết yến</th></tr></thead><tbody>
  <tr><td>Màu sắc</td><td>Trắng ngà, hơi vàng nhạt</td><td>Hồng cam nhạt, vàng cam</td><td>Đỏ cam đến đỏ đậm</td></tr>
  <tr><td>Mức độ phổ biến</td><td>Phổ biến nhất</td><td>Ít hơn</td><td>Hiếm</td></tr>
  <tr><td>Giá</td><td>Nhiều mức giá</td><td>Cao hơn yến trắng</td><td>Cao nhất trong ba loại</td></tr>
  <tr><td>Nguy cơ hàng nhuộm</td><td>Có thể bị tẩy trắng bất thường</td><td>Cao</td><td>Cao</td></tr>
  <tr><td>Dễ kiểm tra nguồn gốc</td><td>Dễ, hỏi nhà yến, xưởng</td><td>Khó hơn</td><td>Khó hơn</td></tr>
  </tbody></table>

  <h2>Vì sao tổ yến có màu khác nhau?</h2>
  <p>Màu tổ yến chủ yếu do môi trường nơi tổ được làm. Theo kinh nghiệm trong nghề, tổ bám vào vách đá có khoáng chất, tổ ở nơi có độ ẩm cao hoặc tổ để lâu trong nhà yến trước khi khai thác thường ngả màu vàng cam, hồng, có khi đỏ.</p>
  <ul>
    <li><b>Nơi làm tổ:</b> tổ bám vách hang đá dễ có màu hơn tổ bám xà gỗ trong nhà yến.</li>
    <li><b>Độ ẩm, không khí:</b> ảnh hưởng đến màu tổ theo thời gian.</li>
    <li><b>Thời gian tổ ở lại:</b> tổ để lâu trước khi khai thác có thể sậm màu hơn.</li>
  </ul>
  <p>Vì phụ thuộc nhiều yếu tố tự nhiên, tổ yến màu xuất hiện ít và không đều, nên khó có số lượng lớn. Nơi làm tổ còn liên quan tới khác biệt giữa yến nhà và yến đảo, xem bài <a href="yen-nha-va-yen-dao.html">yến nhà và yến đảo khác nhau thế nào</a>.</p>

  <h2>Huyết yến có tốt hơn yến trắng không?</h2>
  <p>Không có căn cứ rõ ràng để khẳng định huyết yến hay yến hồng bổ hơn yến trắng. Cả ba đều là tổ yến; điều làm giá chênh lệch là màu sắc đẹp, độ hiếm và tâm lý chuộng hàng hiếm, không phải một công dụng được chứng minh.</p>
  <p>Với nhu cầu dùng thường xuyên trong gia đình, yến trắng đã làm sạch là lựa chọn phổ biến vì dễ mua, giá hợp lý và dễ kiểm tra nguồn gốc. Yến màu thường được chọn khi người mua muốn quà biếu hiếm và chấp nhận giá cao.</p>

  <h2>Cách nhận biết yến hồng, huyết yến nhuộm màu</h2>
  <p>Vì yến màu đắt, trên thị trường có hàng yến trắng bị nhuộm để bán thành yến hồng, huyết yến. Không có mẹo nào chắc chắn 100%, nhưng có vài dấu hiệu nên cẩn thận:</p>
  <ol>
    <li><b>Nước ngâm ra màu:</b> yến màu tự nhiên khi ngâm thường không làm nước chuyển đỏ rõ; nước ngâm đỏ hoặc cam đậm là dấu hiệu đáng ngờ.</li>
    <li><b>Màu loang không đều bất thường:</b> màu đậm ở bề mặt nhưng bên trong sợi lại trắng.</li>
    <li><b>Màu quá rực, đồng đều như sơn:</b> màu tự nhiên thường không đều và hơi ngả cam.</li>
    <li><b>Giá rẻ bất thường:</b> huyết yến hiếm, giá thấp hơn thị trường nhiều cần hỏi kỹ.</li>
    <li><b>Không có giấy tờ:</b> thiếu nhãn, bản tự công bố, thông tin cơ sở sản xuất.</li>
  </ol>
  <p>Yến trắng cũng có thể bị tẩy để trắng tinh bất thường; dấu hiệu chung xem bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>.</p>

  <h2>Nên chọn loại nào?</h2>
  <table><thead><tr><th>Nhu cầu</th><th>Gợi ý</th></tr></thead><tbody>
  <tr><td>Chưng hằng tuần trong gia đình</td><td>Yến trắng tinh chế, sợi vừa</td></tr>
  <tr><td>Muốn chén yến nhiều sợi, đặc</td><td>Yến trắng tinh chế 2 lớp sợi</td></tr>
  <tr><td>Biếu tặng, muốn tổ đẹp</td><td>Yến rút lông định hình</td></tr>
  <tr><td>Muốn quà hiếm, ngân sách cao</td><td>Yến màu từ nơi bán có nguồn gốc và giấy tờ rõ ràng</td></tr>
  </tbody></table>
  <p>Chọn theo ngân sách xem bài <a href="yen-sao-loai-nao-tot.html">yến sào loại nào tốt</a>; so sánh mức độ làm sạch xem bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông</a>.</p>

  <h2>Yến trắng tại Việt Cường Nhân</h2>
  <p>Việt Cường Nhân hiện bán yến trắng từ nhà yến riêng, nhặt lông tại xưởng, nhà máy đạt HACCP, ISO 22000:2018 và GMP. Giá dưới đây lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(109, "Sợi vừa, dùng hằng tuần."), li(112, "Hai lớp sợi, chén yến đặc hơn."), li(114, "Tổ nguyên dáng, hợp biếu tặng.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Huyết yến là gì?", "Huyết yến là tổ yến có màu đỏ cam đến đỏ đậm. Màu tổ chủ yếu do môi trường nơi làm tổ, không phải do máu của chim yến."),
       ("Huyết yến có phải máu chim yến không?", "Không. Chim yến làm tổ bằng nước dãi; tên 'huyết yến' chỉ là cách gọi theo màu đỏ của tổ."),
       ("Huyết yến có bổ hơn yến trắng không?", "Không có căn cứ rõ ràng để khẳng định như vậy. Huyết yến đắt hơn chủ yếu vì hiếm và màu đẹp."),
       ("Làm sao biết huyết yến bị nhuộm?", "Cẩn thận khi nước ngâm ra màu đỏ, màu loang chỉ ở bề mặt, màu quá rực và đồng đều, giá rẻ bất thường hoặc không có giấy tờ nguồn gốc."),
       ("Yến hồng là gì?", "Yến hồng là tổ yến có màu hồng cam nhạt, nằm giữa yến trắng và huyết yến, hiếm hơn yến trắng nên giá cao hơn.")]),
dict(slug="yen-bi-chay-nuoc-khi-chung", cat="Yến sào", ngay="2026-11-05",
  tu_khoa="yến bị chảy nước, yến chưng bị tan, vì sao yến bị chảy nước khi chưng, cách chưng yến không bị tan, yến chưng bị nhão",
  h1="Vì sao yến bị chảy nước khi chưng? Cách khắc phục",
  desc="Yến bị chảy nước, tan sợi khi chưng thường do ngâm quá lâu, chưng quá lâu, lửa quá to hoặc khuấy mạnh. Nguyên nhân, cách khắc phục, thời gian ngâm và chưng.",
  lede="Yến bị chảy nước khi chưng, tức sợi yến tan hết vào nước, thường do ngâm quá lâu, chưng quá lâu, đun lửa quá to hoặc khuấy mạnh tay. Cách khắc phục là ngâm vừa đủ cho sợi nở mềm, chưng cách thủy lửa nhỏ khoảng 20–30 phút với yến tinh chế, đậy kín nắp và chỉ khuấy nhẹ khi thêm đường phèn.",
  tom_tat=["Nguyên nhân thường gặp: ngâm quá lâu, chưng quá lâu, lửa to sôi sùng sục, khuấy mạnh, ngâm hoặc chưng bằng nước nóng.",
           "Thời gian tham khảo: yến tinh chế ngâm 30–60 phút, chưng cách thủy 20–30 phút; yến vụn ngâm 15–20 phút, chưng 10–15 phút.",
           "Chưng cách thủy lửa nhỏ, nước ngoài thố sôi lăn tăn, đậy kín nắp thố.",
           "Đường phèn cho ở 5 phút cuối, khuấy nhẹ; không đun lại nhiều lần yến đã chưng.",
           "Yến chảy nước vẫn ăn được nếu không có mùi vị lạ, chỉ là mất độ dai của sợi."],
  body=f"""  <h2>Vì sao yến bị chảy nước khi chưng?</h2>
  <p>Yến bị chảy nước khi chưng chủ yếu do sợi yến bị làm mềm quá mức: ngâm quá lâu, chưng quá lâu hoặc đun ở nhiệt quá cao. Sợi yến khi ngâm sẽ hút nước và nở ra; nếu tiếp tục chịu nhiệt lâu, sợi mềm dần rồi tan vào nước, chén yến trở thành nước sệt, không còn sợi.</p>
  <p>Ở xưởng Việt Cường Nhân, đây là câu khách mới chưng yến lần đầu hay hỏi nhất: "sao yến nhà em chưng xong mất hết sợi". Hầu như lần nào cũng do một trong các nguyên nhân dưới đây.</p>
  <table><thead><tr><th>Nguyên nhân</th><th>Dấu hiệu</th><th>Cách khắc phục</th></tr></thead><tbody>
  <tr><td>Ngâm quá lâu</td><td>Sợi đã nhũn trước khi chưng</td><td>Ngâm vừa đủ đến khi sợi nở mềm, tơi</td></tr>
  <tr><td>Chưng quá lâu</td><td>Sợi tan dần vào nước</td><td>Yến tinh chế chưng 20–30 phút, yến vụn 10–15 phút</td></tr>
  <tr><td>Lửa quá to, nước sôi sùng sục</td><td>Nước trong thố sôi, sợi đứt vụn</td><td>Chưng cách thủy, lửa nhỏ, sôi lăn tăn</td></tr>
  <tr><td>Nấu trực tiếp trên bếp</td><td>Yến sôi mạnh, nhanh tan</td><td>Chuyển sang chưng cách thủy</td></tr>
  <tr><td>Ngâm hoặc chưng bằng nước nóng ngay từ đầu</td><td>Sợi mềm nhanh, khó giữ dáng</td><td>Ngâm bằng nước sạch nhiệt độ thường</td></tr>
  <tr><td>Khuấy mạnh, xé sợi quá nhỏ</td><td>Sợi đứt vụn, nước đục</td><td>Xé theo thớ sợi, khuấy nhẹ</td></tr>
  <tr><td>Đun lại nhiều lần</td><td>Yến cất tủ lạnh bị nhão dần</td><td>Chưng vừa đủ, hâm cách thủy ngắn</td></tr>
  </tbody></table>

  <h2>Ngâm yến bao lâu để không bị chảy nước?</h2>
  <p>Ngâm yến chỉ cần đến khi sợi nở mềm và tơi ra; ngâm lâu hơn mức đó là nguyên nhân đầu tiên làm yến dễ tan khi chưng. Thời gian thay đổi theo loại yến:</p>
  <table><thead><tr><th>Loại yến</th><th>Ngâm</th><th>Chưng cách thủy</th></tr></thead><tbody>
  <tr><td>Yến tinh chế vụn</td><td>15–20 phút</td><td>10–15 phút</td></tr>
  <tr><td>Yến tinh chế sợi</td><td>30–60 phút</td><td>20–30 phút</td></tr>
  <tr><td>Yến rút lông</td><td>30–60 phút hoặc hơn, đến khi sợi mềm</td><td>20–30 phút</td></tr>
  <tr><td>Chân yến</td><td>Khoảng 2–3 tiếng</td><td>30–40 phút</td></tr>
  </tbody></table>
  <p>Đây là mức tham khảo; tổ khô, dày cần lâu hơn, tổ mỏng nhanh hơn. Chi tiết từng loại xem bài <a href="yen-vun-baby-la-gi.html">yến vụn baby là gì</a> và <a href="chan-yen-chan-tua-la-gi.html">chân yến là gì</a>.</p>

  <h2>Cách chưng yến không bị chảy nước</h2>
  <p>Chưng cách thủy lửa nhỏ, đậy kín nắp và canh đúng thời gian là cách giữ sợi yến dai. Các bước cho một chén khoảng 3–5 g yến khô với 150–200 ml nước:</p>
  <ol>
    <li><b>Ngâm vừa đủ:</b> nước sạch nhiệt độ thường, đến khi sợi nở mềm, tơi.</li>
    <li><b>Vớt qua rây, xé theo thớ:</b> xé nhẹ tay, không xé quá nhỏ.</li>
    <li><b>Cho yến và nước vào thố, đậy nắp:</b> nước ngập yến khoảng 1–2 đốt ngón tay.</li>
    <li><b>Chưng cách thủy lửa nhỏ:</b> nước ngoài thố sôi lăn tăn, ngập khoảng nửa thân thố.</li>
    <li><b>Canh thời gian:</b> yến tinh chế sợi khoảng 20–30 phút; yến vụn 10–15 phút.</li>
    <li><b>Thêm đường phèn ở 5 phút cuối:</b> khuấy nhẹ cho tan rồi tắt bếp.</li>
  </ol>
  <p>Các bước chưng đầy đủ xem bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>. Nếu chưng cùng hạt sen, nên nấu sen trước để không phải chưng yến quá lâu, xem bài <a href="yen-chung-tao-do-hat-sen.html">cách làm yến chưng táo đỏ hạt sen</a>.</p>

  <h2>Yến bị chảy nước rồi có ăn được không?</h2>
  <p>Yến bị chảy nước vì chưng quá tay vẫn ăn được nếu không có mùi chua, mùi lạ hay váng bất thường; chỉ là chén yến mất độ dai và không còn sợi đẹp. Nếu yến có mùi chua, nhớt hoặc đã để lâu ở nhiệt độ phòng thì nên bỏ.</p>
  <p>Dấu hiệu yến hỏng và cách cất yến đã chưng xem bài <a href="bao-quan-yen-sao.html">cách bảo quản yến sào khô và yến đã chưng</a>.</p>

  <h2>Yến tan nhanh có phải yến giả không?</h2>
  <p>Không thể kết luận yến giả chỉ vì chén yến bị tan, vì yến thật chưng sai cách cũng tan. Nếu bạn ngâm và chưng đúng thời gian, lửa nhỏ mà sợi vẫn tan rất nhanh, nước đục trắng, có váng hoặc mùi lạ, thì nên hỏi kỹ nguồn gốc sản phẩm. Các dấu hiệu khác xem bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>.</p>

  <h2>Mẹo giữ sợi yến dai</h2>
  <ul>
    <li><b>Chưng thử mẻ nhỏ</b> khi mới mua loại yến khác để canh thời gian phù hợp.</li>
    <li><b>Dùng thố sứ có nắp</b> thay vì nồi kim loại nấu trực tiếp.</li>
    <li><b>Hẹn giờ</b> khi chưng, tránh quên để quá lâu.</li>
    <li><b>Chưng vừa đủ ăn 2–3 ngày,</b> hạn chế hâm lại nhiều lần.</li>
    <li><b>Muốn sợi rõ, dai:</b> chọn yến tinh chế sợi hoặc yến rút lông thay vì yến vụn.</li>
  </ul>

  <h2>Yến giữ sợi tốt khi chưng</h2>
  <p>Yến sợi dài và dày giữ dáng tốt hơn khi chưng. Giá dưới đây lấy từ bảng giá website Việt Cường Nhân, chưa gồm phí giao hàng:</p>
""" + ul(li(109, "Sợi vừa, chưng 20–30 phút."), li(112, "Hai lớp sợi, chén yến đặc hơn."), li(113, "Sợi dài, giữ dáng tốt.")) + """
  <p>So sánh các loại yến xem bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>; cần hướng dẫn chưng, nhắn Zalo 0978 094 739.</p>""",
  faq=[("Vì sao yến bị chảy nước khi chưng?", "Thường do ngâm quá lâu, chưng quá lâu, lửa quá to hoặc nấu trực tiếp trên bếp, khuấy mạnh tay. Sợi yến bị mềm quá mức nên tan vào nước."),
       ("Chưng yến bao lâu thì không bị tan?", "Yến tinh chế sợi chưng cách thủy lửa nhỏ khoảng 20–30 phút, yến vụn khoảng 10–15 phút. Chân yến cần lâu hơn, khoảng 30–40 phút."),
       ("Yến bị chảy nước có ăn được không?", "Vẫn ăn được nếu không có mùi chua, mùi lạ hay váng bất thường; chỉ là mất độ dai của sợi."),
       ("Yến tan nhanh có phải yến giả không?", "Chưa chắc. Yến thật chưng sai cách cũng tan; nếu chưng đúng mà vẫn tan rất nhanh, nước đục, có mùi lạ thì nên hỏi kỹ nguồn gốc."),
       ("Có nên nấu yến trực tiếp trên bếp không?", "Không nên, vì nước sôi mạnh làm sợi yến nhanh tan. Nên chưng cách thủy với lửa nhỏ.")]),
dict(slug="yen-co-mui-tanh-khong", cat="Yến sào", ngay="2026-11-05",
  tu_khoa="yến có mùi tanh, yến sào có mùi tanh không, cách khử mùi tanh của yến, yến có mùi lạ, yến chưng bị tanh",
  h1="Yến có mùi tanh không? Mùi thế nào là bình thường",
  desc="Yến có mùi tanh không? Yến thật có mùi tanh nhẹ đặc trưng, rõ nhất khi ngâm. Cách phân biệt mùi bình thường với mùi lạ, mùi hỏng và mẹo giảm mùi tanh khi chưng.",
  lede="Yến có mùi tanh nhẹ đặc trưng, rõ nhất khi ngâm nước và khi mở nắp thố lúc vừa chưng xong; đây là mùi bình thường của tổ yến. Mùi chua, mốc, hôi lạ, mùi hóa chất hoặc hoàn toàn không có mùi gì cùng với màu trắng bất thường mới là dấu hiệu cần cẩn thận.",
  tom_tat=["Yến thật có mùi tanh nhẹ, thoang thoảng, rõ hơn khi ngâm và khi vừa chưng xong.",
           "Mùi chua, mốc, hôi lạ, mùi hóa chất là dấu hiệu yến bị ẩm hỏng hoặc đã qua xử lý; nên hỏi kỹ hoặc bỏ.",
           "Giảm mùi tanh: ngâm và xả nước sạch, chưng cùng 1–2 lát gừng, táo đỏ hoặc lá dứa.",
           "Mùi tanh giảm nhiều sau khi chưng cùng đường phèn và để nguội, cất ngăn mát.",
           f"Yến tinh chế đã nhặt sạch lông của Việt Cường Nhân: {P[109][2]} {gia(109)}/100gr, {P[113][2]} {gia(113)}/100gr."],
  body=f"""  <h2>Yến có mùi tanh không?</h2>
  <p>Có. Yến sào thật có mùi tanh nhẹ, thoang thoảng, giống mùi trứng hoặc mùi nước biển nhẹ. Mùi này rõ nhất khi ngâm yến và khi mở nắp thố lúc vừa chưng xong, sau đó dịu đi khi yến nguội.</p>
  <p>Ở xưởng Việt Cường Nhân, khách mới mua yến lần đầu thường hỏi "yến có mùi tanh vậy có sao không". Mùi tanh nhẹ là bình thường; điều cần để ý là mùi có lạ, nồng, chua hay mốc không.</p>

  <h2>Mùi yến thế nào là bình thường, thế nào là bất thường?</h2>
  <p>Mùi bình thường của yến là tanh nhẹ, dễ chịu, không xộc mũi. Bảng dưới giúp phân biệt nhanh.</p>
  <table><thead><tr><th>Mùi</th><th>Đánh giá</th><th>Nên làm gì</th></tr></thead><tbody>
  <tr><td>Tanh nhẹ, thoang thoảng</td><td>Bình thường</td><td>Ngâm, xả sạch rồi chưng như thường</td></tr>
  <tr><td>Tanh rõ hơn khi vừa chưng</td><td>Bình thường</td><td>Để nguội, mùi sẽ dịu</td></tr>
  <tr><td>Chua, lên men</td><td>Yến đã ngâm hoặc đã chưng bị hỏng</td><td>Bỏ, không dùng</td></tr>
  <tr><td>Mốc, ẩm</td><td>Yến khô bị hút ẩm, mốc</td><td>Bỏ phần bị mốc; mốc nhiều thì bỏ cả</td></tr>
  <tr><td>Mùi hóa chất, mùi lạ hắc</td><td>Đáng ngờ đã qua xử lý</td><td>Ngưng dùng, hỏi kỹ nguồn gốc</td></tr>
  <tr><td>Hoàn toàn không mùi, kèm màu trắng tinh bất thường</td><td>Cần cẩn thận</td><td>Hỏi kỹ nguồn gốc, giấy tờ</td></tr>
  </tbody></table>
  <p>Không thể kết luận yến thật hay giả chỉ bằng mùi; nên kết hợp nhiều dấu hiệu khi ngâm, chưng và giấy tờ, xem bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>.</p>

  <h2>Vì sao yến có mùi tanh?</h2>
  <p>Tổ yến được chim yến làm từ nước dãi, nên có mùi tanh tự nhiên. Mùi này thường không mất hẳn sau khi làm sạch, chỉ nhẹ đi; vì vậy yến tinh chế vẫn còn mùi tanh nhẹ là bình thường. Yến thô còn lông và tạp chất thường có mùi rõ hơn yến tinh chế đã được làm sạch; khi ngâm, yến hút nước và nở ra nên mùi cũng lộ rõ hơn lúc còn khô.</p>
  <ul>
    <li><b>Yến thô:</b> mùi rõ hơn, giảm đi sau khi làm sạch; xem bài <a href="cach-lam-sach-yen-tho.html">cách làm sạch yến thô tại nhà</a>.</li>
    <li><b>Yến tinh chế, yến rút lông:</b> đã nhặt lông, làm sạch tại xưởng nên mùi nhẹ hơn.</li>
    <li><b>Nước yến hũ:</b> đã chưng và nêm, mùi tanh thường rất nhẹ.</li>
  </ul>

  <h2>Cách khử mùi tanh của yến khi chưng</h2>
  <p>Có thể giảm mùi tanh của yến bằng cách xả kỹ sau khi ngâm và chưng cùng một chút nguyên liệu thơm. Không cần, và không nên, dùng hóa chất hay chất tẩy.</p>
  <ol>
    <li><b>Ngâm và xả nước sạch:</b> sau khi yến nở mềm, đổ qua rây, xả lại 1–2 lần bằng nước sạch.</li>
    <li><b>Thêm 1–2 lát gừng mỏng:</b> cho vào thố khi chưng, vớt ra trước khi ăn.</li>
    <li><b>Chưng cùng táo đỏ hoặc vài lá dứa:</b> tạo mùi thơm, át mùi tanh; công thức xem bài <a href="yen-chung-tao-do-hat-sen.html">yến chưng táo đỏ hạt sen</a>.</li>
    <li><b>Đường phèn ở 5 phút cuối:</b> vị ngọt thanh giúp mùi tanh khó nhận ra hơn.</li>
    <li><b>Để nguội, cất ngăn mát:</b> yến ăn mát thường ít mùi hơn khi ăn nóng.</li>
  </ol>
  <p>Có thể chưng cùng sữa tươi hoặc nước cốt dừa sau khi tắt bếp cho người không quen mùi yến. Các bước chưng cơ bản xem bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Những lỗi làm yến có mùi khó chịu</h2>
  <ul>
    <li><b>Bảo quản yến khô nơi ẩm:</b> yến hút ẩm, dễ có mùi mốc.</li>
    <li><b>Ngâm yến để lâu ở nhiệt độ phòng:</b> nước ngâm dễ lên men, có mùi chua.</li>
    <li><b>Để yến chưng qua đêm ngoài tủ lạnh:</b> yến dễ chua, hỏng.</li>
    <li><b>Đậy hũ không kín trong tủ lạnh:</b> yến ám mùi thức ăn khác.</li>
  </ul>
  <p>Cách bảo quản đúng xem bài <a href="bao-quan-yen-sao.html">cách bảo quản yến sào khô và yến đã chưng</a>.</p>

  <h2>Chọn yến đã làm sạch để ít mùi hơn</h2>
  <p>Người không quen mùi yến có thể chọn yến tinh chế hoặc yến rút lông đã được nhặt lông, làm sạch tại xưởng. Yến của Việt Cường Nhân được làm sạch tại xưởng đạt HACCP, ISO 22000:2018 và GMP; giá dưới đây lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(109, "Đã nhặt sạch lông, ngâm xong là chưng."), li(113, "Sợi dài, đã nhặt lông bằng tay."), li(124, "Nước yến chưng sẵn, mùi rất nhẹ.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Cần hỏi về mùi của yến đã mua, nhắn Zalo 0978 094 739 kèm ảnh hoặc video để được tư vấn.</p>""",
  faq=[("Yến sào có mùi tanh không?", "Có. Yến thật có mùi tanh nhẹ, thoang thoảng, rõ nhất khi ngâm và khi vừa chưng xong; đây là mùi bình thường."),
       ("Yến có mùi chua có ăn được không?", "Không nên. Mùi chua thường là dấu hiệu yến đã ngâm hoặc đã chưng bị hỏng, nên bỏ."),
       ("Làm sao khử mùi tanh của yến?", "Xả kỹ yến bằng nước sạch sau khi ngâm, chưng cùng 1–2 lát gừng, táo đỏ hoặc lá dứa, thêm đường phèn ở cuối và để nguội trước khi ăn."),
       ("Yến không có mùi gì là yến giả?", "Chưa chắc, nhưng yến hoàn toàn không mùi kèm màu trắng tinh bất thường thì nên hỏi kỹ nguồn gốc và giấy tờ sản phẩm."),
       ("Yến khô có mùi mốc phải làm sao?", "Yến có mùi mốc hoặc đốm mốc là đã bị ẩm hỏng; nên bỏ, và lần sau bảo quản yến khô trong hộp kín, nơi khô ráo.")]),
dict(slug="phan-biet-yen-tay-trang-yen-tron", cat="Yến sào", ngay="2026-11-06",
  tu_khoa="yến tẩy trắng, cách nhận biết yến tẩy trắng, yến trộn tạp chất, yến trộn đường, phân biệt yến thật và yến pha",
  h1="Cách nhận biết yến tẩy trắng, yến trộn tạp chất",
  desc="Cách nhận biết yến tẩy trắng và yến trộn tạp chất bằng mắt, khi ngâm, khi chưng; dấu hiệu nên nghi ngờ, giấy tờ cần hỏi người bán và cách mua yến an toàn hơn.",
  lede="Yến tẩy trắng thường có màu trắng tinh đều bất thường, sợi giòn, dễ gãy, đôi khi có mùi hắc lạ, còn yến trộn tạp chất thường nặng tay, sợi dính bết, khi ngâm nước bị đục, có cặn hoặc tan nhũn. Không có mẹo nào chắc chắn 100%, nên cần kết hợp nhiều dấu hiệu và mua ở nơi có nguồn gốc, giấy tờ rõ ràng.",
  tom_tat=["Yến tự nhiên có màu trắng ngà, hơi vàng, không đều; yến trắng tinh như giấy, đều tuyệt đối là dấu hiệu nên hỏi kỹ.",
           "Yến tẩy trắng thường sợi giòn, dễ gãy vụn, có thể có mùi hắc, mùi hóa chất thay vì mùi tanh nhẹ.",
           "Yến trộn tạp chất thường nặng tay so với kích thước, sợi bết dính, nước ngâm đục, có cặn, vị ngọt hoặc tan nhanh khi chưng.",
           "Không có mẹo nào chắc chắn 100%; hãy kết hợp quan sát, ngâm thử, chưng thử và giấy tờ của người bán.",
           "Giấy tờ nên hỏi: bản tự công bố sản phẩm, chứng nhận an toàn thực phẩm của cơ sở, địa chỉ xưởng có thể đến xem."],
  body=f"""  <h2>Yến tẩy trắng là gì?</h2>
  <p>Yến tẩy trắng là tổ yến đã bị xử lý bằng chất tẩy để có màu trắng tinh, nhìn "sạch" và đẹp hơn, thường để che màu ngả vàng, tạp chất hoặc yến kém chất lượng. Đây là hàng không nên dùng vì người mua không biết đã dùng chất gì và dư lượng ra sao.</p>
  <p>Yến tự nhiên đã làm sạch thường có màu trắng ngà đến vàng nhạt, không đều tuyệt đối. Ở xưởng Việt Cường Nhân, yến chỉ được làm sạch bằng nước sạch và nhặt lông thủ công bằng nhíp, nên sợi giữ màu tự nhiên.</p>

  <h2>Yến trộn tạp chất là gì?</h2>
  <p>Yến trộn tạp chất là yến bị trộn thêm chất độn như bột, đường, chất tạo đông hoặc phụ gia để tăng khối lượng, làm tổ trông dày, đầy đặn hơn, rồi bán theo giá yến. Người mua trả tiền cho phần không phải yến, và không rõ phần trộn thêm là gì.</p>
  <p>Hàng trộn thường gặp ở yến vụn, yến ép miếng hoặc tổ được "đắp" lại với giá rẻ bất thường. Không phải mọi yến đắp tổ hay yến vụn đều là hàng trộn; yến đắp tổ thật chỉ là sợi yến sạch được đắp lại thành tai cho gọn.</p>

  <h2>Cách nhận biết yến tẩy trắng</h2>
  <p>Yến tẩy trắng thường lộ ra qua màu sắc, độ giòn của sợi và mùi. Hãy để ý các dấu hiệu sau:</p>
  <table><thead><tr><th>Dấu hiệu</th><th>Yến tự nhiên đã làm sạch</th><th>Yến nghi tẩy trắng</th></tr></thead><tbody>
  <tr><td>Màu sắc</td><td>Trắng ngà, hơi vàng, không đều</td><td>Trắng tinh như giấy, đều tuyệt đối</td></tr>
  <tr><td>Sợi yến</td><td>Dai, uốn được, to nhỏ không đều</td><td>Giòn, dễ gãy vụn khi bẻ</td></tr>
  <tr><td>Mùi</td><td>Tanh nhẹ đặc trưng</td><td>Mùi hắc, mùi hóa chất, hoặc gần như không mùi</td></tr>
  <tr><td>Khi ngâm</td><td>Nở mềm, sợi tơi, giữ dáng</td><td>Nở rất nhanh, sợi nhũn, dễ đứt</td></tr>
  <tr><td>Khi chưng</td><td>Sợi còn, hơi dai</td><td>Sợi tan nhanh dù chưng đúng thời gian</td></tr>
  </tbody></table>
  <p>Mùi bình thường của yến xem thêm bài <a href="yen-co-mui-tanh-khong.html">yến có mùi tanh không</a>.</p>

  <h2>Cách nhận biết yến trộn tạp chất</h2>
  <p>Yến trộn tạp chất thường nặng tay, sợi bết dính và lộ rõ khi ngâm nước. Các dấu hiệu nên chú ý:</p>
  <ol>
    <li><b>Nặng bất thường:</b> tổ nhỏ nhưng cầm thấy nặng, đặc cứng, không thấy rõ từng lớp sợi.</li>
    <li><b>Sợi bết dính:</b> soi dưới đèn thấy bề mặt bóng, láng như có lớp keo, không thấy sợi đan xen.</li>
    <li><b>Nước ngâm đục, có cặn:</b> nước chuyển đục trắng, có lớp cặn lắng hoặc váng; nếm nước ngâm thấy ngọt.</li>
    <li><b>Tan nhũn khi ngâm:</b> một phần tổ tan thành bột, nhão, không xé được thành sợi.</li>
    <li><b>Sau khi chưng còn ít sợi:</b> khối lượng khô nhiều nhưng chén yến sau chưng có rất ít sợi.</li>
  </ol>
  <p>Yến thật chưng sai cách cũng có thể bị tan, nên hãy chưng thử đúng thời gian trước khi kết luận; xem bài <a href="yen-bi-chay-nuoc-khi-chung.html">vì sao yến bị chảy nước khi chưng</a>.</p>

  <h2>Cách thử yến tại nhà: ngâm và chưng thử</h2>
  <p>Cách đơn giản nhất là ngâm và chưng thử một lượng nhỏ trước khi dùng cả hộp. Đây là cách tham khảo, không thay được kiểm nghiệm.</p>
  <ol>
    <li>Lấy khoảng 2–3 g yến, ngâm trong ly nước sạch, nhiệt độ thường.</li>
    <li>Quan sát sau 30–60 phút với yến tinh chế: yến thật nở mềm, sợi tơi ra, nước khá trong.</li>
    <li>Dùng tay kéo nhẹ một sợi: yến thật có độ dai nhất định, không bở như bột.</li>
    <li>Chưng cách thủy lửa nhỏ 20–30 phút: yến thật vẫn còn sợi, hơi dai, có mùi tanh nhẹ.</li>
  </ol>
  <p>Các bước chưng chuẩn xem bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Những mẹo truyền miệng không đáng tin</h2>
  <p>Nhiều mẹo thử yến được truyền tai, nhưng không mẹo nào đủ để khẳng định yến thật hay giả. Ví dụ đốt sợi yến để ngửi mùi, hay chỉ nhìn màu trắng để kết luận, đều dễ cho kết quả sai. Nên kết hợp nhiều dấu hiệu và ưu tiên mua nơi có nguồn gốc rõ ràng.</p>

  <h2>Giá rẻ bất thường: dấu hiệu dễ thấy nhất</h2>
  <p>Giá rẻ hơn thị trường quá nhiều là dấu hiệu dễ thấy nhất của yến pha, vì công nhặt lông thủ công chiếm phần lớn giá thành yến tinh chế. Giá tham khảo theo bảng giá website Việt Cường Nhân:</p>
""" + ul(li(101, "Yến thô, còn lông, tự làm sạch tại nhà."), li(109, "Yến tinh chế đã nhặt sạch lông."), li(113, "Nhặt lông bằng tay trên tổ nguyên sợi.")) + f"""
  <p>Bảng giá các loại xem bài <a href="gia-yen-sao-bao-nhieu-tien.html">giá yến sào bao nhiêu tiền 100gr</a>.</p>

  <h2>Giấy tờ nên hỏi khi mua yến</h2>
  <ul>
    <li><b>Bản tự công bố sản phẩm</b> cho đúng loại yến đang mua.</li>
    <li><b>Chứng nhận an toàn thực phẩm</b> của cơ sở sản xuất như HACCP, ISO 22000, GMP; xem bài <a href="chung-nhan-haccp-iso-22000-gmp-la-gi.html">HACCP, ISO 22000 và GMP nghĩa là gì</a>.</li>
    <li><b>Nhãn sản phẩm</b> ghi tên, khối lượng, ngày sản xuất, hạn dùng, cơ sở sản xuất.</li>
    <li><b>Địa chỉ xưởng</b> có thể đến xem tận nơi.</li>
  </ul>
  <p>Việt Cường Nhân công khai chứng nhận HACCP, ISO 22000:2018, GMP và bản tự công bố tổ yến thô, tổ yến tinh chế trên <a href="../chung-nhan/">trang chứng nhận</a>; khách có thể hẹn trước để đến xưởng ở Dĩ An xem quy trình làm sạch, địa chỉ trong bài <a href="yen-sao-binh-duong-di-an-mua-o-dau.html">mua yến sào ở Dĩ An</a>. Thêm các dấu hiệu chung ở bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>. Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>; cần hỏi, nhắn Zalo 0978 094 739.</p>""",
  faq=[("Làm sao nhận biết yến tẩy trắng?", "Yến tẩy trắng thường trắng tinh đều bất thường, sợi giòn dễ gãy, có mùi hắc hoặc gần như không mùi, ngâm nhanh nhũn và chưng nhanh tan."),
       ("Yến trắng tinh có phải yến tẩy không?", "Chưa chắc, nhưng yến tự nhiên thường trắng ngà, hơi vàng và không đều. Yến trắng tinh như giấy nên hỏi kỹ nguồn gốc và giấy tờ."),
       ("Yến trộn tạp chất có dấu hiệu gì?", "Tổ nặng bất thường, sợi bóng bết dính, nước ngâm đục có cặn hoặc vị ngọt, một phần tan thành bột khi ngâm, chưng xong còn rất ít sợi."),
       ("Có mẹo nào nhận biết yến thật chắc chắn 100% không?", "Không. Nên kết hợp quan sát, ngâm thử, chưng thử, giá cả và giấy tờ của cơ sở sản xuất."),
       ("Mua yến ở đâu để tránh hàng pha?", "Chọn nơi có địa chỉ xưởng rõ ràng, bản tự công bố sản phẩm, chứng nhận an toàn thực phẩm và cho phép khách đến xem.")]),
dict(slug="yen-tinh-che-1-lop-va-2-lop", cat="Yến sào", ngay="2026-11-06",
  tu_khoa="yến tinh chế 1 lớp 2 lớp, yến tinh chế 1 lớp là gì, yến tinh chế 2 lớp là gì, yến 10 tai và 18-20 tai, nên mua yến 1 lớp hay 2 lớp",
  h1="Yến tinh chế 1 lớp 2 lớp sợi khác nhau thế nào?",
  desc="Yến tinh chế 1 lớp 2 lớp khác nhau ở cách đắp sợi, độ dày tai yến, cảm giác khi ăn và giá. So sánh loại 10 tai, 18–20 tai, bảng giá 100gr và nên chọn loại nào.",
  lede="Yến tinh chế 1 lớp và 2 lớp đều là yến đã nhặt sạch lông tại xưởng, khác nhau ở cách đắp sợi khi định hình: loại 1 lớp đắp một lớp sợi mỏng thành tai yến, loại 2 lớp đắp hai lớp sợi chồng lên nên tai dày, chắc và chén yến nhiều sợi hơn. Loại 1 lớp hợp dùng hằng ngày, loại 2 lớp hợp người thích chén yến đặc sợi hoặc làm quà.",
  tom_tat=["Cả hai đều là yến tinh chế đã nhặt sạch lông, ngâm 30–60 phút rồi chưng cách thủy 20–30 phút.",
           "1 lớp: tai mỏng, sợi đan đều, dễ chia phần; 2 lớp: hai lớp sợi chồng lên, tai dày, chắc tay.",
           f"Giá 100gr: {P[109][2]} {gia(109)}, loại 10 tai và 18–20 tai {gia(110)}, {P[112][2]} {gia(112)}.",
           "Loại 18–20 tai/100gr mỗi tai khoảng 5 g, đủ một chén; loại 10 tai/100gr mỗi tai khoảng 10 g, chia được 2 chén.",
           "Dùng hằng ngày chọn 1 lớp sợi vừa; thích nhiều sợi hoặc biếu tặng chọn 2 lớp."],
  body=f"""  <h2>Yến tinh chế 1 lớp và 2 lớp là gì?</h2>
  <p>Yến tinh chế là tổ yến đã được ngâm, nhặt sạch lông tại xưởng, rồi đắp sợi vào khuôn và sấy khô thành hình tai yến. "1 lớp" và "2 lớp" chỉ số lớp sợi được đắp khi định hình: một lớp sợi mỏng, hoặc hai lớp sợi chồng lên nhau.</p>
  <p>Ở xưởng Việt Cường Nhân, sau khi nhặt lông, thợ đắp sợi yến vào khuôn tai theo từng loại. Cùng là sợi yến sạch, nhưng số lớp và kích thước tai quyết định độ dày, cảm giác khi ăn và giá bán.</p>

  <h2>So sánh yến tinh chế 1 lớp và 2 lớp</h2>
  <p>Khác biệt chính giữa yến tinh chế 1 lớp và 2 lớp là độ dày tai yến, lượng sợi khi chưng và giá. Bảng dưới so sánh theo bảng giá website Việt Cường Nhân.</p>
  <table><thead><tr><th>Tiêu chí</th><th>Yến tinh chế 1 lớp</th><th>Yến tinh chế 2 lớp</th></tr></thead><tbody>
  <tr><td>Cách đắp</td><td>Một lớp sợi mỏng, đan đều</td><td>Hai lớp sợi chồng lên</td></tr>
  <tr><td>Hình dạng tai</td><td>Mỏng, nhẹ</td><td>Dày, chắc tay</td></tr>
  <tr><td>Khi chưng</td><td>Sợi mềm, chén yến vừa</td><td>Nhiều sợi hơn, chén yến đặc</td></tr>
  <tr><td>Ngâm</td><td>30–60 phút</td><td>30–60 phút, có thể lâu hơn chút vì tai dày</td></tr>
  <tr><td>Chưng cách thủy</td><td>20–30 phút</td><td>20–30 phút</td></tr>
  <tr><td>Hợp với</td><td>Dùng hằng ngày, chia phần dễ</td><td>Thích chén yến đặc sợi, biếu tặng</td></tr>
  <tr><td>Giá 100gr</td><td>{gia(109)} – {gia(110)}</td><td>{gia(112)}</td></tr>
  </tbody></table>
  <p>Đây là mức ngâm, chưng tham khảo; tai dày hoặc yến khô hơn thì ngâm lâu hơn. Nếu chưng quá lâu sợi dễ tan, xem bài <a href="yen-bi-chay-nuoc-khi-chung.html">vì sao yến bị chảy nước khi chưng</a>.</p>

  <h2>Yến 1 lớp sợi vừa, 10 tai và 18–20 tai khác nhau thế nào?</h2>
  <p>Trong nhóm 1 lớp, Việt Cường Nhân có ba loại: sợi vừa, 10 tai và 18–20 tai. "10 tai" hay "18–20 tai" là số tai yến trong 100gr, nên số tai càng nhiều thì mỗi tai càng nhỏ.</p>
  <table><thead><tr><th>Loại</th><th>Số tai / 100gr</th><th>Mỗi tai khoảng</th><th>Giá 100gr</th><th>Hợp với</th></tr></thead><tbody>
  <tr><td>{P[109][2]}</td><td>Không cố định</td><td>Tùy tai</td><td>{gia(109)}</td><td>Dùng đều trong gia đình, giá mềm nhất nhóm</td></tr>
  <tr><td>{P[110][2]}</td><td>10 tai</td><td>khoảng 10 g, chia được 2 chén</td><td>{gia(110)}</td><td>Gia đình 2 người, tai to đẹp</td></tr>
  <tr><td>{P[111][2]}</td><td>18–20 tai</td><td>khoảng 5 g, đủ 1 chén</td><td>{gia(111)}</td><td>Người ăn một mình, khỏi cân</td></tr>
  </tbody></table>
  <p>Khối lượng mỗi tai là ước tính từ số tai trong 100gr, từng tai có thể chênh lệch một chút. Cách chia phần và số chén từ một hộp xem bài <a href="100gr-yen-chung-duoc-bao-nhieu-chen.html">100gr yến chưng được bao nhiêu chén</a>.</p>

  <h2>Yến 2 lớp có bổ hơn yến 1 lớp không?</h2>
  <p>Không. Yến 1 lớp và 2 lớp đều là sợi yến sạch, chỉ khác cách đắp khi định hình. Nếu dùng cùng một lượng yến khô, ví dụ 4 g mỗi chén, thì lượng yến bạn ăn là như nhau; yến 2 lớp chỉ cho cảm giác tai dày, sợi nhiều và đẹp hơn khi nhìn.</p>
  <p>Giá yến 2 lớp cao hơn chủ yếu vì tốn công đắp hai lớp sợi và hình thức đẹp hơn, không phải vì công dụng khác.</p>

  <h2>Nên mua yến tinh chế 1 lớp hay 2 lớp?</h2>
  <p>Chọn theo cách dùng và ngân sách:</p>
  <ul>
    <li><b>Dùng hằng ngày, muốn tiết kiệm:</b> {P[109][2]}.</li>
    <li><b>Ăn một mình, không muốn cân:</b> {P[111][2]}, mỗi tai khoảng một chén.</li>
    <li><b>Hai người cùng ăn:</b> {P[110][2]}, mỗi tai chia đôi.</li>
    <li><b>Thích chén yến đặc sợi, hoặc biếu tặng:</b> {P[112][2]}.</li>
    <li><b>Biếu trang trọng, muốn sợi dài nhất:</b> cân nhắc yến rút lông, xem bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông</a>.</li>
  </ul>
  <p>Chưa biết chọn nhóm nào, xem bài <a href="yen-sao-loai-nao-tot.html">yến sào loại nào tốt</a>.</p>

  <h2>Cách chưng yến tinh chế 1 lớp và 2 lớp</h2>
  <p>Hai loại chưng giống nhau: ngâm cho nở mềm, xé tơi theo thớ sợi, chưng cách thủy lửa nhỏ, thêm đường phèn ở cuối.</p>
  <ol>
    <li>Ngâm yến trong nước sạch 30–60 phút; tai 2 lớp dày nên kiểm tra phần giữa đã mềm chưa.</li>
    <li>Vớt qua rây, xé tơi theo thớ sợi.</li>
    <li>Cho yến với 150–200 ml nước mỗi chén vào thố, chưng cách thủy lửa nhỏ 20–30 phút.</li>
    <li>Thêm đường phèn ở 5 phút cuối, khuấy nhẹ rồi tắt bếp.</li>
  </ol>
  <p>Các bước chi tiết xem bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Bảng giá yến tinh chế tại Việt Cường Nhân</h2>
  <p>Giá lấy từ bảng giá website, chưa gồm phí giao hàng. Yến được nhặt lông tại xưởng đạt HACCP, ISO 22000:2018 và GMP.</p>
""" + ul(li(109, "Sợi vừa, dùng hằng ngày."), li(110, "Tai to, khoảng 10 g mỗi tai."), li(111, "Tai nhỏ, khoảng 5 g mỗi tai."), li(112, "Hai lớp sợi, tai dày.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Yến tinh chế 1 lớp và 2 lớp khác nhau thế nào?", "Khác nhau ở cách đắp sợi khi định hình: 1 lớp đắp một lớp sợi mỏng, 2 lớp đắp hai lớp sợi chồng lên nên tai dày hơn, chén yến nhiều sợi hơn và giá cao hơn."),
       ("Yến 2 lớp có bổ hơn yến 1 lớp không?", "Không. Cả hai đều là sợi yến sạch; nếu dùng cùng số gam yến khô mỗi chén thì lượng yến ăn vào như nhau."),
       ("Yến 18–20 tai là gì?", "Là yến tinh chế 1 lớp có khoảng 18–20 tai trong 100gr, mỗi tai khoảng 5 g, đủ cho một chén mà không cần cân."),
       ("Yến 10 tai là gì?", "Là yến tinh chế 1 lớp có khoảng 10 tai trong 100gr, mỗi tai khoảng 10 g, có thể chia đôi cho 2 chén."),
       ("Nên mua yến tinh chế 1 lớp hay 2 lớp?", "Dùng hằng ngày, muốn tiết kiệm thì chọn 1 lớp sợi vừa; thích chén yến đặc sợi hoặc mua biếu thì chọn 2 lớp.")]),
dict(slug="yen-rut-long-kho-la-gi", cat="Yến sào", ngay="2026-11-07",
  tu_khoa="yến rút lông khô, yến rút lông khô là gì, yến rút lông là gì, vì sao yến rút lông khô giá cao, yến rút lông đắp tổ định hình",
  h1="Yến rút lông khô là gì, vì sao giá cao?",
  desc="Yến rút lông khô là gì? Là tổ yến nhặt lông khi tổ còn khô, giữ nguyên sợi và dáng tổ, rất tốn công nên giá cao. So sánh các loại yến rút lông, giá 100gr.",
  lede="Yến rút lông khô là tổ yến được nhặt lông thủ công khi tổ còn khô hoặc gần như khô, không ngâm nở rồi xé tơi như yến tinh chế, nên giữ được sợi yến dài, nguyên và dáng tổ tự nhiên. Vì công nhặt rất chậm và tỉ mỉ, đây là loại yến có giá cao nhất trong nhóm yến đã làm sạch.",
  tom_tat=["Yến rút lông khô: nhặt lông khi tổ còn khô, giữ sợi nguyên và dáng tổ, không ngâm tơi rồi đắp lại.",
           "Giá cao vì công nhặt thủ công rất chậm, sợi giữ dài và tổ đẹp; không phải vì công dụng khác các loại yến sạch khác.",
           f"Giá 100gr tại Việt Cường Nhân: {P[116][2]} {gia(116)}, {P[117][2]} {gia(117)}, {P[115][2]} {gia(115)}, {P[114][2]} {gia(114)}, {P[113][2]} {gia(113)}.",
           "Yến rút lông khô thường cần ngâm lâu hơn yến tinh chế vì sợi dày, tổ chắc; chưng cách thủy khoảng 20–30 phút.",
           "Hợp làm quà biếu trang trọng hoặc người thích chén yến sợi dài, dai; dùng hằng ngày thì yến tinh chế đã đủ."],
  body=f"""  <h2>Yến rút lông khô là gì?</h2>
  <p>Yến rút lông khô là tổ yến được làm sạch bằng cách dùng nhíp rút từng sợi lông khi tổ còn khô hoặc chỉ hơi ẩm, thay vì ngâm cho tổ nở hẳn, xé tơi rồi đắp lại thành tai như yến tinh chế. Nhờ vậy sợi yến giữ được độ dài, độ dày và tổ còn gần như nguyên dáng ban đầu.</p>
  <p>Ở xưởng Việt Cường Nhân, khách xem tận nơi thường thấy rõ khác biệt: tổ rút lông khô nhìn như tổ yến mới lấy từ nhà yến nhưng đã sạch lông, còn yến tinh chế là các tai yến đều nhau được định hình lại.</p>

  <h2>Vì sao yến rút lông khô giá cao?</h2>
  <p>Yến rút lông khô có giá cao chủ yếu vì công làm sạch. Khi tổ còn khô, sợi lông bám chặt và khó thấy hơn, thợ phải gắp từng sợi rất chậm để không làm gãy sợi yến hay vỡ dáng tổ.</p>
  <ul>
    <li><b>Công nhặt thủ công lâu:</b> mỗi tổ cần nhiều thời gian hơn so với nhặt lông yến đã ngâm nở.</li>
    <li><b>Giữ sợi dài, nguyên:</b> sợi không bị đứt vụn trong quá trình ngâm, xé tơi.</li>
    <li><b>Giữ dáng tổ đẹp:</b> hợp làm quà biếu, nhìn rõ là tổ yến tự nhiên.</li>
    <li><b>Chọn tổ đẹp:</b> chỉ những tổ có dáng và sợi tốt mới được làm theo cách này.</li>
  </ul>
  <p>Giá cao phản ánh công làm và hình thức, không có nghĩa yến rút lông khô bổ hơn các loại yến sạch khác khi dùng cùng số gam yến khô. Các yếu tố làm giá yến chênh lệch xem bài <a href="gia-yen-sao-bao-nhieu-tien.html">giá yến sào bao nhiêu tiền 100gr</a>.</p>

  <h2>Các loại yến rút lông khác nhau thế nào?</h2>
  <p>Trong nhóm yến rút lông, cách gọi phản ánh hình dạng thành phẩm sau khi nhặt lông. Cách gọi có thể khác nhau giữa các nơi bán, nên khi mua hãy hỏi rõ người bán. Dưới đây là cách hiểu thường gặp và giá theo bảng giá website Việt Cường Nhân:</p>
  <table><thead><tr><th>Loại</th><th>Thường hiểu là</th><th>Giá 100gr</th></tr></thead><tbody>
  <tr><td>{P[113][2]}</td><td>Sợi yến rút lông được đắp lại thành tổ</td><td>{gia(113)}</td></tr>
  <tr><td>{P[114][2]}</td><td>Rút lông rồi định hình lại dáng tổ đẹp, đều</td><td>{gia(114)}</td></tr>
  <tr><td>{P[115][2]}</td><td>Rút lông, giữ phần khung (xương) tổ, sợi dày</td><td>{gia(115)}</td></tr>
  <tr><td>{P[117][2]}</td><td>Rút lông khô, ép thành miếng gọn</td><td>{gia(117)}</td></tr>
  <tr><td>{P[116][2]}</td><td>Rút lông khi tổ còn khô, gần như nguyên tổ</td><td>{gia(116)}</td></tr>
  </tbody></table>
  <p>Khác biệt giữa yến thô, yến tinh chế và yến rút lông xem bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>.</p>

  <h2>So sánh yến rút lông khô và yến tinh chế</h2>
  <table><thead><tr><th>Tiêu chí</th><th>Yến rút lông khô</th><th>Yến tinh chế 1 lớp sợi vừa</th></tr></thead><tbody>
  <tr><td>Cách làm sạch</td><td>Nhặt lông khi tổ còn khô</td><td>Ngâm nở, nhặt lông, đắp lại thành tai</td></tr>
  <tr><td>Hình dạng</td><td>Gần như nguyên tổ</td><td>Tai yến đều, định hình</td></tr>
  <tr><td>Sợi yến</td><td>Dài, dày, nguyên</td><td>Sợi vừa, đan đều</td></tr>
  <tr><td>Ngâm</td><td>Thường lâu hơn, đến khi sợi mềm</td><td>30–60 phút</td></tr>
  <tr><td>Chưng cách thủy</td><td>20–30 phút</td><td>20–30 phút</td></tr>
  <tr><td>Hợp với</td><td>Biếu trang trọng, thích sợi dai</td><td>Dùng hằng ngày</td></tr>
  <tr><td>Giá 100gr</td><td>{gia(116)}</td><td>{gia(109)}</td></tr>
  </tbody></table>
  <p>So sánh trong nhóm yến tinh chế xem bài <a href="yen-tinh-che-1-lop-va-2-lop.html">yến tinh chế 1 lớp và 2 lớp</a>.</p>

  <h2>Cách ngâm và chưng yến rút lông khô</h2>
  <p>Yến rút lông khô có sợi dày và tổ chắc, nên thường cần ngâm lâu hơn yến tinh chế; ngâm đến khi tổ mềm, sợi tơi ra là được, không cần đúng một con số.</p>
  <ol>
    <li><b>Tách phần dùng:</b> bẻ nhẹ một phần tổ, khoảng 3–5 g cho một chén.</li>
    <li><b>Ngâm nước sạch:</b> nhiệt độ thường, đến khi sợi nở mềm; kiểm tra phần dày ở giữa tổ.</li>
    <li><b>Xé tơi theo thớ sợi:</b> nhẹ tay để giữ sợi dài.</li>
    <li><b>Kiểm tra lại:</b> soi dưới đèn, nhặt sợi lông nhỏ còn sót nếu có.</li>
    <li><b>Chưng cách thủy:</b> 150–200 ml nước mỗi chén, lửa nhỏ, khoảng 20–30 phút; đường phèn cho ở 5 phút cuối.</li>
  </ol>
  <p>Các bước chưng xem bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>; tránh chưng quá lâu làm tan sợi, xem bài <a href="yen-bi-chay-nuoc-khi-chung.html">vì sao yến bị chảy nước khi chưng</a>.</p>

  <h2>Có nên mua yến rút lông khô không?</h2>
  <p>Nên mua yến rút lông khô khi bạn muốn quà biếu trang trọng, người nhận thích tổ yến nhìn tự nhiên, hoặc bạn thích chén yến sợi dài và dai. Nếu chỉ dùng hằng tuần trong gia đình, yến tinh chế 1 lớp sợi vừa tiết kiệm hơn nhiều mà lượng yến mỗi chén vẫn như nhau.</p>
  <ul>
    <li><b>Biếu tặng:</b> {P[116][2]} hoặc {P[114][2]}.</li>
    <li><b>Thích sợi dày, dai, giá mềm hơn trong nhóm:</b> {P[113][2]}.</li>
    <li><b>Dùng hằng ngày:</b> yến tinh chế, xem bài <a href="yen-sao-loai-nao-tot.html">yến sào loại nào tốt</a>.</li>
  </ul>

  <h2>Bảng giá yến rút lông tại Việt Cường Nhân</h2>
  <p>Yến rút lông của Việt Cường Nhân được nhặt lông thủ công tại xưởng, nhà máy đạt HACCP, ISO 22000:2018 và GMP. Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(113), li(114), li(115), li(117), li(116)) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>; quà Tết có yến rút lông xem bài <a href="qua-tet-yen-sao.html">quà Tết yến sào</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Yến rút lông khô là gì?", "Là tổ yến được nhặt lông thủ công khi tổ còn khô hoặc gần như khô, không ngâm tơi rồi đắp lại, nên giữ sợi dài và dáng tổ gần như nguyên."),
       ("Vì sao yến rút lông khô đắt?", "Vì nhặt lông khi tổ còn khô rất chậm và tỉ mỉ, lại giữ được sợi dài, tổ đẹp. Giá cao phản ánh công làm và hình thức, không phải công dụng khác."),
       ("Yến rút lông khô có bổ hơn yến tinh chế không?", "Không có căn cứ để nói như vậy. Cùng số gam yến khô mỗi chén thì lượng yến như nhau; khác biệt là sợi dài, dai và tổ đẹp hơn."),
       ("Yến rút lông khô ngâm bao lâu?", "Thường lâu hơn yến tinh chế vì sợi dày, tổ chắc. Ngâm đến khi sợi mềm và tơi ra, sau đó chưng cách thủy khoảng 20–30 phút."),
       ("Yến rút lông khô giá bao nhiêu?", f"Tại Việt Cường Nhân, {P[116][2]} giá {gia(116)}/100gr, chưa gồm phí giao hàng.")]),
dict(slug="dong-trung-ha-thao-loai-cay-va-loai-gay", cat="Đông trùng hạ thảo", ngay="2026-11-17",
  tu_khoa="đông trùng hạ thảo loại cây, đông trùng hạ thảo loại gãy, đông trùng loại cây và loại gãy khác nhau, nên mua đông trùng loại nào",
  h1="Đông trùng hạ thảo loại cây và loại gãy: chọn loại nào?",
  desc="Đông trùng hạ thảo loại cây và loại gãy khác ở độ dài, hình thức và giá, vị gần như nhau. So sánh, giá 100gr và nên chọn loại nào để nấu ăn, pha trà, biếu.",
  lede="Đông trùng hạ thảo loại cây là nấm sấy khô còn nguyên cọng dài, đều, đẹp; loại gãy là những cọng bị gãy ngắn trong lúc thu hái, sấy và đóng gói. Hai loại cùng một nguồn nấm, vị gần như nhau, khác chủ yếu ở hình thức và giá, nên nấu ăn hằng ngày chọn loại gãy, biếu tặng hoặc đãi khách chọn loại cây.",
  tom_tat=["Loại cây: cọng nguyên, dài đều, màu cam đẹp; loại gãy: cọng ngắn, gãy trong lúc thu hái, sấy, đóng gói.",
           "Cùng một nguồn nấm nên vị gần như nhau; khác biệt chính là hình thức và giá.",
           f"Giá tại Việt Cường Nhân: {P[136][2]} {gia(136)}/100gr, {gia(137)}/50gr; {P[138][2]} {gia(138)}/100gr.",
           "Nấu canh, tiềm, chưng yến hằng ngày: loại gãy tiết kiệm; pha trà, đãi khách, biếu tặng: loại cây.",
           "Cả hai bảo quản giống nhau: hũ, túi kín, nơi khô mát, đậy kín ngay sau khi lấy."],
  body=f"""  <h2>Đông trùng hạ thảo loại cây là gì?</h2>
  <p>Đông trùng hạ thảo loại cây là nấm đông trùng hạ thảo sấy khô còn nguyên cọng, dài và tương đối đều, màu cam tươi. Sau khi sấy, những cọng đẹp, nguyên vẹn được chọn riêng để đóng gói thành loại cây.</p>
  <p>Nấm đông trùng hạ thảo bán ở Việt Cường Nhân là loại nuôi trồng, do công ty bắt đầu nuôi trồng từ năm 2022. Loại cây thường được chọn khi cần hình thức đẹp, như pha trà nhìn rõ từng cọng nấm hay làm quà biếu.</p>

  <h2>Đông trùng hạ thảo loại gãy là gì?</h2>
  <p>Đông trùng hạ thảo loại gãy là những cọng nấm bị gãy ngắn trong quá trình thu hái, sấy khô và phân loại. Nấm vẫn cùng nguồn, cùng cách sấy như loại cây, chỉ là cọng không còn nguyên nên được bán riêng với giá mềm hơn.</p>
  <p>Ở xưởng, khách mua để nấu ăn trong gia đình thường chọn loại gãy, vì khi cho vào nồi canh hay thố chưng thì độ dài cọng không còn quan trọng.</p>

  <h2>So sánh đông trùng hạ thảo loại cây và loại gãy</h2>
  <p>Hai loại khác nhau chủ yếu ở độ dài cọng, hình thức và giá. Bảng dưới so sánh theo bảng giá website Việt Cường Nhân.</p>
  <table><thead><tr><th>Tiêu chí</th><th>Loại cây</th><th>Loại gãy</th></tr></thead><tbody>
  <tr><td>Hình dạng</td><td>Cọng nguyên, dài, đều</td><td>Cọng ngắn, gãy, không đều</td></tr>
  <tr><td>Màu sắc</td><td>Cam tươi</td><td>Cam, tương tự loại cây</td></tr>
  <tr><td>Nguồn nấm, cách sấy</td><td>Như nhau</td><td>Như nhau</td></tr>
  <tr><td>Vị khi nấu</td><td>Ngọt nhẹ, thơm</td><td>Gần như loại cây</td></tr>
  <tr><td>Hợp với</td><td>Pha trà, đãi khách, biếu tặng</td><td>Nấu canh, tiềm, chưng yến hằng ngày</td></tr>
  <tr><td>Giá</td><td>{gia(136)}/100gr, {gia(137)}/50gr</td><td>{gia(138)}/100gr</td></tr>
  </tbody></table>

  <h2>Đông trùng loại gãy có kém hơn loại cây không?</h2>
  <p>Không có căn cứ để nói loại gãy kém hơn loại cây về chất lượng khi cùng nguồn nấm và cách sấy. Loại gãy rẻ hơn vì hình thức không đẹp bằng, không phải vì là nấm khác. Khi nấu, cọng ngắn còn dễ chia lượng và nhanh mềm hơn.</p>
  <p>Điều quan trọng hơn chuyện cây hay gãy là nấm phải khô, màu cam tự nhiên, không ẩm mốc, không mùi lạ, và có nguồn gốc rõ ràng.</p>

  <h2>Nên chọn loại nào cho từng món?</h2>
  <table><thead><tr><th>Món, nhu cầu</th><th>Gợi ý</th><th>Ghi chú</th></tr></thead><tbody>
  <tr><td>Canh gà, canh sườn, hầm</td><td>Loại gãy</td><td>Cho vào 10–15 phút cuối</td></tr>
  <tr><td>Gà ác tiềm đông trùng</td><td>Loại gãy hoặc cây</td><td>Xem công thức bên dưới</td></tr>
  <tr><td>Chưng cùng yến</td><td>Loại gãy</td><td>Cho vào 5–10 phút cuối</td></tr>
  <tr><td>Pha trà</td><td>Loại cây</td><td>Nhìn đẹp trong ly thủy tinh</td></tr>
  <tr><td>Ngâm mật ong</td><td>Loại cây</td><td>Cọng nguyên đẹp trong hũ</td></tr>
  <tr><td>Biếu tặng, đãi khách</td><td>Loại cây</td><td>Hình thức đẹp</td></tr>
  </tbody></table>
  <p>Công thức chi tiết xem bài <a href="nam-dong-trung-ha-thao-tiem-ga-ac.html">nấm đông trùng hạ thảo tiềm gà ác</a> và <a href="yen-chung-dong-trung-ha-thao.html">yến chưng đông trùng hạ thảo</a>. Các cách dùng khác xem bài <a href="cach-dung-dong-trung-ha-thao.html">cách dùng nấm đông trùng hạ thảo sấy khô</a>.</p>

  <h2>Cách nhận biết đông trùng hạ thảo sấy khô chất lượng</h2>
  <ul>
    <li><b>Màu:</b> cam vàng đến cam đậm tự nhiên, không đỏ rực bất thường.</li>
    <li><b>Độ khô:</b> cọng giòn, bẻ gãy được, không dẻo ẩm.</li>
    <li><b>Mùi:</b> thơm nhẹ mùi nấm, không mốc, không chua.</li>
    <li><b>Bao bì:</b> có nhãn, khối lượng, ngày sản xuất, hạn dùng, thông tin cơ sở.</li>
  </ul>

  <h2>Bảo quản đông trùng hạ thảo sấy khô</h2>
  <p>Cả loại cây và loại gãy bảo quản như nhau: để trong hũ hoặc túi kín, nơi khô mát, tránh nắng; lấy bằng tay hoặc muỗng khô và đậy kín ngay để nấm không hút ẩm. Nấm bị mềm, có đốm mốc hoặc mùi lạ thì nên bỏ.</p>

  <h2>Lưu ý khi dùng</h2>
  <p>Nấm đông trùng hạ thảo là thực phẩm, dùng như một nguyên liệu trong món ăn, không thay thế thuốc. Trẻ nhỏ, phụ nữ mang thai, người có bệnh nền hoặc đang dùng thuốc nên hỏi bác sĩ trước khi dùng.</p>

  <h2>Đông trùng hạ thảo tại Việt Cường Nhân</h2>
  <p>Giá lấy từ bảng giá website Việt Cường Nhân, chưa gồm phí giao hàng:</p>
""" + ul(li(136, "Cọng nguyên, hợp pha trà, biếu tặng."), li(137, "Gói nhỏ, dùng thử."), li(138, "Cọng gãy, giá mềm, nấu ăn hằng ngày."), li(140, "Hũ nhỏ tiện dùng.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Đông trùng hạ thảo loại cây và loại gãy khác nhau thế nào?", "Loại cây còn nguyên cọng dài, đều, đẹp; loại gãy là cọng bị gãy ngắn trong lúc thu hái, sấy, đóng gói. Cùng nguồn nấm nên vị gần như nhau, khác chủ yếu ở hình thức và giá."),
       ("Đông trùng loại gãy có kém hơn loại cây không?", "Không có căn cứ để nói như vậy khi cùng nguồn nấm và cách sấy. Loại gãy rẻ hơn vì hình thức không đẹp bằng."),
       ("Nấu ăn nên dùng đông trùng loại nào?", "Nấu canh, tiềm, chưng yến hằng ngày nên dùng loại gãy cho tiết kiệm; pha trà, đãi khách hoặc biếu tặng thì chọn loại cây."),
       ("Đông trùng hạ thảo loại cây giá bao nhiêu?", f"Tại Việt Cường Nhân, {P[136][2]} giá {gia(136)}/100gr và {gia(137)}/50gr, chưa gồm phí giao hàng."),
       ("Đông trùng hạ thảo sấy khô bảo quản thế nào?", "Để hũ hoặc túi kín, nơi khô mát, tránh nắng; lấy bằng dụng cụ khô và đậy kín ngay sau khi dùng.")]),
dict(slug="dong-trung-ha-thao-ngam-mat-ong", cat="Đông trùng hạ thảo", ngay="2026-11-17",
  tu_khoa="đông trùng hạ thảo ngâm mật ong, cách ngâm đông trùng hạ thảo với mật ong, tỉ lệ đông trùng mật ong, đông trùng ngâm mật ong để được bao lâu",
  h1="Đông trùng hạ thảo ngâm mật ong: cách làm và bảo quản",
  desc="Cách làm đông trùng hạ thảo ngâm mật ong tại nhà: tỉ lệ 10–20g nấm khô cho 500ml mật ong, 5 bước làm, thời gian ngâm, cách dùng và bảo quản hũ ngâm đúng cách.",
  lede="Đông trùng hạ thảo ngâm mật ong làm rất đơn giản: dùng khoảng 10–20 g nấm đông trùng sấy khô cho 500 ml mật ong nguyên chất, cho vào hũ thủy tinh sạch, khô, đậy kín và ngâm 2–3 tuần là dùng được. Điều quyết định hũ ngâm ngon và không hỏng là nấm thật khô, hũ thật khô và mật ong không lẫn nước.",
  tom_tat=["Tỉ lệ gợi ý: 10–20 g đông trùng hạ thảo sấy khô cho 500 ml mật ong nguyên chất.",
           "Hũ thủy tinh tráng nước sôi, phơi hoặc sấy thật khô; nấm và dụng cụ cũng phải khô.",
           "Ngâm khoảng 2–3 tuần, nấm mềm và mật ong có màu cam nhạt là dùng được.",
           "Mỗi lần dùng 1–2 thìa cà phê pha với nước ấm dưới 60°C; không cho trẻ dưới 1 tuổi dùng mật ong.",
           f"Nên dùng {P[136][2]} cho hũ ngâm đẹp; giá {gia(136)}/100gr tại Việt Cường Nhân."],
  body=f"""  <h2>Chuẩn bị nguyên liệu và dụng cụ</h2>
  <p>Một hũ đông trùng hạ thảo ngâm mật ong cỡ 500 ml cần 10–20 g nấm đông trùng sấy khô và khoảng 500 ml mật ong nguyên chất. Lượng nấm ít hay nhiều tùy khẩu vị: 10 g cho vị nhẹ, 20 g cho hũ nhiều nấm, nhìn đầy đặn hơn.</p>
  <table><thead><tr><th>Nguyên liệu, dụng cụ</th><th>Định lượng</th><th>Ghi chú</th></tr></thead><tbody>
  <tr><td>Nấm đông trùng hạ thảo sấy khô</td><td>10–20 g</td><td>Loại cây cho hũ đẹp; loại gãy vẫn ngâm được</td></tr>
  <tr><td>Mật ong nguyên chất</td><td>500 ml (khoảng 650–700 g)</td><td>Mật sánh, không lẫn nước</td></tr>
  <tr><td>Hũ thủy tinh có nắp kín</td><td>1 hũ 600–700 ml</td><td>Chừa khoảng trống phía trên</td></tr>
  <tr><td>Đũa hoặc muỗng gỗ, thủy tinh</td><td>1 cái</td><td>Phải khô hoàn toàn</td></tr>
  </tbody></table>
  <p>Ở Việt Cường Nhân, khách ngâm mật ong thường chọn nấm loại cây vì cọng nguyên nổi lơ lửng trong mật nhìn rất đẹp, hợp để bày hoặc biếu. Nếu chỉ ngâm để nhà dùng, loại gãy cũng cho kết quả tương tự, chỉ khác hình thức. Xem thêm so sánh trong bài <a href="dong-trung-ha-thao-loai-cay-va-loai-gay.html">đông trùng hạ thảo loại cây và loại gãy</a>.</p>

  <h2>Cách làm đông trùng hạ thảo ngâm mật ong: 5 bước</h2>
  <ol>
    <li><b>Làm sạch hũ.</b> Rửa hũ và nắp, tráng nước sôi rồi úp ngược cho ráo, phơi nắng hoặc sấy cho thật khô. Hũ còn một giọt nước cũng có thể làm mật lên men.</li>
    <li><b>Kiểm tra nấm.</b> Nấm sấy khô phải giòn, màu cam tự nhiên, không mốc. Không rửa nấm khô bằng nước trước khi ngâm mật ong; nếu muốn làm sạch bụi, chỉ dùng khăn khô lau nhẹ hoặc lắc trong rổ.</li>
    <li><b>Cho nấm vào hũ.</b> Xếp 10–20 g nấm vào hũ. Muốn cọng nấm dựng đẹp thì cho một lớp mật ong mỏng trước rồi mới thả nấm.</li>
    <li><b>Rót mật ong.</b> Rót mật từ từ cho ngập nấm, chừa 2–3 cm phía trên miệng hũ. Dùng đũa khô ấn nhẹ cho nấm chìm và bọt khí thoát lên.</li>
    <li><b>Đậy kín và ngâm.</b> Đậy nắp, để nơi khô mát, tránh nắng. Mấy ngày đầu nấm nổi lên mặt là bình thường; có thể đảo nhẹ bằng đũa khô 1–2 lần mỗi tuần.</li>
  </ol>

  <h2>Ngâm bao lâu thì dùng được?</h2>
  <p>Đông trùng hạ thảo ngâm mật ong dùng được sau khoảng 2–3 tuần. Lúc đó nấm đã ngấm mật, mềm hơn, mật ong ngả màu cam nhạt và có mùi thơm nhẹ của nấm.</p>
  <p>Nếu cần dùng sớm, sau khoảng 1 tuần vẫn dùng được, chỉ là nấm chưa mềm và vị chưa hòa đều. Ngâm càng lâu nấm càng mềm, nhưng nên dùng hết hũ trong vài tháng để giữ hương vị.</p>

  <h2>Cách dùng đông trùng hạ thảo ngâm mật ong</h2>
  <ul>
    <li><b>Pha nước ấm:</b> 1–2 thìa cà phê mật ong kèm vài cọng nấm, pha với 150–200 ml nước ấm. Nước dưới khoảng 60°C để giữ mùi mật ong.</li>
    <li><b>Ăn trực tiếp:</b> nhai luôn cọng nấm đã ngấm mật, vị ngọt dịu, hơi dai.</li>
    <li><b>Pha cùng trà:</b> thêm vào trà gừng, trà chanh hoặc trà táo đỏ để tạo vị ngọt.</li>
    <li><b>Dùng với món tráng miệng:</b> rưới lên sữa chua, bánh, hoặc chè.</li>
  </ul>
  <p>Ngoài ngâm mật ong, nấm đông trùng còn hợp nấu canh, tiềm gà, chưng yến; xem bài <a href="cach-dung-dong-trung-ha-thao.html">cách dùng nấm đông trùng hạ thảo sấy khô</a> và <a href="yen-chung-dong-trung-ha-thao.html">yến chưng đông trùng hạ thảo</a>.</p>

  <h2>Bảo quản hũ đông trùng ngâm mật ong</h2>
  <p>Hũ đông trùng ngâm mật ong bảo quản ở nhiệt độ phòng, nơi khô mát, tránh nắng là được, không cần để tủ lạnh. Tủ lạnh làm mật ong đặc và kết tinh, khó múc hơn.</p>
  <ul>
    <li>Luôn dùng muỗng khô, sạch để lấy; không chấm muỗng đã dùng vào hũ.</li>
    <li>Đậy nắp kín ngay sau mỗi lần lấy để mật không hút ẩm.</li>
    <li>Mật ong kết tinh (đóng đường) là hiện tượng tự nhiên, không phải hỏng.</li>
  </ul>

  <h2>Dấu hiệu hũ ngâm bị hỏng</h2>
  <p>Hũ đông trùng ngâm mật ong bị hỏng khi có mùi chua như men rượu, sủi bọt liên tục, nổi váng hoặc có đốm mốc trên nấm. Nguyên nhân thường gặp là hũ hoặc nấm còn ẩm, mật ong bị pha nước, hoặc dùng muỗng ướt. Khi thấy các dấu hiệu này nên bỏ cả hũ, không cố dùng.</p>
  <table><thead><tr><th>Hiện tượng</th><th>Bình thường hay không?</th><th>Cách xử lý</th></tr></thead><tbody>
  <tr><td>Nấm nổi lên mặt mấy ngày đầu</td><td>Bình thường</td><td>Ấn nhẹ bằng đũa khô</td></tr>
  <tr><td>Mật ngả màu cam</td><td>Bình thường</td><td>Màu từ nấm tan vào mật</td></tr>
  <tr><td>Mật đặc lại, có hạt đường</td><td>Bình thường</td><td>Ngâm hũ vào nước ấm cho tan</td></tr>
  <tr><td>Mùi chua, sủi bọt, có váng</td><td>Hỏng</td><td>Bỏ cả hũ</td></tr>
  </tbody></table>

  <h2>Lưu ý khi dùng</h2>
  <p>Đông trùng hạ thảo ngâm mật ong là món ăn, thức uống trong gia đình, không phải thuốc và không thay thế thuốc chữa bệnh. Không cho trẻ dưới 1 tuổi dùng mật ong. Người đang mang thai, người có bệnh nền như tiểu đường, hoặc đang dùng thuốc nên hỏi bác sĩ trước khi dùng.</p>

  <h2>Mua đông trùng hạ thảo để ngâm mật ong</h2>
  <p>Giá lấy từ bảng giá website Việt Cường Nhân, chưa gồm phí giao hàng:</p>
""" + ul(li(136, "Cọng nguyên, ngâm mật ong đẹp nhất."), li(141, "Vừa đủ cho 1 hũ ngâm 500 ml nhiều nấm."), li(140, "Hũ nhỏ, đủ 1 hũ ngâm vị nhẹ.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Ngâm đông trùng hạ thảo với mật ong theo tỉ lệ nào?", "Tỉ lệ gợi ý là 10–20 g nấm đông trùng sấy khô cho 500 ml mật ong nguyên chất. Dùng 10 g cho vị nhẹ, 20 g cho hũ nhiều nấm."),
       ("Đông trùng hạ thảo ngâm mật ong bao lâu thì dùng được?", "Khoảng 2–3 tuần là nấm ngấm mật, mềm và dùng ngon. Sau 1 tuần vẫn dùng được nhưng vị chưa hòa đều."),
       ("Có cần rửa đông trùng hạ thảo trước khi ngâm mật ong không?", "Không nên rửa nấm khô bằng nước vì hơi ẩm còn lại dễ làm mật ong lên men. Chỉ cần lau hoặc lắc nhẹ cho sạch bụi."),
       ("Đông trùng ngâm mật ong có cần để tủ lạnh không?", "Không cần. Để hũ kín nơi khô mát, tránh nắng; tủ lạnh làm mật đặc và kết tinh, khó múc."),
       ("Đông trùng hạ thảo ngâm mật ong bị chua có dùng được không?", "Không nên dùng. Mùi chua, sủi bọt hoặc có váng là dấu hiệu mật đã lên men do lẫn nước, nên bỏ cả hũ.")]),
dict(slug="bao-quan-dong-trung-ha-thao", cat="Đông trùng hạ thảo", ngay="2026-11-17",
  tu_khoa="bảo quản đông trùng hạ thảo, bảo quản đông trùng hạ thảo sấy khô, bảo quản đông trùng hạ thảo tươi, đông trùng hạ thảo để được bao lâu",
  h1="Bảo quản đông trùng hạ thảo sấy khô và tươi đúng cách",
  desc="Bảo quản đông trùng hạ thảo sấy khô trong hũ kín nơi khô mát, đông trùng tươi trong ngăn mát tủ lạnh. Cách làm, thời gian dùng, dấu hiệu hỏng và lỗi hay gặp.",
  lede="Bảo quản đông trùng hạ thảo đúng cách tùy loại: nấm sấy khô để trong hũ hoặc túi kín, nơi khô mát, tránh nắng, có thể cho thêm gói hút ẩm; đông trùng tươi phải để ngăn mát tủ lạnh và dùng trong thời gian ghi trên nhãn. Kẻ thù lớn nhất của nấm khô là hơi ẩm, còn của nấm tươi là nhiệt độ cao.",
  tom_tat=["Nấm sấy khô: hũ thủy tinh hoặc túi zip kín, nơi khô mát, tránh nắng, tránh gần bếp.",
           "Nấm tươi: để ngăn mát tủ lạnh, không để ngăn đá trừ khi muốn trữ lâu, dùng theo hạn trên nhãn.",
           "Luôn lấy nấm bằng tay khô hoặc muỗng khô, đậy kín ngay sau khi lấy.",
           "Nấm khô bị mềm, có đốm mốc, mùi chua hoặc mùi lạ thì nên bỏ.",
           f"Hũ nhỏ {P[140][2]} ({gia(140)}) tiện dùng dần, ít bị hở khí hơn túi lớn mở nhiều lần."],
  body=f"""  <h2>Vì sao đông trùng hạ thảo dễ hỏng?</h2>
  <p>Đông trùng hạ thảo dễ hỏng chủ yếu vì hút ẩm. Nấm sấy khô rất xốp, để hở trong không khí ẩm của miền Nam vài ngày là có thể mềm lại, sau đó dễ mốc và đổi màu.</p>
  <p>Đông trùng tươi thì chứa nhiều nước nên để ở nhiệt độ phòng rất nhanh hỏng. Vì vậy hai loại có cách bảo quản khác nhau, không nên làm chung một cách.</p>

  <h2>Cách bảo quản đông trùng hạ thảo sấy khô</h2>
  <p>Đông trùng hạ thảo sấy khô bảo quản tốt nhất trong hũ thủy tinh hoặc túi zip kín, đặt nơi khô mát, tránh ánh nắng và tránh gần bếp, máy giặt hay nơi có hơi nước.</p>
  <ol>
    <li><b>Giữ bao bì gốc khi chưa mở.</b> Gói còn niêm phong thì để nguyên, nơi khô mát.</li>
    <li><b>Sau khi mở, chuyển sang hũ kín.</b> Hũ thủy tinh nắp vặn hoặc hũ nhựa thực phẩm có gioăng giữ khô tốt hơn túi bị gập miệng.</li>
    <li><b>Thêm gói hút ẩm thực phẩm.</b> Một gói hút ẩm loại dùng cho thực phẩm trong hũ giúp nấm giữ giòn lâu hơn.</li>
    <li><b>Lấy bằng dụng cụ khô.</b> Không dùng tay ướt hay muỗng vừa khuấy canh để lấy nấm.</li>
    <li><b>Đậy kín ngay.</b> Mỗi lần mở nắp lâu là một lần nấm hút ẩm.</li>
  </ol>
  <p>Mua túi lớn mà dùng ít, có thể chia nhỏ ra vài hũ, mỗi lần chỉ mở một hũ. Ở Việt Cường Nhân, khách dùng lẻ hằng ngày thường chọn hũ 10 g hoặc 20 g cho tiện.</p>

  <h3>Có nên để đông trùng sấy khô trong tủ lạnh?</h3>
  <p>Không bắt buộc. Nếu nhà rất ẩm hoặc không có chỗ khô mát, có thể để hũ đã đậy thật kín vào ngăn mát. Khi lấy ra dùng, mở nhanh, lấy xong đậy lại và cất ngay, để tránh hơi nước đọng trên nấm lạnh.</p>

  <h2>Cách bảo quản đông trùng hạ thảo tươi</h2>
  <p>Đông trùng hạ thảo tươi phải bảo quản trong ngăn mát tủ lạnh, giữ nguyên hũ hoặc hộp đựng, và dùng trong thời gian ghi trên nhãn sản phẩm.</p>
  <ul>
    <li>Để ngăn mát, không để cửa tủ là nơi nhiệt độ thay đổi nhiều.</li>
    <li>Không rửa nấm trước khi cất; chỉ rửa nhẹ ngay trước khi nấu.</li>
    <li>Đã mở hộp thì đậy kín, ưu tiên dùng sớm.</li>
    <li>Muốn trữ lâu hơn, có thể chia phần nhỏ vào túi kín và để ngăn đá; khi nấu cho thẳng vào nồi, không cần rã đông lâu.</li>
  </ul>

  <h2>So sánh bảo quản đông trùng sấy khô và đông trùng tươi</h2>
  <table><thead><tr><th>Tiêu chí</th><th>Đông trùng sấy khô</th><th>Đông trùng tươi</th></tr></thead><tbody>
  <tr><td>Nơi cất</td><td>Hũ, túi kín, nơi khô mát</td><td>Ngăn mát tủ lạnh</td></tr>
  <tr><td>Kẻ thù chính</td><td>Hơi ẩm</td><td>Nhiệt độ cao</td></tr>
  <tr><td>Thời gian dùng</td><td>Theo hạn trên bao bì, đậy kín thì giữ được lâu</td><td>Ngắn, dùng theo hạn trên nhãn</td></tr>
  <tr><td>Có rửa trước khi cất?</td><td>Không</td><td>Không, rửa ngay trước khi nấu</td></tr>
  <tr><td>Hợp với</td><td>Pha trà, ngâm mật ong, nấu canh, chưng yến</td><td>Xào, nấu canh, lẩu</td></tr>
  </tbody></table>

  <h2>Dấu hiệu đông trùng hạ thảo bị hỏng</h2>
  <p>Đông trùng hạ thảo bị hỏng khi có đốm mốc trắng hoặc xanh, mùi chua, mùi hôi hoặc mùi lạ, màu chuyển xỉn đen bất thường. Riêng nấm khô bị mềm dẻo là dấu hiệu đã hút ẩm; nếu chưa có mốc, mùi lạ thì nên dùng sớm và cất lại cho kín.</p>
  <p>Nấm đã mốc thì bỏ cả phần nấm trong hũ, không nhặt riêng cọng mốc ra để dùng tiếp, vì mốc có thể đã lan dù chưa nhìn thấy.</p>

  <h2>Những lỗi bảo quản hay gặp</h2>
  <ul>
    <li><b>Để túi mở miệng, chỉ gập lại:</b> nấm hút ẩm rất nhanh.</li>
    <li><b>Cất gần bếp hoặc cửa sổ nắng:</b> nóng và ẩm làm nấm mau đổi màu.</li>
    <li><b>Dùng muỗng ướt:</b> mang hơi nước vào hũ, dễ mốc.</li>
    <li><b>Để đông trùng tươi ngoài nhiệt độ phòng:</b> rất nhanh hỏng.</li>
  </ul>
  <p>Cách bảo quản yến sào cũng có nhiều điểm giống, xem bài <a href="bao-quan-yen-sao.html">cách bảo quản yến sào khô và yến đã chưng</a>. Cách dùng nấm trong món ăn xem bài <a href="cach-dung-dong-trung-ha-thao.html">cách dùng nấm đông trùng hạ thảo sấy khô</a> và <a href="dong-trung-ha-thao-ngam-mat-ong.html">đông trùng hạ thảo ngâm mật ong</a>.</p>

  <h2>Lưu ý khi dùng</h2>
  <p>Nấm đông trùng hạ thảo là thực phẩm, không phải thuốc và không thay thế thuốc chữa bệnh. Trẻ nhỏ, phụ nữ mang thai, người có bệnh nền hoặc đang dùng thuốc nên hỏi bác sĩ trước khi dùng.</p>

  <h2>Đông trùng hạ thảo tại Việt Cường Nhân</h2>
  <p>Giá lấy từ bảng giá website Việt Cường Nhân, chưa gồm phí giao hàng:</p>
""" + ul(li(136, "Nấm sấy khô cọng nguyên."), li(140, "Hũ nhỏ, tiện dùng dần, ít mở nhiều lần."), li(139, "Nấm tươi, bảo quản ngăn mát.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua số lượng lớn, mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Đông trùng hạ thảo sấy khô bảo quản thế nào?", "Để trong hũ hoặc túi zip kín, nơi khô mát, tránh nắng, có thể thêm gói hút ẩm thực phẩm. Lấy bằng dụng cụ khô và đậy kín ngay."),
       ("Đông trùng hạ thảo tươi để được bao lâu?", "Đông trùng tươi phải để ngăn mát tủ lạnh và dùng trong thời gian ghi trên nhãn sản phẩm. Muốn trữ lâu hơn có thể chia nhỏ để ngăn đá."),
       ("Có nên để đông trùng hạ thảo khô trong tủ lạnh không?", "Không bắt buộc. Nếu nhà ẩm có thể để hũ thật kín trong ngăn mát, lấy ra dùng nhanh rồi cất lại ngay."),
       ("Đông trùng hạ thảo bị mềm có dùng được không?", "Nấm khô bị mềm là đã hút ẩm. Nếu chưa có mốc hay mùi lạ thì nên dùng sớm; có mốc, mùi chua thì bỏ."),
       ("Làm sao biết đông trùng hạ thảo bị hỏng?", "Có đốm mốc, mùi chua hoặc mùi lạ, màu xỉn đen bất thường là nấm đã hỏng và nên bỏ.")]),

dict(slug="tao-do-tan-cuong-va-nhuoc-khuong", cat="Táo đỏ", ngay="2026-11-17",
  tu_khoa="táo đỏ Nhược Khương, táo đỏ Tân Cương và Nhược Khương, táo đỏ Nhược Khương là gì, nên mua táo đỏ loại nào",
  h1="Táo đỏ Tân Cương và táo đỏ Nhược Khương khác gì?",
  desc=f"Táo đỏ Nhược Khương khác táo đỏ Tân Cương size trung, size đại ở kích cỡ quả, độ dày cùi, món hợp và giá. Bảng so sánh, cách chọn và giá tại Việt Cường Nhân.",
  lede=f"Táo đỏ Nhược Khương là táo đỏ mang tên huyện Nhược Khương, một vùng trồng táo thuộc Tân Cương, nên hai loại không đối lập nhau mà khác chủ yếu ở giống, cỡ quả và giá. Ở Việt Cường Nhân, hộp 350gr táo đỏ Nhược Khương giá {gia(147)}, còn táo đỏ Tân Cương size đại hộp 350gr giá {gia(146)}.",
  tom_tat=["Nhược Khương là một huyện thuộc vùng Tân Cương, nên táo Nhược Khương cũng là táo đỏ vùng Tân Cương.",
           "Trên thị trường, “táo đỏ Tân Cương” thường chỉ loại quả to, cùi dày, chia size theo số quả mỗi kg.",
           "Táo đỏ Nhược Khương thường quả nhỏ hơn, hợp pha trà, nấu chè, hầm canh hằng ngày.",
           f"Giá hộp 350gr tại Việt Cường Nhân: Nhược Khương {gia(147)}, Tân Cương size trung {gia(145)}, size đại {gia(146)}.",
           "Biếu tặng hoặc ăn trực tiếp nên chọn Tân Cương size đại; nấu nướng dùng nhiều có thể chọn Nhược Khương cho tiết kiệm."],
  body=f"""  <h2>Táo đỏ Nhược Khương là gì?</h2>
  <p>Táo đỏ Nhược Khương là táo đỏ sấy khô được gọi theo tên huyện Nhược Khương, một huyện nằm ở phía đông nam vùng Tân Cương (Trung Quốc), nơi có nắng nhiều và khí hậu khô. Vì vậy, nói đúng thì táo Nhược Khương cũng là táo đỏ vùng Tân Cương.</p>
  <p>Khi bán ở Việt Nam, người ta tách hai tên gọi để khách dễ chọn: “táo đỏ Tân Cương” thường dùng cho loại quả to, chia size theo số quả mỗi kg; còn “táo đỏ Nhược Khương” dùng cho loại quả nhỏ hơn, giá mềm hơn. Khách hay hỏi Việt Cường Nhân hai loại này loại nào “thật” hơn, câu trả lời là cả hai đều là táo đỏ, chỉ khác giống và cỡ quả.</p>

  <h2>Táo đỏ Tân Cương và táo đỏ Nhược Khương khác nhau ở đâu?</h2>
  <p>Táo đỏ Tân Cương và táo đỏ Nhược Khương khác nhau chủ yếu ở kích cỡ quả, độ dày cùi, món hợp dùng và giá. Bảng dưới tóm tắt theo hàng Việt Cường Nhân đang bán:</p>
  <table><thead><tr><th>Tiêu chí</th><th>Táo đỏ Tân Cương (size trung, đại, thượng hạng)</th><th>Táo đỏ Nhược Khương</th></tr></thead><tbody>
  <tr><td>Vùng</td><td>Vùng Tân Cương</td><td>Huyện Nhược Khương, thuộc vùng Tân Cương</td></tr>
  <tr><td>Cỡ quả</td><td>To, chia size theo số quả mỗi kg (từ {P[144][3].split("(")[1].rstrip(")")} đến {P[142][3].split("(")[1].rstrip(")")})</td><td>Thường nhỏ hơn, không chia size</td></tr>
  <tr><td>Cùi</td><td>Dày, quả càng to cùi càng dày</td><td>Mỏng hơn, quả nhỏ gọn</td></tr>
  <tr><td>Hợp với</td><td>Ăn trực tiếp, biếu tặng, chưng yến, nấu chè</td><td>Pha trà, nấu chè, hầm canh, dùng nhiều mỗi ngày</td></tr>
  <tr><td>Giá hộp 350gr</td><td>{gia(145)} (size trung), {gia(146)} (size đại)</td><td>{gia(147)}</td></tr>
  </tbody></table>
  <p>Vị của hai loại đều ngọt tự nhiên của táo sấy. Độ ngọt, độ dẻo có thể khác nhau giữa các mẻ hàng, nên cách chắc nhất là nếm thử một hộp nhỏ trước khi mua số lượng lớn.</p>

  <h3>Size táo đỏ Tân Cương nghĩa là gì?</h3>
  <p>Size táo đỏ Tân Cương được tính theo số quả trong 1 kg: số quả càng ít thì quả càng to. Ở Việt Cường Nhân có ba size:</p>
""" + ul(li(142), li(143), li(144)) + f"""

  <h2>Nên chọn táo đỏ Tân Cương hay Nhược Khương?</h2>
  <p>Nên chọn táo đỏ theo món mình định làm: ăn trực tiếp và biếu tặng thì chọn Tân Cương size đại hoặc thượng hạng, còn nấu nướng hằng ngày thì táo Nhược Khương hoặc Tân Cương size trung là đủ.</p>
  <table><thead><tr><th>Nhu cầu</th><th>Gợi ý</th></tr></thead><tbody>
  <tr><td>Ăn trực tiếp như món ăn vặt</td><td>Tân Cương size đại hoặc thượng hạng, cùi dày, nhai thích</td></tr>
  <tr><td>Biếu tặng, làm giỏ quà</td><td>Tân Cương size thượng hạng 1kg, quả to đều</td></tr>
  <tr><td>Pha trà táo đỏ mỗi ngày</td><td>Nhược Khương hoặc Tân Cương size trung</td></tr>
  <tr><td>Chưng cùng yến sào</td><td>Tân Cương size trung hoặc size đại, 2–3 quả mỗi chén</td></tr>
  <tr><td>Hầm gà, nấu canh, nấu chè số lượng nhiều</td><td>Nhược Khương, tiết kiệm hơn</td></tr>
  </tbody></table>

  <h2>Cách chọn táo đỏ sấy khô ngon</h2>
  <p>Táo đỏ sấy khô ngon có vỏ đỏ sẫm bóng tự nhiên, quả căng hoặc nhăn nhẹ đều, cầm lên thấy khô ráo, bẻ ra cùi vàng, mùi thơm ngọt, không có mùi chua hay mùi mốc.</p>
  <ul>
    <li><b>Nhìn vỏ:</b> màu đỏ sẫm đều, không có đốm trắng, đốm xanh của mốc.</li>
    <li><b>Sờ quả:</b> khô, không dính tay, không ẩm mềm bất thường.</li>
    <li><b>Bẻ quả:</b> cùi không bị đen, không có sâu, hạt không bị mọt.</li>
    <li><b>Ngửi:</b> thơm mùi táo sấy; có mùi chua, mùi lạ là táo đã hút ẩm hoặc hỏng.</li>
    <li><b>Xem bao bì:</b> có nhãn, ngày đóng gói và hạn dùng rõ ràng.</li>
  </ul>

  <h2>Món ngon với từng loại táo đỏ</h2>
  <p>Cả táo đỏ Tân Cương và táo đỏ Nhược Khương đều dùng được cho trà, chè, chưng yến và món hầm; chỉ khác là quả to thì ít quả mà nhiều cùi, quả nhỏ thì cần nhiều quả hơn một chút.</p>
  <ul>
    <li><b>Trà táo đỏ:</b> 4–5 quả xẻ đôi, hãm nước sôi khoảng 10 phút, có thể thêm vài hạt kỷ tử.</li>
    <li><b>Yến chưng táo đỏ:</b> 2–3 quả táo thái lát cho vào thố cùng yến khi chưng cách thủy, xem <a href="yen-chung-tao-do-hat-sen.html">cách chưng yến táo đỏ hạt sen</a>.</li>
    <li><b>Gà ác tiềm:</b> 6–8 quả táo đỏ cho nước dùng ngọt thanh, xem <a href="nam-dong-trung-ha-thao-tiem-ga-ac.html">nấm đông trùng hạ thảo tiềm gà ác</a>.</li>
    <li><b>Ăn vặt:</b> táo size đại, thượng hạng ăn trực tiếp như mứt.</li>
  </ul>
  <p>Xem thêm cách chọn size và các món khác trong bài <a href="tao-do-tan-cuong-cach-chon-va-mon-ngon.html">táo đỏ Tân Cương: cách chọn size và món ngon</a>.</p>

  <h2>Bảo quản táo đỏ sấy khô</h2>
  <p>Táo đỏ sấy khô bảo quản trong túi hoặc hộp kín, nơi khô mát, tránh nắng; nhà ẩm thì để ngăn mát tủ lạnh. Hộp 350gr nhỏ gọn, mở ra dùng hết sớm nên ít bị hút ẩm hơn túi lớn để lâu.</p>
  <ul>
    <li>Đậy kín ngay sau khi lấy, dùng tay khô hoặc kẹp khô.</li>
    <li>Không để gần bếp, cửa sổ nắng hay nơi có hơi nước.</li>
    <li>Táo có đốm mốc, mùi chua thì bỏ, không dùng tiếp.</li>
  </ul>

  <h2>Lưu ý khi dùng</h2>
  <p>Táo đỏ là thực phẩm khô, không phải thuốc. Táo có vị ngọt tự nhiên khá đậm, người cần hạn chế đường, phụ nữ mang thai hoặc người có bệnh nền nên hỏi bác sĩ về lượng dùng phù hợp.</p>

  <h2>Giá táo đỏ tại Việt Cường Nhân</h2>
  <p>Việt Cường Nhân nhập khẩu và phân phối táo đỏ, bán cùng yến sào tại xưởng ở Dĩ An, Bình Dương. Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(147, "Quả nhỏ, giá mềm, hợp nấu nướng hằng ngày."), li(145), li(146), li(143, "Túi 1kg dùng cho gia đình hoặc quán.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Táo đỏ Nhược Khương có phải táo Tân Cương không?", "Có. Nhược Khương là một huyện thuộc vùng Tân Cương, nên táo Nhược Khương cũng là táo đỏ vùng Tân Cương. Trên thị trường tên “Nhược Khương” thường dùng cho loại quả nhỏ hơn, giá mềm hơn."),
       ("Táo đỏ Nhược Khương và Tân Cương loại nào ngon hơn?", "Không có loại nào ngon hơn tuyệt đối. Tân Cương size đại cùi dày, hợp ăn trực tiếp và biếu tặng; Nhược Khương quả nhỏ, hợp pha trà, nấu chè, hầm canh."),
       ("Táo đỏ Nhược Khương giá bao nhiêu?", f"Tại Việt Cường Nhân, táo đỏ Nhược Khương hộp 350gr giá {gia(147)}, chưa gồm phí giao hàng."),
       ("Pha trà táo đỏ nên dùng loại nào?", "Pha trà dùng táo Nhược Khương hoặc Tân Cương size trung là đủ, mỗi ấm 4–5 quả xẻ đôi, hãm khoảng 10 phút."),
       ("Táo đỏ sấy khô để được bao lâu?", "Táo đỏ để trong túi, hộp kín nơi khô mát dùng theo hạn trên bao bì. Nhà ẩm nên để ngăn mát tủ lạnh; có mốc hoặc mùi chua thì bỏ.")]),

dict(slug="tra-tao-do-ky-tu", cat="Món ngon", ngay="2026-11-17",
  tu_khoa="trà táo đỏ kỷ tử, cách pha trà táo đỏ kỷ tử, trà táo đỏ, trà táo đỏ kỷ tử gừng, trà táo đỏ kỷ tử hoa cúc",
  h1="Cách pha trà táo đỏ kỷ tử thơm ngon tại nhà",
  desc="Cách pha trà táo đỏ kỷ tử tại nhà: định lượng cho 1 ấm 500 ml, 5 bước hãm hoặc đun, 3 biến tấu gừng, hoa cúc, long nhãn và mẹo để trà thơm, ngọt thanh.",
  lede="Cách pha trà táo đỏ kỷ tử đơn giản nhất là xẻ đôi 5–6 quả táo đỏ, cho cùng 1 muỗng canh kỷ tử vào ấm, rót 500 ml nước sôi và hãm 10–15 phút. Muốn trà đậm vị táo hơn thì đun lửa nhỏ 10 phút rồi mới thêm kỷ tử.",
  tom_tat=["Định lượng cho 1 ấm 500 ml: 5–6 quả táo đỏ, 1 muỗng canh kỷ tử (khoảng 10 g), đường phèn hoặc mật ong tùy thích.",
           "Táo đỏ nên xẻ đôi hoặc khía dọc để vị ngọt ra nhanh; kỷ tử cho sau để không bị nát.",
           "Hãm nước sôi 10–15 phút, hoặc đun lửa nhỏ 10 phút cho vị táo đậm hơn.",
           "Có thể thêm 2–3 lát gừng, vài bông cúc khô hoặc long nhãn để đổi vị.",
           f"Táo đỏ Tân Cương size đại hộp 350gr tại Việt Cường Nhân giá {gia(146)}, đủ pha nhiều ấm trà."],
  body=f"""  <h2>Nguyên liệu pha trà táo đỏ kỷ tử</h2>
  <p>Trà táo đỏ kỷ tử chỉ cần ba thứ chính: táo đỏ sấy khô, kỷ tử và nước sôi. Định lượng dưới đây cho 1 ấm khoảng 500 ml, đủ 2–3 cốc.</p>
  <table><thead><tr><th>Nguyên liệu</th><th>Lượng cho 1 ấm 500 ml</th><th>Ghi chú</th></tr></thead><tbody>
  <tr><td>Táo đỏ sấy khô</td><td>5–6 quả size đại, hoặc 7–8 quả nhỏ</td><td>Rửa nhanh, xẻ đôi hoặc khía dọc</td></tr>
  <tr><td>Kỷ tử</td><td>1 muỗng canh, khoảng 10 g</td><td>Chọn hạt đỏ tươi, khô, không dính</td></tr>
  <tr><td>Nước</td><td>500 ml</td><td>Nước lọc đun sôi</td></tr>
  <tr><td>Đường phèn hoặc mật ong</td><td>Tùy thích, có thể bỏ</td><td>Táo đỏ đã có vị ngọt tự nhiên</td></tr>
  </tbody></table>
  <p>Ở Việt Cường Nhân, khách pha trà hằng ngày thường dùng táo đỏ Tân Cương size trung hoặc size đại; quả size đại cùi dày nên chỉ cần 5–6 quả là nước đã ngọt thanh. Muốn biết khác nhau giữa các loại táo, xem bài <a href="tao-do-tan-cuong-va-nhuoc-khuong.html">táo đỏ Tân Cương và táo đỏ Nhược Khương khác gì</a>.</p>

  <h2>Cách pha trà táo đỏ kỷ tử (hãm nước sôi)</h2>
  <p>Cách pha trà táo đỏ kỷ tử bằng hãm nước sôi mất khoảng 15 phút và hợp nhất cho người bận rộn.</p>
  <ol>
    <li><b>Rửa táo và kỷ tử.</b> Rửa nhanh táo đỏ dưới vòi nước, tráng kỷ tử qua một lần nước rồi để ráo. Không ngâm kỷ tử lâu vì hạt dễ nở nát.</li>
    <li><b>Xẻ táo.</b> Dùng dao xẻ đôi hoặc khía 2–3 đường dọc quả để vị ngọt tiết ra nhanh. Có thể bỏ hạt cho dễ uống.</li>
    <li><b>Tráng ấm.</b> Tráng ấm bằng nước sôi để giữ nhiệt khi hãm.</li>
    <li><b>Hãm trà.</b> Cho táo vào ấm, rót 500 ml nước sôi, đậy nắp 10 phút, sau đó thêm kỷ tử và hãm thêm 5 phút.</li>
    <li><b>Nêm vị.</b> Thêm đường phèn khi trà còn nóng, hoặc chờ trà nguội bớt dưới 60 độ mới cho mật ong để giữ mùi thơm.</li>
  </ol>

  <h2>Cách nấu trà táo đỏ kỷ tử đậm vị</h2>
  <p>Muốn trà táo đỏ kỷ tử đậm màu và đậm vị táo, nên đun táo với nước ở lửa nhỏ khoảng 10 phút thay vì chỉ hãm.</p>
  <ol>
    <li>Cho táo đã xẻ và 600 ml nước vào nồi nhỏ, đun sôi.</li>
    <li>Hạ lửa nhỏ, đun liu riu 10 phút cho nước chuyển màu vàng nâu.</li>
    <li>Thêm kỷ tử, đun thêm 2–3 phút rồi tắt bếp.</li>
    <li>Nêm đường phèn, rót ra cốc dùng nóng hoặc để nguội, thêm đá.</li>
  </ol>
  <p>Đun lâu nước sẽ bay hơi, nên cho dư khoảng 100 ml so với cách hãm để còn lại đủ 500 ml trà.</p>

  <h2>3 cách biến tấu trà táo đỏ kỷ tử</h2>
  <p>Trà táo đỏ kỷ tử dễ phối thêm nguyên liệu để đổi vị, mỗi cách chỉ cần thêm một thứ.</p>
  <h3>Trà táo đỏ kỷ tử gừng</h3>
  <p>Thêm 2–3 lát gừng tươi đập dập vào cùng lúc với táo. Trà có vị ấm cay nhẹ, hợp những ngày trời lạnh hoặc mưa.</p>
  <h3>Trà táo đỏ kỷ tử hoa cúc</h3>
  <p>Thêm 5–6 bông cúc khô ở bước cho kỷ tử, hãm 5 phút rồi vớt hoa ra để trà không bị đắng. Trà có mùi thơm hoa nhẹ, uống lạnh rất dễ chịu.</p>
  <h3>Trà táo đỏ kỷ tử long nhãn</h3>
  <p>Thêm 8–10 cùi long nhãn khô cùng lúc với táo. Long nhãn ngọt sẵn nên có thể bỏ đường.</p>

  <h2>Mẹo pha trà táo đỏ kỷ tử ngon</h2>
  <ul>
    <li><b>Xẻ táo là bắt buộc:</b> táo nguyên quả hãm 15 phút gần như chưa ra vị.</li>
    <li><b>Kỷ tử cho sau:</b> cho từ đầu hạt nát, nước đục.</li>
    <li><b>Không nêm quá ngọt:</b> nếm trước rồi mới thêm đường, vì táo đỏ đã ngọt tự nhiên.</li>
    <li><b>Ăn luôn cái:</b> táo và kỷ tử sau khi hãm vẫn mềm, ngọt, ăn được.</li>
    <li><b>Pha vừa đủ uống trong ngày:</b> trà để qua đêm ở nhiệt độ phòng dễ chua; dư thì cất ngăn mát và dùng trong ngày hôm sau.</li>
  </ul>

  <h2>Bảo quản táo đỏ và kỷ tử khô</h2>
  <p>Táo đỏ và kỷ tử khô đều sợ ẩm: để trong túi hoặc hũ kín, nơi khô mát, tránh nắng; nhà ẩm thì để ngăn mát tủ lạnh. Kỷ tử bị dính chùm, có mùi chua hoặc đốm mốc thì nên bỏ.</p>
  <p>Táo đỏ còn dùng được cho nhiều món khác như <a href="yen-chung-tao-do-hat-sen.html">yến chưng táo đỏ hạt sen</a> hay <a href="nam-dong-trung-ha-thao-tiem-ga-ac.html">đông trùng hạ thảo tiềm gà ác</a>. Cách chọn size táo xem bài <a href="tao-do-tan-cuong-cach-chon-va-mon-ngon.html">táo đỏ Tân Cương: cách chọn size và món ngon</a>.</p>

  <h2>Lưu ý khi uống trà táo đỏ kỷ tử</h2>
  <p>Trà táo đỏ kỷ tử là đồ uống thực phẩm, không phải thuốc và không thay thế thuốc chữa bệnh. Phụ nữ mang thai, người cần kiểm soát đường huyết, người có bệnh nền hoặc đang dùng thuốc nên hỏi bác sĩ trước khi uống thường xuyên. Không cho trẻ nhỏ ăn nguyên quả táo còn hạt để tránh hóc.</p>

  <h2>Mua táo đỏ pha trà tại Việt Cường Nhân</h2>
  <p>Việt Cường Nhân nhập khẩu và phân phối táo đỏ Tân Cương, bán cùng yến sào. Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(146, "Hộp nhỏ, tiện pha trà dần."), li(143, "Túi 1kg cho gia đình uống thường xuyên."), li(147, "Quả nhỏ, giá mềm, hợp pha trà, nấu chè.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Pha trà táo đỏ kỷ tử cần bao nhiêu quả táo?", "Một ấm 500 ml dùng 5–6 quả táo đỏ size đại hoặc 7–8 quả nhỏ, cùng khoảng 1 muỗng canh kỷ tử."),
       ("Hãm trà táo đỏ kỷ tử bao lâu?", "Hãm táo với nước sôi khoảng 10 phút, thêm kỷ tử rồi hãm thêm 5 phút. Muốn đậm vị hơn thì đun lửa nhỏ 10 phút."),
       ("Có cần bỏ hạt táo đỏ khi pha trà không?", "Không bắt buộc, chỉ cần xẻ đôi hoặc khía quả. Bỏ hạt giúp ăn cái dễ hơn, nhất là khi cho trẻ nhỏ ăn."),
       ("Trà táo đỏ kỷ tử để qua đêm được không?", "Không nên để qua đêm ở nhiệt độ phòng vì dễ chua. Pha dư thì cất ngăn mát, đậy kín và dùng trong ngày hôm sau."),
       ("Bà bầu uống trà táo đỏ kỷ tử được không?", "Phụ nữ mang thai nên hỏi bác sĩ trước khi uống thường xuyên, nhất là khi cần kiểm soát đường huyết.")]),

dict(slug="thach-nha-dam-lam-mon-gi", cat="Món ngon", ngay="2026-11-17",
  tu_khoa="thạch nha đam, thạch nha đam làm món gì, món ngon từ thạch nha đam, nha đam đường phèn, sữa chua nha đam",
  h1="Thạch nha đam làm món gì? 5 món giải nhiệt dễ làm",
  desc="Thạch nha đam làm được 5 món mát dễ làm: nha đam đường phèn, sữa chua nha đam, nước chanh nha đam hạt chia, chè nha đam táo đỏ, trà trái cây. Định lượng và mẹo.",
  lede="Thạch nha đam làm được nhiều món mát trong 5–15 phút: nha đam đường phèn, sữa chua nha đam, nước chanh nha đam hạt chia, chè nha đam táo đỏ và trà trái cây nha đam. Dùng thạch nha đam làm sẵn thì không phải gọt, ngâm hay trụng nha đam tươi.",
  tom_tat=["Thạch nha đam là phần thịt lá nha đam đã gọt, cắt hạt lựu và chế biến sẵn, vớt ra là dùng được.",
           "5 món dễ làm: nha đam đường phèn, sữa chua nha đam, nước chanh nha đam hạt chia, chè nha đam táo đỏ, trà trái cây nha đam.",
           "Mỗi ly thường dùng 2–3 muỗng canh thạch nha đam, khoảng 50–80 g.",
           "Món đã có đường hoặc sữa chua ngọt nên chọn nha đam không đường; món cần nước đường sẵn chọn nha đam có đường.",
           f"Thạch nha đam túi 1kg tại Việt Cường Nhân giá {gia(148)}, có loại có đường và không đường."],
  body=f"""  <h2>Thạch nha đam là gì?</h2>
  <p>Thạch nha đam là phần thịt trong của lá nha đam đã được gọt vỏ, cắt hạt lựu và chế biến sẵn, đóng túi để dùng ngay cho chè, sữa chua, nước giải khát. So với nha đam tươi, thạch nha đam không còn nhớt và không có vị đắng của nhựa vỏ, nên không phải ngâm, trụng mất công.</p>
  <p>Ở Việt Cường Nhân có hai loại túi 1kg:</p>
  <table><thead><tr><th>Loại</th><th>Đặc điểm</th><th>Hợp với món</th></tr></thead><tbody>
  <tr><td>Nha đam có đường</td><td>Ngọt sẵn, vớt ra ăn được ngay</td><td>Nha đam đường phèn, chè, topping trà</td></tr>
  <tr><td>Nha đam không đường</td><td>Vị nhạt, tự nêm ngọt theo ý</td><td>Sữa chua, nước chanh, món cần kiểm soát lượng đường</td></tr>
  </tbody></table>

  <h2>Thạch nha đam làm món gì? 5 món dễ làm</h2>
  <p>Thạch nha đam hợp nhất với món mát: chè, sữa chua, nước chanh, trà trái cây. Năm món dưới đây đều làm trong 5–15 phút, không cần dụng cụ đặc biệt.</p>

  <h3>1. Nha đam đường phèn</h3>
  <p>Nha đam đường phèn là món đơn giản nhất: nấu nước đường phèn, để nguội rồi cho thạch nha đam vào, ướp lạnh.</p>
  <ul>
    <li><b>Nguyên liệu (4 chén):</b> 300 g thạch nha đam, 1 lít nước, 80–100 g đường phèn, 2–3 lá dứa.</li>
    <li><b>Cách làm:</b> đun nước với lá dứa và đường phèn đến khi đường tan, vớt lá dứa, để nguội. Cho thạch nha đam vào, cất ngăn mát 1 tiếng rồi dùng với đá.</li>
    <li><b>Mẹo:</b> dùng nha đam có đường thì giảm đường phèn còn khoảng một nửa.</li>
  </ul>

  <h3>2. Sữa chua nha đam</h3>
  <p>Sữa chua nha đam là món ăn vặt nhanh nhất, chỉ cần trộn 2 thứ.</p>
  <ul>
    <li><b>Nguyên liệu (1 hũ):</b> 1 hũ sữa chua 100 g, 2 muỗng canh thạch nha đam (khoảng 50 g).</li>
    <li><b>Cách làm:</b> vớt thạch nha đam để ráo nước, trộn vào sữa chua, để lạnh 10 phút. Có thể thêm vài miếng trái cây hoặc ít granola.</li>
    <li><b>Mẹo:</b> sữa chua có đường nên chọn nha đam không đường cho vị vừa.</li>
  </ul>

  <h3>3. Nước chanh nha đam hạt chia</h3>
  <p>Nước chanh nha đam hạt chia là món giải khát chua ngọt, làm trong 15 phút.</p>
  <ul>
    <li><b>Nguyên liệu (2 ly):</b> 1 quả chanh, 1 muỗng cà phê hạt chia, 100 g thạch nha đam, 400 ml nước, đường hoặc mật ong tùy thích.</li>
    <li><b>Cách làm:</b> ngâm hạt chia với 100 ml nước 10 phút cho nở. Vắt chanh, pha với phần nước còn lại và đường. Cho hạt chia, thạch nha đam vào, thêm đá.</li>
    <li><b>Mẹo:</b> vắt chanh xong dùng ngay, để lâu vỏ chanh làm nước bị đắng.</li>
  </ul>

  <h3>4. Chè nha đam táo đỏ</h3>
  <p>Chè nha đam táo đỏ có vị ngọt thanh của táo đỏ và độ giòn của nha đam, dùng nóng hay lạnh đều được.</p>
  <ul>
    <li><b>Nguyên liệu (4 chén):</b> 300 g thạch nha đam, 8–10 quả táo đỏ, 1 muỗng canh kỷ tử, 1 lít nước, 60–80 g đường phèn.</li>
    <li><b>Cách làm:</b> táo đỏ xẻ đôi, đun với nước lửa nhỏ 10 phút. Thêm đường phèn, kỷ tử, đun 2 phút rồi tắt bếp. Để nguội bớt mới cho thạch nha đam vào để giữ độ giòn.</li>
    <li><b>Mẹo:</b> phần nước táo đỏ chính là nền của <a href="tra-tao-do-ky-tu.html">trà táo đỏ kỷ tử</a>, nấu dư uống riêng cũng ngon.</li>
  </ul>

  <h3>5. Trà trái cây nha đam</h3>
  <p>Trà trái cây nha đam là cách dùng thạch nha đam làm topping, giống ly trà ngoài quán.</p>
  <ul>
    <li><b>Nguyên liệu (2 ly):</b> 300 ml trà xanh hoặc trà lài pha nhạt để nguội, 2–3 muỗng canh siro hoặc nước đường, 100 g thạch nha đam, trái cây như cam, dứa, dâu.</li>
    <li><b>Cách làm:</b> cho thạch nha đam và trái cây cắt nhỏ vào ly, thêm đá, rót trà và siro, khuấy đều.</li>
    <li><b>Mẹo:</b> nha đam có đường dùng làm topping vừa vị, không cần thêm nhiều siro.</li>
  </ul>

  <h2>So sánh nhanh 5 món từ thạch nha đam</h2>
  <table><thead><tr><th>Món</th><th>Thời gian</th><th>Lượng nha đam</th><th>Loại nên dùng</th></tr></thead><tbody>
  <tr><td>Nha đam đường phèn</td><td>15 phút + 1 tiếng ướp lạnh</td><td>300 g cho 4 chén</td><td>Có đường hoặc không đường</td></tr>
  <tr><td>Sữa chua nha đam</td><td>5 phút</td><td>50 g mỗi hũ</td><td>Không đường</td></tr>
  <tr><td>Nước chanh nha đam hạt chia</td><td>15 phút</td><td>100 g cho 2 ly</td><td>Không đường</td></tr>
  <tr><td>Chè nha đam táo đỏ</td><td>15 phút</td><td>300 g cho 4 chén</td><td>Không đường</td></tr>
  <tr><td>Trà trái cây nha đam</td><td>10 phút</td><td>100 g cho 2 ly</td><td>Có đường</td></tr>
  </tbody></table>

  <h2>Mẹo dùng và bảo quản thạch nha đam</h2>
  <p>Thạch nha đam giữ giòn ngon nhất khi để lạnh và cho vào món sau cùng, không đun sôi lâu.</p>
  <ul>
    <li><b>Vớt bằng muỗng sạch, khô:</b> không dùng muỗng đã nhúng vào món khác để phần còn lại trong túi không bị hỏng.</li>
    <li><b>Bảo quản:</b> làm theo hướng dẫn trên bao bì; túi đã mở thì buộc kín hoặc chuyển sang hộp có nắp, cất ngăn mát và dùng sớm.</li>
    <li><b>Muốn bớt ngọt:</b> với loại có đường, tráng qua nước đun sôi để nguội rồi để ráo.</li>
    <li><b>Dấu hiệu hỏng:</b> nước chua, có mùi lạ, thạch nhớt hoặc đổi màu thì bỏ.</li>
  </ul>
  <p>Muốn kết hợp với yến cho bữa xế, có thể dùng nước yến hũ ướp lạnh, xem bài <a href="nuoc-yen-hu-uong-luc-nao.html">nước yến hũ uống lúc nào</a>.</p>

  <h2>Lưu ý khi dùng</h2>
  <p>Thạch nha đam là thực phẩm, dùng như một nguyên liệu món ăn, không phải thuốc. Nên ăn lượng vừa phải trong ngày. Phụ nữ mang thai, trẻ nhỏ và người có bệnh nền nên hỏi bác sĩ trước khi ăn thường xuyên; cho trẻ nhỏ ăn thì cắt hạt nhỏ hơn để tránh hóc.</p>

  <h2>Mua thạch nha đam tại Việt Cường Nhân</h2>
  <p>Việt Cường Nhân bán thạch nha đam cùng yến sào và táo đỏ. Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(148, "Ngọt sẵn, hợp nha đam đường phèn, topping trà."), li(149, "Tự nêm ngọt, hợp sữa chua, nước chanh, chè."), li(147, "Nấu chè nha đam táo đỏ.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a>. Mua sỉ cho quán chè, quán nước hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Thạch nha đam làm món gì ngon?", "Thạch nha đam làm ngon nhất các món mát: nha đam đường phèn, sữa chua nha đam, nước chanh nha đam hạt chia, chè nha đam táo đỏ và trà trái cây nha đam."),
       ("Thạch nha đam có cần nấu lại không?", "Không cần. Thạch nha đam đã chế biến sẵn, vớt ra là dùng được. Nếu cho vào chè nóng, nên cho sau cùng để thạch giữ độ giòn."),
       ("Nên mua nha đam có đường hay không đường?", "Món đã có vị ngọt như sữa chua, chè, nước chanh nên chọn không đường để tự nêm. Cần ăn ngay hoặc làm topping trà thì chọn loại có đường."),
       ("Thạch nha đam mở túi để được bao lâu?", "Túi đã mở nên buộc kín hoặc chuyển sang hộp có nắp, cất ngăn mát và dùng sớm, theo hướng dẫn trên bao bì. Nước chua hoặc có mùi lạ thì bỏ."),
       ("Thạch nha đam 1kg giá bao nhiêu?", f"Tại Việt Cường Nhân, thạch nha đam túi 1kg giá {gia(148)} cho cả loại có đường và không đường, chưa gồm phí giao hàng.")]),
dict(slug="quy-trinh-san-xuat-yen-viet-cuong-nhan", cat="Về Việt Cường Nhân", ngay="2026-11-17",
  tu_khoa="quy trình sản xuất yến sào, quy trình làm sạch tổ yến, xưởng yến sào Việt Cường Nhân, quy trình nhặt lông yến, sản xuất nước yến chưng",
  h1="Quy trình sản xuất yến sào tại xưởng Việt Cường Nhân",
  desc="Quy trình sản xuất yến sào tại Việt Cường Nhân: từ nhà yến, phân loại, ngâm, nhặt lông bằng tay, sấy, định hình đến đóng gói và chưng nước yến hũ.",
  lede="Quy trình sản xuất yến sào tại Việt Cường Nhân đi qua 6 khâu chính: thu tổ từ nhà yến, phân loại tổ thô, ngâm nở, nhặt lông bằng tay, sấy và định hình, rồi đóng gói dán nhãn. Một phần yến sạch được chuyển sang nhà máy để chưng thành nước yến đóng hũ.",
  tom_tat=["Chuỗi khép kín: nhà yến tại Gò Công Tây (Tiền Giang cũ) và Bình Thuận, xưởng nhặt lông tại Lâm Đồng, xưởng tinh chế và nhà máy nước yến tại khu vực Dĩ An.",
           "6 khâu làm sạch tổ yến: thu tổ, phân loại, ngâm nở, nhặt lông bằng tay, sấy và định hình, đóng gói dán nhãn.",
           "Lông yến được nhặt thủ công bằng nhíp trên nền trắng, từng sợi một.",
           "Hệ thống quản lý an toàn thực phẩm đạt HACCP, ISO 22000:2018 và GMP do G-CERTI cấp.",
           f"Thành phẩm gồm yến thô, yến tinh chế, yến rút lông và nước yến chưng; ví dụ {P[109][2]} {gia(109)}/100gr."],
  body=f"""  <h2>Chuỗi sản xuất yến sào của Việt Cường Nhân</h2>
  <p>Việt Cường Nhân tự làm gần như trọn chuỗi sản xuất yến sào, từ nhà yến đến hũ nước yến. Công ty thành lập tháng 6 năm 2009; năm 2018 bắt đầu xây và nuôi yến tại Gò Công Tây (Tiền Giang cũ) và Bình Thuận, năm 2019 đưa vào hoạt động xưởng tinh chế đầu tiên tại Dĩ An, năm 2020 mở thêm 2 xưởng nhặt lông tại Đạ Tẻh và Madagui (Lâm Đồng), năm 2022 xây nhà máy nước yến chưng sẵn.</p>
  <table><thead><tr><th>Khâu</th><th>Nơi thực hiện</th><th>Kết quả</th></tr></thead><tbody>
  <tr><td>Nuôi yến, thu tổ</td><td>Nhà yến Gò Công Tây, Bình Thuận</td><td>Tổ yến thô</td></tr>
  <tr><td>Nhặt lông, làm sạch</td><td>Xưởng nhặt lông Lâm Đồng, xưởng tinh chế Dĩ An</td><td>Yến tinh chế, yến rút lông</td></tr>
  <tr><td>Chưng, tiệt trùng, đóng hũ</td><td>Nhà máy 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp</td><td>Nước yến chưng đóng hũ</td></tr>
  <tr><td>Đóng gói, giao hàng</td><td>Cơ sở đóng gói 261-263 Võ Thị Sáu, Phường Đông Hòa</td><td>Hộp, túi, lốc thành phẩm</td></tr>
  </tbody></table>
  <p>Vì tự làm sạch và đóng gói, xưởng biết rõ mỗi lô yến đến từ đâu và đã qua những khâu nào. Đây cũng là điều khách hay hỏi nhất khi đến xưởng.</p>

  <h2>Quy trình làm sạch tổ yến: 6 khâu</h2>
  <p>Quy trình làm sạch tổ yến tại xưởng Việt Cường Nhân gồm 6 khâu, làm chủ yếu bằng tay để giữ sợi yến nguyên và dai.</p>
  <h3>1. Thu tổ từ nhà yến</h3>
  <p>Tổ yến được thu từ nhà yến khi chim đã rời tổ. Tổ mới thu còn lông, bụi và tạp chất tự nhiên, gọi là yến thô.</p>
  <h3>2. Phân loại tổ thô</h3>
  <p>Tổ thô được chia theo kích thước, độ dày, độ nguyên vẹn và lượng lông. Tổ đẹp, ít lông thường làm yến rút lông hoặc bán yến thô loại tốt; tổ bể, nứt hoặc nhiều lông đi làm yến tinh chế. Cách phân loại này giải thích vì sao cùng là yến nhưng giá mỗi loại khác nhau.</p>
  <h3>3. Ngâm nở bằng nước sạch</h3>
  <p>Tổ yến được ngâm trong nước sạch đến khi mềm, sợi tách ra để lộ lông và bụi.</p>
  <h3>4. Nhặt lông bằng tay</h3>
  <p>Nhặt lông là khâu tốn công nhất: thợ dùng nhíp nhặt từng sợi lông trên nền trắng dưới đèn. Với yến rút lông, thợ nhặt ngay trên tổ còn nguyên sợi; với yến tinh chế, tổ được xé tơi rồi mới nhặt, sau đó đắp lại thành tổ hoặc miếng.</p>
  <h3>5. Sấy khô và định hình</h3>
  <p>Yến sạch được đắp vào khuôn để định hình thành tổ, miếng hoặc giữ dạng sợi, vụn, rồi sấy khô. Yến khô đúng độ mới để được lâu và giữ được sợi khi chưng.</p>
  <h3>6. Kiểm tra, đóng gói, dán nhãn</h3>
  <p>Thành phẩm được kiểm tra lại lông sót và khối lượng, đóng hộp, dán nhãn có tên sản phẩm, khối lượng, ngày sản xuất, hạn dùng và thông tin cơ sở sản xuất.</p>
  <p>Nếu bạn mua yến thô và muốn tự làm sạch ở nhà, các bước tương tự được hướng dẫn ở bài <a href="cach-lam-sach-yen-tho.html">cách làm sạch yến thô tại nhà</a>.</p>

  <h2>Quy trình sản xuất nước yến chưng đóng hũ</h2>
  <p>Nước yến chưng tại nhà máy Việt Cường Nhân được làm từ yến đã làm sạch, chưng, đóng hũ và tiệt trùng. Có hai dòng: nước yến chưng thủ công ghi rõ lượng yến tươi mỗi hũ, và nước yến VCN Nest ghi lượng tổ yến thô mỗi hũ.</p>
  <ol>
    <li>Yến sạch được cân theo công thức của từng dòng sản phẩm.</li>
    <li>Chưng cùng nước và nguyên liệu phối trộn theo công thức.</li>
    <li>Rót hũ, đóng nắp kín.</li>
    <li>Tiệt trùng, để nguội, kiểm tra nắp và nhãn.</li>
    <li>Đóng lốc, đóng hộp, lưu kho chờ giao.</li>
  </ol>
  <p>Cách dùng và bảo quản nước yến hũ có ở bài <a href="nuoc-yen-chung-san-cach-dung-bao-quan.html">nước yến chưng sẵn: cách dùng và bảo quản</a>.</p>

  <h2>Tiêu chuẩn an toàn thực phẩm áp dụng</h2>
  <p>Hệ thống quản lý an toàn thực phẩm của Việt Cường Nhân đạt HACCP, ISO 22000:2018 và GMP do G-CERTI cấp. Phạm vi chứng nhận gồm sơ chế và kinh doanh yến sào, sản phẩm từ yến (yến chưng sẵn, nước yến, yến đóng gói) và nuôi cấy, sản xuất nấm đông trùng hạ thảo.</p>
  <ul>
    <li><b>HACCP:</b> xác định và kiểm soát các bước có thể gây mất an toàn trong sản xuất.</li>
    <li><b>ISO 22000:2018:</b> hệ thống quản lý an toàn thực phẩm cho cả chuỗi.</li>
    <li><b>GMP:</b> yêu cầu về nhà xưởng, vệ sinh, con người và thiết bị.</li>
  </ul>
  <p>Tổ yến thô, tổ yến tinh chế và nấm đông trùng hạ thảo có hồ sơ tự công bố. Bản scan giấy tờ xem tại <a href="../chung-nhan/">trang chứng nhận</a>; ý nghĩa từng chứng nhận xem bài <a href="chung-nhan-haccp-iso-22000-gmp-la-gi.html">HACCP, ISO 22000 và GMP nghĩa là gì</a>.</p>

  <h2>Thành phẩm từ quy trình sản xuất yến sào</h2>
  <p>Mỗi khâu trong quy trình tạo ra một nhóm sản phẩm với mức giá khác nhau. Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(101, "Sau khâu phân loại, còn lông, tự làm sạch tại nhà."), li(109, "Đã nhặt sạch lông, đắp tổ và sấy khô."), li(113, "Nhặt lông trên tổ còn nguyên sợi."), li(124, "Chưng và tiệt trùng tại nhà máy.")) + """
  <p>Muốn xem trực tiếp, bạn gọi hoặc nhắn Zalo 0978 094 739 để hẹn giờ ghé xưởng; địa chỉ chi tiết có ở bài <a href="yen-sao-binh-duong-di-an-mua-o-dau.html">mua yến sào ở Dĩ An</a>. Đặt hàng online qua <a href="../#san-pham">bảng giá sản phẩm</a>.</p>""",
  faq=[("Yến sào Việt Cường Nhân được làm sạch như thế nào?", "Tổ yến được phân loại, ngâm nở bằng nước sạch, nhặt lông bằng tay với nhíp, sau đó định hình, sấy khô, kiểm tra lại và đóng gói."),
       ("Việt Cường Nhân có nhà yến riêng không?", "Có. Từ năm 2018 Việt Cường Nhân xây và nuôi yến tại Gò Công Tây (Tiền Giang cũ) và Bình Thuận, cùng các xưởng nhặt lông tại Đạ Tẻh và Madagui (Lâm Đồng)."),
       ("Nước yến hũ Việt Cường Nhân sản xuất ở đâu?", "Nước yến chưng được sản xuất tại nhà máy 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp, TP. Hồ Chí Minh, đi vào hoạt động từ năm 2022."),
       ("Xưởng yến Việt Cường Nhân có chứng nhận gì?", "Hệ thống quản lý an toàn thực phẩm đạt HACCP, ISO 22000:2018 và GMP do G-CERTI cấp; tổ yến thô, tổ yến tinh chế có hồ sơ tự công bố."),
       ("Có được đến xem xưởng làm yến không?", "Bạn gọi hoặc nhắn Zalo 0978 094 739 trước để được hẹn giờ và địa điểm phù hợp, vì xưởng là nơi đang sản xuất.")]),
dict(slug="viet-cuong-nhan-la-ai", cat="Về Việt Cường Nhân", ngay="2026-11-17",
  tu_khoa="Việt Cường Nhân, công ty Việt Cường Nhân, yến sào Việt Cường Nhân, Việt Cường Nhân là ai, VCN Nest",
  h1="Việt Cường Nhân là ai? Hành trình từ nhà yến đến nhà máy",
  desc="Việt Cường Nhân là công ty yến sào thành lập năm 2009 tại Dĩ An, có nhà yến, xưởng nhặt lông, nhà máy nước yến, đạt HACCP, ISO 22000, GMP. Hành trình và sản phẩm.",
  lede="Việt Cường Nhân là Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân, thành lập tháng 6 năm 2009, trụ sở tại Phường Dĩ An, TP. Hồ Chí Minh. Công ty làm yến sào theo chuỗi khép kín: nhà yến, xưởng nhặt lông, xưởng tinh chế, nhà máy nước yến chưng sẵn, cùng trang trại nấm đông trùng hạ thảo và nha đam.",
  tom_tat=["Tên đầy đủ: Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân, mã số doanh nghiệp 3701518691, thành lập tháng 6 năm 2009.",
           "Chuỗi khép kín: nhà yến Gò Công Tây và Bình Thuận (2018), xưởng tinh chế Dĩ An (2019), 2 xưởng nhặt lông Lâm Đồng (2020), nhà máy nước yến (2022).",
           "Hệ thống quản lý an toàn thực phẩm đạt HACCP, ISO 22000:2018 và GMP do G-CERTI cấp.",
           "Sản phẩm có mặt tại nhiều chuỗi siêu thị, bán trên TikTok Shop, Shopee, Facebook, website và xuất khẩu sang Campuchia, Hàn Quốc.",
           "Phương châm: \"Chất lượng tạo nên giá trị – Uy tín tạo nên thương hiệu\". Hotline, Zalo 0978 094 739."],
  body=f"""  <h2>Việt Cường Nhân là ai?</h2>
  <p>Việt Cường Nhân là doanh nghiệp sản xuất và kinh doanh yến sào, nước yến chưng, nấm đông trùng hạ thảo và thực phẩm dinh dưỡng, có trụ sở tại Dĩ An (Bình Dương cũ, nay thuộc TP. Hồ Chí Minh). Tên pháp lý là Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân, mã số doanh nghiệp 3701518691, thành lập tháng 6 năm 2009.</p>
  <table><thead><tr><th>Thông tin</th><th>Chi tiết</th></tr></thead><tbody>
  <tr><td>Tên công ty</td><td>Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân</td></tr>
  <tr><td>Năm thành lập</td><td>Tháng 6 năm 2009</td></tr>
  <tr><td>Trụ sở</td><td>Số 24/22 Khu phố Thống Nhất 1, Phường Dĩ An, TP. Hồ Chí Minh</td></tr>
  <tr><td>Nhà máy</td><td>511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp, TP. Hồ Chí Minh</td></tr>
  <tr><td>Cơ sở đóng gói</td><td>261-263 Võ Thị Sáu, KP. Tây A, Phường Đông Hòa, TP. Hồ Chí Minh</td></tr>
  <tr><td>Chứng nhận</td><td>HACCP, ISO 22000:2018, GMP (G-CERTI)</td></tr>
  <tr><td>Liên hệ</td><td>Hotline, Zalo 0978 094 739</td></tr>
  </tbody></table>

  <h2>Hành trình phát triển của Việt Cường Nhân</h2>
  <p>Việt Cường Nhân đi từ một công ty thương mại năm 2009 đến chuỗi sản xuất yến sào khép kín sau hơn một thập kỷ. Các mốc chính:</p>
  <ol>
    <li><b>2009:</b> thành lập Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân.</li>
    <li><b>2018:</b> xây dựng và nuôi yến tại Gò Công Tây (Tiền Giang cũ) và Bình Thuận; mua bán yến thô, yến tinh chế.</li>
    <li><b>2019:</b> đưa vào hoạt động xưởng tinh chế yến sào đầu tiên tại Dĩ An.</li>
    <li><b>2020:</b> mở thêm 2 xưởng nhặt lông yến tại Đạ Tẻh và Madagui (Lâm Đồng), nâng lên 3 xưởng.</li>
    <li><b>2022:</b> nuôi trồng nấm đông trùng hạ thảo, xây nhà máy nước yến chưng sẵn.</li>
    <li><b>2024:</b> mở rộng hợp tác trong và ngoài nước; phát triển thêm thực phẩm dinh dưỡng, mỹ phẩm.</li>
  </ol>
  <p>Từng khâu trong chuỗi, từ thu tổ đến đóng hũ, được mô tả ở bài <a href="quy-trinh-san-xuat-yen-viet-cuong-nhan.html">quy trình sản xuất yến sào tại xưởng Việt Cường Nhân</a>.</p>

  <h2>Việt Cường Nhân sản xuất những gì?</h2>
  <p>Việt Cường Nhân có 5 nhóm sản phẩm chính, phần lớn do công ty tự nuôi, tự sơ chế và đóng gói.</p>
  <table><thead><tr><th>Nhóm</th><th>Ví dụ</th><th>Nguồn</th></tr></thead><tbody>
  <tr><td>Tổ yến thô</td><td>{P[101][2]}</td><td>Nhà yến Gò Công Tây, Bình Thuận</td></tr>
  <tr><td>Yến đã nhặt sạch lông</td><td>{P[109][2]}, {P[113][2]}</td><td>Xưởng nhặt lông Lâm Đồng, xưởng tinh chế Dĩ An</td></tr>
  <tr><td>Nước yến chưng đóng hũ</td><td>{P[124][2]}, nước yến VCN Nest</td><td>Nhà máy nước yến Tân Đông Hiệp</td></tr>
  <tr><td>Nấm đông trùng hạ thảo</td><td>{P[136][2]}</td><td>Trang trại nuôi trồng của công ty</td></tr>
  <tr><td>Táo đỏ, thạch nha đam, mỹ phẩm</td><td>Táo đỏ Tân Cương, nha đam, xà bông T'Beauty</td><td>Kho táo đỏ, trang trại và nhà máy nha đam</td></tr>
  </tbody></table>
  <p>Nếu mới tìm hiểu yến, bạn có thể đọc bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a> để chọn loại hợp nhu cầu.</p>

  <h2>Chứng nhận an toàn thực phẩm của Việt Cường Nhân</h2>
  <p>Hệ thống quản lý an toàn thực phẩm của Việt Cường Nhân đạt HACCP, ISO 22000:2018 và GMP do G-CERTI cấp. Phạm vi chứng nhận gồm sơ chế và kinh doanh yến sào, sản phẩm từ yến, nuôi cấy và sản xuất nấm đông trùng hạ thảo, đóng gói nhụy hoa nghệ tây, táo đỏ.</p>
  <ul>
    <li>HACCP: hiệu lực đến 30/11/2026.</li>
    <li>ISO 22000:2018: hiệu lực đến 28/06/2027.</li>
    <li>GMP: hiệu lực đến 21/08/2027.</li>
    <li>Hồ sơ tự công bố: tổ yến thô, tổ yến tinh chế, nấm đông trùng hạ thảo.</li>
  </ul>
  <p>Bản scan giấy tờ xem tại <a href="../chung-nhan/">trang chứng nhận</a>; ý nghĩa từng chứng nhận xem bài <a href="chung-nhan-haccp-iso-22000-gmp-la-gi.html">HACCP, ISO 22000 và GMP nghĩa là gì</a>.</p>

  <h2>Sản phẩm Việt Cường Nhân bán ở đâu?</h2>
  <p>Sản phẩm Việt Cường Nhân có ở kênh siêu thị, kênh online và xuất khẩu. Trong nước, công ty cung cấp yến thô cho các xưởng tinh chế trên toàn quốc; sản phẩm có mặt tại LOTTE Mart, KingKong Mart, Z-Mart, LongBeach Mart, YOUTH MARKET, HELLO MART, Taka Mart, JAPAN VINA, J24 MART và một số spa, cửa hàng làm đẹp.</p>
  <ul>
    <li><b>Online:</b> website vietcuongnhan.com, TikTok Shop, Shopee, Facebook.</li>
    <li><b>Tại xưởng:</b> nhà máy Tân Đông Hiệp và cơ sở đóng gói Đông Hòa, gọi trước 0978 094 739 để hẹn giờ. Chi tiết ở bài <a href="yen-sao-binh-duong-di-an-mua-o-dau.html">mua yến sào ở Dĩ An</a>.</li>
    <li><b>Xuất khẩu:</b> Campuchia (nước yến chưng đóng hũ), Hàn Quốc (nước yến chưng đóng hũ và yến tinh chế).</li>
  </ul>

  <h2>Tầm nhìn và giá trị cốt lõi</h2>
  <p>Phương châm của Việt Cường Nhân là "Chất lượng tạo nên giá trị – Uy tín tạo nên thương hiệu". Công ty đặt mục tiêu trở thành doanh nghiệp hàng đầu tại Việt Nam trong lĩnh vực thực phẩm dinh dưỡng, mỹ phẩm và dịch vụ thương mại.</p>
  <ul>
    <li><b>Chất lượng:</b> luôn đặt chất lượng lên hàng đầu.</li>
    <li><b>Uy tín:</b> xây dựng niềm tin lâu dài.</li>
    <li><b>Đổi mới:</b> không ngừng cải tiến.</li>
    <li><b>Trách nhiệm:</b> cam kết với cộng đồng.</li>
  </ul>
  <p>Đọc thêm ở <a href="../gioi-thieu/">trang giới thiệu Việt Cường Nhân</a>.</p>

  <h2>Một số sản phẩm tiêu biểu</h2>
  <p>Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(101), li(109), li(124), li(136)) + """
  <p>Xem đầy đủ và đặt hàng ở <a href="../#san-pham">bảng giá sản phẩm</a>. Mua sỉ hoặc làm đại lý: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Việt Cường Nhân là công ty gì?", "Việt Cường Nhân là Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân, thành lập năm 2009 tại Dĩ An, sản xuất và kinh doanh yến sào, nước yến chưng, nấm đông trùng hạ thảo, táo đỏ, nha đam và mỹ phẩm."),
       ("Yến sào Việt Cường Nhân có nhà yến riêng không?", "Có. Từ năm 2018 công ty xây và nuôi yến tại Gò Công Tây (Tiền Giang cũ) và Bình Thuận, cùng các xưởng nhặt lông tại Lâm Đồng và xưởng tinh chế tại Dĩ An."),
       ("Việt Cường Nhân ở đâu?", "Trụ sở tại Số 24/22 Khu phố Thống Nhất 1, Phường Dĩ An; nhà máy tại 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp; cơ sở đóng gói tại 261-263 Võ Thị Sáu, Phường Đông Hòa, TP. Hồ Chí Minh."),
       ("VCN Nest là gì?", "VCN Nest là dòng nước yến chưng đóng hũ của Việt Cường Nhân, sản xuất tại nhà máy nước yến ở Tân Đông Hiệp, có loại 0.3gr và 0.8gr tổ yến thô mỗi hũ."),
       ("Việt Cường Nhân có chứng nhận gì?", "Hệ thống quản lý an toàn thực phẩm đạt HACCP, ISO 22000:2018 và GMP do G-CERTI cấp; tổ yến thô, tổ yến tinh chế và nấm đông trùng hạ thảo có hồ sơ tự công bố.")]),
dict(slug="mua-yen-online-can-kiem-tra-gi", cat="Yến sào", ngay="2026-11-17",
  tu_khoa="mua yến online, mua yến sào online, mua yến sào online uy tín, kiểm tra yến khi nhận hàng, đặt yến sào qua mạng",
  h1="Mua yến sào online cần kiểm tra những gì?",
  desc="Mua yến online cần kiểm tra 4 nhóm: thông tin người bán, mô tả và giá sản phẩm, giấy tờ chứng nhận, cách kiểm hàng khi nhận. Checklist dễ làm, kèm chính sách đổi trả.",
  lede="Mua yến online an toàn hơn khi bạn kiểm tra 4 nhóm thông tin trước và sau khi đặt: người bán là ai, sản phẩm được mô tả và báo giá rõ ràng không, cơ sở sản xuất có giấy tờ gì, và khi nhận hàng được kiểm tra, đổi trả ra sao. Không có dấu hiệu nào chắc chắn 100%, nhưng càng nhiều điểm rõ ràng thì rủi ro càng thấp.",
  tom_tat=["Kiểm tra người bán: tên công ty, mã số doanh nghiệp, địa chỉ xưởng, số điện thoại gọi được.",
           "Kiểm tra sản phẩm: tên loại yến (thô, tinh chế, rút lông), khối lượng, giá cho từng quy cách, ảnh thật sợi yến.",
           "Kiểm tra giấy tờ: chứng nhận HACCP, ISO 22000, GMP còn hiệu lực và hồ sơ tự công bố sản phẩm.",
           "Khi nhận: kiểm tra kiện, số lượng, niêm phong trước khi thanh toán, quay video lúc mở hàng.",
           f"Giá yến cao cấp không rẻ bất thường; ví dụ {P[109][2]} tại Việt Cường Nhân {gia(109)}/100gr."],
  body=f"""  <h2>Vì sao cần kiểm tra khi mua yến online?</h2>
  <p>Mua yến online tiện nhưng bạn không được cầm sợi yến lên xem như ở cửa hàng, nên phải dựa vào thông tin người bán đưa ra. Yến sào là thực phẩm giá cao, vì vậy dành vài phút kiểm tra trước khi đặt giúp bạn tránh mua nhầm loại, nhầm khối lượng hoặc hàng không rõ nguồn gốc.</p>
  <p>Khách hay hỏi xưởng Việt Cường Nhân câu "mua online có sợ hàng pha không". Câu trả lời ngắn: chọn người bán minh bạch thông tin và có chính sách kiểm hàng, đổi trả rõ ràng là cách giảm rủi ro hiệu quả nhất.</p>

  <h2>1. Kiểm tra thông tin người bán</h2>
  <p>Người bán yến online uy tín công khai đầy đủ tên doanh nghiệp, mã số doanh nghiệp, địa chỉ và số điện thoại liên lạc được.</p>
  <ul>
    <li><b>Tên pháp lý và mã số doanh nghiệp:</b> có thể tra trên Cổng thông tin quốc gia về đăng ký doanh nghiệp.</li>
    <li><b>Địa chỉ xưởng hoặc cửa hàng:</b> tìm được trên bản đồ, có thể hẹn đến xem.</li>
    <li><b>Số điện thoại, Zalo:</b> gọi thử, hỏi vài câu về loại yến, cách chưng. Người làm yến thật trả lời cụ thể.</li>
    <li><b>Trang chính sách:</b> có chính sách vận chuyển, kiểm hàng, đổi trả viết rõ ràng.</li>
  </ul>
  <p>Ví dụ, chân trang website Việt Cường Nhân ghi tên Công ty TNHH Thương mại - Dịch vụ Việt Cường Nhân, mã số doanh nghiệp 3701518691, trụ sở, nhà máy, cơ sở đóng gói và hotline 0978 094 739.</p>

  <h2>2. Kiểm tra mô tả sản phẩm và giá</h2>
  <p>Mô tả sản phẩm yến cần ghi rõ loại yến, khối lượng và giá cho từng quy cách; mô tả mập mờ là dấu hiệu nên hỏi lại.</p>
  <table><thead><tr><th>Cần có</th><th>Vì sao quan trọng</th></tr></thead><tbody>
  <tr><td>Loại yến: thô, tinh chế, rút lông, chân tua, vụn</td><td>Mỗi loại có mức làm sạch và giá khác nhau</td></tr>
  <tr><td>Khối lượng tịnh (50gr, 100gr...)</td><td>So sánh giá cho đúng, tránh nhầm khối lượng hộp</td></tr>
  <tr><td>Giá cho từng quy cách</td><td>Biết trước tổng tiền, tránh "inbox báo giá" rồi đổi giá</td></tr>
  <tr><td>Ảnh thật sợi yến, video cận cảnh</td><td>Nhìn được độ dày sợi, màu, lông còn sót</td></tr>
  <tr><td>Nguồn gốc: nhà yến, nơi làm sạch</td><td>Biết hàng đi qua những khâu nào</td></tr>
  </tbody></table>
  <p>Giá rẻ bất thường so với mặt bằng chung là điểm cần cảnh giác. Tham khảo khung giá từng loại ở bài <a href="gia-yen-sao-bao-nhieu-tien.html">giá yến sào bao nhiêu tiền 100gr</a>, và phân biệt các loại ở bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>.</p>

  <h2>3. Kiểm tra giấy tờ, chứng nhận</h2>
  <p>Giấy chứng nhận cho biết cơ sở sản xuất được đánh giá về quy trình an toàn thực phẩm. Khi xem, hãy đối chiếu 3 điểm:</p>
  <ol>
    <li>Tên và địa chỉ trên giấy trùng với cơ sở sản xuất sản phẩm bạn mua.</li>
    <li>Phạm vi chứng nhận có ghi nhóm sản phẩm yến sào.</li>
    <li>Số chứng nhận, tổ chức cấp và thời hạn hiệu lực còn hạn.</li>
  </ol>
  <p>Ngoài chứng nhận hệ thống, sản phẩm yến nên có hồ sơ tự công bố. Việt Cường Nhân công khai bản scan HACCP, ISO 22000:2018, GMP và hồ sơ tự công bố tổ yến thô, tổ yến tinh chế tại <a href="../chung-nhan/">trang chứng nhận</a>. Ý nghĩa từng chứng nhận xem bài <a href="chung-nhan-haccp-iso-22000-gmp-la-gi.html">HACCP, ISO 22000 và GMP nghĩa là gì</a>.</p>

  <h2>4. Kiểm tra khi nhận hàng</h2>
  <p>Khi nhận yến, hãy kiểm tra kiện hàng trước khi thanh toán và quay video lúc mở hộp để có căn cứ nếu cần đổi trả.</p>
  <ol>
    <li><b>Bên ngoài kiện:</b> không móp, rách, ướt.</li>
    <li><b>Số lượng và loại:</b> đúng với đơn đã xác nhận.</li>
    <li><b>Niêm phong, tem nhãn:</b> còn nguyên; nhãn có tên sản phẩm, khối lượng, ngày sản xuất, hạn dùng, cơ sở sản xuất.</li>
    <li><b>Quay video khi mở hộp:</b> quay liền mạch từ lúc cắt băng keo.</li>
    <li><b>Xem sợi yến:</b> sợi tự nhiên to nhỏ không đều, màu trắng ngà, không bóng nhựa, có mùi tanh nhẹ đặc trưng.</li>
  </ol>
  <p>Các dấu hiệu khi ngâm và chưng để nhận biết yến thật có ở bài <a href="cach-chon-yen-sao-that.html">cách chọn mua yến sào thật, tránh hàng pha</a>.</p>

  <h2>Chính sách khi mua yến online tại Việt Cường Nhân</h2>
  <p>Theo chính sách hiện hành trên website Việt Cường Nhân, khách được kiểm tra hàng trước khi thanh toán và được đổi trả nếu hàng sai, thiếu hoặc hư hỏng.</p>
  <table><thead><tr><th>Nội dung</th><th>Chi tiết</th></tr></thead><tbody>
  <tr><td>Thời gian giao</td><td>TP. Hồ Chí Minh và lân cận 1–2 ngày làm việc; tỉnh khác 2–5 ngày làm việc</td></tr>
  <tr><td>Phí giao</td><td>Giá web chưa gồm phí giao; phí báo khi gọi xác nhận đơn, trước khi giao</td></tr>
  <tr><td>Kiểm hàng</td><td>Kiểm tra kiện, số lượng, loại, niêm phong trước khi thanh toán</td></tr>
  <tr><td>Đổi trả</td><td>Báo trong 03 ngày kể từ khi nhận nếu giao sai, thiếu, hư hỏng, hết hạn; có ảnh hoặc video mở hàng</td></tr>
  <tr><td>Hoàn tiền</td><td>Chuyển khoản trong 07 ngày làm việc kể từ khi nhận lại hàng</td></tr>
  </tbody></table>
  <p>Chi tiết xem <a href="../chinh-sach/van-chuyen.html">chính sách vận chuyển và kiểm hàng</a> và <a href="../chinh-sach/doi-tra.html">chính sách đổi trả</a>.</p>

  <h2>Đặt yến online tại Việt Cường Nhân</h2>
  <p>Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(109, "Đã nhặt sạch lông, ngâm xong là chưng."), li(113, "Sợi dài, hợp biếu tặng.")) + """
  <p>Chọn sản phẩm ở <a href="../#san-pham">bảng giá</a>, điền thông tin đặt hàng, nhân viên sẽ gọi xác nhận và báo phí giao. Cần tư vấn chọn loại hoặc mua sỉ: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Mua yến sào online có an toàn không?", "An toàn hơn khi người bán công khai tên doanh nghiệp, địa chỉ xưởng, giấy chứng nhận và có chính sách kiểm hàng, đổi trả rõ ràng. Luôn kiểm tra hàng và quay video lúc mở hộp."),
       ("Mua yến online cần kiểm tra gì trước khi đặt?", "Kiểm tra thông tin người bán, loại yến, khối lượng, giá từng quy cách, ảnh thật sợi yến và giấy chứng nhận an toàn thực phẩm còn hiệu lực."),
       ("Nhận yến rồi mới thấy sai loại thì làm sao?", "Tại Việt Cường Nhân, bạn báo qua điện thoại hoặc Zalo 0978 094 739 trong 03 ngày kể từ khi nhận, kèm ảnh hoặc video mở hàng để được đổi sản phẩm hoặc hoàn tiền."),
       ("Có được kiểm tra yến trước khi thanh toán không?", "Theo chính sách của Việt Cường Nhân, bạn được kiểm tra bên ngoài kiện, số lượng, loại sản phẩm và niêm phong trước khi thanh toán."),
       ("Đặt yến online bao lâu thì nhận?", "Với Việt Cường Nhân, TP. Hồ Chí Minh và khu vực lân cận nhận trong 1–2 ngày làm việc, các tỉnh khác 2–5 ngày làm việc.")]),
dict(slug="thanh-phan-dinh-duong-yen-sao", cat="Yến sào", ngay="2026-11-17",
  tu_khoa="thành phần dinh dưỡng yến sào, trong tổ yến có gì, tổ yến làm từ gì, protein trong yến sào, axit sialic trong yến",
  h1="Trong tổ yến có gì? Thành phần dinh dưỡng yến sào",
  desc="Thành phần dinh dưỡng yến sào gồm chủ yếu protein (glycoprotein), carbohydrate, axit amin và khoáng chất. Tổ yến làm từ gì, vì sao mỗi lô khác nhau, cách ăn cho đúng.",
  lede="Thành phần dinh dưỡng yến sào chủ yếu là protein, phần lớn ở dạng glycoprotein, cùng carbohydrate (trong đó có axit sialic), các axit amin, một ít khoáng chất và nước. Tỷ lệ từng chất thay đổi theo nguồn tổ, mùa thu hoạch và cách sơ chế, nên muốn số liệu chính xác cho một sản phẩm cần xem phiếu kiểm nghiệm của chính lô hàng đó.",
  tom_tat=["Tổ yến được chim yến làm từ nước bọt, khô lại thành sợi đan xen.",
           "Thành phần chính là protein (dạng glycoprotein), tiếp theo là carbohydrate, axit amin, khoáng chất và nước.",
           "Axit sialic là thành phần carbohydrate hay được nhắc đến nhất khi nói về yến sào.",
           "Tỷ lệ các chất khác nhau giữa các lô; số liệu chính xác cần phiếu kiểm nghiệm.",
           "Yến sào là thực phẩm, không phải thuốc; người có bệnh nền, bà bầu, trẻ nhỏ nên hỏi bác sĩ trước khi dùng thường xuyên."],
  body=f"""  <h2>Tổ yến làm từ gì?</h2>
  <p>Tổ yến được chim yến làm hoàn toàn từ nước bọt. Chim nhả nước bọt thành từng sợi, gắn lên vách hoặc xà nhà yến; sợi gặp không khí thì khô và cứng lại, chồng lên nhau thành chiếc tổ hình chén.</p>
  <p>Khi mới thu hoạch, tổ còn lẫn lông chim và bụi. Phần ăn được là sợi yến; lông và tạp chất được loại bỏ ở khâu làm sạch, như mô tả ở bài <a href="quy-trinh-san-xuat-yen-viet-cuong-nhan.html">quy trình sản xuất yến sào tại xưởng Việt Cường Nhân</a>.</p>

  <h2>Thành phần dinh dưỡng yến sào gồm những gì?</h2>
  <p>Thành phần dinh dưỡng yến sào gồm 5 nhóm chính: protein, carbohydrate, axit amin, khoáng chất và nước. Trong đó protein là nhóm chiếm phần lớn khối lượng khô.</p>
  <table><thead><tr><th>Nhóm chất</th><th>Có gì trong tổ yến</th><th>Ghi chú</th></tr></thead><tbody>
  <tr><td>Protein</td><td>Chủ yếu là glycoprotein (protein gắn với chuỗi đường)</td><td>Nhóm chiếm nhiều nhất, tạo nên độ dai của sợi yến</td></tr>
  <tr><td>Carbohydrate</td><td>Các loại đường gắn trên glycoprotein, trong đó có axit sialic</td><td>Axit sialic là thành phần hay được nhắc đến nhất</td></tr>
  <tr><td>Axit amin</td><td>Nhiều loại axit amin khác nhau</td><td>Là đơn vị cấu tạo nên protein</td></tr>
  <tr><td>Khoáng chất</td><td>Một lượng nhỏ khoáng như canxi, natri, kali, magie, sắt</td><td>Phụ thuộc môi trường nhà yến và nguồn nước</td></tr>
  <tr><td>Nước</td><td>Độ ẩm còn lại sau khi sấy khô</td><td>Yến khô đúng độ thì bảo quản được lâu</td></tr>
  </tbody></table>

  <h3>Glycoprotein là gì?</h3>
  <p>Glycoprotein là protein có gắn các chuỗi đường. Đây là thành phần tạo nên cấu trúc sợi yến: khi ngâm nước, sợi nở ra, mềm và trong; khi chưng quá lâu hoặc quá nóng, cấu trúc này bị phá vỡ khiến yến tan thành nước. Vì vậy cách chưng ảnh hưởng nhiều tới chén yến, xem bài <a href="yen-bi-chay-nuoc-khi-chung.html">vì sao yến bị chảy nước khi chưng</a>.</p>

  <h3>Axit sialic là gì?</h3>
  <p>Axit sialic là một loại đường có trong cấu trúc glycoprotein của tổ yến. Đây là thành phần được nhắc đến nhiều trong các tài liệu về yến sào và thường được dùng làm một chỉ tiêu khi phân tích mẫu yến.</p>

  <h2>Vì sao thành phần mỗi lô yến khác nhau?</h2>
  <p>Thành phần yến sào không cố định, vì tổ yến là sản phẩm tự nhiên. Ở xưởng Việt Cường Nhân, chúng tôi thấy các lô yến khác nhau rõ về độ dày sợi, độ nở và màu sắc, và thành phần cũng thay đổi theo:</p>
  <ul>
    <li><b>Nguồn tổ:</b> vùng nuôi, điều kiện nhà yến, thức ăn tự nhiên của chim.</li>
    <li><b>Mùa thu hoạch:</b> tổ ở các mùa khác nhau có độ dày và độ chắc khác nhau.</li>
    <li><b>Vị trí trên tổ:</b> phần chân tổ dày, đặc hơn phần thân, xem bài <a href="chan-yen-chan-tua-la-gi.html">chân yến là gì</a>.</li>
    <li><b>Cách sơ chế:</b> ngâm, làm sạch, sấy ảnh hưởng tới độ ẩm và độ nguyên của sợi.</li>
  </ul>
  <p>Vì vậy bài này không đưa ra con số tỷ lệ cụ thể. Một con số chung cho mọi loại yến sẽ không chính xác với sản phẩm bạn đang cầm trên tay.</p>

  <h2>Thành phần yến thô, yến tinh chế và nước yến khác nhau ra sao?</h2>
  <p>Yến thô, yến tinh chế và yến rút lông có cùng bản chất là sợi tổ yến; khác nhau chủ yếu ở mức làm sạch và độ nguyên sợi. Nước yến đóng hũ thì khác hơn, vì ngoài yến còn có nước và nguyên liệu phối trộn theo công thức.</p>
  <table><thead><tr><th>Sản phẩm</th><th>Thành phần</th><th>Cách đọc thông tin</th></tr></thead><tbody>
  <tr><td>Yến thô</td><td>Sợi yến kèm lông, tạp chất tự nhiên</td><td>Khối lượng gồm cả phần sẽ bỏ đi khi làm sạch</td></tr>
  <tr><td>Yến tinh chế, rút lông</td><td>Sợi yến đã làm sạch, sấy khô</td><td>Khối lượng gần như toàn bộ là phần ăn được</td></tr>
  <tr><td>Nước yến hũ</td><td>Yến, nước và nguyên liệu phối trộn</td><td>Xem lượng yến ghi trên nhãn, ví dụ 12gr yến tươi hoặc 0.8gr tổ yến thô mỗi hũ</td></tr>
  </tbody></table>
  <p>So sánh chi tiết hơn có ở bài <a href="nuoc-yen-hu-va-yen-to-chung.html">nước yến hũ và yến tổ tự chưng</a>.</p>

  <h2>Ăn yến thế nào cho đúng?</h2>
  <p>Yến sào là thực phẩm bổ sung trong bữa ăn, không thay thế bữa ăn chính và không phải thuốc. Nhiều gia đình dùng mỗi lần khoảng 3–5 g yến khô, chưng cách thủy để giữ sợi.</p>
  <ul>
    <li>Chưng lửa nhỏ, không đun sôi sùng sục, theo bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn</a>.</li>
    <li>Ăn kèm chế độ ăn đa dạng, đủ các nhóm chất.</li>
    <li>Bà bầu, trẻ nhỏ, người lớn tuổi và người có bệnh nền nên hỏi bác sĩ trước khi dùng thường xuyên.</li>
  </ul>

  <h2>Yến sào tại Việt Cường Nhân</h2>
  <p>Yến tinh chế và yến rút lông của Việt Cường Nhân được làm sạch tại xưởng, có hồ sơ tự công bố sản phẩm (xem <a href="../chung-nhan/">trang chứng nhận</a>). Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(109, "Đã nhặt sạch lông, ngâm xong là chưng."), li(113, "Sợi dài, nguyên tổ.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a> hoặc nhắn Zalo 0978 094 739.</p>""",
  faq=[("Trong tổ yến có chất gì?", "Tổ yến chủ yếu là protein dạng glycoprotein, cùng carbohydrate (trong đó có axit sialic), các axit amin, một ít khoáng chất và nước."),
       ("Tổ yến làm từ gì?", "Tổ yến được chim yến làm từ nước bọt; nước bọt khô lại thành sợi, đan chồng lên nhau thành tổ gắn trên vách nhà yến."),
       ("Yến sào bao nhiêu phần trăm protein?", "Protein là nhóm chiếm phần lớn khối lượng khô, nhưng tỷ lệ cụ thể khác nhau theo nguồn tổ, mùa và cách sơ chế. Số liệu chính xác cần xem phiếu kiểm nghiệm của từng lô."),
       ("Yến tinh chế có mất chất so với yến thô không?", "Yến tinh chế và yến thô cùng là sợi tổ yến; khác nhau chủ yếu ở việc đã loại bỏ lông và tạp chất. Khâu làm sạch dùng nước sạch và nhặt lông bằng tay."),
       ("Ăn yến có thay được thuốc không?", "Không. Yến sào là thực phẩm, không phải thuốc và không thay thế thuốc chữa bệnh. Người có bệnh nền nên hỏi bác sĩ.")]),
dict(slug="mua-yen-si-lam-dai-ly", cat="Yến sào", ngay="2026-11-17",
  tu_khoa="mua yến sỉ, mua yến sào sỉ, làm đại lý yến sào, nhập yến sào về bán, nguồn yến sỉ uy tín",
  h1="Mua yến sào sỉ, làm đại lý: cần chuẩn bị gì?",
  desc="Mua yến sỉ, làm đại lý yến sào cần chuẩn bị 6 việc: chọn kênh bán, chọn dòng sản phẩm, vốn và tồn kho, giấy tờ nguồn gốc, kiến thức tư vấn, bảo quản. Kèm cách liên hệ.",
  lede="Muốn mua yến sỉ hoặc làm đại lý yến sào, bạn nên chuẩn bị 6 việc trước khi nhập hàng: xác định kênh bán, chọn dòng sản phẩm hợp khách, tính vốn và lượng tồn kho, yêu cầu giấy tờ nguồn gốc từ nhà cung cấp, nắm kiến thức để tư vấn và chuẩn bị chỗ bảo quản. Chuẩn bị kỹ giúp bạn bán đều, ít tồn và giữ được khách lâu dài.",
  tom_tat=["6 việc cần chuẩn bị: kênh bán, dòng sản phẩm, vốn và tồn kho, giấy tờ nguồn gốc, kiến thức tư vấn, chỗ bảo quản.",
           "Nhà cung cấp nên có chứng nhận an toàn thực phẩm (HACCP, ISO 22000, GMP) và hồ sơ tự công bố sản phẩm.",
           "Người mới thường bắt đầu với 2–3 dòng dễ bán: yến tinh chế, yến thô và nước yến hũ.",
           "Việt Cường Nhân cung cấp yến thô cho các xưởng tinh chế trên toàn quốc và có sản phẩm tại nhiều chuỗi siêu thị.",
           "Giá sỉ và chính sách đại lý: nhắn Zalo 0978 094 739 để được tư vấn theo số lượng."],
  body=f"""  <h2>Mua yến sỉ, làm đại lý yến sào có gì khác?</h2>
  <p>Mua yến sỉ là nhập số lượng lớn một lần để bán lại hoặc dùng cho cơ sở kinh doanh; làm đại lý là hợp tác lâu dài với một nhà cung cấp, bán sản phẩm của họ theo chính sách riêng. Cả hai đều cần chuẩn bị giống nhau ở khâu chọn sản phẩm, vốn và giấy tờ.</p>
  <table><thead><tr><th>Tiêu chí</th><th>Mua sỉ</th><th>Làm đại lý</th></tr></thead><tbody>
  <tr><td>Cách nhập</td><td>Theo từng đơn, linh hoạt</td><td>Theo thỏa thuận hợp tác lâu dài</td></tr>
  <tr><td>Thương hiệu</td><td>Có thể bán theo thương hiệu nhà cung cấp</td><td>Bán sản phẩm, nhãn của nhà cung cấp</td></tr>
  <tr><td>Hỗ trợ</td><td>Tùy nhà cung cấp</td><td>Thường có hình ảnh, tư vấn sản phẩm</td></tr>
  <tr><td>Hợp với</td><td>Cửa hàng, quán, người mua làm quà số lượng lớn</td><td>Người muốn bán yến lâu dài, có kênh bán ổn định</td></tr>
  </tbody></table>

  <h2>6 việc cần chuẩn bị trước khi mua yến sỉ</h2>
  <h3>1. Xác định kênh bán</h3>
  <p>Kênh bán quyết định nên nhập loại yến nào và nhập bao nhiêu. Bán tại cửa hàng, bán online, bán cho người quen hay làm quà doanh nghiệp đều có nhóm khách và mức giá phù hợp khác nhau. Với quà biếu cuối năm, xem thêm bài <a href="qua-tang-doanh-nghiep-yen-sao.html">quà tặng doanh nghiệp yến sào</a>.</p>
  <h3>2. Chọn dòng sản phẩm hợp khách</h3>
  <p>Người mới thường bắt đầu với 2–3 dòng dễ bán thay vì nhập đủ loại:</p>
  <ul>
    <li><b>Yến tinh chế:</b> đã sạch lông, khách gia đình dễ dùng.</li>
    <li><b>Yến thô:</b> cho khách quen tự làm sạch, hoặc bán cho cơ sở tinh chế.</li>
    <li><b>Nước yến hũ:</b> giá thấp mỗi hũ, dễ bán lẻ và làm quà nhỏ.</li>
  </ul>
  <p>Hiểu rõ khác biệt từng loại qua bài <a href="yen-tho-yen-tinh-che-yen-rut-long-khac-nhau.html">yến thô, yến tinh chế và yến rút lông khác nhau thế nào</a>.</p>
  <h3>3. Tính vốn và lượng tồn kho</h3>
  <p>Yến sào giá cao nên vốn ban đầu đọng nhiều ở hàng tồn. Hãy nhập vừa đủ bán trong một khoảng thời gian ngắn, theo dõi loại nào bán chạy rồi mới tăng dần. Nước yến hũ có hạn dùng ghi trên nhãn, cần xoay vòng hàng theo ngày sản xuất.</p>
  <h3>4. Yêu cầu giấy tờ nguồn gốc</h3>
  <p>Giấy tờ là thứ giúp bạn trả lời khách khi được hỏi "yến này ở đâu ra". Nên yêu cầu nhà cung cấp:</p>
  <ul>
    <li>Thông tin doanh nghiệp: tên, mã số doanh nghiệp, địa chỉ cơ sở sản xuất.</li>
    <li>Chứng nhận an toàn thực phẩm còn hiệu lực, ví dụ HACCP, ISO 22000, GMP.</li>
    <li>Hồ sơ tự công bố sản phẩm cho đúng loại yến bạn nhập.</li>
    <li>Nhãn sản phẩm đầy đủ: tên, khối lượng, ngày sản xuất, hạn dùng.</li>
  </ul>
  <p>Ý nghĩa từng chứng nhận xem ở bài <a href="chung-nhan-haccp-iso-22000-gmp-la-gi.html">HACCP, ISO 22000 và GMP nghĩa là gì</a>.</p>
  <h3>5. Nắm kiến thức để tư vấn</h3>
  <p>Khách mua yến hay hỏi cách ngâm, chưng, ăn bao nhiêu, bà bầu hay trẻ nhỏ ăn được không. Người bán trả lời đúng và không nói quá công dụng sẽ giữ được khách lâu. Các câu hỏi thường gặp có trong mục <a href="./">Kiến thức</a>, ví dụ bài <a href="cach-chung-yen-sao.html">cách chưng yến sào</a>. Với câu hỏi về sức khỏe, nên khuyên khách hỏi bác sĩ.</p>
  <h3>6. Chuẩn bị chỗ bảo quản</h3>
  <p>Yến khô cần hộp kín, nơi khô ráo, tránh nắng và ẩm; nước yến hũ để nơi khô mát. Hướng dẫn chi tiết ở bài <a href="bao-quan-yen-sao.html">cách bảo quản yến sào</a>.</p>

  <h2>Chọn nguồn yến sỉ uy tín thế nào?</h2>
  <p>Nguồn yến sỉ uy tín là nơi minh bạch xuất xứ, có cơ sở sản xuất thật và giấy tờ đầy đủ. Một số câu nên hỏi nhà cung cấp:</p>
  <ol>
    <li>Yến lấy từ nhà yến nào, làm sạch ở đâu?</li>
    <li>Có thể đến xem xưởng không?</li>
    <li>Có giao hàng đều theo số lượng cam kết không?</li>
    <li>Xử lý thế nào khi hàng giao sai, thiếu hoặc hư hỏng?</li>
  </ol>

  <h2>Mua yến sỉ tại Việt Cường Nhân</h2>
  <p>Việt Cường Nhân có nhà yến tại Gò Công Tây (Tiền Giang cũ) và Bình Thuận, xưởng nhặt lông tại Lâm Đồng, xưởng tinh chế và nhà máy nước yến tại khu vực Dĩ An. Công ty cung cấp yến thô cho các xưởng tinh chế trên toàn quốc; sản phẩm có mặt tại nhiều chuỗi siêu thị và xuất khẩu sang Campuchia, Hàn Quốc. Thông tin thêm ở bài <a href="viet-cuong-nhan-la-ai.html">Việt Cường Nhân là ai</a>.</p>
  <p>Giá bán lẻ tham khảo trên website (chưa gồm phí giao hàng):</p>
""" + ul(li(101), li(109), li(128), li(130)) + """
  <p>Giá sỉ và chính sách đại lý phụ thuộc số lượng và dòng sản phẩm, vui lòng nhắn Zalo 0978 094 739 để được tư vấn. Bạn cũng có thể hẹn đến xưởng xem hàng trước khi nhập; địa chỉ ở bài <a href="yen-sao-binh-duong-di-an-mua-o-dau.html">mua yến sào ở Dĩ An</a>. Bảng giá lẻ đầy đủ xem tại <a href="../#san-pham">bảng giá sản phẩm</a>.</p>""",
  faq=[("Mua yến sỉ ở đâu uy tín?", "Nên chọn nơi có cơ sở sản xuất thật, công khai tên doanh nghiệp, chứng nhận an toàn thực phẩm và hồ sơ tự công bố sản phẩm, cho phép đến xem xưởng trước khi nhập."),
       ("Làm đại lý yến sào cần bao nhiêu vốn?", "Tùy kênh bán và dòng sản phẩm. Người mới nên nhập vừa đủ 2–3 dòng dễ bán, theo dõi loại bán chạy rồi tăng dần để không đọng vốn ở hàng tồn."),
       ("Mới bán yến nên nhập loại nào?", "Thường bắt đầu với yến tinh chế cho khách gia đình, yến thô cho khách quen tự làm sạch và nước yến hũ để bán lẻ, làm quà nhỏ."),
       ("Mua yến sỉ cần giấy tờ gì?", "Nên yêu cầu thông tin doanh nghiệp, chứng nhận an toàn thực phẩm còn hiệu lực, hồ sơ tự công bố sản phẩm và nhãn đầy đủ ngày sản xuất, hạn dùng."),
       ("Muốn làm đại lý Việt Cường Nhân liên hệ ai?", "Nhắn Zalo 0978 094 739 để được tư vấn giá sỉ và chính sách đại lý theo số lượng.")]),
dict(slug="yen-chung-sua-tuoi", cat="Món ngon", ngay="2026-11-17",
  tu_khoa="yến chưng sữa tươi, yến chưng hạt chia, cách làm yến chưng sữa tươi, yến sữa tươi hạt chia",
  h1="Yến chưng sữa tươi và yến chưng hạt chia cho cả nhà",
  desc="Cách làm yến chưng sữa tươi và yến chưng hạt chia tại nhà: nguyên liệu định lượng, các bước chưng cách thủy, thời gian, mẹo để sữa không bị tách và sợi yến vẫn dai.",
  lede="Yến chưng sữa tươi làm bằng cách chưng yến với nước trước khoảng 20–25 phút, để nguội bớt rồi mới thêm sữa tươi và hâm nhẹ, không đun sôi. Thêm hạt chia đã ngâm nở là có món yến chưng hạt chia mát, dễ ăn cho cả nhà.",
  tom_tat=["Mỗi chén dùng khoảng 3–5 g yến khô, 100 ml nước và 100 ml sữa tươi.",
           "Chưng yến với nước 20–25 phút trước, thêm sữa sau cùng để sữa không bị tách, sợi yến không bị nát.",
           "Hạt chia ngâm 10–15 phút cho nở, thêm vào khi yến đã nguội bớt.",
           "Yến chưng sữa để ngăn mát, đậy kín và dùng trong ngày.",
           f"Yến hợp món này: {P[109][2]} {gia(109)}/100gr hoặc {P[106][2]} {gia(106)}/100gr."],
  cac_buoc=[("Ngâm yến", "Ngâm 3–5 g yến khô trong nước sạch 30–60 phút cho nở mềm, vớt ra để ráo."),
            ("Chưng yến với nước", "Cho yến và 100 ml nước vào thố, chưng cách thủy lửa nhỏ 20–25 phút."),
            ("Thêm đường phèn", "Thêm đường phèn trong 5 phút cuối nếu muốn ngọt, khuấy cho tan."),
            ("Thêm sữa tươi", "Tắt bếp, để yến nguội bớt rồi thêm 100 ml sữa tươi, hâm nhẹ 2–3 phút, không để sôi."),
            ("Thêm hạt chia", "Cho 1 muỗng cà phê hạt chia đã ngâm nở, khuấy đều, dùng ấm hoặc để lạnh.")],
  body=f"""  <h2>Nguyên liệu yến chưng sữa tươi (1 chén)</h2>
  <p>Yến chưng sữa tươi chỉ cần 4 nguyên liệu chính, dễ tìm và làm trong khoảng 40 phút kể cả thời gian ngâm.</p>
  <table><thead><tr><th>Nguyên liệu</th><th>Định lượng</th><th>Ghi chú</th></tr></thead><tbody>
  <tr><td>Yến khô (tinh chế hoặc rút lông)</td><td>3–5 g</td><td>Yến vụn cũng được, giá mềm hơn</td></tr>
  <tr><td>Nước lọc</td><td>100 ml</td><td>Để chưng yến</td></tr>
  <tr><td>Sữa tươi</td><td>100 ml</td><td>Có đường hoặc không đường</td></tr>
  <tr><td>Đường phèn</td><td>Tùy khẩu vị</td><td>Bỏ qua nếu dùng sữa có đường</td></tr>
  <tr><td>Hạt chia (cho bản hạt chia)</td><td>1 muỗng cà phê</td><td>Ngâm trước 10–15 phút</td></tr>
  </tbody></table>

  <h2>Cách làm yến chưng sữa tươi: 5 bước</h2>
  <p>Điểm quan trọng nhất của yến chưng sữa tươi là chưng yến với nước trước, thêm sữa sau cùng. Sữa đun lâu dễ bị tách, đóng váng và làm món bị khét mùi.</p>
  <ol>
    <li><b>Ngâm yến:</b> ngâm 3–5 g yến khô trong nước sạch 30–60 phút cho nở mềm, vớt ra, xé sợi vừa ăn, để ráo.</li>
    <li><b>Chưng yến với nước:</b> cho yến và 100 ml nước vào thố có nắp, đặt vào nồi nước sôi lăn tăn, chưng lửa nhỏ 20–25 phút.</li>
    <li><b>Thêm đường phèn:</b> nếu dùng sữa không đường, thêm đường phèn trong 5 phút cuối, khuấy cho tan.</li>
    <li><b>Thêm sữa tươi:</b> tắt bếp, để yến nguội bớt vài phút rồi rót 100 ml sữa tươi vào, hâm nhẹ 2–3 phút trong nồi cách thủy, không để sôi.</li>
    <li><b>Hoàn thành:</b> dùng ấm, hoặc để nguội rồi cất ngăn mát để ăn lạnh.</li>
  </ol>
  <p>Cách ngâm và chưng yến cơ bản có ở bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Yến chưng hạt chia</h2>
  <p>Yến chưng hạt chia là bản biến tấu của yến chưng sữa tươi, thêm hạt chia cho món có độ sánh và giòn nhẹ.</p>
  <ul>
    <li><b>Ngâm hạt chia:</b> 1 muỗng cà phê hạt chia ngâm với 3–4 muỗng canh nước 10–15 phút cho nở thành lớp gel.</li>
    <li><b>Cho vào sau cùng:</b> thêm hạt chia khi yến chưng sữa đã nguội bớt, khuấy đều để hạt không vón cục.</li>
    <li><b>Không có sữa:</b> có thể làm yến chưng đường phèn hạt chia, thêm hạt chia vào chén yến đường phèn đã nguội.</li>
  </ul>

  <h2>So sánh 3 cách làm</h2>
  <table><thead><tr><th>Món</th><th>Thời gian</th><th>Vị</th><th>Hợp khi</th></tr></thead><tbody>
  <tr><td>Yến chưng sữa tươi</td><td>Khoảng 30 phút chưng</td><td>Béo nhẹ, thơm sữa</td><td>Ăn sáng, bữa xế</td></tr>
  <tr><td>Yến chưng sữa tươi hạt chia</td><td>Thêm 10–15 phút ngâm chia</td><td>Béo, sánh, giòn hạt</td><td>Ăn lạnh, đổi vị</td></tr>
  <tr><td>Yến chưng đường phèn hạt chia</td><td>Khoảng 30 phút chưng</td><td>Ngọt thanh</td><td>Người không uống sữa</td></tr>
  </tbody></table>

  <h2>Mẹo để yến chưng sữa ngon</h2>
  <ul>
    <li><b>Không chưng yến quá lâu:</b> quá 30 phút hoặc lửa to, sợi yến dễ tan, xem bài <a href="yen-bi-chay-nuoc-khi-chung.html">vì sao yến bị chảy nước khi chưng</a>.</li>
    <li><b>Không đun sôi sữa:</b> chỉ hâm ấm để sữa không tách.</li>
    <li><b>Đổi vị:</b> thêm vài quả <a href="tao-do-tan-cuong-cach-chon-va-mon-ngon.html">táo đỏ Tân Cương</a> hoặc kỷ tử khi chưng yến với nước.</li>
    <li><b>Bảo quản:</b> để nguội, đậy kín, cất ngăn mát và dùng trong ngày vì có sữa.</li>
  </ul>

  <h2>Lưu ý khi cho cả nhà dùng</h2>
  <p>Yến chưng sữa là món ăn, không phải thuốc. Trẻ nhỏ, bà bầu, người dị ứng sữa hoặc có bệnh nền nên hỏi bác sĩ trước khi ăn thường xuyên. Cho trẻ ăn thì xé sợi yến nhỏ, ngâm hạt chia thật nở; tham khảo thêm bài <a href="tre-may-tuoi-an-duoc-yen.html">trẻ mấy tuổi ăn được yến</a>.</p>

  <h2>Yến phù hợp để chưng sữa tươi</h2>
  <p>Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(109, "Sợi vừa, chưng sữa giữ sợi đẹp."), li(106, "Giá mềm, hợp nấu cho cả nhà hằng ngày.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a> hoặc nhắn Zalo 0978 094 739.</p>""",
  faq=[("Yến chưng sữa tươi có cần chưng sữa cùng yến không?", "Không nên. Chưng yến với nước trước 20–25 phút, thêm sữa sau cùng và chỉ hâm ấm để sữa không bị tách."),
       ("Một chén yến chưng sữa cần bao nhiêu yến?", "Khoảng 3–5 g yến khô, 100 ml nước và 100 ml sữa tươi cho một chén."),
       ("Yến chưng sữa để được bao lâu?", "Vì có sữa, nên để nguội, đậy kín, cất ngăn mát và dùng trong ngày."),
       ("Hạt chia cho vào yến lúc nào?", "Ngâm hạt chia 10–15 phút cho nở, cho vào khi yến chưng đã nguội bớt và khuấy đều."),
       ("Trẻ nhỏ ăn yến chưng sữa được không?", "Nên hỏi bác sĩ trước, nhất là trẻ dị ứng sữa. Khi cho ăn, xé sợi yến nhỏ và dùng lượng ít.")]),
dict(slug="sup-ga-yen-sao", cat="Món ngon", ngay="2026-11-17",
  tu_khoa="súp gà yến sào, cách nấu súp gà yến sào, súp yến gà bắp, súp yến cho tiệc",
  h1="Cách nấu súp gà yến sào cho bữa tiệc gia đình",
  desc="Cách nấu súp gà yến sào cho 6 người: nguyên liệu định lượng, ngâm yến, luộc gà lấy nước dùng, nấu súp sánh mịn với bắp, nấm, trứng. Thời gian, mẹo giữ sợi yến không tan.",
  lede="Súp gà yến sào nấu bằng nước luộc gà, thịt gà xé, bắp, nấm, trứng và yến đã ngâm nở, làm sánh bằng bột năng; yến cho vào cuối cùng, nấu thêm vài phút để giữ sợi. Một nồi cho khoảng 6 người cần 10 g yến khô và mất chừng 1 giờ kể cả thời gian luộc gà.",
  tom_tat=["Nồi súp 6 chén dùng khoảng 10 g yến khô, 400 g ức gà, 1 trái bắp, 100 g nấm, 2 quả trứng.",
           "Tổng thời gian khoảng 1 giờ: ngâm yến, luộc gà lấy nước dùng, nấu súp 15 phút.",
           "Cho yến vào sau khi súp đã sánh, đun lửa nhỏ 3–5 phút để sợi yến không tan.",
           "Yến vụn hoặc yến tinh chế vụn đắp tổ hợp nấu súp vì giá mềm và tơi sợi.",
           f"Ví dụ {P[106][2]} {gia(106)}/100gr, {P[107][2]} {gia(107)}/100gr."],
  cac_buoc=[("Ngâm yến", "Ngâm 10 g yến khô trong nước sạch 30–60 phút cho nở, vớt ra để ráo."),
            ("Luộc gà lấy nước dùng", "Luộc 400 g ức gà với 1,5 lít nước, gừng và hành tím khoảng 20 phút, vớt gà xé sợi, lọc nước dùng."),
            ("Nấu súp", "Cho bắp, nấm, cà rốt vào nước dùng, nấu 10 phút, thêm gà xé và nêm gia vị."),
            ("Làm sánh và thêm trứng", "Hòa bột năng với nước, đổ từ từ vào nồi và khuấy; đánh trứng, rót thành sợi vào súp."),
            ("Thêm yến", "Cho yến vào, đun lửa nhỏ 3–5 phút rồi tắt bếp, rắc hành ngò, tiêu.")],
  body=f"""  <h2>Nguyên liệu súp gà yến sào (6 chén)</h2>
  <p>Súp gà yến sào cho bữa tiệc gia đình khoảng 6 người cần các nguyên liệu sau:</p>
  <table><thead><tr><th>Nguyên liệu</th><th>Định lượng</th></tr></thead><tbody>
  <tr><td>Yến khô (vụn hoặc tinh chế)</td><td>10 g</td></tr>
  <tr><td>Ức gà hoặc đùi gà</td><td>400 g</td></tr>
  <tr><td>Nước</td><td>1,5 lít</td></tr>
  <tr><td>Bắp ngọt tách hạt</td><td>1 trái</td></tr>
  <tr><td>Nấm (nấm hương tươi, nấm đông cô hoặc nấm rơm)</td><td>100 g</td></tr>
  <tr><td>Cà rốt cắt hạt lựu</td><td>1/2 củ</td></tr>
  <tr><td>Trứng gà</td><td>2 quả</td></tr>
  <tr><td>Bột năng</td><td>2–3 muỗng canh</td></tr>
  <tr><td>Gừng, hành tím, hành lá, ngò, tiêu, muối, hạt nêm</td><td>Vừa đủ</td></tr>
  </tbody></table>
  <p>Ở xưởng Việt Cường Nhân, khách mua yến nấu súp thường chọn yến vụn vì giá mềm, sợi tơi dễ hòa vào súp; yến sợi đẹp hợp chưng hơn. Tìm hiểu thêm ở bài <a href="yen-vun-baby-la-gi.html">yến vụn baby là gì</a>.</p>

  <h2>Cách nấu súp gà yến sào: 5 bước</h2>
  <p>Cách nấu súp gà yến sào gồm 5 bước, khoảng 1 giờ. Điểm cần nhớ là cho yến vào sau cùng.</p>
  <ol>
    <li><b>Ngâm yến (30–60 phút):</b> ngâm 10 g yến khô trong nước sạch cho nở mềm, vớt ra, xé tơi, để ráo. Nếu dùng yến thô, cần làm sạch lông trước theo bài <a href="cach-lam-sach-yen-tho.html">cách làm sạch yến thô tại nhà</a>.</li>
    <li><b>Luộc gà lấy nước dùng (20 phút):</b> cho gà vào 1,5 lít nước cùng vài lát gừng, 2 củ hành tím đập dập, đun sôi rồi hạ lửa, vớt bọt. Gà chín vớt ra xé sợi; lọc nước dùng cho trong.</li>
    <li><b>Nấu súp (10 phút):</b> đun sôi lại nước dùng, cho bắp, nấm, cà rốt vào nấu đến khi chín mềm. Thêm gà xé, nêm muối, hạt nêm vừa ăn.</li>
    <li><b>Làm sánh và thêm trứng (3 phút):</b> hòa bột năng với ít nước nguội, vừa đổ từ từ vào nồi vừa khuấy đều đến khi súp sánh. Đánh tan trứng, rót thành dòng mảnh vào súp, khuấy nhẹ để trứng thành sợi.</li>
    <li><b>Thêm yến (3–5 phút):</b> cho yến vào, đun lửa nhỏ, khuấy nhẹ rồi tắt bếp. Múc ra chén, rắc hành lá, ngò, tiêu.</li>
  </ol>

  <h2>Mẹo nấu súp gà yến sào ngon</h2>
  <ul>
    <li><b>Yến cho sau cùng:</b> đun yến lâu trong nồi súp nóng sẽ làm sợi tan, mất độ dai. 3–5 phút lửa nhỏ là đủ.</li>
    <li><b>Nước dùng trong:</b> vớt bọt kỹ khi luộc gà; có thể thêm vài miếng xương gà để nước ngọt hơn.</li>
    <li><b>Súp không vón:</b> hòa bột năng với nước nguội, đổ từ từ và khuấy liên tục.</li>
    <li><b>Trứng thành sợi đẹp:</b> rót trứng khi súp đang sôi nhẹ, khuấy một chiều.</li>
    <li><b>Đổi vị:</b> thêm vài cọng <a href="cach-dung-dong-trung-ha-thao.html">đông trùng hạ thảo</a> hoặc cua xé cho bữa tiệc.</li>
  </ul>

  <h2>Súp gà yến sào cho tiệc: tính lượng thế nào?</h2>
  <p>Với súp khai vị, mỗi người thường dùng một chén nhỏ. Có thể nhân định lượng theo số khách:</p>
  <table><thead><tr><th>Số người</th><th>Yến khô</th><th>Gà</th><th>Nước</th></tr></thead><tbody>
  <tr><td>4 người</td><td>6–7 g</td><td>250–300 g</td><td>1 lít</td></tr>
  <tr><td>6 người</td><td>10 g</td><td>400 g</td><td>1,5 lít</td></tr>
  <tr><td>10 người</td><td>15–20 g</td><td>700 g</td><td>2,5 lít</td></tr>
  </tbody></table>

  <h2>Bảo quản súp còn dư</h2>
  <p>Súp nguội nên đậy kín, cất ngăn mát và dùng trong ngày; khi hâm lại chỉ đun lửa nhỏ, không nấu sôi lâu. Yến khô chưa dùng bảo quản theo bài <a href="bao-quan-yen-sao.html">cách bảo quản yến sào</a>.</p>
  <p>Súp gà yến là món ăn, không phải thuốc. Người có bệnh nền, bà bầu và trẻ nhỏ nên hỏi bác sĩ trước khi ăn thường xuyên; nấu cho bé thì tham khảo bài <a href="chao-yen-cho-be.html">cháo yến cho bé</a>.</p>

  <h2>Yến nấu súp tại Việt Cường Nhân</h2>
  <p>Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(106, "Đã nhặt sạch lông, hợp nấu súp, cháo."), li(107, "Sợi nhỏ, tơi, hợp món cho bé và súp.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a> hoặc nhắn Zalo 0978 094 739.</p>""",
  faq=[("Nấu súp gà yến sào cần bao nhiêu yến?", "Khoảng 10 g yến khô cho nồi súp 6 chén; 4 người dùng 6–7 g, 10 người dùng 15–20 g."),
       ("Khi nào cho yến vào súp?", "Cho yến vào sau cùng, khi súp đã sánh và có trứng, đun lửa nhỏ 3–5 phút rồi tắt bếp để sợi yến không tan."),
       ("Nấu súp nên dùng loại yến nào?", "Yến vụn hoặc yến tinh chế vụn đắp tổ hợp nấu súp vì giá mềm, sợi tơi; yến sợi đẹp nên dùng để chưng."),
       ("Súp gà yến để qua đêm được không?", "Nên dùng trong ngày. Súp còn dư để nguội, đậy kín, cất ngăn mát; hâm lại bằng lửa nhỏ."),
       ("Có thể thay gà bằng cua không?", "Được. Có thể dùng thịt cua xé hoặc kết hợp gà và cua; cách nấu tương tự, yến vẫn cho vào sau cùng.")]),
dict(slug="xa-bong-handmade-tbeauty", cat="Mỹ phẩm", ngay="2026-11-17",
  tu_khoa="xà bông handmade, xà bông thủ công, chọn mùi xà bông, cách dùng xà bông handmade, xà bông hương hoa",
  h1="Xà bông handmade: cách chọn mùi hương và cách dùng",
  desc="Xà bông handmade tại Việt Cường Nhân có hơn 20 mùi chia 4 nhóm: hoa, trái cây, hương ấm, tươi mát. Cách chọn mùi theo sở thích, cách dùng đúng, bảng giá theo từng cục.",
  lede="Chọn xà bông handmade dễ nhất là chọn theo nhóm mùi: hương hoa (sen, hồng, lan, mẫu đơn), trái cây (dứa, măng cụt, xoài, bưởi), hương ấm (gạo rang, vani, mật ong, bông cà phê) và tươi mát (trà xanh, bạc hà). Khi dùng, làm ướt xà bông, xoa tạo bọt trên tay hoặc bông tắm rồi mới thoa lên da, xả sạch và để cục xà bông khô ráo sau mỗi lần dùng.",
  tom_tat=["Xà bông thủ công tại Việt Cường Nhân có hơn 20 mùi, cục từ 67 g đến 140 g.",
           "4 nhóm mùi: hương hoa, trái cây, hương ấm, tươi mát; chọn theo sở thích và thời điểm dùng.",
           "Cách dùng: làm ướt, tạo bọt trên tay hoặc bông tắm, thoa nhẹ, xả sạch.",
           "Da nhạy cảm nên thử trên vùng da nhỏ trước; ngưng dùng nếu thấy khó chịu.",
           f"Giá từ {gia(201)}/cục 110g; có hộp quà 3 cục {gia(246)}."],
  body=f"""  <h2>Xà bông thủ công là gì?</h2>
  <p>Xà bông thủ công (xà bông handmade) là xà bông được làm theo mẻ nhỏ, đổ khuôn và cắt từng cục, nên mỗi cục có hình dáng, màu sắc riêng. Bên cạnh yến sào, Việt Cường Nhân có bán dòng xà bông thủ công với nhiều mùi hương, quy cách theo từng cục.</p>
  <p>Vì là sản phẩm làm theo mẻ, màu và vân trên từng cục có thể khác nhau đôi chút so với ảnh. Mùi hương là tiêu chí chọn chính.</p>

  <h2>Cách chọn mùi xà bông handmade</h2>
  <p>Cách chọn mùi xà bông handmade đơn giản nhất là chọn theo 4 nhóm mùi, rồi thử 1–2 mùi trong nhóm mình thích.</p>
  <table><thead><tr><th>Nhóm mùi</th><th>Mùi có sẵn</th><th>Hợp với</th></tr></thead><tbody>
  <tr><td>Hương hoa</td><td>Sen, hoa hồng, hoa lan, lyly, hoa mẫu đơn, hoa sứ, hoa hướng dương, bông bưởi</td><td>Người thích mùi dịu, nữ tính, dùng làm quà</td></tr>
  <tr><td>Trái cây</td><td>Dứa, măng cụt, xoài, bưởi, cam, dâu, nho, chuối, cherry, dừa</td><td>Người thích mùi ngọt, tươi vui, trẻ trung</td></tr>
  <tr><td>Hương ấm</td><td>Gạo rang, vani, mật ong, bắp, bông cà phê</td><td>Người thích mùi ấm, dễ chịu, dùng buổi tối</td></tr>
  <tr><td>Tươi mát</td><td>Trà xanh, bạc hà</td><td>Người thích mùi sạch, mát, dùng buổi sáng hoặc ngày nóng</td></tr>
  </tbody></table>

  <h3>Mẹo chọn mùi</h3>
  <ul>
    <li><b>Mới dùng lần đầu:</b> chọn mùi quen như sen, trà xanh, dừa.</li>
    <li><b>Dùng cho cả nhà:</b> chọn mùi nhẹ, dễ chịu như trà xanh, gạo rang.</li>
    <li><b>Làm quà:</b> chọn hương hoa hoặc hộp quà nhiều mùi để người nhận thử.</li>
    <li><b>Đổi mùi theo mùa:</b> mùa nóng dùng bạc hà, trà xanh; mùa mát dùng vani, mật ong.</li>
  </ul>

  <h2>Cách dùng xà bông handmade đúng cách</h2>
  <p>Xà bông handmade dùng như xà bông cục thông thường, nhưng nên tạo bọt trước khi thoa để dùng tiết kiệm và cục xà bông bền hơn.</p>
  <ol>
    <li><b>Làm ướt da và cục xà bông</b> bằng nước sạch.</li>
    <li><b>Tạo bọt:</b> xoa xà bông giữa hai lòng bàn tay hoặc trên bông tắm, lưới tạo bọt.</li>
    <li><b>Thoa bọt lên da</b>, massage nhẹ, tránh vùng mắt.</li>
    <li><b>Xả sạch</b> bằng nước, lau khô.</li>
    <li><b>Để cục xà bông lên khay thoát nước</b>, nơi khô ráo, không ngâm trong nước.</li>
  </ol>
  <p>Giữ cục xà bông khô giữa các lần dùng là cách đơn giản nhất để xà bông không bị nhũn và dùng được lâu, xem bài <a href="cach-giu-xa-bong-handmade-ben-lau.html">cách bảo quản xà bông handmade dùng bền</a>.</p>

  <h2>Lưu ý khi dùng</h2>
  <ul>
    <li>Da nhạy cảm nên thử trên một vùng da nhỏ ở cổ tay trước khi dùng toàn thân.</li>
    <li>Ngưng dùng nếu thấy đỏ, ngứa hoặc khó chịu; trường hợp kéo dài nên hỏi bác sĩ da liễu.</li>
    <li>Tránh để bọt dính vào mắt; nếu dính, rửa ngay bằng nhiều nước sạch.</li>
    <li>Dùng cho trẻ nhỏ thì người lớn nên hỏi ý kiến bác sĩ và trông chừng khi tắm.</li>
    <li>Xà bông là mỹ phẩm làm sạch, không phải thuốc.</li>
  </ul>

  <h2>Bảng giá xà bông thủ công tại Việt Cường Nhân</h2>
  <p>Giá lấy từ bảng giá website, chưa gồm phí giao hàng. Một số mùi tiêu biểu:</p>
""" + ul(li(201, "Tươi mát, hợp dùng hằng ngày."), li(207, "Hương ấm, dễ chịu."), li(211, "Hương hoa nhẹ."), li(222, "Hương hoa, cục lớn."), li(226, "Hương ấm ngọt."), li(246, "Hợp làm quà.")) + f"""
  <p>Xem đủ hơn 20 mùi và đặt hàng tại <a href="../#san-pham">bảng giá sản phẩm</a>. Muốn kết hợp xà bông với yến sào làm quà Tết, xem bài <a href="qua-tet-yen-sao.html">quà Tết yến sào</a>. Mua số lượng lớn làm quà tặng: nhắn Zalo 0978 094 739.</p>""",
  faq=[("Xà bông handmade có mấy mùi?", "Tại Việt Cường Nhân có hơn 20 mùi, chia 4 nhóm: hương hoa, trái cây, hương ấm và tươi mát."),
       ("Nên chọn mùi xà bông nào cho người mới dùng?", "Nên chọn mùi quen và nhẹ như sen, trà xanh hoặc dừa, rồi đổi sang mùi khác khi đã quen."),
       ("Dùng xà bông handmade thế nào cho đúng?", "Làm ướt da và xà bông, tạo bọt trên tay hoặc bông tắm, thoa nhẹ, xả sạch, rồi để cục xà bông lên khay thoát nước cho khô."),
       ("Da nhạy cảm dùng xà bông handmade được không?", "Nên thử trên vùng da nhỏ ở cổ tay trước. Nếu thấy đỏ, ngứa thì ngưng dùng và hỏi bác sĩ da liễu khi cần."),
       ("Xà bông thủ công giá bao nhiêu?", f"Tại Việt Cường Nhân, giá từ {gia(201)} cho cục 110g; hộp quà 3 cục giá {gia(246)}, chưa gồm phí giao hàng.")]),
dict(slug="cach-giu-xa-bong-handmade-ben-lau", cat="Mỹ phẩm", ngay="2026-11-17",
  tu_khoa="bảo quản xà bông handmade, cách giữ xà bông không bị nhũn, xà bông handmade bị nhũn, dùng xà bông cục bền lâu",
  h1="Cách bảo quản xà bông handmade dùng bền, không nhũn",
  desc="Cách bảo quản xà bông handmade để không bị nhũn: khay thoát nước, để nơi khô thoáng, tránh tia nước, cắt nhỏ, dùng luân phiên. Cách cất cục chưa dùng và xử lý khi bị mềm.",
  lede="Bảo quản xà bông handmade đúng cách chủ yếu là giữ cục xà bông khô giữa các lần dùng: đặt trên khay có lỗ thoát nước, để nơi thoáng, tránh tia nước chiếu trực tiếp và không ngâm trong nước đọng. Cục chưa dùng thì cất nơi khô mát, tránh nắng, gói giấy hoặc để trong hộp thoáng.",
  tom_tat=["Xà bông nhũn chủ yếu vì ngâm trong nước đọng hoặc để chỗ ẩm, không kịp khô giữa các lần dùng.",
           "Dùng khay có lỗ hoặc rãnh thoát nước, đặt xa vòi sen.",
           "Cắt cục lớn thành 2–3 miếng nhỏ, dùng từng miếng để phần còn lại luôn khô.",
           "Dùng luân phiên 2 cục để mỗi cục có thời gian khô.",
           "Cục chưa dùng cất nơi khô mát, tránh nắng, gói giấy hoặc hộp thoáng."],
  cac_buoc=[("Dùng khay thoát nước", "Đặt xà bông trên khay có lỗ hoặc rãnh thoát nước, không để nước đọng dưới cục."),
            ("Để xa tia nước", "Đặt khay ở nơi không bị vòi sen xối trực tiếp, thoáng khí."),
            ("Tạo bọt rồi cất", "Tạo bọt trên tay hoặc bông tắm rồi đặt xà bông lại khay ngay, không để cục ngâm nước."),
            ("Cắt nhỏ, dùng luân phiên", "Cắt cục lớn thành miếng nhỏ hoặc dùng luân phiên 2 cục để mỗi cục khô hẳn."),
            ("Cất cục chưa dùng", "Gói giấy hoặc để hộp thoáng, nơi khô mát, tránh nắng.")],
  body=f"""  <h2>Vì sao xà bông handmade bị nhũn?</h2>
  <p>Xà bông handmade bị nhũn chủ yếu vì tiếp xúc nước quá lâu và không kịp khô giữa các lần dùng. Khi cục xà bông nằm trong khay đọng nước hoặc ngay dưới vòi sen, lớp ngoài hút nước, mềm ra và tan nhanh.</p>
  <ul>
    <li>Khay đựng không thoát nước, cục xà bông ngâm trong nước đọng.</li>
    <li>Nhà tắm ẩm, ít thông gió, cục xà bông không khô được.</li>
    <li>Cầm cục xà bông chà trực tiếp lên da nhiều lần, mỗi lần dùng tốn nhiều.</li>
    <li>Để cục xà bông bị tia nước chiếu trong lúc tắm.</li>
  </ul>

  <h2>Cách bảo quản xà bông handmade đang dùng: 5 bước</h2>
  <p>Cách bảo quản xà bông handmade đang dùng gồm 5 thói quen đơn giản, giúp cục xà bông khô nhanh và bền hơn.</p>
  <ol>
    <li><b>Dùng khay thoát nước:</b> chọn khay có lỗ, rãnh hoặc khay gỗ có nan để nước chảy hết, cục xà bông không nằm trong vũng nước.</li>
    <li><b>Đặt xa tia nước:</b> để khay ở góc thoáng, không bị vòi sen xối trực tiếp. Nếu nhà tắm nhỏ, có thể mang khay ra ngoài sau khi tắm.</li>
    <li><b>Tạo bọt rồi cất ngay:</b> xoa xà bông trên tay hoặc bông tắm vài vòng để tạo bọt, rồi đặt cục xà bông lại khay. Không để cục xà bông trên sàn hay trong chậu nước.</li>
    <li><b>Cắt nhỏ, dùng luân phiên:</b> cục lớn cắt thành 2–3 miếng, dùng từng miếng; hoặc dùng luân phiên 2 cục khác mùi để mỗi cục có một ngày khô hẳn.</li>
    <li><b>Lau nhẹ khi quá ướt:</b> nếu cục xà bông còn ướt nhiều sau khi tắm, thấm nhẹ bằng khăn khô trước khi đặt lại khay.</li>
  </ol>

  <h2>So sánh các loại khay đựng xà bông</h2>
  <table><thead><tr><th>Loại khay</th><th>Thoát nước</th><th>Lưu ý</th></tr></thead><tbody>
  <tr><td>Khay phẳng, không lỗ</td><td>Kém, đọng nước</td><td>Dễ làm xà bông nhũn, nên tránh</td></tr>
  <tr><td>Khay có lỗ hoặc rãnh</td><td>Tốt</td><td>Đổ nước đọng ở đáy khay thường xuyên</td></tr>
  <tr><td>Khay gỗ có nan</td><td>Tốt</td><td>Để khay khô, vệ sinh định kỳ</td></tr>
  <tr><td>Túi lưới tạo bọt</td><td>Tốt</td><td>Treo lên sau khi dùng; tạo bọt nhiều, ít hao</td></tr>
  </tbody></table>

  <h2>Cách cất xà bông handmade chưa dùng</h2>
  <p>Xà bông chưa dùng nên cất nơi khô mát, tránh nắng và tránh ẩm để giữ màu và mùi hương.</p>
  <ul>
    <li>Để nguyên bao bì hoặc gói bằng giấy, đặt trong hộp thoáng.</li>
    <li>Không cất trong nhà tắm; tủ quần áo hoặc kệ khô ráo là chỗ hợp.</li>
    <li>Tránh nơi nắng chiếu trực tiếp hoặc gần bếp, nhiệt độ cao.</li>
    <li>Dùng trong thời hạn ghi trên bao bì.</li>
  </ul>
  <p>Một mẹo nhỏ: đặt vài cục xà bông chưa dùng trong tủ quần áo để quần áo có mùi thơm nhẹ.</p>

  <h2>Xà bông đã bị mềm, nhũn thì làm sao?</h2>
  <p>Xà bông mềm do ngấm nước thường vẫn dùng được nếu không có mùi lạ. Đặt cục xà bông ở nơi thoáng, trên khay thoát nước 1–2 ngày cho khô lại, sau đó dùng theo các bước trên. Nếu xà bông có mùi lạ, đổi màu bất thường hoặc gây khó chịu khi dùng thì nên bỏ.</p>
  <p>Mẩu xà bông nhỏ còn lại có thể gom vào túi lưới tạo bọt để dùng hết, không lãng phí.</p>

  <h2>Chọn xà bông thủ công tại Việt Cường Nhân</h2>
  <p>Cách chọn mùi theo sở thích có ở bài <a href="xa-bong-handmade-tbeauty.html">xà bông handmade: cách chọn mùi hương và cách dùng</a>. Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(201, "Tươi mát, dùng hằng ngày."), li(213, "Cục lớn 133g, có thể cắt đôi dùng dần."), li(246, "Dùng luân phiên hoặc làm quà.")) + """
  <p>Đặt hàng tại <a href="../#san-pham">bảng giá sản phẩm</a> hoặc nhắn Zalo 0978 094 739. Ngoài xà bông, Việt Cường Nhân còn có yến sào, nước yến và đông trùng hạ thảo, xem bài <a href="viet-cuong-nhan-la-ai.html">Việt Cường Nhân là ai</a>.</p>""",
  faq=[("Vì sao xà bông handmade nhanh bị nhũn?", "Chủ yếu vì cục xà bông ngâm trong nước đọng hoặc để nơi ẩm, không kịp khô giữa các lần dùng."),
       ("Để xà bông handmade ở đâu cho bền?", "Đặt trên khay có lỗ hoặc rãnh thoát nước, ở nơi thoáng và không bị vòi sen xối trực tiếp."),
       ("Xà bông bị mềm còn dùng được không?", "Thường vẫn dùng được nếu không có mùi lạ. Để nơi thoáng 1–2 ngày cho khô lại; nếu đổi màu, có mùi lạ thì nên bỏ."),
       ("Cất xà bông chưa dùng thế nào?", "Để nguyên bao bì hoặc gói giấy, cất trong hộp thoáng nơi khô mát, tránh nắng và không để trong nhà tắm."),
       ("Có nên cắt nhỏ xà bông không?", "Nên, với cục lớn. Cắt thành 2–3 miếng và dùng từng miếng giúp phần còn lại luôn khô, dùng được lâu hơn.")]),
dict(slug="yen-chung-gung-duong-phen", cat="Món ngon", ngay="2026-11-17",
  tu_khoa="yến chưng gừng, yến chưng gừng đường phèn, cách chưng yến với gừng, yến chưng gừng táo đỏ",
  h1="Yến chưng gừng đường phèn cho ngày se lạnh",
  desc="Cách làm yến chưng gừng đường phèn tại nhà: nguyên liệu cho 1 chén và 4 chén, 5 bước chưng cách thủy, lượng gừng vừa vị, mẹo không bị cay gắt, biến tấu với táo đỏ.",
  lede="Yến chưng gừng đường phèn làm bằng cách chưng yến đã ngâm với nước và vài lát gừng mỏng khoảng 20–25 phút, thêm đường phèn ở 5 phút cuối rồi vớt gừng ra. Món có vị ngọt thanh, thơm và ấm nhẹ của gừng, hợp ăn vào buổi sáng hay chiều tối những ngày trời se lạnh.",
  tom_tat=["Mỗi chén dùng 3–5 g yến khô, 150–200 ml nước, 2–3 lát gừng mỏng và đường phèn tùy khẩu vị.",
           "Chưng cách thủy lửa nhỏ 20–25 phút; thêm đường phèn 5 phút cuối.",
           "Vớt gừng ra sau khi chưng để vị không bị cay gắt.",
           "Có thể thêm 2–3 quả táo đỏ để vị ngọt hơn.",
           f"Yến hợp món này: {P[109][2]} {gia(109)}/100gr hoặc {P[106][2]} {gia(106)}/100gr."],
  cac_buoc=[("Ngâm yến", "Ngâm 3–5 g yến khô trong nước sạch 30–60 phút cho nở mềm, vớt ra để ráo."),
            ("Sơ chế gừng", "Gọt vỏ gừng, rửa sạch, thái 2–3 lát thật mỏng."),
            ("Chưng yến với gừng", "Cho yến, gừng và 150–200 ml nước vào thố, chưng cách thủy lửa nhỏ 20–25 phút."),
            ("Thêm đường phèn", "Thêm đường phèn trong 5 phút cuối, khuấy nhẹ cho tan."),
            ("Vớt gừng", "Tắt bếp, vớt lát gừng ra, dùng ấm.")],
  body=f"""  <h2>Nguyên liệu yến chưng gừng đường phèn</h2>
  <p>Yến chưng gừng chỉ cần 4 nguyên liệu: yến, gừng, đường phèn và nước. Định lượng cho 1 chén và cho cả nhà 4 chén:</p>
  <table><thead><tr><th>Nguyên liệu</th><th>1 chén</th><th>4 chén</th></tr></thead><tbody>
  <tr><td>Yến khô (tinh chế hoặc rút lông)</td><td>3–5 g</td><td>12–20 g</td></tr>
  <tr><td>Nước lọc</td><td>150–200 ml</td><td>600–800 ml</td></tr>
  <tr><td>Gừng tươi</td><td>2–3 lát mỏng</td><td>1 khúc khoảng 3 cm, thái lát</td></tr>
  <tr><td>Đường phèn</td><td>Tùy khẩu vị</td><td>Tùy khẩu vị</td></tr>
  <tr><td>Táo đỏ (tùy chọn)</td><td>2–3 quả</td><td>8–10 quả</td></tr>
  </tbody></table>

  <h2>Cách làm yến chưng gừng đường phèn: 5 bước</h2>
  <p>Cách làm yến chưng gừng giống cách chưng yến đường phèn thông thường, chỉ thêm gừng thái lát mỏng vào cùng lúc chưng.</p>
  <ol>
    <li><b>Ngâm yến (30–60 phút):</b> ngâm yến khô trong nước sạch đến khi nở mềm, vớt ra, xé sợi vừa ăn, để ráo.</li>
    <li><b>Sơ chế gừng:</b> gọt vỏ, rửa sạch, thái thật mỏng. Lát mỏng giúp mùi thơm ra nhanh mà không quá cay.</li>
    <li><b>Chưng yến với gừng (20–25 phút):</b> cho yến, gừng và nước vào thố có nắp, đặt vào nồi nước sôi lăn tăn, chưng lửa nhỏ.</li>
    <li><b>Thêm đường phèn:</b> cho đường phèn vào trong 5 phút cuối, khuấy nhẹ cho tan.</li>
    <li><b>Vớt gừng:</b> tắt bếp, vớt lát gừng ra để vị không bị cay gắt khi để lâu, múc ra chén dùng ấm.</li>
  </ol>
  <p>Các bước ngâm, chưng cơ bản xem thêm ở bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Mẹo để yến chưng gừng ngon</h2>
  <ul>
    <li><b>Ít gừng thôi:</b> 2–3 lát mỏng cho mỗi chén là đủ thơm; nhiều gừng sẽ át mùi yến.</li>
    <li><b>Không chưng quá lâu:</b> quá 30 phút hoặc lửa to làm sợi yến tan, xem bài <a href="yen-bi-chay-nuoc-khi-chung.html">vì sao yến bị chảy nước khi chưng</a>.</li>
    <li><b>Chọn gừng:</b> gừng tươi, vỏ mỏng, không dập úng.</li>
    <li><b>Đổi vị:</b> thêm 2–3 quả <a href="tao-do-tan-cuong-cach-chon-va-mon-ngon.html">táo đỏ Tân Cương</a> xẻ đôi, hoặc vài hạt kỷ tử ở 5 phút cuối.</li>
  </ul>

  <h2>So sánh yến chưng gừng với các cách chưng khác</h2>
  <table><thead><tr><th>Món</th><th>Vị</th><th>Hợp khi</th></tr></thead><tbody>
  <tr><td>Yến chưng gừng đường phèn</td><td>Ngọt thanh, thơm ấm</td><td>Ngày se lạnh, buổi sáng sớm, chiều tối</td></tr>
  <tr><td>Yến chưng đường phèn</td><td>Ngọt thanh, giữ mùi yến</td><td>Ăn hằng ngày</td></tr>
  <tr><td>Yến chưng táo đỏ hạt sen</td><td>Ngọt, bùi</td><td>Đổi vị, xem bài <a href="yen-chung-tao-do-hat-sen.html">yến chưng táo đỏ hạt sen</a></td></tr>
  <tr><td>Yến chưng sữa tươi</td><td>Béo nhẹ</td><td>Bữa xế, xem bài <a href="yen-chung-sua-tuoi.html">yến chưng sữa tươi</a></td></tr>
  </tbody></table>

  <h2>Bảo quản và lưu ý</h2>
  <p>Yến chưng gừng ngon nhất khi ăn ấm ngay sau khi chưng. Nếu còn dư, để nguội, đậy kín, cất ngăn mát và dùng trong vài ngày; khi ăn hâm cách thủy cho ấm.</p>
  <p>Yến chưng gừng là món ăn, không phải thuốc. Trẻ nhỏ, bà bầu và người có bệnh nền nên hỏi bác sĩ trước khi ăn thường xuyên; cho trẻ ăn thì giảm gừng hoặc bỏ gừng.</p>

  <h2>Yến phù hợp để chưng gừng</h2>
  <p>Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(109, "Sợi vừa, chưng giữ sợi đẹp."), li(106, "Giá mềm, hợp chưng cho cả nhà."), li(142, "Thêm vào khi chưng để đổi vị.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a> hoặc nhắn Zalo 0978 094 739.</p>""",
  faq=[("Chưng yến với gừng có được không?", "Được. Thêm 2–3 lát gừng mỏng khi chưng yến cách thủy, chưng 20–25 phút rồi vớt gừng ra, món có vị thơm ấm nhẹ."),
       ("Chưng yến gừng bao lâu?", "Chưng cách thủy lửa nhỏ khoảng 20–25 phút, thêm đường phèn trong 5 phút cuối."),
       ("Cho bao nhiêu gừng vào yến là vừa?", "Khoảng 2–3 lát gừng mỏng cho một chén 3–5 g yến khô. Nhiều gừng sẽ át mùi yến và cay."),
       ("Trẻ em ăn yến chưng gừng được không?", "Nên hỏi bác sĩ trước. Nếu cho trẻ ăn, nên giảm hoặc bỏ gừng và dùng lượng ít."),
       ("Yến chưng gừng để được bao lâu?", "Để nguội, đậy kín, cất ngăn mát và dùng trong vài ngày; hâm cách thủy trước khi ăn.")]),
dict(slug="che-yen-hat-sen-long-nhan", cat="Món ngon", ngay="2026-11-17",
  tu_khoa="chè yến hạt sen long nhãn, chè yến hạt sen, cách nấu chè yến long nhãn, chè yến sào",
  h1="Cách nấu chè yến hạt sen long nhãn tại nhà",
  desc="Cách nấu chè yến hạt sen long nhãn cho 4 chén: nguyên liệu định lượng, ninh hạt sen bở, ngâm long nhãn, chưng yến riêng rồi hợp lại. Thời gian, mẹo hạt sen không đắng.",
  lede="Chè yến hạt sen long nhãn nấu bằng cách ninh hạt sen đến khi bở, thêm long nhãn và đường phèn, rồi cho yến đã chưng riêng vào sau cùng. Một nồi 4 chén cần khoảng 10–15 g yến khô, 150 g hạt sen tươi và 50 g long nhãn, mất chừng 1 giờ.",
  tom_tat=["4 chén cần 10–15 g yến khô, 150 g hạt sen, 50 g long nhãn, 1 lít nước, đường phèn tùy khẩu vị.",
           "Ninh hạt sen 20–30 phút đến khi bở; bỏ tim sen để chè không đắng.",
           "Chưng yến riêng 20–25 phút rồi mới cho vào nồi chè để sợi yến không tan.",
           "Long nhãn cho vào 5–10 phút cuối để giữ vị ngọt, không bị nhừ.",
           f"Yến hợp nấu chè: {P[106][2]} {gia(106)}/100gr."],
  cac_buoc=[("Ngâm yến", "Ngâm 10–15 g yến khô trong nước sạch 30–60 phút cho nở, vớt ra để ráo."),
            ("Chưng yến riêng", "Chưng cách thủy yến với ít nước 20–25 phút."),
            ("Ninh hạt sen", "Rửa 150 g hạt sen, bỏ tim, ninh với 1 lít nước 20–30 phút đến khi bở."),
            ("Thêm long nhãn, đường phèn", "Cho 50 g long nhãn đã rửa và đường phèn vào, nấu thêm 5–10 phút."),
            ("Hợp yến vào chè", "Cho yến đã chưng vào nồi, khuấy nhẹ, tắt bếp.")],
  body=f"""  <h2>Nguyên liệu chè yến hạt sen long nhãn (4 chén)</h2>
  <p>Chè yến hạt sen long nhãn cần 5 nguyên liệu chính, dễ mua ở chợ và cửa hàng đồ khô:</p>
  <table><thead><tr><th>Nguyên liệu</th><th>Định lượng</th><th>Ghi chú</th></tr></thead><tbody>
  <tr><td>Yến khô</td><td>10–15 g</td><td>Yến vụn hoặc tinh chế đều được</td></tr>
  <tr><td>Hạt sen tươi</td><td>150 g</td><td>Hạt sen khô thì ngâm trước 2–3 tiếng</td></tr>
  <tr><td>Long nhãn sấy</td><td>50 g</td><td>Chọn loại cùi dày, màu nâu vàng, không mốc</td></tr>
  <tr><td>Nước lọc</td><td>1 lít</td><td>Thêm khoảng 100 ml để chưng yến</td></tr>
  <tr><td>Đường phèn</td><td>80–100 g</td><td>Tùy khẩu vị</td></tr>
  </tbody></table>

  <h2>Cách nấu chè yến hạt sen long nhãn: 5 bước</h2>
  <p>Bí quyết của chè yến là chưng yến riêng và cho vào sau cùng. Nếu nấu yến chung từ đầu với hạt sen, sợi yến sẽ tan trước khi hạt sen kịp bở.</p>
  <ol>
    <li><b>Ngâm yến (30–60 phút):</b> ngâm yến khô trong nước sạch đến khi nở mềm, xé tơi, để ráo.</li>
    <li><b>Chưng yến riêng (20–25 phút):</b> cho yến và khoảng 100 ml nước vào thố, chưng cách thủy lửa nhỏ.</li>
    <li><b>Ninh hạt sen (20–30 phút):</b> rửa hạt sen, dùng tăm đẩy bỏ tim sen. Cho vào nồi với 1 lít nước, đun sôi rồi hạ lửa nhỏ, ninh đến khi hạt sen bở mềm.</li>
    <li><b>Thêm long nhãn và đường phèn (5–10 phút):</b> long nhãn rửa nhanh qua nước, cho vào nồi cùng đường phèn, nấu thêm đến khi đường tan, long nhãn nở.</li>
    <li><b>Hợp yến vào chè:</b> cho phần yến đã chưng vào nồi, khuấy nhẹ, tắt bếp ngay.</li>
  </ol>
  <p>Cách ngâm và chưng yến chi tiết có ở bài <a href="cach-chung-yen-sao.html">cách chưng yến sào đường phèn tại nhà</a>.</p>

  <h2>Mẹo nấu chè yến ngon</h2>
  <ul>
    <li><b>Bỏ tim sen:</b> tim sen có vị đắng, để lại sẽ làm cả nồi chè đắng.</li>
    <li><b>Hạt sen không bị sượng:</b> ninh lửa nhỏ, không cho đường quá sớm vì đường làm hạt sen khó bở.</li>
    <li><b>Long nhãn cho sau:</b> nấu lâu long nhãn bị nhừ, nước chè đục.</li>
    <li><b>Ăn nóng hoặc lạnh:</b> mùa lạnh ăn ấm, mùa nóng để nguội rồi cất ngăn mát.</li>
    <li><b>Đổi vị:</b> thêm vài quả táo đỏ hoặc kỷ tử cùng lúc cho long nhãn.</li>
  </ul>

  <h2>Chè yến hạt sen long nhãn khác yến chưng hạt sen thế nào?</h2>
  <table><thead><tr><th>Món</th><th>Cách làm</th><th>Lượng yến</th><th>Hợp khi</th></tr></thead><tbody>
  <tr><td>Chè yến hạt sen long nhãn</td><td>Nấu nồi chè, yến cho sau cùng</td><td>10–15 g cho 4 chén</td><td>Đãi cả nhà, khách đến chơi</td></tr>
  <tr><td>Yến chưng hạt sen</td><td>Chưng từng thố</td><td>3–5 g mỗi chén</td><td>Ăn riêng từng phần, xem bài <a href="yen-chung-tao-do-hat-sen.html">yến chưng táo đỏ hạt sen</a></td></tr>
  </tbody></table>

  <h2>Bảo quản và lưu ý</h2>
  <p>Chè yến còn dư để nguội, đậy kín, cất ngăn mát và dùng trong vài ngày. Hâm lại bằng lửa nhỏ, không đun sôi lâu.</p>
  <p>Chè yến là món ăn, không phải thuốc. Long nhãn và đường phèn có vị ngọt, người cần hạn chế đường, bà bầu, trẻ nhỏ và người có bệnh nền nên hỏi bác sĩ trước khi ăn thường xuyên.</p>

  <h2>Yến nấu chè tại Việt Cường Nhân</h2>
  <p>Giá lấy từ bảng giá website, chưa gồm phí giao hàng:</p>
""" + ul(li(106, "Giá mềm, hợp nấu chè, súp."), li(109, "Sợi vừa, chè đẹp mắt hơn.")) + """
  <p>Đặt hàng qua <a href="../#san-pham">bảng giá sản phẩm</a> hoặc nhắn Zalo 0978 094 739.</p>""",
  faq=[("Nấu chè yến hạt sen long nhãn cần bao nhiêu yến?", "Khoảng 10–15 g yến khô cho nồi 4 chén, cùng 150 g hạt sen và 50 g long nhãn."),
       ("Có nên nấu yến chung với hạt sen từ đầu không?", "Không nên. Hạt sen cần ninh 20–30 phút, trong khi yến nấu lâu sẽ tan. Nên chưng yến riêng rồi cho vào sau cùng."),
       ("Vì sao chè hạt sen bị đắng?", "Thường do còn tim sen. Dùng tăm đẩy bỏ tim trước khi nấu."),
       ("Chè yến ăn nóng hay lạnh?", "Ăn được cả hai: ngày lạnh ăn ấm, ngày nóng để nguội rồi cất ngăn mát."),
       ("Chè yến để được bao lâu?", "Để nguội, đậy kín, cất ngăn mát và dùng trong vài ngày; hâm lại bằng lửa nhỏ.")]),
]
