import base64
import json

from flask import Response

from backend.aws.cognito_provider import CognitoProvider
from backend.aws.secret_provider import SecretProvider
from backend.globals import REFRESH_TOKEN_EXPIRE
from datetime import datetime


class AccessController:
    def __init__(self):
        self._cognito_pool_data = SecretProvider().get_secret()
        self._cognito_provider = CognitoProvider(
            self._cognito_pool_data.get("COGNITO_POOL_CLIENT_ID"),
            self._cognito_pool_data.get("COGNITO_POOL_CLIENT_SECRET"))

    def sign_in(self, user):
        cognito_result = self._cognito_provider.sign_in(user)
        if cognito_result is not False:
            payload = {
                "accessToken": cognito_result["AuthenticationResult"]["AccessToken"],
            }
            response = Response(json.dumps({"payload": payload}), status=200)
            response.set_cookie("refreshToken",
                                cognito_result["AuthenticationResult"]["RefreshToken"],
                                samesite="None",
                                secure=True,
                                httponly=True,
                                expires=datetime.now().timestamp() + REFRESH_TOKEN_EXPIRE * 60)
            response.set_cookie("username",
                                base64.b64encode(user.get("username").encode()).decode(),
                                samesite="None",
                                secure=True,
                                domain=".perfect-projects.com",
                                expires=datetime.now().timestamp() + REFRESH_TOKEN_EXPIRE * 60)
            return response
        return Response(status=401)

    def refresh_token(self, refresh_token, username):
        response = self._cognito_provider.refresh_token(refresh_token, username)
        if response is not False:
            payload = {
                "accessToken": response["AuthenticationResult"]["AccessToken"]
            }
            return Response(json.dumps({"payload": payload}), status=200)
        return Response(status=401)

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
