from backend.aws.cognito_provider import CognitoProvider
from backend.aws.secret_provider import SecretProvider


class SignUpController:
    def __init__(self):
        self.cognito_pool_data = SecretProvider().get_secret()

        print("MY SECRETS!")
        print(self.cognito_pool_data)
        self._cognito_provider = CognitoProvider(
            self.cognito_pool_data.get("COGNITO_POOL_CLIENT_ID"),
            self.cognito_pool_data.get("COGNITO_POOL_CLIENT_SECRET"))

    def create_account(self, new_user):
        self._cognito_provider.create_user(new_user)
