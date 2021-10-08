import json

from flask import Blueprint, request

from backend.controllers.sign_in_controller import SignInController

sign_in = Blueprint("sign_in", __name__)


@sign_in.route("/sign-in", methods=["POST"])
def sign_up_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    user = decoded_data.get("user")
    return {"payload": SignInController().sign_in(user)}
