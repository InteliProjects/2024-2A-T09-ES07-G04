from ..regulation.models import Tag
from ..regulator.models import Regulator
from sqlalchemy.exc import SQLAlchemyError

class FilterService:
    @staticmethod
    def get_all_filters():
        try:
            tags = Tag.query.order_by(Tag.name).all()
            regulators = Regulator.query.order_by(Regulator.name).all()
            data = {
                "tags": [tag.to_dict() for tag in tags],
                "regulators": [regulator.to_dict() for regulator in regulators]
            }
            return data
        except SQLAlchemyError as e:
            print(f"Error: {str(e)}")
            return None
