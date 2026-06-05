from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()

# Database quản lý truyện
class Truyen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ten_truyen = db.Column(db.String(100), nullable = False)
    tac_gia = db.Column(db.String(100), nullable = False)
    the_loai = db.Column(db.String(100), nullable = False)
    mo_ta = db.Column(db.Text, nullable = False)
    chaps = db.relationship('chuong', backref = 'truyen', lazy = True)

# Database quản lý người dùng
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    role = db.Column(db.String(20), nullable=False, default='user')

# Database quản lý chương
class Chuong(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ten_chuong = db.Column(db.String(100), nullable=False)
    noi_dung = db.Column(db.Text, nullable=False)
    truyen_id = db.Column(db.Integer, db.ForeignKey('truyen.id'), nullable=False)

db.create_all()
