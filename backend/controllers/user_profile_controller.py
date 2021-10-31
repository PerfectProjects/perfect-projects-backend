import json

from flask import Response, g

from backend.aws.dynamodb.project_dynamodb_provider import ProjectDynamodbProvider


class UserProfileController:
    def __init__(self):
        self.dynamodb = ProjectDynamodbProvider("project")
        self.user_id = g.user.get("Username")

    def add_project(self, project):
        result = self.dynamodb.add_project(project, self.user_id)

        return Response(json.dumps({"success": result}),
                        status=200,
                        mimetype='application/json')

    def get_all_projects(self):
        result = self.dynamodb.get_all_user_projects(self.user_id)
        items = result.get("Items")
        projects = []
        for item in items:
            projects.append({
                "id": item.get("id"),
                "title": item.get("title"),
                "description": item.get("description")
            })
        return Response(json.dumps({"projects": projects}),
                        status=200,
                        mimetype='application/json')

    def delete_project(self, project_id):

        result = self.dynamodb.delete_project(project_id)

        if result:
            return Response(json.dumps({"success": result}),
                            status=200,
                            mimetype='application/json')

        return Response(json.dumps({"success": result}),
                        status=400,
                        mimetype='application/json')
