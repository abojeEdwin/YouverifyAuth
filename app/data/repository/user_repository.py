from pymongo import MongoClient
from app.data.model.user import User

class UserRepository:
    def __init__(self, connection_string="mongodb://localhost:27017", db_name="YouverifyAuth", collection_name="user"):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_user(self, user: User):
        user_dict = user.__dict__
        result = self.collection.insert_one(user_dict)
        return result.inserted_id

    def find_user_by_email(self, email: str):
        user_data = self.collection.find_one({"email": email})
        if user_data:
            return User(email=user_data.get("email"), password=user_data.get("password"))
        return None



