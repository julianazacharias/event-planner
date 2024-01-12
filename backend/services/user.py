# from flask import request
# from extensions import db

# from .base import BaseService
# from models.user import User
# from schemas.user import UserSchema

# user_schema = UserSchema()

# class UserService(BaseService):
#     @classmethod
#     def create_user(cls):
#         user_json = request.get_json()
#         user = user_schema.load(user_json)
#         # user = user(username=ns.payload["username"], person_id=ns.payload["person_id"])

#         if User.find_by_username(user.username):
#             return {"message": "user_username_exists"}, 400
        
#         try:
#             user.insert()
#         except:
#             return {"message": "Error inserting"}, 500
        
#         return user_schema.dump(user), 201

#     @classmethod
#     def find_by_username(cls, username: str) -> "User":
#         return cls.query.filter_by(username=username).first()