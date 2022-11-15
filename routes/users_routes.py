from flask import Blueprint

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/v1/users")
def get():
    return {"code": 200}
