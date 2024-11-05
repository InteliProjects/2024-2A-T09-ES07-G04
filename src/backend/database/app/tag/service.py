from ..regulation.models import Tag
from ..database import db
from sqlalchemy.exc import SQLAlchemyError

class TagService:
    @staticmethod
    def find_all():
        try:
            tags = Tag.query.order_by(Tag.name).all()
            return [tag.to_dict() for tag in tags]
        except SQLAlchemyError as e:
            print(f"Error querying the database: {str(e)}")
            return None

    @staticmethod
    def create(name):
        try:
            new_tag = Tag(name=name)
            db.session.add(new_tag)
            db.session.commit()
            return new_tag.to_dict()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error creating tag: {str(e)}")
            return None

    @staticmethod
    def update(tag_id, new_name):
        try:
            tag = Tag.query.get(tag_id)
            if tag:
                tag.name = new_name
                db.session.commit()
                return tag.to_dict()
            return None
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error updating tag: {str(e)}")
            return None

    @staticmethod
    def remove(tag_id):
        try:
            tag = Tag.query.get(tag_id)
            if tag:
                db.session.delete(tag)
                db.session.commit()
                return tag.to_dict()
            return None
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error deleting tag: {str(e)}")
            return None
