import json

import flask

from backend.aws.cognito_provider import CognitoProvider
from backend.aws.secret_provider import SecretProvider


class SignInController:
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
                "refreshToken": cognito_result["AuthenticationResult"]["RefreshToken"]
            }
            return flask.Response(json.dumps({"payload": payload}), status=200)
        return flask.Response(status=401)

    def refresh_token(self, refresh_token, username):
        response = self._cognito_provider.refresh_token(refresh_token, username)
        if response is not False:
            payload = {
                "accessToken": response["AuthenticationResult"]["AccessToken"]
            }
            return flask.Response(json.dumps({"payload": payload}), status=200)
        return flask.Response(status=401)
