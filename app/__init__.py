from flask import Flask
from app.controller.user_controller import user_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp, url_prefix='/api/users')
    return app
