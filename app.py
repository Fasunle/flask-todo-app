from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://kehinde@localhost:5432/todoapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Todo(db.Model):

    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<Todo ID: {self.id}, description: {self.description} Completed: {self.completed}>"


db.create_all()  #   create tables for the specified schema(s)


@app.route("/")
def index():
    return "Hello world"

db.session.add(
    Todo(description="Life is very interesting. I love to make money than I need.")
)  # changes the state to Pending

db.session.commit()  # changes the state to committed

todos = Todo.query.all()  # changes the state to Flushed

if __name__ == "__main__":
    app.run(debug=True)
