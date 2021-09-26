from flask import Flask
from flask_cors import CORS

from backend.rest.sign_up_endpoint import sign_up

app = Flask(__name__)
CORS(app)
app.register_blueprint(sign_up)
