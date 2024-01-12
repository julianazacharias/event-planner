from extensions import db 

from .base import Base

class User(Base):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=False)

    person = db.relationship("Person", uselist=False, back_populates="user", single_parent=True)

    __table_args__ = (db.UniqueConstraint("person_id", name="uq_person_id"),)