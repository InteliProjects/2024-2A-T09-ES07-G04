# Libraries
from flask import Flask
from flask_cors import CORS

# Blueprints
from .pln.controller import pln_blueprint

def createApp():
    app = Flask(__name__)

    CORS(app)
    
    # Register blueprints
    app.register_blueprint(pln_blueprint, url_prefix='/pln')

    return app