from extensions import db 

from .base import Base

class Person(Base):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    document_id = db.Column(db.String(255), unique=True)
    phone_number = db.Column(db.String(255), unique=True)
    
    user = db.relationship("User", uselist=False, back_populates="person")