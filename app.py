from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://kehinde@localhost:5432/example"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Todo(db.Model):

    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self) -> str:
        return f"<Todo ID: {self.id}, name: {self.description}>"


# create tables from Models
db.create_all()


db.session.add(
    Todo(description="Life is very interesting. I love to make money than I need.")
)  # changes the state to Pending

db.session.commit()  # changes the state to committed

todos = Todo.query.all()  # changes the state to Flushed

print("A todo item\n", todos[0])
print("A list of all todos\n", todos)
