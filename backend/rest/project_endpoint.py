from flask import Blueprint, request

from backend.controllers.project_controller import ProjectController
from backend.controllers.sign_in_controller import SignInController
from backend.decorators import require_authentication

project = Blueprint("project", __name__)


@project.route("/project", methods=["GET"])
@require_authentication
def project_endpoint():
    project_id = request.args.get("id")
    return ProjectController().get_project(project_id)

