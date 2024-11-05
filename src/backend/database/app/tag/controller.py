from flask import Blueprint, jsonify, request
from .service import TagService

tag_blueprint = Blueprint('tags', __name__)

@tag_blueprint.route('', methods=['GET'])
def find_all():
    tags = TagService.find_all()
    return jsonify(tags)

@tag_blueprint.route('', methods=['POST'])
def create():
    data = request.json
    name = data.get('name')
    if name:
        tag = TagService.create(name)
        if tag:
            return jsonify(tag), 201
        return jsonify({"error": "Tag creation failed."}), 400
    return jsonify({"error": "Name is required."}), 400

@tag_blueprint.route('/<int:tag_id>', methods=['PUT'])
def update(tag_id):
    data = request.json
    new_name = data.get('name')
    if new_name:
        tag = TagService.update(tag_id, new_name)
        if tag:
            return jsonify(tag), 200
        return jsonify({"error": "Tag not found."}), 404
    return jsonify({"error": "Name is required."}), 400

@tag_blueprint.route('/<int:tag_id>', methods=['DELETE'])
def remove(tag_id):
    tag = TagService.remove(tag_id)
    if tag:
        return jsonify(tag), 200
    return jsonify({"error": "Tag not found."}), 404
