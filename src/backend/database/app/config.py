# Libraries
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'chave_aqui'
