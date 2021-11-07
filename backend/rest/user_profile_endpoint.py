import json

from flask import Blueprint, request

from backend.controllers.user_profile_controller import UserProfileController
from backend.decorators import require_authentication

user_profile = Blueprint('user_profile', __name__)


@user_profile.route('/user-profile', methods=["GET"])
@require_authentication
def user_profile_endpoint():
    return UserProfileController().get_all_projects()


@user_profile.route('/user-profile/add-project', methods=["POST"])
@require_authentication
def add_project_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    project = decoded_data.get("projectData")
    return UserProfileController().add_project(project)


@user_profile.route('/user-profile/delete-project', methods=["DELETE"])
@require_authentication
def delete_project_endpoint():
    decoded_data = request.data.decode()
    decoded_data = json.loads(decoded_data)
    project_id = decoded_data.get("projectId")
    return UserProfileController().delete_project(project_id)
