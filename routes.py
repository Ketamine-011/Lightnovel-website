from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from models import User, db, Truyen, Chuong
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user


def check_role(role):
    if current_user.role != role:
        abort(403) 
        
    
def Routes(app):
    @app.route("/dang_nhap", methods = ["GET", "POST"])
    def login():
        if request.method == "POST":
            login_username = request.form["username"]
            login_pw = request.form["password"]
            check_username = User.query.filter_by(username=login_username).first()
            if check_username and check_password_hash(check_username.password, login_pw):
                login_user(check_username)

                return redirect(url_for("home"))
            else:
                return render_template("dang_nhap.html", error = "Tên đăng nhập hoặc mật khẩu không đúng.")
        return render_template("dang_nhap.html")
    
            

    @app.route("/dang_ky", methods = ["GET", "POST"])
    def register():
        if request.method == "POST":
            regis_username = request.form["username"]
            regis_email = request.form["email"]
            pw = request.form["password"]

            #Hàm filter_by trả về đối tượng nếu có tồn tại trong database, nếu không có sẽ trả về None.
            #Hàm first() sẽ lấy phần tử đầu tiên trong kết quả truy vấn. Nếu không có, nó sẽ trả về None.
            #Không có hàm first(), câu truy vấn sẽ không được thực thi và chỉ trả về câu truy vấn

            if User.query.filter_by(username=regis_username).first():
                return render_template("dang_ky.html", error="Tên đăng nhập đã tồn tại.")
            elif User.query.filter_by(email=regis_email).first():
                return render_template("dang_ky.html", error="Email đã tồn tại.")
            else:
                # Mã hóa mật khẩu trước khi lưu vào database
                hashed_pw = generate_password_hash(pw)


                new_user = User(username = regis_username, email = regis_email, password = hashed_pw)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for("login"))

        return render_template("dang_ky.html")

    @app.route("/dang_xuat")
    def logout():
        logout_user() 
        return redirect(url_for("home"))




# ======================
# Trang chủ + tìm kiếm
# ======================

    @app.route("/")
    def home():
        tu_khoa = request.args.get("q", "")
        top_10 = []

        if tu_khoa:
            ds_truyen = Truyen.query.filter(
                Truyen.ten_truyen.contains(tu_khoa)
            ).all()
        else:
            ds_truyen = Truyen.query.all()
            top_10 = Truyen.query.order_by(Truyen.luot_xem.desc()).limit(10).all()

        return render_template(
            "trang_chu.html",
            ds_truyen=ds_truyen,
            top_10=top_10
        )
    @app.route("/truyen/<int:id>")
    def chi_tiet_truyen(id):
        truyen = Truyen.query.get_or_404(id)
        ds_chuong = Chuong.query.filter_by(id_truyen=id).all() 
        
        # Tự động cộng 1 lượt xem khi có người click vào xem truyện
        truyen.luot_xem += 1
        db.session.commit()
        
        return render_template("chi_tiet_truyen.html", truyen=truyen, ds_chuong=ds_chuong)
    @app.route("/quan_ly")
    @login_required
    def quan_ly():
        check_role("admin")
        tat_ca_truyen = Truyen.query.all()

        chon_id = request.args.get("truyen_id", type=int)
        chon_truyen = None
        ds_chuong = []
        if chon_id:
            chon_truyen = Truyen.query.get(selected_id)
            if chon_truyen:
                ds_chuong = Chuong.query.filter_by(id_truyen=selected_id).all()
   

        return render_template("quan_ly.html", 
                           ds_truyen=tat_ca_truyen,
                           selected_truyen=chon_truyen,
                           selected_truyen_id=chon_id,
                           ds_chuong=ds_chuong)
 
    @app.route("/them-truyen", methods=["GET", "POST"])
    @login_required
    def them_truyen():
        check_role("admin")
        if request.method == "POST":
            ten = request.form["ten_truyen"]
            tac_gia = request.form["tac_gia"]
            the_loai = request.form["the_loai"]
            mo_ta = request.form["mo_ta"]
            truyen_moi = Truyen(ten_truyen=ten, tac_gia=tac_gia, the_loai=the_loai, mo_ta=mo_ta, luot_xem=0)
            db.session.add(truyen_moi)
            db.session.commit()
            return redirect(url_for("quan_ly"))

        return render_template("quan_ly.html")


    @app.route("/sua-truyen/<int:id>", methods=["POST"])
    @login_required
    def sua_truyen(id):
        check_role("admin")
        truyen = Truyen.query.get_or_404(id)
        
        truyen.ten_truyen = request.form["ten_truyen"]
        truyen.tac_gia = request.form["tac_gia"]
        truyen.the_loai = request.form["the_loai"]
        truyen.mo_ta = request.form["mo_ta"]
        
        db.session.commit()
        return redirect(url_for("quan_ly"))


    @app.route("/xoa-truyen/<int:id>", methods=["POST"])
    @login_required
    def xoa_truyen(id):
        check_role("admin")
        truyen = Truyen.query.get_or_404(id)
        db.session.delete(truyen)
        db.session.commit()
        return redirect(url_for("quan_ly"))


    #======================
    #Thêm, sửa, xóa chương
    #======================

    @app.route("/them-chuong", methods=["POST"])
    @login_required
    def them_chuong():
        check_role("admin")
        chuong = Chuong(
            ten_chuong=request.form["ten_chuong"],
            noi_dung=request.form["noi_dung"],
            truyen_id=request.form["truyen_id"]
        )
        db.session.add(chuong)
        db.session.commit()
        return redirect(url_for("quan_ly"))


    @app.route("/sua-chuong/<int:id>", methods=["POST"])
    @login_required
    def sua_chuong(id):
        check_role("admin")
        chuong = Chuong.query.get_or_404(id)
        chuong.ten_chuong = request.form["ten_chuong"]
        chuong.noi_dung = request.form["noi_dung"]
        db.session.commit()
        return redirect(url_for("quan_ly"))


    @app.route("/xoa-chuong/<int:id>", methods=["POST", "GET"])
    @login_required
    def xoa_chuong(id):
        check_role("admin")
        chuong = Chuong.query.get_or_404(id)
        db.session.delete(chuong)
        db.session.commit()
        return redirect(url_for("quan_ly")) 
    @app.route("/doc-chuong/<int:id>")
    def doc_truyen(id):
        chuong_hien_tai = db.session.get(Chuong, id)

        if not chuong_hien_tai:
            abort(404)

            truyen_chu_quan = db.session.get(Truyen, chuong_hien_tai.truyen_id)


        if truyen_chu_quan:
            truyen_chu_quan.luot_xem = truyen_chu_quan.luot_xem + 1
            db.session.commit() 

        chuong_truoc = Chuong.query.filter(
            Chuong.truyen_id == chuong_hien_tai.truyen_id,
            Chuong.id < id
        ).order_by(Chuong.id.desc()).first()


        chuong_tiep = Chuong.query.filter(
            Chuong.truyen_id == chuong_hien_tai.truyen_id,
            Chuong.id > id
        ).order_by(Chuong.id.asc()).first()


        return render_template(
            "doc_truyen.html",
            chuong=chuong_hien_tai,       # Khớp với biến {{ chuong }} ngoài HTML
            truyen=truyen_chu_quan,       # Khớp với biến {{ truyen }} ngoài HTML
            prev_chuong=chuong_truoc,     # Khớp với biến {{ prev_chuong }} ngoài HTML
            next_chuong=chuong_tiep       # Khớp với biến {{ next_chuong }} ngoài HTML
        )