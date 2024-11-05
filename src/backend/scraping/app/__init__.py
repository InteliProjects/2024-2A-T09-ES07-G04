# Libraries
from flask import Flask
from flask_cors import CORS

# Setup
from .config import Config

# Blueprints
from .scraping.controller import scraping_blueprint

def createApp():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    
    # Register blueprints
    app.register_blueprint(scraping_blueprint, url_prefix='/')

    return app