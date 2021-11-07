import io
import json

from flask import Response, g

from backend.aws.dynamodb.project_dynamodb_provider import ProjectDynamodbProvider
from backend.aws.s3.s3_provider import S3Provider


class ProjectController:
    def __init__(self):
        self.dynamodb = ProjectDynamodbProvider()
        self.s3 = S3Provider()
        self.user_id = g.user.get("Username")

    def get_project(self, project_id):
        result = self.dynamodb.get_project(project_id)
        if result:
            item_description = self.s3.get_file(project_id).get("Body").read().decode("ascii")
            item = result.get("Item")
            project = {
                "id": item.get("id"),
                "title": item.get("title"),
                "description": item_description,
                "author": item.get("user_id")
            }
            return Response(json.dumps(project),
                            status=200,
                            mimetype='application/json')
        return Response(status=404, mimetype='application/json')

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