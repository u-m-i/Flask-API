from flask import Blueprint, current_app

request_blueprint = Blueprint("request", __name__)


@request_blueprint.route("/tell", methods=["GET"])
def joke_get():
    pass

@request_blueprint.route("/seriously", methods=["POST"])
def joke_post():
    pass




