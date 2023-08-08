from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS

app = Flask(__name__)
# cors = CORS(app, resources={r"/": {"origins": "http://localhost:8000"}})
# app.config['WTF_CSRF_ENABLED'] = False

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

from app.routes import user_bp

app.register_blueprint(user_bp, url_prefix='/v1')