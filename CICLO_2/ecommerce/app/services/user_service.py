from ..repositories.user_repository import UserRepository
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash

# Serviço de Usuário
class UserService:
    @staticmethod
    def create_user(username, password, email):
        # Cria um novo usuário com senha criptografada
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password, email=email)
        UserRepository.save(user)
        return user

    @staticmethod
    def authenticate(username, password):
        # Autentica o usuário verificando a senha
        user = UserRepository.find_by_username(username)
        if user and check_password_hash(user.password, password):
            return user
        return None
