from flask import Blueprint

from backend.controllers.user_profile_controller import UserProfileController
from backend.decorators import require_authentication

user_profile = Blueprint('user_profile', __name__)


@user_profile.route('/user-profile', methods=["GET"])
@require_authentication
def user_profile_endpoint():
    return UserProfileController().get_all_projects()

