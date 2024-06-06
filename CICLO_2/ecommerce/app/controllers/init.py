from flask import Blueprint
from .user_controller import user_bp
from .product_controller import product_bp
from .order_controller import order_bp

# Criação de um blueprint principal que agrupa todos os outros blueprints
main_bp = Blueprint('main_bp', __name__)

# Registro dos blueprints de usuário, produto e ordem com prefixos de URL
main_bp.register_blueprint(user_bp, url_prefix='/user')
main_bp.register_blueprint(product_bp, url_prefix='/product')
main_bp.register_blueprint(order_bp, url_prefix='/order')

# Exportação do blueprint principal para uso na aplicação principal
__all__ = ['main_bp']
