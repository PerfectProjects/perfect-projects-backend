import json

from flask import Blueprint, Response, request

from backend.controllers.user_profile_controller import UserProfileController
from backend.decorators import require_authentication

user_profile = Blueprint('user_profile', __name__)


@user_profile.route('/user-profile', methods=["GET"])
@require_authentication
def user_profile_endpoint():
    return Response(json.dumps({
        "projects": {}}),
                    status=200,
                    mimetype='application/json')


@user_profile.route('/user-profile/add-project', methods=["POST"])
@require_authentication
def add_project_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    project = decoded_data.get("projectData")
    return UserProfileController().add_project(project)
