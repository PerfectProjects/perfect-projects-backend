from flask import Blueprint

sign_up = Blueprint('sign_up', __name__)


@sign_up.route('/sign-up', methods=["POST"])
def sign_up_endpoint():
    return {"success": True}
