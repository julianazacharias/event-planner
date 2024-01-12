from flask import request
from flask_restx import Resource, Namespace
# from services.person import PersonService
from models.person import Person
from schemas.person import PersonSchema

person_ns = Namespace("person", description="Person Actions", path="/person")
person_schema = PersonSchema()

@person_ns.route("/")
class PersonResource(Resource):
    def get(self):
        return {"hello": "restx - person"}
    
@person_ns.route("/list")
class PersonListResource(Resource):
    # @person_ns.marshal_list_with(person_schema)
    def get(self):
        person_list = Person.list()
        return person_list, 200


# @person_ns.route("/person")
# class PersonResource(Resource):
    
#     @person_ns.expect(person_schema)
#     @person_ns.marshal_with(person_schema)
#     def post(self):      
#         person_json = request.get_json()
#         person = person_schema.load(person_json)        

#         try:
#             person.insert()
#         except Exception as e:
#             return {"message": f"Error inserting: {str(e)}"}, 500

#         return person_schema.dump(person), 201
    
    # @person_ns.marshal_list_with(person_schema)
    # def get(self):
    #     person_list = Person.list()
    #     return person_list, 200

    # @person_ns.marshal_with(person_schema)
    # def get_by_id(self, person_id: int):
    #     person = Person.get_by_id(person_id)
    #     if not person:
    #         return {"message": "person not found"}, 404

    #     return person_schema.dump(person), 200

    # @person_ns.marshal_with(person_schema)
    # def deactivate(self, person_id: int):
    #     person = Person.get_by_id(person_id)
    #     if not person:
    #         return {"message": "person not found"}, 404

    #     Person.deactivate(person)
    #     return {"message": "Person deactivated"}, 200
    
    # @person_ns.marshal_with(person_schema)
    # def delete(self, person_id: int):
    #     person = Person.get_by_id(person_id)
    #     if not person:
    #         return {"message": "person not found"}, 404

    #     Person.delete(person)
    #     return {"message": "Person deleted"}, 200