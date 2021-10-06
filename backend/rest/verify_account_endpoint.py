import json

from flask import Blueprint, request, Response
from backend.controllers.register_account_controller import RegisterAccountController

verify_account = Blueprint('verify_account', __name__)


@verify_account.route('/verify-account', methods=["POST"])
def verify_account_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    username = decoded_data.get("username")
    confirmation_code = decoded_data.get("confirmationCode")
    return Response(json.dumps({"success": RegisterAccountController().verify_account(username, confirmation_code)}),
                    status=200,
                    mimetype='application/json')
