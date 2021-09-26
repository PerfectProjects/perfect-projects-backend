import json

from flask import Blueprint, request

from backend.controllers.sign_up_controller import SignUpController

sign_up = Blueprint('sign_up', __name__)


@sign_up.route('/sign-up', methods=["POST"])
def sign_up_endpoint():
    print("This is a new user")
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    new_user = decoded_data.get("newUser")

    SignUpController().create_account(new_user)

    return {"success": True}
