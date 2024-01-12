from __future__ import annotations
from typing import Union

from extensions import db
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base(object):
    __abstract__ = True

    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.utcnow, nullable=False)
    deactivated_at = db.Column(db.DateTime)

    @declared_attr
    def __tablename__(cls) -> str:
        """
        Generate __tablename__ automatically

        Returns:
            Table name
        """
        return cls.__name__.lower()
    
    def insert(self) -> Base:
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self) -> Base:
        db.session.delete(self)
        db.session.commit()
        return self
    
    @classmethod
    def deactivate(cls, id: int):
        entity = db.session.query(cls).filter_by(id=id).first()
        if entity:
            entity.is_active = False
            entity.deactivated_at = db.datetime.utcnow()
            db.session.commit()

    @classmethod
    def update(cls, id: int, to_update: dict) -> None:
        db.session.query(cls).filter(cls.id == id).update(to_update)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id: int) -> Union[Base, None]:
        row = db.session.query(cls).filter_by(id=id).first()
        return row

    @classmethod
    def list(cls) -> Union[Base, None]:
        rows = db.session.query(cls).all()
        return rows