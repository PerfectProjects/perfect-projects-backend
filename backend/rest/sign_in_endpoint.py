import json

from flask import Blueprint, request, session
from flask_cors import cross_origin

from backend.controllers.sign_in_controller import SignInController

sign_in = Blueprint("sign_in", __name__)


@sign_in.route("/sign-in", methods=["POST"])
def sign_in_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    user = decoded_data.get("user")
    refresh_token = request.cookies.get("REFRESH_TOKEN")
    print(refresh_token)
    return SignInController().sign_in(user)
