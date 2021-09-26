from flask import Flask
from flask_cors import CORS

from backend.rest.sign_in_endpoint import sign_in
from backend.rest.sign_up_endpoint import sign_up

app = Flask(__name__)
CORS(app)

# Registered endpoints
app.register_blueprint(sign_up)
app.register_blueprint(sign_in)
