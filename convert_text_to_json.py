import json
import re

text = """
# A
– a, ba, boa, ca, cha, choa, da, doa, đa, ga, gia, ha, hoa, *kha, khoa, la, loa, ma, na, nga, ngoa, nha, oa, pa, pha, qua, ra, roa, sa, soa, ta, tha, thoa, toa, tra, va, xa, xoa
– à, bà, cà, chà, dà, đà, gà, già, hà, hoà, khà, là, loà, mà, nà, ngà, nhà, nhoà, oà, phà, quà, rà, sà, tà, thà, thoà, toà, trà, và, xà, xoà
– ả, bả, cả, chả, dả, đả, gả, giả, hả, hoả, *khả, khoả, lả, *loả, mả, nả, ngả, nhả, phả, quả, rả, sả, tả, thả, thoả, toả, trả, vả, xả, xoả
– ã, bã, chã, dã, đã, gã, giã, lã, loã, mã, nã, ngã, ngoã, nhã, rã, sã, tã, thoã, trã, vã, xã, xoã
– á, bá, cá, chá, choá, dá, doá, đá, đoá, gá, goá, giá, há, hoá, khá, khoá, lá, loá, má, ná, nhá, phá, quá, rá, sá, tá, thá, *thoá, toá, trá, vá, xá, xoá
– ạ, bạ, cạ, chạ, dạ, doạ, đoạ, gạ, giạ, hạ, hoạ, lạ, mạ, nạ, quạ, rạ, sạ, tạ, toạ, vạ, xạ

# AC
– ác, bác, các, chác, choác, dác, đác, đoác, gác, giác, hác, hoác, khác, khoác, lác, mác, nác, ngác, ngoác, nhác, phác, quác, rác, sác, tác, thác, toác, trác, vác, xác, xoác
– bạc, cạc, chạc, choạc, dạc, đạc, gạc, hạc, khạc, lạc, *loạc, mạc, nạc, ngạc, ngoạc, nhạc, phạc, quạc, rạc, sạc, tạc, *thạc, toạc, trạc, vạc, xạc, xoạc

# ACH
– ách, bách, cách, chách, dách, đách, hách, khách, lách, mách, nách, ngách, nhách, oách, phách, quách, rách, sách, tách, thách, trách, vách, xách
– ạch, bạch, cạch, chạch, đạch, gạch, hạch, hoạch, lạch, mạch, ngạch, oạch, phạch, quạch, rạch, sạch, tạch, thạch, trạch, vạch, xạch, xoạch

# AI
– ai, bai, cai, chai, choai, dai, đai, gai, giai, hai, hoai, khai, khoai, lai, mai, nai, ngai, ngoai, nhai, nhoai, oai, phai, quai, rai, sai, tai, thai, *thoai, trai, vai, *xoai
– bài, cài, chài, choài, dài, đài, đoài, gài, hài, hoài, lài, loài, mài, nài, ngài, ngoài, nhài, nhoài, oài, quài, rài, sài, soài, tài, *thài, toài, vài, xài, xoài
– ải, bải, cải, chải, dải, giải, hải, hoải, *khải, khoải, *lải, mải, nải, ngải, ngoải, nhải, oải, phải, quải, rải, sải, soải, tải, thải, thoải, trải, vải, xải, xoải
– bãi, cãi, chãi, choãi, dãi, doãi, đãi, gãi, giãi, hãi, lãi, mãi, ngãi, nhãi, rãi, sãi, tãi, thãi, vãi
– ái, bái, cái, chái, choái, dái, đái, đoái, gái, hái, khái, khoái, lái, mái, nái, ngái, ngoái, nhái, oái, phái, quái, rái, sái, soái, tái, thái, thoái, toái, trái, vái, xái
– bại, choại, dại, đại, gại, giại, hại, hoại, lại, loại, mại, nại, ngại, ngoại, nhại, oại, quại, tại, thoại, toại, trại, vại

# AM
– am, cam, dam, đam, gam, giam, ham, kham, lam, nam, nham, ram, sam, tam, tham, xam
– chàm, dàm, đàm, hàm, làm, ngàm, nhàm, nhoàm, phàm, *sàm, tàm, tràm, vàm, xàm, xoàm
– *ảm, cảm, đảm, giảm, khảm, *lảm, nhảm, thảm, trảm, xảm
– hãm, lãm
– ám, bám, cám, dám, đám, giám, hám, khám, mám, nám, nhám, rám, *sám, tám, thám, trám, xám
– *cạm, chạm, dạm, đạm, giạm, hạm, lạm, *nạm, ngoạm, phạm, rạm, sạm, tạm, trạm, *vạm, xạm

# AN
– an, ban, can, chan, dan, đan, đoan, gan, gian, han, hoan, khan, khoan, lan, loan, man, nan, ngan, ngoan, nhan, oan, pan, quan, ran, san, tan, than, toan, van, voan, *xan, xoan
– bàn, càn, dàn, đàn, đoàn, gàn, giàn, hàn, hoàn, khàn, làn, loàn, màn, nàn, ngàn, nhàn, phàn, quàn, ràn, sàn, *soàn, tàn, toàn, tràn, vàn, xoàn
– bản, cản, đản, đoản, giản, khản, khoản, nản, nhản, oản, phản, quản, sản, tản, thản, toản
– dãn, doãn, giãn, hãn, hoãn, lãn, mãn, ngoãn, nhãn, noãn
– án, bán, cán, chán, choán, dán, đán, đoán, gán, gián, hán, hoán, khán, khoán, lán, nán, ngán, oán, phán, quán, rán, sán, *soán, tán, thán, *thoán, toán, trán, ván, xán
– bạn, cạn, chạn, dạn, đạn, đoạn, gạn, hạn, hoạn, lạn, loạn, mạn, nạn, ngạn, ngoạn, nhạn, phạn, rạn, sạn, soạn, vạn

# ANG
– ang, bang, *cang, chang, choang, dang, đang, gang, giang, hang, hoang, khang, khoang, lang, loang, mang, nang, ngang, nhang, oang, phang, quang, rang, sang, tang, thang, *thoang, toang, trang, vang, xang, xoang
– bàng, càng, chàng, choàng, dàng, đàng, đoàng, gàng, giàng, hàng, khàng, làng, *loàng, màng, nàng, ngàng, nhàng, oàng, phàng, quàng, ràng, sàng, tàng, toàng, tràng, vàng, *xàng, xoàng
– ảng, bảng, cảng, choảng, đảng, đoảng, giảng, hảng, hoảng, *khảng, khoảng, lảng, *loảng, mảng, *phảng, quảng, rảng, sảng, soảng, tảng, *thảng, thoảng, *trảng, vảng, xoảng
– đãng, hãng, hoãng, lãng, loãng, mãng, ngãng, nhãng, quãng, vãng
– áng, báng, cáng, cháng, choáng, dáng, đáng, giáng, háng, kháng, khoáng, láng, loáng, máng, náng, ngáng, nhoáng, quáng, ráng, sáng, táng, tháng, thoáng, toáng, tráng, váng, xáng
– bạng, chạng, choạng, dạng, giạng, hạng, khạng, lạng, *loạng, mạng, nạng, nhạng, nhoạng, quạng, rạng, soạng, tạng, toạng, trạng, vạng

# ANH
– anh, banh, canh, chanh, danh, doanh, đanh, ganh, gianh, hanh, khanh, khoanh, lanh, *loanh, manh, nanh, nhanh, oanh, panh, phanh, quanh, ranh, sanh, tanh, thanh, toanh, tranh, vanh, xanh
– bành, cành, chành, dành, doành, đành, đoành, gành, giành, hành, hoành, lành, mành, nành, ngành, nhành, *oành, phành, *quành, rành, sành, tành, thành, trành, vành, *xoành
– ảnh, bảnh, cảnh, dảnh, đảnh, gảnh, giảnh, hảnh, hoảnh, khảnh, khoảnh, lảnh, mảnh, ngảnh, ngoảnh, nhảnh, rảnh, sảnh, *thảnh, vảnh
– hãnh, lãnh, mãnh, rãnh, vãnh
– ánh, bánh, cánh, chánh, đánh, gánh, hánh, hoánh, khánh, lánh, mánh, nánh, nhánh, quánh, sánh, tánh, thánh, tránh, vánh
– bạnh, cạnh, chạnh, gạnh, hạnh, hoạnh, lạnh, mạnh, nạnh, ngạnh, nhạnh, quạnh, tạnh, *thạnh, trạnh, vạnh

# AO
– ao, bao, cao, chao, dao, đao, gao, giao, hao, khao, lao, mao, nao, ngao, ngoao, nhao, phao, rao, sao, tao, thao, trao, vao, xao
– ào, bào, cào, chào, dào, đào, gào, hào, lào, mào, nào, ngào, nhào, phào, quào, rào, sào, tào, thào, trào, vào, xào
– ảo, bảo, cảo, chảo, đảo, giảo, hảo, khảo, lảo, *nảo, nhảo, rảo, sảo, tảo, thảo, *trảo, xảo
– bão, chão, hão, lão, mão, não, ngão, nhão, rão
– áo, báo, cáo, cháo, *dáo, đáo, gáo, giáo, *háo, kháo, láo, máo, náo, ngáo, ngoáo, nháo, pháo, quáo, ráo, sáo, táo, tháo, tráo, váo, xáo
– bạo, cạo, chạo, dạo, đạo, gạo, *hạo, khạo, lạo, mạo, nạo, ngạo, nhạo, rạo, sạo, tạo, thạo, trạo, xạo

# AP
– áp, cáp, đáp, gáp, giáp, háp, kháp, láp, *náp, ngáp, ngoáp, nháp, pháp, ráp, sáp, táp, tháp, tráp, váp, xáp
– bạp, cạp, chạp, đạp, giạp, hạp, khạp, lạp, mạp, nạp, nhạp, oạp, rạp, sạp, tạp, thạp, vạp

# AT
– át, bát, cát, chát, dát, đát, giát, hát, khát, khoát, lát, loát, mát, nát, ngát, nhát, oát, phát, quát, rát, sát, soát, tát, *thát, thoát, toát, trát, vát, xát, xoát
– ạt, bạt, chạt, dạt, đạt, đoạt, gạt, giạt, hạt, hoạt, lạt, loạt, mạt, nạt, ngạt, nhạt, phạt, quạt, rạt, sạt, soạt, tạt, thoạt, trạt, vạt, xoạt

# AU
– au, cau, chau, đau, *gau, hau, khau, lau, mau, *ngau, nhau, phau, rau, sau, tau, thau, trau
– bàu, *càu, dàu, gàu, giàu, hàu, làu, màu, ngàu, nhàu, *quàu, tàu, tràu, xàu
– bảu, cảu, chảu, giảu, lảu, nhảu, rảu, trảu, xảu
– báu, cáu, cháu, đáu, gáu, háu, kháu, láu, máu, náu, ngáu, ráu, sáu, táu, tháu
– bạu, cạu, *lạu, quạu

# AY
– bay, cay, chay, day, đay, gay, hay, hoay, khay, lay, *loay, may, *moay, nay, ngay, *ngoay, nhay, *nhoay, phay, quay, ray, say, tay, thay, vay, xay, xoay
– bày, cày, chày, dày, đày, gày, giày, mày, này, ngày, quày, rày, tày, thày, vày
– bảy, chảy, dảy, đảy, gảy, khảy, lảy, mảy, nảy, ngoảy, nhảy, phảy, quảy, rảy, sảy, thảy, trảy, vảy, xảy
– dãy, đãy, gãy, giãy, hãy, nãy, rãy
– áy, cáy, cháy, dáy, đáy, gáy, háy, hoáy, kháy, khoáy, láy, máy, náy, ngáy, ngoáy, nháy, nhoáy, ráy, *táy, toáy, váy, xáy, xoáy
– cạy, chạy, dạy, gạy, lạy, mạy, nạy, ngoạy, nhạy, quạy, rạy, vạy

# ĂC
– *ắc, bắc, cắc, chắc, đắc, hắc, hoắc, khắc, lắc, mắc, *nắc, ngắc, ngoắc, nhắc, phắc, quắc, rắc, sắc, tắc, *thắc, trắc, vắc, xắc
– cặc, chặc, dặc, đặc, gặc, giặc, hặc, hoặc, khặc, *lặc, mặc, nặc, ngoặc, quặc, rặc, sặc, tặc, trặc, vặc

# ĂM
– *ăm, băm, căm, chăm, dăm, đăm, găm, giăm, hăm, khăm, lăm, măm, năm, ngăm, nhăm, oăm, phăm, *quăm, răm, săm, tăm, thăm, trăm, xăm
– bằm, cằm, chằm, dằm, đằm, gằm, giằm, hằm, khoằm, *lằm, nằm, nhằm, *quằm, rằm, tằm, trằm, vằm
– bẳm, hẳm, khẳm, lẳm, thẳm
– ẵm, bẵm, đẵm, giẵm
– cắm, chắm, đắm, gắm, hoắm, khắm, lắm, mắm, nắm, ngắm, nhắm, quắm, rắm, sắm, tắm, thắm, trắm, xắm
– bặm, cặm, chặm, dặm, đặm, gặm, giặm, *hặm, khặm, lặm, nhặm, quặm, rặm, sặm

# ĂN
– ăn, *băn, căn, chăn, dăn, khăn, khoăn, lăn, *loăn, *măn, năn, ngăn, nhăn, phăn, quăn, răn, săn, tăn, thăn, *thoăn, trăn, văn, xăn, xoăn
– *bằn, cằn, *chằn, dằn, đằn, gằn, giằn, hằn, hoằn, khằn, lằn, mằn, *ngằn, *ngoằn, nhằn, *oằn, quằn, rằn, tằn, *thằn, trằn, vằn
– bẳn, cẳn, dẳn, hẳn, hoẳn, khẳn, rẳn, mẳn, nhẳn, *tẳn, xoẳn
– chẵn, đẵn, nhẵn, sẵn
– bắn, cắn, chắn, đắn, gắn, hắn, khắn, khoắn, mắn, nắn, ngắn, nhắn, quắn, rắn, sắn, tắn, thắn, vắn, xắn, xoắn
– bặn, cặn, chặn, dặn, đặn, gặn, giặn, lặn, mặn, nặn, nhặn, quặn, rặn, tặn, trặn, vặn

# ĂNG
– *ăng, băng, căng, chăng, dăng, đăng, găng, giăng, hăng, hoăng, khăng, lăng, *loăng, măng, năng, nhăng, phăng, quăng, răng, săng, tăng, thăng, trăng, văng, xăng
– bằng, chằng, dằng, đằng, giằng, hằng, *khằng, lằng, *loằng, *nằng, ngoằng, nhằng, rằng, *sằng, tằng, thằng, vằng, xằng
– ẳng, cẳng, chẳng, dẳng, đẳng, khẳng, lẳng, ngẳng, nhẳng, oẳng, phẳng, quẳng, thẳng, vẳng
– bẵng, đẵng, gẵng, hẵng, hoẵng, lẵng, ngẵng, ngoẵng, nhẵng, xẵng
– ắng, *bắng, dắng, đắng, gắng, hắng, khắng, khoắng, lắng, mắng, nắng, nhắng, sắng, thắng, thoắng, trắng, vắng
– *bặng, chặng, *dặng, đặng, gặng, lặng, nặng, nhặng, quặng, rặng, tặng, thặng

# ĂP
– ắp, bắp, cắp, chắp, đắp, gắp, khắp, lắp, nắp, nhắp, phắp, quắp, rắp, sắp, tắp, thắp, xắp
– bặp, cặp, chặp, gặp, lặp, quặp

# ĂT
– ắt, bắt, cắt, chắt, choắt, dắt, đắt, gắt, giắt, hắt, hoắt, khắt, khoắt, lắt, *loắt, mắt, ngắt, ngoắt, nhắt, oắt, phắt, quắt, rắt, sắt, tắt, thắt, thoắt, trắt, vắt, xắt
– bặt, cặt, chặt, dặt, đặt, gặt, giặt, lặt, mặt, ngặt, ngoặt, nhặt, oặt, quặt, rặt, sặt, vặt

# ÂC
– bấc, cấc, gấc, giấc, khấc, lấc, nấc, ngấc, nhấc, quấc, tấc, xấc
– bậc, chậc

# ÂM
– âm, câm, châm, dâm, đâm, giâm, hâm, khâm, lâm, mâm, ngâm, nhâm, râm, sâm, tâm, thâm, trâm, vâm, xâm
– ầm, bầm, cầm, chầm, dầm, đầm, gầm, giầm, hầm, lầm, mầm, nầm, ngầm, nhầm, *phầm, rầm, sầm, tầm, thầm, trầm, xầm
– ẩm, bẩm, cẩm, chẩm, gẩm, hẩm, lẩm, mẩm, ngẩm, nhẩm, phẩm, rẩm, sẩm, tẩm, thẩm, trẩm, xẩm
– *ẫm, bẫm, cẫm, chẫm, dẫm, đẫm, gẫm, giẫm, lẫm, mẫm, ngẫm, rẫm, sẫm, thẫm, trẫm
– ấm, bấm, cấm, chấm, dấm, đấm, gấm, giấm, *hấm, *khấm, lấm, nấm, ngấm, nhấm, rấm, sấm, tấm, thấm
– *ậm, bậm, chậm, dậm, đậm, gậm, giậm, *hậm, mậm, nậm, ngậm, nhậm, rậm, sậm, *tậm, thậm, *trậm, *vậm

# ÂN
– ân, bân, cân, chân, dân, gân, *hân, huân, khân, khuân, lân, luân, *mân, ngân, nhân, phân, quân, rân, sân, tân, thân, trân, truân, tuân, vân, xuân
– bần, cần, chần, dần, đần, gần, giần, lần, mần, nần, ngần, nhần, nhuần, phần, quần, *rần, sần, tần, thần, thuần, trần, tuần, vần
– ẩn, bẩn, cẩn, chẩn, chuẩn, dẩn, khẩn, khuẩn, lẩn, *luẩn, mẩn, ngẩn, nhẩn, quẩn, sẩn, tẩn, thẩn, vẩn, xẩn, xuẩn, uẩn
– cẫn, dẫn, đẫn, lẫn, mẫn, nẫn, nhẫn, phẫn, quẫn, thẫn, thuẫn, *tuẫn, vẫn
– ấn, bấn, cấn, chấn, dấn, giấn, hấn, huấn, khấn, lấn, luấn, mấn, *nấn, ngấn, nhấn, phấn, quấn, rấn, sấn, tấn, trấn, tuấn, vấn
– bận, cận, chận, dận, đận, giận, hận, lận, luận, mận, nhận, nhuận, phận, quận, rận, tận, thận, thuận, trận, vận

# ÂNG
– bâng, câng, châng, dâng, khuâng, lâng, nâng, *nhâng, tâng, *trâng, vâng
– quầng, tầng, vầng
– hẩng, ngẩng, quẩng
– cẫng, hẫng, nẫng
– bấng, đấng, nấng
– nậng

# ÂP
– ấp, *bấp, cấp, chấp, dấp, gấp, *giấp, hấp, *khấp, lấp, *mấp, nấp, *ngấp, nhấp, *phấp, rấp, sấp, tấp, thấp, trấp, vấp, xấp
– ập, bập, cập, chập, dập, đập, gập, giập, hập, *khập, lập, mập, nập, ngập, nhập, phập, rập, sập, tập, thập, trập, vập, *xập

# ÂT
– ất, bất, cất, chất, đất, hất, khất, khuất, lất, mất, ngất, nhất, phất, quất, rất, sất, suất, tất, thất, truất, tuất, uất, vất, xuất
– bật, cật, chật, dật, đật, gật, giật, *khật, lật, luật, mật, ngật, nhật, phật, quật, rật, tật, thật, thuật, trật, vật

# ÂU
– âu, bâu, câu, châu, dâu, đâu, gâu, *giâu, hâu, khâu, lâu, mâu, nâu, ngâu, nhâu, râu, sâu, tâu, thâu, trâu, xâu
– *ầu, bầu, cầu, chầu, dầu, đầu, gầu, giầu, hầu, lầu, mầu, ngầu, nhầu, rầu, sầu, tầu, thầu, trầu, vầu, xầu
– ẩu, bẩu, cẩu, chẩu, dẩu, đẩu, hẩu, khẩu, lẩu, mẩu, nhẩu, tẩu, thẩu, trẩu, vẩu, xẩu
– chẫu, dẫu, gẫu, hẫu, mẫu, nẫu, ngẫu, phẫu
– ấu, bấu, cấu, chấu, dấu, đấu, gấu, giấu, hấu, khấu, mấu, nấu, ngấu, sấu, tấu, thấu, trấu, vấu, xấu
– ậu, bậu, cậu, chậu, dậu, đậu, giậu, hậu, lậu, mậu, nậu, ngậu, nhậu, sậu, tậu

# ÂY
– bây, cây, chây, dây, đây, gây, giây, hây, khuây, lây, mây, nây, ngây, *nguây, nhây, phây, quây, rây, sây, tây, thây, trây, vây, xây
– bầy, cầy, chầy, dầy, đầy, gầy, giầy, hầy, lầy, mầy, nầy, ngầy, nhầy, quầy, rầy, sầy, tầy, thầy, trầy, vầy
– ẩy, bẩy, dẩy, đẩy, gẩy, hẩy, khẩy, lẩy, mẩy, nẩy, nguẩy, nhẩy, phẩy, quẩy, rẩy, sẩy, tẩy, trẩy, vẩy, xẩy
– bẫy, dẫy, đẫy, gẫy, giẫy, lẫy, nẫy, nhẫy, quẫy, rẫy, vẫy
– ấy, bấy, cấy, chấy, dấy, đấy, gấy, giấy, hấy, khuấy, lấy, mấy, nấy, ngấy, quấy, sấy, tấy, thấy, vấy
– bậy, cậy, dậy, đậy, gậy, lậy, mậy, nậy, ngậy, nguậy, nhậy, quậy, sậy, vậy

# E
– be, che, *choe, de, đe, e, ghe, gie, he, hoe, ke, khe, khoe, le, loe, me, ne, nghe, ngoe, nhe, nhoe, oe, phe, que, re, se, te, the, toe, tre, ve, xe, xoe
– bè, chè, choè, dè, đè, è, ghè, hè, hoè, kè, khè, lè, loè, mè, nè, nghè, nhè, nhoè, phè, què, rè, sè, tè, thè, toè, vè, xè, xoè
– bẻ, chẻ, dẻ, đẻ, ghẻ, giẻ, kẻ, khẻ, khoẻ, lẻ, mẻ, nẻ, nhẻ, oẻ, quẻ, rẻ, sẻ, tẻ, thẻ, toẻ, trẻ, vẻ, xẻ
– bẽ, chẽ, dẽ, đẽ, ghẽ, kẽ, khẽ, lẽ, mẽ, nhẽ, quẽ, rẽ, sẽ, tẽ, *thẽ, toẽ, trẽ, vẽ
– bé, ché, choé, dé, đé, é, ghé, gié, hé, ké, khé, khoé, lé, loé, mé, né, nghé, ngoé, nhé, oé, qué, ré, té, thé, toé, vé, xé
– bẹ, choẹ, ẹ, ghẹ, hẹ, hoẹ, kẹ, lẹ, mẹ, nẹ, nghẹ, nhẹ, oẹ, sẹ, trẹ

# EC
– *béc, đéc, éc, héc, *kéc, léc, méc, *phéc, séc, *véc
– *bẹc, ẹc, khẹc, *vẹc

# EM
– bem, đem, em, hem, kem, khem, lem, nem, nhem, tem, xem
– bèm, *chèm, *đèm, gièm, hèm, kèm, *lèm, mèm, nhèm, rèm, *tèm, thèm, trèm
– bẻm, hẻm, lẻm, nhẻm
– hẽm, kẽm
– chém, dém, đém, ém, ghém, kém, lém, mém, ném, sém, tém
– lẹm, nhẹm, vẹm

# EN
– ben, chen, *choen, den, đen, en, ghen, gien, hen, hoen, ken, khen, khoen, len, *loen, men, nen, nghen, *ngoen, nhen, *nhoen, phen, quen, ren, sen, ten, then, *toen, ven, xen, *xoen
– bèn, chèn, choèn, *dèn, đèn, ghèn, hèn, kèn, khèn, lèn, mèn, *nghèn, nhoèn, phèn, quèn, rèn, thèn, *toèn, *xèn, *xoèn
– ẻn, hẻn, hoẻn, lẻn, ngoẻn, nhoẻn, sẻn, vẻn, *xẻn
– *bẽn, chẽn, lẽn, nghẽn, tẽn, trẽn
– bén, chén, én, hén, kén, khén, lén, mén, nén, nghén, nhén, quén, rén, vén, xén
– bẹn, *chẹn, đẹn, hẹn, *kẹn, lẹn, nghẹn, nhẹn, thẹn, vẹn

# ENG
– beng, cheng, eng, keng, *leng, teng, meng
– phèng, xèng
– chẻng, kẻng, lẻng, rẻng, xẻng
– béng, léng, phéng

# EO
– beo, cheo, deo, đeo, eo, gieo, heo, keo, kheo, khoeo, leo, meo, neo, nheo, pheo, queo, reo, seo, teo, theo, treo, veo, xeo
– bèo, chèo, đèo, *èo, hèo, kèo, khoèo, lèo, mèo, nèo, nghèo, ngoèo, nhèo, phèo, quèo, sèo, tèo, *thèo, trèo, vèo, xèo
– bẻo, *chẻo, dẻo, ẻo, hẻo, kẻo, khoẻo, lẻo, nẻo, nghẻo, ngoẻo, rẻo, *tẻo, thẻo, trẻo, vẻo, xẻo
– bẽo, đẽo, *ẽo, *kẽo, lẽo, nghẽo, nhẽo, xẽo
– béo, chéo, đéo, éo, *giéo, héo, kéo, khéo, léo, méo, néo, ngoéo, nhéo, quéo, réo, téo, tréo, véo, xéo
– bẹo, chẹo, ẹo, ghẹo, giẹo, kẹo, lẹo, mẹo, nghẹo, ngoẹo, nhẹo, quẹo, sẹo, tẹo, thẹo, trẹo, vẹo, xẹo

# EP
– bép, chép, dép, ép, ghép, kép, khép, lép, mép, nép, nhép, phép, tép, thép, xép
– bẹp, dẹp, đẹp, ẹp, giẹp, hẹp, kẹp, lẹp, mẹp, nẹp, nhẹp, *tẹp, xẹp

# ET
– bét, chét, đét, *ét, ghét, hét, hoét, két, khét, khoét, lét, loét, mét, nét, nghét, ngoét, nhét, nhoét, phét, quét, rét, sét, tét, thét, toét, trét, vét, xét, xoét
– bẹt, chẹt, choẹt, dẹt, đẹt, ẹt, kẹt, lẹt, loẹt, mẹt, nẹt, nghẹt, nhẹt, nhoẹt, quẹt, rẹt, tẹt, toẹt, trẹt, vẹt, xẹt, xoẹt

# Ê
– bê, chê, dê, đê, ê, ghê, giê, hê, huê, kê, khê, khuê, lê, mê, nê, nghê, *pê, phê, quê, rê, sê, suê, tê, thê, thuê, trê, vê, xê, xuê
– bề, chề, dề, đề, ề, ghề, hề, huề, kề, *khề, lề, mề, nề, nghề, *phề, rề, sề, tề, thề, trề, về, *xề, *xuề
– bể, dể, để, *hể, kể, lể, nể, nghể, nhể, rể, sể, tể, thể, *uể, xể, xuể
– bễ, dễ, đễ, hễ, lễ, mễ, nghễ, *nhễ, rễ, tễ, trễ
– bế, chế, dế, đế, ế, ghế, huế, kế, khế, mế, phế, quế, rế, tế, thế, thuế, tuế, uế, vế, xế
– bệ, chệ, dệ, duệ, đệ, hệ, huệ, kệ, *khệ, lệ, mệ, nệ, nghệ, nhuệ, phệ, quệ, rệ, sệ, tệ, thệ, trệ, tuệ, vệ, xệ

# ÊCH
– chếch, đếch, ếch, ghếch, hếch, huếch, kếch, *khuếch, *lếch, *mếch, nghếch, *nguếch, nhếch, phếch, *rếch, tếch, thếch, tuếch, vếch, xếch
– bệch, chệch, *chuệch, dệch, ệch, ghệch, hệch, kệch, lệch, nghệch, *nguệch, nhệch, *quệch, rệch, trệch, xệch, *xuệch

# ÊM
– chêm, đêm, êm, nêm, rêm, têm, thêm
– đềm, kềm, mềm, thềm, *xềm
– *chễm
– *chếm, đếm, ếm, nếm
– đệm, nệm

# ÊN
– bên, hên, kên, lên, *mên, nên, phên, quên, rên, sên, tên, trên, vên, xên
– bền, dền, đền, giền, kền, mền, nền, rền, *sền, vền
– *bển, hển, *nghển, *trển
– bến, đến, hến, mến, nến, rến, sến
– bện, chện, dện, nện, nghện, nhện, quện, rện, thện, vện

# ÊNH
– bênh, chênh, dênh, đênh, hênh, *huênh, kênh, khênh, lênh, mênh, nênh, nghênh, *nhênh, sênh, tênh, thênh, vênh, xênh
– bềnh, chềnh, dềnh, *duềnh, đềnh, *đuềnh, ềnh, ghềnh, *hềnh, kềnh, khềnh, lềnh, rềnh, *tuềnh, *xềnh, *xuềnh
– chểnh, *đểnh, *đuểnh, ghểnh, hểnh, khểnh, nghểnh, sểnh, tểnh, vểnh, xểnh
– *chễnh, ễnh, kễnh, khễnh, *nghễnh, tễnh
– chếnh, *chuếnh, *trếnh
– bệnh, *chệnh, *chuệnh, kệnh, *khệnh, lệnh, mệnh, phệnh

# ÊP
– bếp, kếp, nếp, *sếp, thếp, xếp
– đệp, rệp, tệp, xệp

# ÊT
– bết, chết, dết, hết, kết, lết, mết, nết, phết, quết, rết, tết, thết, trết, vết
– bệt, dệt, ghệt, hệt, *lệt, mệt, phệt, quệt, rệt, sệt, trệt, vệt, xệt

# ÊU
– bêu, đêu, êu, kêu, khêu, lêu, nêu, nghêu, rêu, sêu, têu, thêu, trêu, vêu, xêu
– bều, đều, kều, khều, lều, nghều, phều, *quều, rều, sều, *thều, vều, xều
– đểu, *lểu, nghểu, nhểu, thểu
– *nghễu, phễu
– hếu, kếu, lếu, mếu, nếu, *nhếu, phếu, sếu, tếu, *trếu, vếu
– bệu, nghệu, rệu, trệu

# I
– bi, chi, di, duy, đi, ghi, gi, hi, huy, i, khi, khuy, ki, li, mi, ni, nghi, nguy, nhi, pi, phi, phuy, quy, ri, si, suy, thi, ti, tri, truy, tuy, uy, vi, xi, y
– bì, chì, chuỳ, dì, đì, ghì, gì, hì, ì, khì, kì, lì, mì, nì, nghì, nhì, phì, quỳ, rì, sì, thì, thuỳ, tì, truỳ, trì, tuỳ, vì, xì, xuỳ, ỳ
– bỉ, chỉ, gỉ, hỉ, huỷ, ỉ, khỉ, kỉ, mỉ, nghỉ, nhỉ, nỉ, phỉ, quỷ, rỉ, sỉ, thỉ, thuỷ, tỉ, tuỷ, uỷ, vỉ, xỉ, ỷ
– bĩ, dĩ, đĩ, hĩ, kĩ, lĩ, luỹ, mĩ, nghĩ, nhĩ, quỹ, rĩ, sĩ, thĩ, tĩ, trĩ, vĩ
– bí, chí, *dí, gí, hí, huý, *í, khí, kí, lí, luý, mí, *nghí, nhí, phí, quý, rí, suý, thí, thuý, tí, trí, tuý, uý, ví, xí, xuý, ý
– bị, chị, dị, ị, khuỵ, kị, lị, luỵ, mị, nghị, nguỵ, nhị, nhuỵ, phị, quỵ, rị, sị, thị, thuỵ, tị, trị, truỵ, tuỵ, vị, xị

# IA
– bia, chia, hia, khuya, kia, lia, luya, mia, nia, ria, thia, tia, tuya, xuya
– bìa, chìa, dìa, đìa, kìa, lìa, phìa, rìa, thìa, xìa
– đỉa, ỉa, mỉa, rỉa, sỉa, tỉa, trỉa, vỉa, xỉa
– chĩa, dĩa, đĩa, nghĩa, nĩa
– khía, mía, nghía, nhía, phía, thía, tía, vía, xía
– bịa, chịa, địa, gịa, khịa, lịa, phịa, rịa, sịa, tịa, *trịa

# ICH
– bích, chích, đích, gích, hích, huých, ích, khích, kích, *lích, luých, mích, nhích, ních, phích, quých, rích, thích, tích, trích, vích, xích
– bịch, dịch, địch, hịch, huỵch, ịch, kịch, lịch, mịch, nghịch, nịch, phịch, rịch, thịch, tịch, trịch, uỵch

# IÊC
– biếc, chiếc, diếc, điếc, ghiếc, giếc, liếc, nhiếc, siếc, thiếc, tiếc, xiếc
– diệc, tiệc, việc

# IÊM
– chiêm, diêm, điêm, khiêm, kiêm, liêm, nghiêm, niêm, thiêm, tiêm, viêm, xiêm
– diềm, điềm, hiềm, kiềm, liềm, niềm, riềm, *tiềm
– điểm, hiểm, kiểm, *siểm, thiểm, xiểm, yểm
– diễm, liễm, *nghiễm, nhiễm
– biếm, chiếm, điếm, giếm, hiếm, *khiếm, kiếm, liếm, phiếm, tiếm, yếm
– *diệm, điệm, kiệm, liệm, niệm, nghiệm, nhiệm, tiệm

# IÊN
– biên, chiên, chuyên, diên, duyên, điên, hiên, huyên, khiên, khuyên, kiên, liên, miên, niên, nghiên, nguyên, nhiên, phiên, quyên, riên, thiên, thuyên, tiên, *tuyên, uyên, viên, xiên, xuyên, yên
– biền, chiền, chuyền, điền, ghiền, hiền, huyền, khiền, kiền, liền, miền, nghiền, nguyền, phiền, quyền, thiền, thuyền, tiền, tuyền, triền, truyền, viền
– biển, chuyển, điển, hiển, khiển, khuyển, quyển, suyển, thiển, triển, tuyển, *viển, uyển
– diễn, *huyễn, liễn, miễn, nhiễn, nhuyễn, suyễn, tiễn, viễn
– biến, chiến, chuyến, điến, hiến, khiến, *khuyến, kiến, liến, luyến, miến, nghiến, phiến, quyến, tiến, tuyến, xuyến, yến
– biện, chiện, chuyện, diện, điện, hiện, huyện, kiện, luyện, miện, nghiện, nguyện, phiện, quyện, thiện, tiện, triện, truyện, viện

# IÊNG
– chiêng, điêng, giêng, *hiêng, khiêng, kiêng, liêng, nghiêng, riêng, siêng, thiêng, *tiêng, triêng, *yêng
– chiềng, diềng, giềng, kiềng, *niềng, riềng, tiềng, thiềng, triềng, xiềng
– kiểng, liểng, xiểng, yểng
– khiễng, kiễng, niễng
– biếng, chiếng, điếng, giếng, hiếng, kiếng, liếng, miếng, tiếng, viếng
– khiệng, liệng, miệng

# IÊP
– chiếp, diếp, hiếp, khiếp, kiếp, liếp, nhiếp, thiếp, tiếp
– diệp, điệp, hiệp, liệp, nghiệp, thiệp, tiệp
# IÊT
– biết, chiết, diết, giết, huyết, khiết, khuyết, kiết, miết, *niết, phiết, quyết, riết, siết, thiết, thuyết, tiết, triết, tuyết, viết, xiết, xuyết, yết
– biệt, diệt, duyệt, hiệt, huyệt, kiệt, liệt, miệt, niệt, nghiệt, nguyệt, nhiệt, phiệt, quyệt, riệt, thiệt, tiệt, triệt, tuyệt, việt

# IÊU
– chiêu, diêu, điêu, *khiêu, kiêu, liêu, miêu, niêu, nhiêu, *phiêu, riêu, siêu, thiêu, tiêu, xiêu, yêu
– chiều, diều, điều, kiều, liều, miều, nhiều, thiều, tiều, triều
– biểu, chiểu, điểu, hiểu, kiểu, thiểu, tiểu, yểu
– diễu, giễu, liễu, miễu, nhiễu, riễu, tiễu
– biếu, chiếu, diếu, điếu, hiếu, khiếu, kiếu, miếu, phiếu, riếu, thiếu, tiếu, yếu
– diệu, điệu, hiệu, kiệu, liệu, niệu, phiệu, thiệu, triệu

# IM
– chim, dim, ghim, him, im, kim, lim, phim, rim, sim, tim
– bìm, chìm, dìm, ghìm, kìm, lìm, tìm
– ỉm, mỉm, nghỉm, tỉm
– hĩm, mĩm
– bím, chím, dím, mím, nhím, phím, thím, tím
– lịm, vịm

# IN
– bin, din, đin, hin, in, khin, lin, luyn, min, nin, gin, phin, rin, sin, pin, *thin, tin, tuyn, vin, xin
– gìn, *ìn, *khìn, kìn, mìn, nghìn, nhìn, thìn
– chỉn, ỉn, xỉn
– chĩn, dĩn, rĩn, tĩn
– chín, ín, kín, nín, nhín, thín, tín
– *bịn, mịn, nhịn, rịn, vịn, xịn

# INH
– binh, chinh, dinh, đinh, huynh, *inh, khinh, khuynh, kinh, linh, minh, ninh, nghinh, *nhinh, *phinh, rinh, sinh, thinh, tinh, trinh, vinh, xinh
– bình, chình, đình, hình, huỳnh, ình, khuỳnh, kình, lình, mình, phình, quỳnh, rình, sình, thình, tình, trình, *uỳnh, xình
– bỉnh, chỉnh, đỉnh, hỉnh, khỉnh, khuỷnh, kỉnh, lỉnh, nghỉnh, nhỉnh, phỉnh, quỷnh, rỉnh, thỉnh, tỉnh, xỉnh
– bĩnh, chĩnh, *dĩnh, đĩnh, hĩnh, ĩnh, nghĩnh, phĩnh, tĩnh, trĩnh, vĩnh, xĩnh
– bính, chính, dính, đính, ghính, kính, lính, nính, nhính, phính, quýnh, sính, thính, tính, xính
– bịnh, định, lịnh, nịnh, thịnh, tịnh, *trịnh, vịnh

# IP
– *bíp, chíp, díp, gíp, híp, khuýp, kíp, líp, míp, níp, nhíp, típ, tuýp
– bịp, dịp, kịp, nhịp, quỵp, rịp

# IT
– bít, buýt, chít, đít, hít, huýt, ít, khít, kít, lít, mít, nít, nguýt, nhít, *pít, quýt, rít, sít, suýt, thít, tít, trít, *tuýt, vít, xít, xuýt
– bịt, chịt, dịt, địt, ghịt, ịt, khịt, kịt, mịt, nghịt, nhịt, nịt, quỵt, rịt, sịt, suỵt, thịt, tịt, trịt, vịt, xịt, xuỵt

# IU
– chiu, điu, hiu, iu, khiu, liu, niu, nghiu, phiu, riu, thiu, tiu
– bìu, dìu, đìu, lìu, rìu, thìu, *trìu, xìu
– bỉu, ỉu, khuỷu, lỉu, nghỉu, nguỷu, nhỉu, thỉu, xỉu
– bĩu, *kĩu, tĩu, trĩu
– bíu, chíu, díu, khíu, líu, míu, nhíu, níu, *quýu, ríu, tíu, tríu, víu, xíu
– bịu, chịu, dịu, địu, khuỵu, lịu, nghịu, nhịu, nịu, phịu, tịu, xịu

# O
– bo, cho, co, do, đo, gio, go, ho, kho, lo, mo, *ngo, nho, no, o, pho, ro, so, tho, to, tro, vo, xo
– bò, chò, cò, dò, đò, giò, gò, hò, *khò, lò, mò, ngò, nò, phò, rò, sò, thò, tò, trò, vò
– bỏ, chỏ, cỏ, dỏ, đỏ, giỏ, hỏ, khỏ, mỏ, ngỏ, nhỏ, nỏ, rỏ, sỏ, thỏ, tỏ, trỏ, vỏ, xỏ
– bõ, chõ, đõ, gõ, lõ, mõ, ngõ, nõ, rõ, võ
– bó, chó, có, dó, đó, gió, hó, khó, ló, mó, ngó, nhó, nó, ó, phó, ró, thó, tó, vó, xó
– bọ, cọ, dọ, đọ, giọ, *gọ, họ, lọ, mọ, ngọ, nhọ, nọ, *ọ, rọ, sọ, thọ, trọ, vọ, xọ

# OC
– bóc, chóc, cóc, dóc, gióc, góc, hóc, khóc, lóc, móc, ngóc, nhóc, nóc, óc, phóc, róc, sóc, thóc, tóc, tróc, vóc, xóc
– bọc, chọc, cọc, dọc, đọc, học, lọc, mọc, ngọc, nhọc, nọc, ọc, rọc, sọc, thọc, tọc, trọc, vọc, xọc

# OI
– choi, coi, doi, gioi, hoi, khoi, loi, moi, ngoi, nhoi, noi, oi, phoi, roi, soi, thoi, toi, voi, xoi
– chòi, còi, dòi, đòi, giòi, hòi, lòi, mòi, ngòi, nòi, *òi, phòi, ròi, sòi, thòi, tròi, tòi, vòi
– bỏi, chỏi, cỏi, đỏi, giỏi, gỏi, hỏi, khỏi, lỏi, mỏi, ỏi, rỏi, sỏi, thỏi, tỏi
– cõi, dõi, lõi, rõi, sõi
– bói, chói, cói, dói, đói, giói, gói, hói, khói, lói, mói, ngói, nhói, nói, ói, rói, sói, thói, tói, trói, *xói
– vói, xói
– chọi, dọi, đọi, giọi, gọi, lọi, mọi, rọi, trọi, vọi

# OM
– bom, *com, dom, đom, gom, hom, khom, lom, mom, nhom, nom, om, *pom, *thom, *tom, *trom, xom
– chòm, còm, dòm, hòm, khòm, lòm, mòm, ngòm, nhòm, nòm, sòm, thòm, tòm, *tròm, vòm
– *bỏm, chỏm, *cỏm, dỏm, đỏm, hỏm, lỏm, mỏm, ngỏm, nhỏm, nỏm, ỏm, rỏm, thỏm
– bõm, chõm, hõm, lõm, mõm, nhõm, tõm, trõm
– cóm, dóm, đóm, hóm, khóm, lóm, móm, ngóm, nhóm, róm, thóm, tóm, xóm
– cọm, khọm, *lọm, sọm

# ON
– bon, *chon, con, don, đon, *gion, gon, hon, lon, *mon, ngon, *nhon, non, son, thon, ton, von, xon
– bòn, còn, đòn, giòn, gòn, hòn, lòn, mòn, ròn, sòn, *tòn, tròn, vòn
– chỏn, *cỏn, giỏn, hỏn, lỏn, *ngỏn, *ỏn, rỏn, *vỏn
– nõn
– bón, cón, đón, món, ngón, nhón, nón, rón, són, vón, xón
– bọn, chọn, cọn, dọn, đọn, gọn, lọn, mọn, ngọn, nhọn, nọn, trọn

# ONG
– bong, chong, cong, dong, đong, giong, hong, long, mong, nhong, nong, ong, phong, rong, song, *thong, tong, trong, vong, xong
– bòng, chòng, còng, dòng, đòng, hòng, khòng, lòng, mòng, *ngòng, nhòng, nòng, *òng, phòng, ròng, sòng, thòng, tòng, tròng, vòng
– bỏng, chỏng, dỏng, *đỏng, giỏng, gỏng, hỏng, khỏng, lỏng, mỏng, ngỏng, *nhỏng, ỏng, phỏng, tỏng, trỏng, vỏng
– bõng, chõng, cõng, dõng, lõng, ngõng, *nhõng, *õng, sõng, thõng, võng, xõng
– bóng, chóng, cóng, dóng, đóng, gióng, hóng, lóng, móng, ngóng, nhóng, nóng, óng, phóng, róng, sóng, tróng, vóng
– bọng, cọng, dọng, đọng, giọng, gọng, họng, lọng, mọng, ngọng, nọng, tọng, trọng, vọng

# OOC
– coóc, moóc, *phoóc, soóc

# OONG
– boong, loong, moong, soong, toong, xoong
– choòng, goòng, *toòng
– boóng

# OP
– bóp, chóp, cóp, góp, hóp, lóp, móp, ngóp, nhóp, nóp, óp, thóp, tóp
– cọp, dọp, họp, lọp, mọp, ọp, tọp, vọp, xọp

# OT
– bót, chót, cót, đót, gót, hót, lót, mót, ngót, nhót, nót, ót, phót, rót, sót, thót, tót, trót, vót, xót
– bọt, chọt, cọt, đọt, giọt, gọt, lọt, mọt, ngọt, nhọt, nọt, phọt, rọt, sọt, thọt, tọt, trọt, vọt

# Ô
– bô, cô, dô, đô, giô, gô, hô, khô, lô, mô, ngô, nhô, nô, ô, phô, pô, rô, sô, thô, tô, *trô, vô, xô
– bồ, chồ, cồ, dồ, đồ, giồ, gồ, hồ, lồ, mồ, *ngồ, ồ, rồ, *sồ, thồ, tồ, trồ, vồ, xồ
– bổ, cổ, đổ, gổ, hổ, khổ, lổ, mổ, ngổ, nhổ, nổ, ổ, phổ, rổ, sổ, thổ, tổ, trổ, vổ, xổ
– *bỗ, chỗ, cỗ, dỗ, đỗ, giỗ, gỗ, hỗ, lỗ, mỗ, *ngỗ, *nỗ, rỗ, sỗ, trỗ, vỗ
– bố, cố, đố, hố, khố, lố, mố, ngố, nhố, ố, phố, số, thố, tố, trố, vố, xố
– bộ, chộ, cộ, độ, gộ, hộ, lộ, mộ, ngộ, nộ, rộ, sộ, tộ, trộ

# ÔC
– bốc, chốc, cốc, dốc, đốc, gốc, hốc, khốc, lốc, mốc, ngốc, nhốc, nốc, ốc, phốc, rốc, sốc, thốc, tốc, trốc, vốc, xốc
– bộc, cộc, dộc, độc, gộc, hộc, lộc, mộc, ngộc, ộc, rộc, thộc, tộc, xộc

# ÔI
– bôi, côi, dôi, đôi, hôi, khôi, lôi, môi, ngôi, nhôi, nôi, ôi, phôi, sôi, thôi, tôi, trôi, vôi, xôi
– bồi, chồi, dồi, đồi, giồi, gồi, hồi, lồi, mồi, ngồi, nhồi, nồi, rồi, sồi, tồi, trồi
– bổi, chổi, cổi, dổi, đổi, giổi, hổi, nổi, ổi, phổi, sổi, thổi, trổi, xổi
– chỗi, cỗi, dỗi, đỗi, giỗi, lỗi, mỗi, nỗi, rỗi, trỗi
– bối, chối, cối, dối, đối, giối, gối, hối, khối, lối, mối, nhối, nối, ối, phối, rối, thối, tối, trối, vối, xối
– bội, chội, cội, dội, đội, giội, gội, hội, lội, mội, nhội, nội, tội, trội, vội

# ÔM
– *bôm, chôm, côm, *đôm, gôm, hôm, *lôm, môm, nhôm, nôm, ôm, *phôm, rôm, tôm, xôm
– bồm, chồm, cồm, đồm, gồm, lồm, mồm, *nhồm, nồm, ồm, *thồm, xồm
– dổm, hổm, *lổm, ngổm, nhổm, xổm
– chỗm
– cốm, đốm, gốm, lốm, ốm
– cộm, *lộm, nộm, rộm, trộm

# ÔN
– bôn, chôn, côn, đôn, *giôn, gôn, hôn, khôn, môn, ngôn, *nhôn, nôn, ôn, phôn, thôn, tôn, trôn, vôn, *xôn
– bồn, chồn, cồn, dồn, đồn, hồn, lồn, *mồn, *ngồn, *nhồn, ồn, *phồn, *sồn, thồn, tồn, *vồn, xồn
– bổn, cổn, *hổn, *lổn, ngổn, nhổn, ổn, *rổn, thổn, tổn
– hỗn, *thỗn
– bốn, chốn, cốn, đốn, khốn, lốn, ngốn, nhốn, rốn, thốn, tốn, trốn, vốn, xốn
– bộn, chộn, cộn, độn, hộn, lộn, nộn, ngộn, nhộn, rộn, thộn, trộn, xộn

# ÔNG
– bông, chông, công, dông, đông, giông, gông, hông, không, lông, mông, ngông, nhông, nông, ông, phông, rông, sông, thông, tông, trông, vông, xông
– bồng, chồng, cồng, *dồng, đồng, giồng, gồng, hồng, lồng, mồng, ngồng, nhồng, nồng, *ồng, phồng, rồng, sồng, *tồng, trồng, vồng, *xồng
– bổng, chổng, cổng, đổng, hổng, khổng, lổng, mổng, nổng, ổng, phổng, sổng, tổng, trổng, vổng, xổng
– bỗng, hỗng, ngỗng, nỗng, phỗng, rỗng
– bống, chống, cống, đống, giống, hống, khống, mống, nống, ống, rống, sống, thống, tống, trống, vống, xống
– bộng, cộng, dộng, động, lộng, mộng, nhộng, phộng, rộng, trộng

# ÔP
– bốp, chốp, cốp, đốp, lốp, ốp, phốp, *sốp, tốp, xốp
– bộp, chộp, cộp, dộp, độp, giộp, gộp, hộp, *lộp, nộp, ộp, rộp, sộp, thộp, xộp

# ÔT
– bốt, chốt, cốt, dốt, đốt, giốt, hốt, lốt, mốt, ngốt, nhốt, nốt, ốt, phốt, rốt, sốt, thốt, tốt, trốt, xốt
– bột, chột, cột, dột, đột, gột, hột, lột, một, ngột, nhột, nột, sột, thột, tột

# Ơ
– bơ, chơ, cơ, dơ, đơ, giơ, gơ, hơ, huơ, khơ, khuơ, lơ, mơ, ngơ, nhơ, nơ, ơ, phơ, quơ, rơ, sơ, thơ, tơ, trơ, vơ, xơ
– bờ, chờ, cờ, dờ, đờ, giờ, gờ, hờ, khờ, lờ, mờ, ngờ, nhờ, ờ, phờ, quờ, rờ, sờ, thờ, tờ, trờ, vờ, *xờ
– bở, chở, dở, giở, gở, hở, lở, mở, nhở, nở, ở, phở, quở, rở, sở, thở, thuở, tở, trở, vở, xở
– *bỡ, cỡ, dỡ, đỡ, gỡ, hỡ, lỡ, mỡ, ngỡ, nhỡ, nỡ, rỡ, sỡ, vỡ, xỡ
– bớ, chớ, cớ, dớ, đớ, hớ, khớ, lớ, mớ, ngớ, nhớ, nớ, ớ, quớ, rớ, sớ, thớ, tớ, trớ, vớ, xớ
– bợ, chợ, dợ, đợ, lợ, mợ, ngợ, nhợ, nợ, ợ, rợ, sợ, thợ, tợ, trợ, vợ

# ƠI
– bơi, chơi, cơi, dơi, hơi, khơi, lơi, ngơi, nhơi, nơi, ơi, phơi, rơi, thơi, tơi, trơi, vơi, xơi
– bời, cời, dời, đời, giời, hời, lời, mời, ngời, nhời, rời, thời, tời, trời, vời
– bởi, cởi, gởi, hởi, khởi, lởi, nhởi, sởi, xởi
– cỡi, hỡi, lỡi
– bới, chới, đới, giới, khới, lới, mới, nới, ới, phới, sới, thới, tới, với, xới
– đợi, gợi, hợi, lợi, ngợi, rợi, sợi, vợi

# ƠM
– bơm, cơm, *chơm, đơm, *ngơm, *nhơm, nơm, rơm, *sơm, thơm, xơm
– bờm, chờm, đờm, gờm, hờm, *lờm, mờm, *ngờm, nhờm, *nờm, rờm, *sờm, xờm
– chởm, đởm, *lởm, rởm, tởm
– cỡm, lỡm, nỡm, *ỡm
– cớm, chớm, gớm, hớm, mớm, nhớm, ớm, rớm, sớm, thớm
– bợm, cợm, dợm, hợm, lợm, ngợm

# ƠN
– bơn, chơn, cơn, dơn, đơn, hơn, lơn, mơn, nhơn, ơn, *phơn, rơn, sơn, *thơn, trơn, *xơn
– chờn, dờn, đờn, giờn, *gờn, hờn, lờn, nhờn, rờn, sờn, vờn
– đởn, hởn, *lởn, mởn, nhởn, phởn, rởn, sởn, tởn, vởn
– bỡn, cỡn, giỡn, *nhỡn, phỡn, rỡn
– chớn, cớn, *dớn, đớn, hớn, lớn, mớn, ngớn, nhớn, ớn, *phớn, *sớn, tớn, trớn
– bợn, chợn, cợn, dợn, gợn, lợn, rợn, tợn, trợn

# ƠP
– bớp, chớp, dớp, đớp, hớp, khớp, lớp, ngớp, nhớp, nớp, rớp
– bợp, chợp, cợp, hợp, lợp, ngợp, nợp, rợp, tợp

# ƠT
– bớt, chớt, cớt, chớt, đớt, hớt, lớt, ngớt, nhớt, nớt, ớt, phớt, rớt, sớt, thớt, trớt, vớt, xớt
– bợt, chợi, cợt, đợt, gợt, hợt, lợt, nhợt, ợt, trợt, vợt

# U
– bu, chu, cu, du, đu, gu, hu, khu, lu, mu, ngu, nhu, nu, phu, *pu, ru, su, thu, tru, tu, u, vu, xu
– bù, chù, cù, dù, đù, gù, hù, khù, lù, mù, ngù, phù, rù, sù, thù, trù, tù, ù, vù, xù
– bủ, chủ, củ, đủ, hủ, *khủ, *lủ, mủ, ngủ, nhủ, phủ, rủ, thủ, trủ, tủ, ủ
– cũ, giũ, hũ, lũ, mũ, ngũ, nhũ, phũ, rũ, vũ, xũ
– bú, chú, cú, đú, giú, *gú, hú, khú, lú, mú, nhú, phú, rú, sú, thú, trú, tú, ú, vú, *xú
– bụ, cụ, dụ, đụ, gụ, hụ, khụ, lụ, mụ, ngụ, nhụ, nụ, phụ, sụ, thụ, trụ, tụ, ụ, vụ, xụ

# UA
– bua, chua, cua, dua, đua, hua, khua, lua, mua, nua, phua, rua, thua, tua, vua, xua
– bùa, chùa, dùa, đùa, gùa, hùa, lùa, mùa, rùa, thùa, ùa, vùa
– bủa, của, nủa, rủa, sủa, thủa, tủa, ủa
– dũa, đũa, giũa, lũa, rũa
– búa, chúa, dúa, đúa, lúa, múa, nhúa, túa, úa
– bụa, giụa, lụa, ngụa, nhụa, pụa, rụa, sụa, trụa

# UC
– cúc, chúc, đúc, húc, khúc, lúc, múc, *ngúc, nhúc, núc, phúc, rúc, súc, thúc, trúc, túc, úc, *vúc, xúc
– bục, chục, cục, dục, đục, giục, gục, hục, khục, lục, mục, ngục, nhục, nục, phục, rục, sục, thục, trục, tục, ục, vục, xục

# UI
– chui, cui, đui, *hui, khui, lui, mui, phui, rui, sui, thui, trui, tui, ui, vui, xui
– bùi, chùi, cùi, dùi, đùi, giùi, gùi, *hùi, lùi, mùi, ngùi, nhùi, nùi, sùi, *thùi, *trùi, vùi, xùi
– củi, dủi, đủi, giủi, hủi, lủi, *mủi, ngủi, nhủi, phủi, rủi, sủi, thủi, tủi, ủi
– chũi, cũi, dũi, đũi, gũi, lũi, mũi, trũi
– búi, chúi, cúi, dúi, giúi, húi, lúi, múi, nhúi, núi, thúi, túi, úi, xúi
– bụi, cụi, dụi, giụi, gụi, hụi, lụi, mụi, nhụi, rụi, thụi, trụi, tụi, xụi

# UM
– chum, cum, đum, hum, khum, lum, nhum, rum, *sum, thum, tum, um, *xum
– *bùm, chùm, cùm, đùm, giùm, hùm, lùm, rùm, sùm, *thùm, trùm, tùm, ùm, *xùm
– củm, lủm, *mủm, ngủm, thủm, tủm
– chũm, hũm, lũm, *mũm, tũm, vũm
– chúm, cúm, dúm, đúm, khúm, lúm, *múm, nhúm, núm, rúm, trúm, túm, úm, xúm
– bụm, chụm, cụm, dụm, hụm, *lụm, ngụm, rụm, sụm, trụm, tụm

# UN
– chun, cun, dun, đun, giun, hun, mun, phun, run, sun, thun, *tun, un, vun, *xun
– bùn, chùn, cùn, dùn, đùn, gùn, hùn, lùn, mùn, *ngùn, nùn, phùn, rùn, trùn, ùn, *vùn
– bủn, chủn, củn, hủn, lủn, mủn, ngủn, nhủn, rủn, *tủn, *ủn
– chũn, cũn, lũn, nhũn
– bún, cún, dún, lún, mún, ngún, nhún, phún, rún, sún
– đụn, lụn, mụn, sụn, vụn

# UNG
– bung, chung, cung, dung, *đung, hung, khung, lung, *mung, nhung, nung, phung, rung, sung, thung, trung, tung, ung, vung, xung
– bùng, chùng, cùng, dùng, đùng, gùng, hùng, khùng, lùng, mùng, ngùng, nhùng, nùng, phùng, rùng, sùng, thùng, trùng, tùng, *ùng, vùng, *xùng
– bủng, chủng, củng, *đủng, khủng, lủng, mủng, *ngủng, *nhủng, *rủng, sủng, thủng, ủng, *xủng
– cũng, dũng, đũng, lũng, nhũng, nũng, sũng, thũng, trũng, vũng
– búng, chúng, cúng, dúng, đúng, húng, *khúng, *lúng, *ngúng, nhúng, núng, phúng, rúng, súng, thúng, trúng, túng, úng, *xúng
– bụng, cụng, dụng, đụng, *khụng, lụng, nhụng, phụng, rụng, thụng, trụng, tụng, vụng

# UÔC
– chuốc, cuốc, duốc, đuốc, guốc, luốc, nhuốc, *puốc, quốc, ruốc, thuốc, *tuốc
– buộc, chuộc, cuộc, duộc, giuộc, guộc, luộc, nuộc, thuộc, tuộc

# UÔI
– chuôi, duôi, đuôi, muôi, nguôi, nuôi, xuôi
– buồi, chuồi, muồi, ruồi, tuồi
– buổi, đuổi, ruổi, tuổi
– chuỗi, duỗi, muỗi
– chuối, cuối, duối, đuối, muối, nuối, ruối, suối
– chuội, cuội, muội, nguội

# UÔM
– chuôm, *luôm, nhuôm, uôm
– buồm
– cuỗm, muỗm
– nhuốm, nuốm
– buộm, *luộm, nhuộm, ruộm, thuộm, xuộm

# UÔN
– buôn, khuôn, luôn, muôn, *ruôn, suôn, thuôn, tuôn
– buồn, chuồn, *cuồn, *đuồn, luồn, nguồn, thuồn, tuồn
– đuỗn, thuỗn
– cuốn, muốn, thuốn, tuốn, uốn
– cuộn, guộn, muộn

# UÔNG
– buông, chuông, cuông, khuông, luông, muông, nuông, suông, truông, tuông, vuông
– buồng, chuồng, cuồng, guồng, luồng, muồng, ruồng, *suồng, thuồng, truồng, tuồng, xuồng
– thuổng, uổng, xuổng
– luỗng, muỗng, ruỗng
– cuống, đuống, huống, luống, muống, uống, xuống
– chuộng, cuộng, ruộng

# UÔT
– buốt, chuốt, huốt, luốt, muốt, nuốt, ruốt, suốt, tuốt, vuốt
– buột, chuột, đuột, guột, nuột, ruột, tuột, uột, vuột

# UP
– búp, cúp, đúp, giúp, húp, lúp, múp, núp, rúp, súp, túp, úp
– bụp, chụp, cụp, đụp, hụp, *lụp, *ngụp, sụp, thụp, ụp, xụp

# UT
– bút, chút, cút, dút, đút, gút, hút, lút, mút, ngút, nhút, nút, phút, rút, sút, thút, trút, tút, út, vút, xút
– bụt, chụt, cụt, *dụt, đụt, hụt, *khụt, lụt, mụt, ngụt, nhụt, phụt, rụt, sụt, thụt, trụt, tụt, *ụt, vụt

# Ư
– chư, cư, dư, hư, khư, lư, ngư, như, nư, sư, thư, tư, ư
– chừ, cừ, dừ, đừ, gừ, hừ, khừ, lừ, ngừ, nhừ, thừ, trừ, từ, ừ, xừ
– cử, dử, đử, hử, khử, lử, nhử, sử, thử, tử, ử, xử
– chữ, cữ, dữ, giữ, hữ, lữ, ngữ, nữ, trữ
– bứ, chứ, cứ, dứ, đứ, hứ, khứ, ngứ, nhứ, sứ, thứ, *trứ, tứ, ứ, xứ
– bự, cự, dự, hự, lự, ngự, nhự, nự, sự, thự, trự, tự, xự

# ƯA
– chưa, cưa, dưa, đưa, lưa, mưa, *ngưa, nưa, *rưa, sưa, thưa, trưa, tưa, ưa, xưa
– bừa, chừa, dừa, lừa, ngừa, thừa, vừa
– bửa, chửa, cửa, lửa, mửa, ngửa, nửa, rửa, sửa, thửa, *xửa
– bữa, chữa, giữa, lữa, nữa, rữa, sữa, vữa
– bứa, chứa, cứa, dứa, đứa, hứa, khứa, lứa, mứa, ngứa, nứa, phứa, rứa, sứa, tứa, ứa
– bựa, cựa, dựa, lựa, mựa, ngựa, nhựa, phựa, rựa, tựa, ựa, vựa

# ƯC
– bức, chức, *cức, dức, đức, hức, lức, mức, nhức, nức, phức, rức, sức, thức, tức, ức, vức, xức
– bực, chực, cực, dực, đực, hực, lực, mực, ngực, nực, rực, sực, thực, trực, ực, vực, xực

# ƯI
– chửi, cửi, gửi, ngửi

# ƯM
– hừm

# ƯN
– chưn

# ƯNG
– bưng, chưng, cưng, dưng, đưng, hưng, lưng, mưng, ngưng, nhưng, *phưng, rưng, sưng, thưng, trưng, tưng, ưng, xưng
– bừng, chừng, dừng, đừng, gừng, hừng, khừng, lừng, mừng, ngừng, phừng, rừng, sừng, thừng, trừng, từng, *ừng, vừng, xừng
– bửng, chửng, *dửng, hửng, lửng, mửng, ngửng, *tửng, sửng, trửng, ửng, vửng, xửng
– chững, hững, lững, những, sững, thững, vững
– bứng, chứng, cứng, dứng, đứng, hứng, khứng, trứng, ứng, xứng
– bựng, chựng, dựng, đựng, khựng, lựng, nựng, sựng, vựng

# ƯƠC
– bước, chước, cước, đước, hước, khước, ngước, nước, phước, rước, thước, trước, tước, ước, xước
– chược, cược, dược, được, lược, mược, ngược, nhược, *thược, tược, vược, xược

# ƯƠI
– bươi, khươi, mươi, ngươi, rươi, tươi, *ươi
– cười, *đười, lười, mười, người, *rười
– bưởi, mưởi, rưởi, sưởi, tưởi
– *cưỡi, lưỡi, rưỡi, thưỡi
– cưới, dưới, lưới, rưới, tưới
– dượi, rượi

# ƯƠM
– bươm, gươm, hươm, *lươm, tươm, ươm
– chườm, cườm, gườm, hườm, lườm, *nườm, rườm
– bướm, rướm, ướm
– đượm, gượm, hượm, lượm

# ƯƠN
– bươn, hươn, khươn, lươn, ươn, vươn
– đườn, lườn, sườn, *thườn, trườn, ườn, vườn
– đưỡn, phưỡn, thưỡn, ưỡn
– dướn, mướn, nhướn, phướn, rướn
– lượn, mượn, rượn, vượn

# ƯƠNG
– bương, chương, cương, dương, đương, giương, gương, hương, lương, mương, nhương, nương, phương, rương, sương, thương, trương, tương, ương, vương, xương
– chường, cường, dường, đường, giường, hường, lường, mường, *ngường, nhường, nường, phường, rường, thường, trường, tường, xường
– chưởng, hưởng, khưởng, ngưởng, thưởng, trưởng, tưởng, vưởng, xưởng
– chưỡng, cưỡng, dưỡng, gưỡng, khưỡng, lưỡng, ngưỡng, nhưỡng, trưỡng
– bướng, chướng, dướng, giướng, hướng, *lướng, nhướng, nướng, phướng, sướng, trướng, tướng, vướng, xướng
– dượng, gượng, lượng, ngượng, nhượng, phượng, sượng, thượng, trượng, tượng, vượng

# ƯƠP
– bướp, cướp, mướp, tướp, ướp
– chượp, nượp

# ƯƠT
– khướt, lướt, mướt, sướt, thướt, tướt, ướt
– dượt, khượt, lượt, mượt, rượt, sượt, thượt, trượt, tượt, vượt

# ƯƠU
– bươu, hươu
– tườu
– mưỡu
– bướu, khướu
– rượu

# ƯT
– bứt, cứt, dứt, đứt, lứt, mứt, ngứt, nhứt, nứt, phứt, rứt, sứt, vứt
– bựt, giựt, nhựt

# ƯU
– bưu, *cưu, hưu, lưu, mưu, ngưu, sưu, ưu
– cừu, *trừu
– *bửu, cửu, sửu, tửu
– cữu, hữu
– cứu, *khứu, mứu
– cựu, lựu, tựu
"""

