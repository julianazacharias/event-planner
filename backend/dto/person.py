from flask_restx.fields import Integer,String
from extensions import api 

class PersonDto:

    person_model = api.model("Person", {
        "id": Integer,
        "first_name": String,
        "surname": String,
        "email": String,
        "document_id": String,
        "phone_number": String
    })
     
    person_input = api.model("Person", {
        "first_name": String,
        "surname": String,
        "email": String,
        "document_id": String,
        "phone_number": Integer
    })