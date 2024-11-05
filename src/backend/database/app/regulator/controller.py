from flask import Blueprint, jsonify
from .service import RegulatorService, OrganizationService

regulator_blueprint = Blueprint('regulators', __name__)

#Get all regulator
@regulator_blueprint.route('', methods=['GET']) 
def get_all_regulations():
    regulators = RegulatorService.get_all_regulations()
    return jsonify(regulators)

#get regulator by ID
@regulator_blueprint.route('/<int:id>', methods=['GET'])
def get_regulator_by_id(id):
    regulator = RegulatorService.get_regulation_by_id(id)
    if regulator:
        return jsonify(regulator)
    else:
        return jsonify({'error': 'Regulador não encontrado'}), 404

#Get all Organization
@regulator_blueprint.route('/organization', methods=['GET']) 
def get_all_organization():
    organization = OrganizationService.get_all_organization()
    return jsonify(organization)

#get Organization by ID
@regulator_blueprint.route('/organization/<int:id>', methods=['GET'])
def get_organization_by_id(id):
    organization = OrganizationService.get_organization_by_id(id)
    if organization:
        return jsonify(organization)
    else:
        return jsonify({'error': 'Organização não encontrada'}), 404
