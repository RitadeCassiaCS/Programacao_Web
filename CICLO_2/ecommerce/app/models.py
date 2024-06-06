from . import db
from datetime import datetime

# Modelo de Usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)  # Nome de usuário único
    password = db.Column(db.String(200), nullable=False)  # Senha do usuário
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email do usuário único
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Data de criação do usuário

# Modelo de Produto
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)  # Nome do produto
    description = db.Column(db.String(500), nullable=False)  # Descrição do produto
    price = db.Column(db.Float, nullable=False)  # Preço do produto
    stock = db.Column(db.Integer, nullable=False)  # Quantidade em estoque

# Modelo de Ordem
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Relacionamento com o usuário
    total_price = db.Column(db.Float, nullable=False)  # Preço total da ordem
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Data de criação da ordem
    user = db.relationship('User', backref=db.backref('orders', lazy=True))  # Relacionamento inverso com o usuário
