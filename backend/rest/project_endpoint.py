import json

from flask import Blueprint, request

from backend.controllers.project_controller import ProjectController
from backend.decorators import require_authentication

project = Blueprint("project", __name__)


@project.route("/project", methods=["GET"])
@require_authentication
def project_endpoint():
    project_id = request.args.get("id")
    return ProjectController().get_project(project_id)


@project.route('/project', methods=["POST"])
@require_authentication
def add_project_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    project = decoded_data.get("projectData")
    return ProjectController().add_project(project)


@project.route('/project', methods=["DELETE"])
@require_authentication
def delete_project_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    project_id = decoded_data.get("projectId")
    return ProjectController().delete_project(project_id)
