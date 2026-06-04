from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Truyen, Chuong

def regis_routes(app):
    @app.route("/")
    
    def regis_routes(app):
        import os
    @app.route("/")
    def home():

     tu_khoa = request.args.get("q", "")

     if tu_khoa:
        ds_truyen = Truyen.query.filter(
            Truyen.ten_truyen.contains(tu_khoa)
        ).all()
     else:
        ds_truyen = Truyen.query.all()

    return render_template(
        "home.html",
     ds_truyen="ds_truyen"
    )


    @app.route("/xoa-truyen/<int:id>")
    def xoa_truyen(id):

     truyen = Truyen.query.get_or_404(id)

    db.session.delete(truyen)
    db.session.commit()

    return redirect(url_for("home"))


    @app.route("/them-chuong", methods=["POST"])
    def them_chuong():

     chuong = Chuong(
        ten_chuong=request.form["ten_chuong"],
        noi_dung=request.form["noi_dung"],
        truyen_id=request.form["truyen_id"]
    )

    db.session.add(chuong)
    db.session.commit()

    return redirect(url_for("home"))


    @app.route("/sua-chuong/<int:id>", methods=["POST"])
    def sua_chuong(id):

     chuong = Chuong.query.get_or_404(id)

    chuong.ten_chuong = request.form["ten_chuong"]
    chuong.noi_dung = request.form["noi_dung"]

    db.session.commit()

    return redirect(url_for("home"))


    @app.route("/xoa-chuong/<int:id>")
    def xoa_chuong(id):

     chuong = Chuong.query.get_or_404(id)

    db.session.delete(chuong)
    db.session.commit()

    return redirect(url_for("home"))