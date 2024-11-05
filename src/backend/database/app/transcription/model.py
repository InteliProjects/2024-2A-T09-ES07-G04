from ..database import db

class Transcription(db.Model):
    __tablename__ = 'transcription'

    id = db.Column(db.Integer, primary_key=True)
    audio_name = db.Column(db.String(255), nullable=False)
    transcription_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'audio_name': self.audio_name,
            'transcription_text': self.transcription_text,
            'created_at': self.created_at,
        }
