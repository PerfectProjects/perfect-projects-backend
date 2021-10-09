from flask import Blueprint, request

from backend.controllers.sign_in_controller import SignInController

refresh_token = Blueprint("refresh_token", __name__)


@refresh_token.route("/refresh-token", methods=["GET"])
def refresh_token_endpoint():
    ref_token = request.headers.get("refreshToken")
    username = request.headers.get("username")
    return {"accessToken": SignInController().refresh_token(ref_token, username)}
