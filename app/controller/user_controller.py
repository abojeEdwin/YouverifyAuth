from flask import Blueprint, request, jsonify
from app.service.user_service import User_Service
from app.data.model.user import User
from app.exception.duplicate_email_exception import Duplicate_Email_Exception
from app.exception.invalid_password_exception import Invalid_Password_Exception
from app.exception.user_not_found_exception import User_Not_Found_Exception
import traceback

user_bp = Blueprint('user', __name__)
user_service = User_Service()

@user_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        user = User(email=data.get('email'), password=data.get('password'))
        registered_user = user_service.register(user)
        return jsonify({"message": "User registered successfully", "email": registered_user.email}), 201
    except (Duplicate_Email_Exception, ValueError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"error": "An unexpected error occurred"}), 500

@user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = User(email=data.get('email'), password=data.get('password'))
        token = user_service.login(user)
        return jsonify({"token": token}), 200
    except (User_Not_Found_Exception, Invalid_Password_Exception) as e:
        return jsonify({"error": str(e)}), 401
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({"error": "An unexpected error occurred"}), 500
