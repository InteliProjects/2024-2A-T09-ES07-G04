from ..database import db

class Regulator(db.Model):
    __tablename__ = 'regulator'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    scrapingurl = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'scrapingurl': self.scrapingurl,
        }

class Organization(db.Model):
    __tablename__ = 'organization'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    