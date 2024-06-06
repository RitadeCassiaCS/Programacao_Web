from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..services.product_service import ProductService

product_bp = Blueprint('product_bp', __name__)

# Rota para criar um novo produto
@product_bp.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    product = ProductService.create_product(data['name'], data['description'], data['price'], data['stock'])
    return jsonify(id=product.id, name=product.name, description=product.description, price=product.price, stock=product.stock), 201

# Rota para obter todos os produtos
@product_bp.route('/products', methods=['GET'])
def get_products():
    products = ProductService.get_all_products()
    return jsonify([{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price, 'stock': product.stock} for product in products]), 200

# Rota para obter um produto pelo ID
@product_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = ProductService.get_product_by_id(id)
    if product:
        return jsonify(id=product.id, name=product.name, description=product.description, price=product.price, stock=product.stock), 200
    return jsonify({"msg": "Product not found"}), 404

# Rota para atualizar um produto pelo ID
@product_bp.route('/products/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    data = request.get_json()
    product = ProductService.update_product(id, data['name'], data['description'], data['price'], data['stock'])
    if product:
        return jsonify(id=product.id, name=product.name, description=product.description, price=product.price, stock=product.stock), 200
    return jsonify({"msg": "Product not found"}), 404

# Rota para deletar um produto pelo ID
@product_bp.route('/products/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    success = ProductService.delete_product(id)
    if success:
        return jsonify({"msg": "Product deleted"}), 200
    return jsonify({"msg": "Product not found"}), 404
