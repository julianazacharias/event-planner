from flask import Flask 

from extensions import api, db, ma
from resources.user import user_ns
from resources.person import person_ns

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

api.add_namespace(user_ns)
api.add_namespace(person_ns)

def create_tables():
    db.create_all()

if __name__ == "__main__":
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)