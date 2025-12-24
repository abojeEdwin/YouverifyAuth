import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def generate_token(email: str) -> str:
    secret_key = os.getenv("SECRET_KEY")
    payload = {
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, secret_key, algorithm='HS256')