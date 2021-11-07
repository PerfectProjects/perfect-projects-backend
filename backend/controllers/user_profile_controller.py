import json

from flask import Response, g

from backend.aws.dynamodb.project_dynamodb_provider import ProjectDynamodbProvider
from backend.aws.s3.s3_provider import S3Provider


class UserProfileController:
    def __init__(self):
        self.dynamodb = ProjectDynamodbProvider()
        self.s3 = S3Provider()
        self.user_id = g.user.get("Username")

    def get_all_projects(self):
        result = self.dynamodb.get_all_user_projects(self.user_id)
        items = result.get("Items")
        projects = []
        for item in items:
            item_id = item.get("id")
            item_description = self.s3.get_file(item_id).get("Body").read().decode("utf-8")
            projects.append({
                "id": item_id,
                "title": item.get("title"),
                "author": item.get("user_id"),
                "description": item_description})
        return Response(json.dumps({"projects": projects}),
                        status=200,
                        mimetype='application/json')
