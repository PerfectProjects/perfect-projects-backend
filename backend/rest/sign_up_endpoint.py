import json

from flask import Blueprint, request
from backend.controllers.sign_up_controller import SignUpController

sign_up = Blueprint('sign_up', __name__)


@sign_up.route('/sign-up', methods=["POST"])
def sign_up_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    new_user = decoded_data.get("newUser")
    return {"success": SignUpController().create_account(new_user)}
