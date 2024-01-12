# from flask import request
# from extensions import db

# from .base import BaseService
# from schemas.person import PersonSchema

# person_schema = PersonSchema()

# class PersonService(BaseService):
#     @classmethod
#     def create_person(cls):        
#         person_json = request.get_json()
#         person = person_schema.load(person_json)        

#         try:
#             person.insert()
#         except:
#             return {"message": "Error inserting"}, 500

#         return person_schema.dump(person), 201
    

    
    # def deactivate(id):        

    #     person.is_active = False
    #     person.deactivated_at = db.datetime.utcnow

        # entity = db.session.query(person).filter(person.id == id)
        # entity = person_model.query.filter_by(id=ns.payload["id"]).first() 
        # entity = cls.query.filter_by(username=username).first()

        # ------->> QUAL DOS 3 É O IDEAL?

        # entity.update()
        # db.session.commit()