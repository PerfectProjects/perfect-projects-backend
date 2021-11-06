import io
import json

from flask import Response, g

from backend.aws.dynamodb.project_dynamodb_provider import ProjectDynamodbProvider
from backend.aws.s3.s3_provider import S3Provider


class UserProfileController:
    def __init__(self):
        self.dynamodb = ProjectDynamodbProvider()
        self.s3 = S3Provider()
        self.user_id = g.user.get("Username")

    def add_project(self, project):
        project_id = self.dynamodb.add_project(project, self.user_id)
        if project_id:
            description = project.get("description")
            binary_file = io.BytesIO(description.encode("ascii"))
            response = self.s3.upload_object_file(binary_file, project_id)
            return Response(json.dumps({"success": response}),
                            status=200,
                            mimetype='application/json')
        return Response(json.dumps({"success": False}),
                        status=200,
                        mimetype='application/json')

    def get_all_projects(self):
        result = self.dynamodb.get_all_user_projects(self.user_id)
        items = result.get("Items")
        projects = []
        for item in items:
            item_id = item.get("id")
            binary_item_description = self.s3.get_file(item_id).get("Body").read()
            projects.append({
                "id": item_id,
                "title": item.get("title"),
                "description": binary_item_description.decode("utf-8")})
        return Response(json.dumps({"projects": projects}),
                        status=200,
                        mimetype='application/json')

    def delete_project(self, project_id):
        dynamodb_result = self.dynamodb.delete_project(project_id)
        s3_result = self.s3.delete_file(project_id)

        if dynamodb_result and s3_result:
            return Response(json.dumps({"success": True}),
                            status=200,
                            mimetype='application/json')

        return Response(json.dumps({"success": False}),
                        status=400,
                        mimetype='application/json')
