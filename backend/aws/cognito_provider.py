import base64
import hashlib
import hmac

import boto3
from botocore.exceptions import ClientError


class CognitoProvider:

    def __init__(self, app_client_id, app_client_secret):
        self.client = boto3.client("cognito-idp")
        self.app_client_id = app_client_id
        self.app_client_secret = app_client_secret

    def _create_secret_hash(self, username):
        message = bytes(username + self.app_client_id, "utf-8")
        key = bytes(self.app_client_secret, "utf-8")
        return base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()

    def create_user(self, new_user):
        username = new_user.get("username")
        email = new_user.get("email")
        password = new_user.get("password")

        secret_hash = self._create_secret_hash(username)

        try:
            self.client.sign_up(
                ClientId=self.app_client_id,
                SecretHash=secret_hash,
                Username=username,
                Password=password,
                UserAttributes=[{"Name": "email", "Value": email}])
        except Exception as error:
            print(error)
            return False
        return True

    def sign_in(self, user):
        username = user.get("username")
        password = user.get("password")

        secret_hash = self._create_secret_hash(username)

        try:
            response = self.client.initiate_auth(
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": username,
                    "PASSWORD": password,
                    "SECRET_HASH": secret_hash
                },
                ClientMetadata={
                    "USERNAME": username,
                    "PASSWORD": password
                },
                ClientId=self.app_client_id)

            print("response!")
            print(response)
        except ClientError as error:
            print(error)
            return False
        return response

    def verify_account(self, verify_code, token):
        try:
            response = self.client.verify_user_attribute(
                AccessToken=token,
                AttributeName="email",
                Code=verify_code)

            print("response!")
            print(response)
        except Exception as error:
            print(error)
            return False
        return True
