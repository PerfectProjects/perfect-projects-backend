import json

from flask import Blueprint, request, Response
from backend.controllers.register_account_controller import RegisterAccountController

user_profile = Blueprint('user_profile', __name__)


@user_profile.route('/get-user', methods=["GET"])
def get_user_endpoint():
    #TODO
    projects = [
        {"projectId": 613211, "projectName": "Simple Game!"},
        {"projectId": 255411, "projectName": "Fancy Bathroom"},
        {"projectId": 544411, "projectName": "Sea Picture"}]
    user_name = "reoskaro"
    return Response(json.dumps({
        "projects": projects,
        "userName": user_name}),
                    status=200,
                    mimetype='application/json')
