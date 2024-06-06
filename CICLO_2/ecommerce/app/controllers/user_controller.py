from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ..services.user_service import UserService

user_bp = Blueprint('user_bp', __name__)

# Rota para registro de usuário
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = UserService.create_user(data['username'], data['password'], data['email'])
    return jsonify(id=user.id, username=user.username, email=user.email), 201

# Rota para login de usuário
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = UserService.authenticate(data['username'], data['password'])
    if user:
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401
