from flask import Flask
from flask_cors import CORS

from backend.rest.access_endpoint import access
from backend.rest.project_endpoint import project
from backend.rest.scores_endpoint import scores
from backend.rest.user_profile_endpoint import user_profile

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)

# Registered endpoints
app.register_blueprint(access)
app.register_blueprint(user_profile)
app.register_blueprint(project)
app.register_blueprint(scores)
