from .models import Regulator, Organization, db
from sqlalchemy import text

class RegulatorService:

    @staticmethod
    def get_all_regulations():
        regulations = Regulator.query.all()
        return [regulation.to_dict() for regulation in regulations]

    @staticmethod
    def get_regulation_by_id(id):
        regulation = Regulator.query.get(id)
        if regulation:
            return regulation.to_dict() 
        return None
    
class OrganizationService:
    
    @staticmethod
    def get_all_organization():
        organizations = Organization.query.all()
        return [organization.to_dict() for organization in organizations]

    @staticmethod
    def get_organization_by_id(id):
        organization = Organization.query.get(id)
        if organization:
            return organization.to_dict()  
        return None