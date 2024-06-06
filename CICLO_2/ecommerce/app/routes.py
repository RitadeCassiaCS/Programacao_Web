from flask import current_app as app
from .controllers.user_controller import user_bp

app.register_blueprint(user_bp, url_prefix='/user')



from flask import current_app as app
from .controllers import main_bp

# Registro do blueprint principal na aplicação
app.register_blueprint(main_bp)



from flask import current_app as app
from .controllers.user_controller import user_bp
from .controllers.order_controller import order_bp

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(order_bp, url_prefix='/api')  # Prefixo para as rotas de ordem



from flask import current_app as app
from .controllers.user_controller import user_bp
from .controllers.product_controller import product_bp

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(product_bp, url_prefix='/api')
