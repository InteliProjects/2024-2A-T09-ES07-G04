# Libraries
from flask import Flask
from flask_cors import CORS

# Setup
from .database import Database
from .config import Config

# Blueprints
from .regulator.controller import regulator_blueprint
from .regulation.controller import regulation_blueprint
from .filter.controller import filter_blueprint
from .tag.controller import tag_blueprint
from .transcription.controller import audio_blueprint 

def createApp():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    
    # Create and initialize database instance
    Database().init_app(app)

    # Register blueprints
    app.register_blueprint(regulator_blueprint, url_prefix='/regulators')
    app.register_blueprint(regulation_blueprint, url_prefix='/regulations')
    app.register_blueprint(filter_blueprint, url_prefix='/filters')
    app.register_blueprint(tag_blueprint, url_prefix='/tags')
    app.register_blueprint(audio_blueprint, url_prefix='/audio')

    return app