def convert_to_json(text):
    sections = text.strip().split("\n\n")
    data = {}

    # Định nghĩa các thanh
    tones = {
        "huyền": ['à', 'ằ', 'ầ', 'ò', 'ồ', 'ờ', 'è', 'ề', 'ù', 'ừ', 'ì', 'ỳ'],
        "sắc": ['á', 'ắ', 'ấ', 'ó', 'ố', 'ớ', 'é', 'ế', 'ú', 'ứ', 'í', 'ý'],
        "hỏi": ['ả', 'ẳ', 'ẩ', 'ỏ', 'ổ', 'ở', 'ẻ', 'ể', 'ủ', 'ử', 'ỉ', 'ỷ'],
        "ngã": ['ã', 'ẵ', 'ẫ', 'õ', 'ỗ', 'ỡ', 'ẽ', 'ễ', 'ũ', 'ữ', 'ĩ', 'ỹ'],
        "nặng": ['ạ', 'ặ', 'ậ', 'ọ', 'ộ', 'ợ', 'ẹ', 'ệ', 'ụ', 'ự', 'ị', 'ỵ']
    }

    for section in sections:
        title, *lines = section.split("\n")
        title = title.strip("# ").strip()
        data[title] = {}

        for line in lines:
            if not line.strip():
                continue
            parts = line.split("–")
            if len(parts) < 2:
                continue  # Bỏ qua dòng không hợp lệ
            
            accent = parts[0].strip()
            words = parts[1].strip()

            # Loại bỏ dấu *
            words_list = [re.sub(r'\*', '', word.strip().rstrip(',')) for word in words.split(",")]

            # Phân loại từ vào các thanh
            for word in words_list:
                accent_key = "khác"  # Mặc định là "khác"
                for tone, accents in tones.items():
                    if any(char in accents for char in word):  # Kiểm tra nếu từ chứa bất kỳ ký tự nào trong thanh
                        accent_key = tone
                        break
                
                if accent_key not in data[title]:
                    data[title][accent_key] = []
                data[title][accent_key].append(word)

    return data

json_data = convert_to_json(text)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print("Đã chuyển đổi và lưu vào data.json")