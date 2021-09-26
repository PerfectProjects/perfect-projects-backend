import base64
import hashlib
import hmac

import boto3
from botocore.exceptions import ClientError


class CognitoProvider:

    def __init__(self):
        self.client = boto3.client("cognito-idp")
        self.app_client_id = ""
        self.app_client_secret = ""
        self.username = None
        self.password = None
        self.email = None

    def _create_secret_hash(self, username):
        message = bytes(username + self.app_client_id, "utf-8")
        key = bytes(self.app_client_secret, "utf-8")
        return base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()

    def create_user(self, new_user):
        self.username = new_user.get("nickname")
        self.email = new_user.get("email")
        self.password = new_user.get("password")

        secret_hash = self._create_secret_hash(self.username)

        try:
            self.client.sign_up(
                ClientId=self.app_client_id,
                SecretHash=secret_hash,
                Username=self.username,
                Password=self.password,
                UserAttributes=[{"Name": "email", "Value": self.email}])
        except ClientError as error:
            print(error)
            return False
        return True
