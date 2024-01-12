from extensions import ma
from models.person import Person

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        load_only = ("user",)
        dump_only = ("id",)
        include_fk = True