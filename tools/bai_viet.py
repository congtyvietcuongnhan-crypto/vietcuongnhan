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
]
