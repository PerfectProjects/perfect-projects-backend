import json

import flask
from flask import Blueprint, request, Flask, jsonify

from backend.controllers.sign_in_controller import SignInController

sign_in = Blueprint("sign_in", __name__)


@sign_in.route("/sign-in", methods=["POST"])
def sign_in_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    user = decoded_data.get("user")
    return SignInController().sign_in(user)
