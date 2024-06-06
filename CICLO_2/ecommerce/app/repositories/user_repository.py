from ..models import User
from .. import db

# Repositório de Usuário
class UserRepository:
    @staticmethod
    def find_by_username(username):
        # Busca usuário pelo nome de usuário
        return User.query.filter_by(username=username).first()

    @staticmethod
    def save(user):
        # Salva o usuário no banco de dados
        db.session.add(user)
        db.session.commit()
