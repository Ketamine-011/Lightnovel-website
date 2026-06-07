from flask import Flask
from models import db, User
from routes import Routes  
from flask_login import LoginManager



app = Flask(__name__)


app.config['SECRET_KEY'] = 'abcdxyz123456'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lightnovel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

Routes(app)


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)