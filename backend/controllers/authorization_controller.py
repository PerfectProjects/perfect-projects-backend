import json

import flask

from backend.aws.cognito_provider import CognitoProvider
from backend.aws.secret_provider import SecretProvider


class AuthorizationController:
    def __init__(self):
        pass