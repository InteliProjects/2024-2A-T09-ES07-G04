from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Database:
    @staticmethod
    def init_app(app):
        db.init_app(app)