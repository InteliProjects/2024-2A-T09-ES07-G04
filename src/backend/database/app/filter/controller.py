from flask import Blueprint, jsonify, request
from .service import FilterService
import requests
import json
from threading import Thread

filter_blueprint = Blueprint('filters', __name__)

@filter_blueprint.route('', methods=['GET'])
def get_all_filters():
    filters = FilterService.get_all_filters()
    return jsonify(filters)
