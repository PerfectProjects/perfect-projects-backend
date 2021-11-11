import json

from flask import Response, g

from backend.aws.dynamodb.project_dynamodb_provider import ProjectDynamodbProvider
from backend.aws.s3.s3_provider import S3Provider


class UserProfileController:
    def __init__(self):
        self._dynamodb = ProjectDynamodbProvider()
        self._s3 = S3Provider()
        self._user_id = g.user.get("Username")

    def get_all_projects(self):
        result = self._dynamodb.get_all_user_projects(self._user_id)
        items = result.get("Items")
        projects = []
        for item in items:
            item_id = item.get("id")
            projects.append({
                "id": item_id,
                "title": item.get("title"),
                "author": item.get("user_id")})
        return Response(json.dumps({"projects": projects}),
                        status=200,
                        mimetype='application/json')
