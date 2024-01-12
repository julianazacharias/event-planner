from flask_restx.fields import Integer,String, Nested
from extensions import api 

from dto.person import PersonDto

person_dto = PersonDto()

class UserDto:

    user_model = api.model("User", {
        "id": Integer,
        "username": String,
        "password": String,
        "person": Nested(person_dto.person_model)
    })
     
    user_input = api.model("User", {
        "username": String,
        "password": String
    })