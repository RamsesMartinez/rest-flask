from flask import Flask
from flask_restful import Api
from db import database

from routes.users_routes import users_blueprint

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.register_blueprint(users_blueprint)


if __name__ == "__main__":
    database.create_database("./db/database.db")
    app.run()
