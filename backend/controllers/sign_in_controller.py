from backend.aws.cognito_provider import CognitoProvider
from backend.aws.secret_provider import SecretProvider


class SignInController:
    def __init__(self):
        self._cognito_pool_data = SecretProvider().get_secret()
        self._cognito_provider = CognitoProvider(
            self._cognito_pool_data.get("COGNITO_POOL_CLIENT_ID"),
            self._cognito_pool_data.get("COGNITO_POOL_CLIENT_SECRET"))

    def sign_in(self, user):
        return self._cognito_provider.sign_in(user)
