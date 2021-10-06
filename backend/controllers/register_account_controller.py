from backend.aws.cognito_provider import CognitoProvider
from backend.aws.secret_provider import SecretProvider


class RegisterAccountController:
    def __init__(self):
        self._cognito_pool_data = SecretProvider().get_secret()
        self._cognito_provider = CognitoProvider(
            self._cognito_pool_data.get("COGNITO_POOL_CLIENT_ID"),
            self._cognito_pool_data.get("COGNITO_POOL_CLIENT_SECRET"))

    def create_account(self, new_user):
        return self._cognito_provider.create_user(new_user)

    def verify_account(self, username, confirmation_code):
        return self._cognito_provider.verify_account(username, confirmation_code)
