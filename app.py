from flask import Flask

from backend.rest.sign_up_endpoint import sign_up

app = Flask(__name__)
app.register_blueprint(sign_up)
