# from typing import Union

# from extensions import db

# from sqlalchemy.ext.declarative import as_declarative

# @as_declarative()
# class BaseService:

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()
#         return self

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#         return self
    
#     @classmethod
#     def list_all(cls):
#         entities = db.session.query(cls).all()
#         return entities
    
#     @classmethod
#     def get_by_id(cls, id: int):
#         entity = db.session.query(cls).filter_by(id=id).first()
#         return entity
    
#     @classmethod
#     def update(cls, id: int, to_update: dict):
#         db.session.query(cls).filter(cls.id == id).update(to_update)
#         db.session.commit()
    
#     @classmethod
#     def deactivate(cls, id: int):
#         entity = db.session.query(cls).filter_by(id=id).first()
#         if entity:
#             entity.is_active = False
#             entity.deactivated_at = db.datetime.utcnow()
#             db.session.commit()
    
    # @classmethod
    # def deactivate(cls, id: int, to_update: dict) -> None:      
    #     entity = db.session.query(cls).filter_by(id=id).first()
    #     entity.is_active = False
    #     entity.deactivated_at = db.datetime.utcnow
    #     db.session.query(cls).filter(cls.id == id).update(to_update)
    #     db.session.commit()
        
