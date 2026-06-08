# Novels Haven - Website Đọc Truyện LightNovel Trực Tuyến
Dự án môn học xây dựng ứng dụng web đọc và quản lý truyện LightNovel trực tuyến, sử dụng ngôn ngữ lập trình Python và Micro - Framework Flask
### **Tóm tắt chức năng của hệ thống**
### 1. Phân Hệ Người đọc
* **Đăng ký & Đăng nhập:** Cho phép độc giả tạo tài khoản mới và đăng nhập duy trì phiên làm việc qua Session Cookie.
* **Giao diện trang chủ :** Hiển thị danh sách toàn bộ truyện có trong hệ thống, tích hợp phân trang tự động ở phía Client (hiển thị 12 truyện mỗi lượt bấm "Xem thêm"), tự động hiển thị trang quản lý đối với `role = admin`.
* **Thanh Sidebar Top 10 Hot:** Tự động tính toán hiển thị bảng xếp hạng 10 bộ truyện có số lượng tương tác tích lũy (`luot_xem`) cao nhất hệ thống theo thời gian thực.
* **Tìm kiếm truyện:** Tìm kiếm truyện thông minh theo từ khóa nhập vào.
* **Trang Chi tiết truyện:** Hiển thị tóm tắt mô tả, tác giả, thể loại và danh sách toàn bộ các chương hiện có của bộ truyện đó. Đồng thời tự động tăng 1 lượt xem khi người dùng click vào xem truyện và chương.
* **Trang Đọc chương truyện:** Đọc nội dung văn bản chi tiết của chương, tích hợp hệ thống nút điều hướng thông minh cho phép chuyển sang "Chương trước" hoặc "Chương tiếp" (chỉ chuyển giữa các chương trong cùng một bộ truyện).
### 2. Phân hệ quản trị
* **Phân quyền:** Nếu tài khoản không có quyền `role='admin'` mà vẫn cố tình truy cập trực tiếp vào trang quản trị, hệ thống sẽ trả về lỗi `403 Forbidden`.
* **Quản lý (`/quan_ly`):** Dồn toàn bộ các thao tác xử lý dữ liệu về một trang quản trị giao diện Tab tiện lợi.
* **Quản lý Truyện:** * Xem danh sách toàn bộ truyện hiện có kèm mã ID định danh.
  * Thêm truyện mới, Sửa thông tin truyện và Xóa truyện thông qua các Pop-up Modal Bootstrap.
* **Quản lý Chương :** * Chọn một bộ truyện cụ thể từ thanh Select để lọc ra danh sách chương tương ứng.
  * Thêm chương mới, sửa nội dung chương và xóa chương khỏi database.
### 3.Hướng dẫn cách dùng
* **Bước 1:** Clone code về máy tính
  * **Yêu cầu phải tải Git trước đó**
  * Chọn 1 thư mục bất kì trên máy tính, xóa hết đường dẫn trên thanh điều hướng, gõ `cmd` rồi nhấn Enter.
  * Trong cửa sổ CMD vừa hiện ra, gõ `git clone https://github.com/Ketamine-011/Lightnovel-website` để clone dự án về máy, sau đó, thư mục dự án đã xuất hiện ngay tại thư mục chọn ban đầu.
* **Bước 2:** cài đặt các moi trường ảo và thư viện bắt buộc.
  * Khởi tạo môi trường ảo: `python -m venv venv`.
  * Kích hoạt môi trường ảo (Windows): `.\venv\Scripts\activate`, (MacOs/Linux): `source venv/bin/activate`.
  * Cài đặt các thư viện của dự án: `pip install flask flask_sqlalchemy flask_login werkzeug`.
* **Bước 3:** Khởi tạo DataBase và nạp dữ liệu mẫu (nạp sẵn tài khoản admin và 50 bộ truyện) 
  * `python seed_data.py.`
  * Tài khoản admin: `admin`.
  * Mật khẩu: `admin123`.
* **Bước 4:** Khởi chạy Server Flask
  * `python app.py`.
  * **Sau khi Server khởi động thành công, truy cập `http://127.0.0.1:5000` để trải nghiệm.**
### Nếu làm tất cả các bước trên nhưng vẫn còn lỗi về import thư viện thì làm như sau:
  * Bước 1: Bấm `Ctr + Shift + p` để mở *Command Palette* (
    hoặc bấm vào bánh răng góc dưới cùng bên trái chọn *Command Palette*)
  * Bước 2: Trên thanh tìm kiếm, gõ Python: Select Interpreter
  * Bước 3: Bấm vào đó và chọn phiên bản python có dạng `venv`
  *(Thao tác này giúp Vs Code hiểu và nạp đúng các thư viện vừa cài trong môi trường ảo vào workspace)*
