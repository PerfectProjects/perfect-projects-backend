import json

import flask
from flask import Response

from backend.aws.cognito_provider import CognitoProvider
from backend.aws.dynamodb.project_dynamodb_provider import ProjectDynamodbProvider
from backend.aws.secret_provider import SecretProvider


class UserProfileController:
    def __init__(self):
        self.dynamodb = ProjectDynamodbProvider("project")

    def add_project(self, project):
        response = self.dynamodb.add_item(project)

        return Response(json.dumps({"success": response}),
                        status=200,
                        mimetype='application/json')
