import json

from flask import Response, g

from backend.aws.dynamodb.projects_dynamodb_provider import ProjectsDynamodbProvider
from backend.aws.s3.s3_provider import S3Provider


class UserProfileController:
    def __init__(self):
        self._dynamodb = ProjectsDynamodbProvider()
        self._s3 = S3Provider()
        self._user_id = g.user.get("Username")

    def get_all_projects(self):
        dynamo_result = self._dynamodb.get_all_user_projects(self._user_id)
        items = dynamo_result.get("Items")
        projects = []
        for item in items:
            item_id = item.get("id")
            item_picture = self._s3.get_file(f"{item_id}/picture")

            if item_picture:
                item_picture = item_picture.get("Body").read().decode("ascii")
            else:
                item_picture = ""

            projects.append({
                "id": item_id,
                "title": item.get("title"),
                "mainPicture": item_picture,
                "author": item.get("user_id"),
                "briefDescription": item.get("brief_description"),
                "visible": item.get("visible"),
                "timestamp": int(item.get("timestamp"))
            })
        return Response(json.dumps({"projects": projects}),
                        status=200,
                        mimetype='application/json')
