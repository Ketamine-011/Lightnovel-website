# File truyện mẫu và tài khoản Admin khởi tạo ban đầu
import random
from werkzeug.security import generate_password_hash
from app import app
from models import db, Truyen, User

def seed_data():
    with app.app_context():
        tai_khoan_admin = User.query.filter_by(username="admin").first()
        if not tai_khoan_admin:
            hash_pw = generate_password_hash("admin123")
            admin_user = User(
                username="admin",
                email="admin@gmail.com",
                password=hash_pw,
                role="admin"  
            )
            db.session.add(admin_user)
            print(" Tài khoản: admin | Mật khẩu: admin123")
        else:
            print("Tài khoản Admin đã tồn tại từ trước.")


        #Nạp truyện=
        if Truyen.query.first():
            print("⚠️ Database đã có truyện rồi, không nạp trùng nữa ông nhé!")
            db.session.commit() #commit phần admin
            return

        print("📚 Đang khởi tạo danh sách 50 bộ truyện mẫu...")
        novels = [
            Truyen(
                ten_truyen="Thần Kê Biến Dị",
                tac_gia="Kê Gia",
                the_loai="Tu Tiên",
                mo_ta="Một chú gà bình thường trải qua dị biến, bước trên con đường nghịch thiên cải mệnh, tiến hóa thành Thần Thú vạn cổ vô song.",
                luot_xem=15420
            ),
            Truyen(
                ten_truyen="Cửu Tinh Bá Thể Quyết",
                tac_gia="Đông Phương Thanh",
                the_loai="Huyền Huyễn",
                mo_ta="Thiếu niên bị tước đoạt huyết mạch, nghịch thiên tu luyện Cửu Tinh Bá Thể, một tay che trời, chém rách tinh không.",
                luot_xem=14320
            ),
            Truyen(
                ten_truyen="Đại Quản Gia Là Ma Hoàng",
                tac_gia="Dạ Ma",
                the_loai="Trùng Sinh",
                mo_ta="Ma Hoàng đệ nhất thiên hạ bị đệ tử phản bội, trùng sinh thành đại quản gia của một gia tộc đang lụi tàn.",
                luot_xem=13890
            ),
            Truyen(
                ten_truyen="Ta Là Tà Đế",
                tac_gia="Mộng Thần",
                the_loai="Hệ Thống",
                mo_ta="Xuyên không sở hữu hệ thống vạn giới, hành trình đi qua các vị diện thu thập tâm tình để trở thành đệ nhất Tà Đế.",
                luot_xem=13120
            ),
            Truyen(
                ten_truyen="Vạn Cổ Tối Cường Tông",
                tac_gia="Quân Thường Tiếu",
                the_loai="Hài Hước",
                mo_ta="Hành trình xây dựng đệ nhất tông môn thiên hạ của một chưởng môn lầy lội và những đệ tử quái dị.",
                luot_xem=12890
            ),
            Truyen(
                ten_truyen="Tuyệt Thế Đường Môn",
                tac_gia="Đường Gia Tam Thiếu",
                the_loai="Huyền Huyễn",
                mo_ta="Nơi không có ma pháp, không có đấu khí, chỉ có Vũ Hồn. Đường Môn lụi tàn, liệu thiếu niên thiên tài có thể vực dậy?",
                luot_xem=11500
            ),
            Truyen(
                ten_truyen="Phàm Nhân Tu Tiên",
                tac_gia="Vong Ngữ",
                the_loai="Tu Tiên",
                mo_ta="Một người bình thường, tư chất bình thường, làm sao từng bước vượt qua ranh giới sinh tử để phi thăng Tiên Giới?",
                luot_xem=11210
            ),
            Truyen(
                ten_truyen="Tiên Nghịch",
                tac_gia="Nhĩ Căn",
                the_loai="Tu Tiên",
                mo_ta="Tu tiên là nghịch thiên hay thuận thiên? Hành trình sát phạt quyết đoán của Vương Lâm để tìm lại công lý cho gia tộc.",
                luot_xem=10800
            ),
            Truyen(
                ten_truyen="Quỷ Bí Chi Chủ",
                tac_gia="Mực Thích Lặn Nước",
                the_loai="Khoa Huyễn",
                mo_ta="Thế giới mang phong cách steampunk kết hợp huyền bí ma thuật. Hành trình của Kẻ Khờ vươn lên làm chủ thần linh.",
                luot_xem=10430
            ),
            Truyen(
                ten_truyen="Thế Giới Hoàn Mỹ",
                tac_gia="Thần Đông",
                the_loai="Huyền Huyễn",
                mo_ta="Một hạt bụi có thể lấp biển, một cọng cỏ chém hết tinh thần. Thiếu niên hoang dã một mình gánh vác cả thiên địa.",
                luot_xem=9980
            ),
            Truyen(
                ten_truyen="Đấu Phá Thương Khung",
                tac_gia="Thiên Tằm Thổ Đậu",
                the_loai="Huyền Huyễn",
                mo_ta="Ba mươi năm Hà Đông, ba mươi năm Hà Tây, chớ khinh thiếu niên nghèo! Tiêu Viêm từng bước thu phục dị hỏa, xưng bá đại lục.",
                luot_xem=9540
            ),
            Truyen(
                ten_truyen="Đại Phụng Đả Canh Nhân",
                tac_gia="Thanh San",
                the_loai="Xuyên Không",
                mo_ta="Cảnh sát xuyên không về làm người canh đêm tại vương triều phong kiến, dùng kiến thức phá án và tu luyện võ đạo.",
                luot_xem=9120
            ),
            Truyen(
                ten_truyen="Kiếm Lai",
                tac_gia="Phong Hỏa",
                the_loai="Võ Hiệp",
                mo_ta="Bên trong tiểu trấn thần bí, một thiếu niên nghèo khổ mang theo một thanh kiếm rách, chém ra một con đường trường sinh.",
                luot_xem=8870
            ),
            Truyen(
                ten_truyen="Trách Thiên Ký",
                tac_gia="Miêu Nị",
                the_loai="Tu Tiên",
                mo_ta="Thiếu niên mười bốn tuổi mang theo phong thư hôn ước rời núi, đối đầu với cả giang sơn để nghịch thiên cải mệnh.",
                luot_xem=8540
            ),
            Truyen(
                ten_truyen="Nhất Niệm Vĩnh Hằng",
                tac_gia="Nhĩ Căn",
                the_loai="Hài Hước",
                mo_ta="Bạch Tiểu Thuần một lòng sợ chết, vì mục tiêu sống thọ mà dấn thân vào con đường tu tiên đầy dở khóc dở cười.",
                luot_xem=8210
            ),
            Truyen(
                ten_truyen="Ta Có Một Tòa Kinh Khủng Ốc",
                tac_gia="Ngã Hội Tu Giày",
                the_loai="Kinh Dị",
                mo_ta="Thừa kế nhà ma từ cha mẹ mất tích, trần ca tìm thấy chiếc điện thoại đen mở ra thế giới kinh dị rùng rợn.",
                luot_xem=7980
            ),
            Truyen(
                ten_truyen="Toàn Chức Pháp Sư",
                tac_gia="Loạn",
                the_loai="Đô Thị",
                mo_ta="Mở mắt ra thế giới quen thuộc biến thành thế giới ma pháp. Mạc Phàm sở hữu thiên phú song hệ ma pháp hiếm có.",
                luot_xem=7650
            ),
            Truyen(
                ten_truyen="Linh Vũ Thiên Hạ",
                tac_gia="Vũ Phong",
                the_loai="Huyền Huyễn",
                mo_ta="Lục Thiếu Du xuyên không làm thiếu gia phế vật, tu luyện song hệ Linh Vũ quyết tâm đứng trên đỉnh cao nhân sinh.",
                luot_xem=7420
            ),
            Truyen(
                ten_truyen="Thần Đạo Đan Tôn",
                tac_gia="Cô Độc Giả",
                the_loai="Trùng Sinh",
                mo_ta="Đan Đế đệ nhất trùng sinh sau vạn năm, tu luyện Thần Đạo, dung hợp đan võ, trấn áp thiên kiêu vạn giới.",
                luot_xem=7110
            ),
            Truyen(
                ten_truyen="Đế Bá",
                tac_gia="Yếm Bút Tiêu Sinh",
                the_loai="Huyền Huyễn",
                mo_ta="Nuôi một con quạ đen đi qua ngàn năm lịch sử, Lý Thất Dạ thức tỉnh vạn cổ, lấy lại thân xác vô địch thiên hạ.",
                luot_xem=6890
            ),
            Truyen(
                ten_truyen="Ma Đạo Tổ Sư",
                tac_gia="Mặc Hương Đồng Khứu",
                the_loai="Đông Phương",
                mo_ta="Di Lăng Lão Tổ Ngụy Vô Tiện trùng sinh sau mười ba năm, cùng Lam Vong Cơ phá giải những âm mưu tà ác năm xưa.",
                luot_xem=6650
            ),
            Truyen(
                ten_truyen="Toàn Chức Cao Thủ",
                tac_gia="Hồ Điệp Lam",
                the_loai="Võng Du",
                mo_ta="Diệp Tu - đấu thần của tựa game Vinh Quang bị câu lạc bộ ruồng bỏ, làm lại từ đầu tại một quán net nhỏ.",
                luot_xem=6420
            ),
            Truyen(
                ten_truyen="Vạn Tộc Chi Kiếp",
                tac_gia="Lão Ưng Chật Vật",
                the_loai="Huyền Huyễn",
                mo_ta="Chư thiên vạn tộc săn lùng nhân loại, Tô Vũ dùng một cuốn sổ da cũ để mở ra thời đại quật khởi của nhân tộc.",
                luot_xem=6200
            ),
            Truyen(
                ten_truyen="Thương Nguyên Đồ",
                tac_gia="Ngã Ăn Tây Hồng Thị",
                the_loai="Võ Hiệp",
                mo_ta="Yêu ma tàn sát nhân gian, thiếu niên Mạnh Xuyên thức tỉnh thần thông, dùng một ngọn đao bảo vệ giang sơn thái bình.",
                luot_xem=5980
            ),
            Truyen(
                ten_truyen="Nguyên Tôn",
                tac_gia="Thiên Tằm Thổ Đậu",
                the_loai="Huyền Huyễn",
                mo_ta="Chu Nguyên bị cướp mất thánh long khí vận, kinh mạch bế tắc, bằng vào ý chí kiên định mà mở mạch trùng sinh.",
                luot_xem=5760
            ),
            Truyen(
                ten_truyen="Thượng Cổ Thần Vương",
                tac_gia="Tinh Linh",
                the_loai="Huyền Huyễn",
                mo_ta="Tần Vấn Thiên phế vật nghịch thiên khai mở chín tầng trời tinh hồn, trở thành Thần Vương thống trị thượng cổ.",
                luot_xem=5540
            ),
            Truyen(
                ten_truyen="Trường Sinh Bất Tử",
                tac_gia="Quan Kỳ",
                the_loai="Hệ Thống",
                mo_ta="Tìm kiếm con đường trường sinh bất tử thông qua việc xây dựng giang sơn, thành lập vương triều tối cao.",
                luot_xem=5320
            ),
            Truyen(
                ten_truyen="Ta Lái Xe Bus Kinh Dị",
                tac_gia="Hắc Dạ",
                the_loai="Kinh Dị",
                mo_ta="Chuyến xe bus đêm đưa hành khách đi qua những vùng đất chết, đối mặt với những thế lực tâm linh đáng sợ.",
                luot_xem=5110
            ),
            Truyen(
                ten_truyen="Huyền Thiên Tà Tôn",
                tac_gia="Mặc Nhiên",
                the_loai="Xuyên Không",
                mo_ta="Bác sĩ hiện đại mang theo tà công cổ đại xuyên không, chữa bệnh cứu người nhưng sát phạt vô tình với kẻ địch.",
                luot_xem=4980
            ),
            Truyen(
                ten_truyen="Độc Bộ Thiên Hạ",
                tac_gia="Trạch Trư",
                the_loai="Huyền Huyễn",
                mo_ta="Diệp Húc vô tình nhặt được đỉnh báu, từ đó mở ra con đường tu luyện khí phách, độc bộ thiên hạ vô song.",
                luot_xem=4760
            ),
            Truyen(
                ten_truyen="Y Đạo Quan Trường",
                tac_gia="Thạch Đầu",
                the_loai="Đô Thị",
                mo_ta="Thần y giáng thế vào chốn quan trường phức tạp, dùng y thuật và trí tuệ để thăng tiến, bảo vệ công lý.",
                luot_xem=4540
            ),
            Truyen(
                ten_truyen="Đại Long Vương",
                tac_gia="Lam Sắc",
                the_loai="Huyền Huyễn",
                mo_ta="Sở hữu huyết mạch Thần Long cổ đại, thiếu niên phá vỡ xiềng xích nô lệ, chấn hưng long tộc.",
                luot_xem=4320
            ),
            Truyen(
                ten_truyen="Vô Địch Thật Tịch Mịch",
                tac_gia="Tân Phong",
                the_loai="Hài Hước",
                mo_ta="Lâm Phàm sở hữu thể chất bất tử bất diệt, đối thủ mạnh đến đâu cũng không thể giết chết anh ta, quả thực quá tịch mịch.",
                luot_xem=4120
            ),
            Truyen(
                ten_truyen="Chăn Nuôi Toàn Nhân Loại",
                tac_gia="Hồng Vĩ",
                the_loai="Khoa Huyễn",
                mo_ta="Nhân vật chính phát hiện ra mình có khả năng kiến tạo và chăn nuôi các nền văn minh nhỏ bé trong sân nhà.",
                luot_xem=3950
            ),
            Truyen(
                ten_truyen="Đường Chuyên",
                tac_gia="Kiết Dữ 2",
                the_loai="Lịch Sử",
                mo_ta="Thanh niên hiện đại rơi về thời Đường thịnh vượng, dùng tư duy hiện đại làm điên đảo cả vương triều.",
                luot_xem=3760
            ),
            Truyen(
                ten_truyen="Vạn Cổ Thần Đế",
                tac_gia="Phi Thiên Ngư",
                the_loai="Huyền Huyễn",
                mo_ta="Trương Nhược Trần bị vị hôn thê giết chết, trùng sinh sau 800 năm để tìm lại chân tướng và báo thù.",
                luot_xem=3540
            ),
            Truyen(
                ten_truyen="Chân Vũ Thế Giới",
                tac_gia="Tàm Kiếm Triền Miên",
                the_loai="Võ Hiệp",
                mo_ta="Dịch Vân nhặt được một Tử Thần Thẻ Bài bí ẩn, mở ra võ đạo chân chính của vũ trụ bao la.",
                luot_xem=3320
            ),
            Truyen(
                ten_truyen="Nghịch Thiên Tà Thần",
                tac_gia="Hỏa Tinh Dẫn Lực",
                the_loai="Huyền Huyễn",
                mo_ta="Mang theo huyền thiên bảo châu, Vân Triệt sống lại with tà cốt vô địch, khiến chư thần vạn giới phải run sợ.",
                luot_xem=3110
            ),
            Truyen(
                ten_truyen="Ta Khóa Bản Thể 10 Vạn Năm",
                tac_gia="Thần Bí Nhân",
                the_loai="Hệ Thống",
                mo_ta="Bị nhốt trong không gian thần bí mười vạn năm, ngày thức tỉnh cũng là lúc nhân vật chính vô địch thiên hạ.",
                luot_xem=2980
            ),
            Truyen(
                ten_truyen="Đạo Quân",
                tac_gia="Dược Thiên Sầu",
                the_loai="Mưu Kế",
                mo_ta="Bậc thầy khảo cổ xuyên không, không có võ công vô địch nhưng dùng mưu kế thao túng cả giang sơn giang hồ.",
                luot_xem=2760
            ),
            Truyen(
                ten_truyen="Tuyết Trung Hãn Đao Hành",
                tac_gia="Phong Hỏa",
                the_loai="Võ Hiệp",
                mo_ta="Thế tử Bắc Lương Từ Phượng Niên giả làm kẻ chơi bời, rèn luyện đao pháp bảo vệ giang sơn bờ cõi.",
                luot_xem=2540
            ),
            Truyen(
                ten_truyen="Vũ Động Càn Khôn",
                tac_gia="Thiên Tằm Thổ Đậu",
                the_loai="Huyền Huyễn",
                mo_ta="Lâm Động nhặt được một thạch phù thần bí, từ một thiếu niên gia tộc sa sút vươn lên xoay chuyển càn khôn.",
                luot_xem=2320
            ),
            Truyen(
                ten_truyen="Đại Chúa Tể",
                tac_gia="Thiên Tằm Thổ Đậu",
                the_loai="Huyền Huyễn",
                mo_ta="Tại đại thiên thế giới giao thoa, Mục Trần từng bước tu luyện, thống trị vạn giới, trở thành Đại Chúa Tể.",
                luot_xem=2120
            ),
            Truyen(
                ten_truyen="Sát Thần",
                tac_gia="Nghịch Thương Thiên",
                the_loai="Huyền Huyễn",
                mo_ta="Thạch Nhan mang theo võ hồn tinh tú, đi qua con đường nhuốm máu để chứng đạo thành Sát Thần tối cao.",
                luot_xem=1980
            ),
            Truyen(
                ten_truyen="Thần Ma Hệ Thống",
                tac_gia="Bạch Thủy",
                the_loai="Mạt Thế",
                mo_ta="Thế giới sụp đổ, thây ma hoành hành, con người phải dựa vào hệ thống săn giết quái vật để sinh tồn.",
                luot_xem=1760
            ),
            Truyen(
                ten_truyen="Y Thủ Che Thiên",
                tac_gia="Mộ Anh Lạc",
                the_loai="Ngôn Tình",
                mo_ta="Thần y thế kỷ 21 xuyên không thành tiểu thư phế vật, dùng độc bộ y thuật khuấy đảo cả vương triều.",
                luot_xem=1540
            ),
            Truyen(
                ten_truyen="Thần Cấp Hệ Thống",
                tac_gia="Trầm Mặc",
                the_loai="Hệ Thống",
                mo_ta="Làm việc gì cũng tăng điểm kinh nghiệm, học kỹ năng gì cũng max cấp ngay lập tức, hệ thống thần cấp vô địch.",
                luot_xem=1320
            ),
            Truyen(
                ten_truyen="Vạn Cổ Đại Đế",
                tac_gia="Mộ Vũ",
                the_loai="Trùng Sinh",
                mo_ta="Đại Đế trùng sinh vào thân xác một thiếu niên phế vật, tu luyện vạn cổ bất diệt quyết, quét ngang chư thiên.",
                luot_xem=1120
            ),
            Truyen(
                ten_truyen="Thương Khung Chiến Ký",
                tac_gia="Phi Vũ",
                the_loai="Võ Hiệp",
                mo_ta="Một thanh kiếm, một bầu rượu, thiếu niên tiêu dao đi khắp thế gian, viết nên khúc chiến ca thương khung bất hủ.",
                luot_xem=980
            ),
            Truyen(
                ten_truyen="Huyết Tế Thiên独立",
                tac_gia="Ma Đao",
                the_loai="Kinh Dị",
                mo_ta="Bí mật về giáo phái cổ xưa dùng máu hiến tế thần linh, mở ra kỷ nguyên bóng tối bao trùm nhân gian.",
                luot_xem=760
            )
        ]

        # Thêm đồng loạt 50 bộ truyện
        db.session.add_all(novels)
        db.session.commit()
        print("🎉 Đã nạp thành công 50 bộ truyện mẫu siêu đẹp vào Database!")

if __name__ == "__main__":
    seed_data()