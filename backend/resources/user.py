from flask import request
from flask_restx import Resource, Namespace

from models.user import User
# from services.user import UserService
from schemas.user import UserSchema

user_ns = Namespace("user", description="User Actions")
user_schema  = UserSchema()


@user_ns.route("/")
class UserResource(Resource):
    def get(self):
        return {"hello": "restx"}

@user_ns.route("/list")
class UserListResource(Resource):
    @user_ns.marshal_list_with(user_schema.dump)
    def get(self):
        return User.list()


# @user_ns.route("/users")
# class UserResource(Resource):    
#     @user_ns.expect(user_schema)
#     @user_ns.marshal_with(user_schema)
#     def post(self):        
#         user_json = request.get_json()
#         user = user_schema.load(user_json)

#         if User.query.filter_by(username=user.username).first():
#             return {"message": "user_username_exists"}, 400
        
#         try:
#             user.insert()
#         except Exception as e:
#             return {"message": f"Error inserting: {str(e)}"}, 500
        
#         return user_schema.dump(user), 201
 

#     @user_ns.marshal_list_with(user_schema)
#     def get(self):
#         return User.list()

#     @user_ns.marshal_with(user_schema)
#     def get_by_id(self, user_id: int):
#         user = User.get_by_id(user_id)
#         if not user:
#             return {"message": "user_not_found"}, 404

#         return user_schema.dump(user), 200
    
#     @user_ns.marshal_with(user_schema)
#     def deactivate(self, user_id: int):
#         user = User.get_by_id(user_id)
#         if not user:
#             return {"message": "user_not_found"}, 404

#         User.deactivate(user)
#         return {"message": "user_deactivated"}, 200
    
#     @user_ns.marshal_with(user_schema)
#     def delete(self, user_id: int):
#         user = User.get_by_id(user_id)
#         if not user:
#             return {"message": "user_not_found"}, 404

#         User.delete(user)
#         return {"message": "user_deleted"}, 200