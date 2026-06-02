from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Truyen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ten_truyen = db.Column(db.String(100), nullable = False)
    tac_gia = db.Column(db.String(100), nullable = False)
    the_loai = db.Column(db.String(100), nullable = False)
    mo_ta = db.Column(db.Text, nullable = False)

