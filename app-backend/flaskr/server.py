# Standard imports
# Local imports
# Third party imports
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)


@app.route("/models/<model>")
def get_supported_models():
    pass


@app.route("/odqa/<model>")
def predict():
    pass
