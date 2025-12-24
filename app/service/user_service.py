
from app.data.repository.user_repository import UserRepository
from app.data.model.user import User
from app.exception.duplicate_email_exception import Duplicate_Email_Exception
from app.exception.invalid_password_exception import Invalid_Password_Exception
from app.exception.user_not_found_exception import User_Not_Found_Exception
from app.utils.validators import verify_password, hash_password, validate_email
from app.utils.generate_token import generate_token

class User_Service:
    def __init__(self):
        self.user_repository = UserRepository()

    def register(self, request: User) -> User:
        if not validate_email(request.email):
            raise ValueError("Invalid email format")
        if self.user_repository.find_user_by_email(request.email):
            raise Duplicate_Email_Exception("User already exist")
        if not request.password:
            raise ValueError("Password is required")
        
        user = User()
        user.email = request.email
        user.password = hash_password(request.password)
        return self.user_repository.create_user(user)


    def login(self, request: User) -> str:
        user = self.user_repository.find_user_by_email(request.email)
        if not user:
            raise User_Not_Found_Exception("User not found")
        if not verify_password(request.password, user.password):
            raise Invalid_Password_Exception("Invalid password")
        
        token = generate_token(user.email)
        return token
