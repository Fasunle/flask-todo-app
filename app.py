from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, jsonify, render_template, request


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


@app.route("/")
def index():
    return render_template("index.html", data=Todo.query.all())


@app.route("/todos/create", methods=["POST"])
def create_todo():
    """Create a todo item"""
    body = {}
    error = False

    try:
        description = request.get_json()["description"]
        todo = Todo(description=description)
        body["description"] = todo.description
        db.session.add(todo)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()

        if error == True:
            abort(400)
        else:
            return jsonify(body)


if __name__ == "__main__":
    app.run(debug=True)
