from backend.aws.cognito_provider import CognitoProvider


class SignUpController:
    def __init__(self):
        self._cognito_provider = CognitoProvider()

    def create_account(self, new_user):
        self._cognito_provider.create_user(new_user)
