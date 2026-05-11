from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://gym_developer:11810qasim@localhost/gym_system"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = '9a8d782e874f3e779dfa49e6dacb27ec5a4d4992d732506b9911ead37820c357'
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

from flask_gym.models import Member   # ← must come AFTER db is defined

@login_manager.user_loader            # ← AFTER Member is imported
def load_user(user_id):
    return Member.query.get(int(user_id))

@login_manager.unauthorized_handler   # ← ADD THIS
def unauthorized():
    return jsonify({'message': 'Unauthorized'}), 401