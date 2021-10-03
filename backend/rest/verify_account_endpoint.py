import json

from flask import Blueprint, request, Response
from backend.controllers.sign_up_controller import SignUpController

verify_account = Blueprint('verify_account', __name__)


@verify_account.route('/verify-account', methods=["POST"])
def verify_account_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    verify_code = decoded_data.get("verifyCode")

    print("hello!@! !!")
    return Response(json.dumps({"success": SignUpController().verify_account(verify_code)}), status=200,
                    mimetype='application/json')
