from psycopg2 import connect
from flask import Flask

# web app instance
app = Flask(__name__)

# connect asynchronously
try:
    connection = connect("dbname=students")
    cursor = connection.cursor()
    print("connected to database")
except:
    print("Unable to connect to the database")


@app.route('/')
def index():
    return "<h1>Hello World!</h1>"


@app.route('/createtb/<tbname>')
def createTb(tbname):
    # create a table
    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {tbname} (id INTEGER PRIMARY KEY, name TEXT NOT NULL, class TEXT NOT NULL);"
    )

    # save the transaction
    connection.commit()
    return f"<h1>Created {tbname} Table successfully</h1>"


@app.route('/add-new-student/<string:name>/<int:id>')
def addNewStudent(name, id):
    cursor.execute(
        f"INSERT INTO  juniors (id, name, class) VALUES ({id}, {name}, 'JSS 3');"
    )

    connection.commit()  # ensure to commit the transaction

    return f"<h1>Welcome {name} to our school!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # # close the connection
    cursor.close()
    connection.close()
