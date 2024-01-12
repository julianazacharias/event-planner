from extensions import ma
from models.user import User
from schemas.person import PersonSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    person = ma.Nested(PersonSchema, many=False)

    class Meta:
        model = User
        load_instance = True
        load_only = ("password",)
        dump_only = ("id",)