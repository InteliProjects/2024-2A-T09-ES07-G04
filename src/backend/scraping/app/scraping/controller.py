from flask import Blueprint, jsonify, request
from .service import ScrapingService

scraping_blueprint = Blueprint('scraping', __name__)

@scraping_blueprint.route('bacen', methods=['POST'])
def scraping_bacen():
    data = request.get_json()
    try:
        scraping_data = ScrapingService.scraping_bacen(data['url'])
        return jsonify(scraping_data), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {e}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500