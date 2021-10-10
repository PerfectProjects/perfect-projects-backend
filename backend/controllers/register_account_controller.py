import json

from flask import Response

from backend.aws.cognito_provider import CognitoProvider
from backend.aws.secret_provider import SecretProvider


class RegisterAccountController:
    def __init__(self):
        self._cognito_pool_data = SecretProvider().get_secret()
        self._cognito_provider = CognitoProvider(
            self._cognito_pool_data.get("COGNITO_POOL_CLIENT_ID"),
            self._cognito_pool_data.get("COGNITO_POOL_CLIENT_SECRET"))

    def create_account(self, new_user):
        result = self._cognito_provider.create_user(new_user)
        if result is True:
            return Response(json.dumps({"success": result}),
                            status=200,
                            mimetype='application/json')

        return Response(json.dumps({"success": result}),
                        status=400,
                        mimetype='application/json')

    def verify_account(self, username, confirmation_code):
        result = self._cognito_provider.verify_account(username, confirmation_code)
        if result is True:
            return Response(json.dumps({"success": result}),
                            status=200,
                            mimetype='application/json')

        return Response(json.dumps({"success": result}),
                        status=400,
                        mimetype='application/json')
