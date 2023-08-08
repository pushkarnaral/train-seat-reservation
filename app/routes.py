from flask import Blueprint, request, jsonify
from app import db, bcrypt
from app.models import User
from flask_cors import cross_origin

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
@cross_origin()
def register():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

# Add login and profile management routes
from flask_jwt_extended import create_access_token
from app import bcrypt

# ...

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    user = User.query.filter_by(email=data['email']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid email or password'}), 401