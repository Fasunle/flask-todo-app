from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://kehinde@localhost:5432/example"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
# migrate = Migrate(app, db)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"<Person ID: {self.id}, name: {self.name}, email: {self.email}>"


db.create_all()     # without this, the table does not get created


db.session.add(
    Person(name="Kehinde Fasunle", email="kfasunle@gmail.com")
)   # changes the state to Pending

db.session.commit()  # changes the state to committed

persons = Person.query.all()  # changes the state to Flushed

print(persons)
