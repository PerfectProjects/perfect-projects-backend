import json

from flask import Blueprint, request

from backend.controllers.access_controller import AccessController

access = Blueprint("access", __name__)


@access.route('/access/sign-up', methods=["POST"])
def sign_up_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    new_user = decoded_data.get("newUser")
    return AccessController().create_account(new_user)


@access.route("/access/sign-in", methods=["POST"])
def sign_in_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    user = decoded_data.get("user")
    return AccessController().sign_in(user)


@access.route("/access/refresh-token", methods=["GET"])
def refresh_token_endpoint():
    ref_token = request.cookies.get("refreshToken")
    username = request.headers.get("username")
    return AccessController().refresh_token(ref_token, username)


@access.route('/access/verify-account', methods=["POST"])
def verify_account_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    username = decoded_data.get("username")
    confirmation_code = decoded_data.get("confirmationCode")
    return AccessController().verify_account(username, confirmation_code)
