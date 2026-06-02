from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# =========================
# Cấu hình SQLite
# =========================
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# =========================
# Model Student
# =========================
class Student(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    age = db.Column(
        db.Integer,
        nullable=False
    )

    major = db.Column(
        db.String(100),
        nullable=False
    )

# =========================
# Trang chủ
# =========================
@app.route("/")
def home():

    students = Student.query.all()

    return render_template(
        "index.html",
        students=students
    )

# =========================
# Thêm sinh viên
# =========================
@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        major = request.form["major"]

        student = Student(
            name=name,
            age=age,
            major=major
        )

        db.session.add(student)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")

# =========================
# Cập nhật sinh viên
# =========================
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_student(id):

    student = Student.query.get_or_404(id)

    if request.method == "POST":

        student.name = request.form["name"]
        student.age = request.form["age"]
        student.major = request.form["major"]

        db.session.commit()

        return redirect(url_for("home"))

    return render_template(
        "update.html",
        student=student
    )

# =========================
# Xóa sinh viên
# =========================
@app.route("/delete/<int:id>")
def delete_student(id):

    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    return redirect(url_for("home"))

# =========================
# Main
# =========================
if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)
