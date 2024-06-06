from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.order_service import OrderService
from ..services.user_service import UserService

order_bp = Blueprint('order_bp', __name__)

# Rota para criar uma nova ordem
@order_bp.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
    data = request.get_json()
    current_user = get_jwt_identity()
    user = UserService.find_by_username(current_user)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    order = OrderService.create_order(user.id, data['total_price'])
    return jsonify(id=order.id, user_id=order.user_id, total_price=order.total_price, created_at=order.created_at), 201

# Rota para listar todas as ordens
@order_bp.route('/orders', methods=['GET'])
@jwt_required()
def get_orders():
    orders = OrderService.get_all_orders()
    orders_list = [
        {
            "id": order.id,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "created_at": order.created_at
        }
        for order in orders
    ]
    return jsonify(orders_list), 200

# Rota para obter uma ordem específica por ID
@order_bp.route('/orders/<int:order_id>', methods=['GET'])
@jwt_required()
def get_order(order_id):
    order = OrderService.get_order_by_id(order_id)
    if not order:
        return jsonify({"msg": "Order not found"}), 404

    order_data = {
        "id": order.id,
        "user_id": order.user_id,
        "total_price": order.total_price,
        "created_at": order.created_at
    }
    return jsonify(order_data), 200

# Rota para atualizar o status de uma ordem
@order_bp.route('/orders/<int:order_id>', methods=['PUT'])
@jwt_required()
def update_order(order_id):
    data = request.get_json()
    order = OrderService.get_order_by_id(order_id)
    if not order:
        return jsonify({"msg": "Order not found"}), 404

    updated_order = OrderService.update_order(order_id, data['total_price'])
    return jsonify(id=updated_order.id, user_id=updated_order.user_id, total_price=updated_order.total_price, created_at=updated_order.created_at), 200
