from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Truyen
from routes import regis_routes

app = Flask(__name__)

# =========================
# Cấu hình SQLite
# =========================
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///novels.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)
