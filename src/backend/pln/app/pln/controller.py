from flask import Blueprint, request, jsonify
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from .services import preprocess_text, pln_query_pipeline, preprocess_tagguing, associated_pipeline
import os

pln_blueprint = Blueprint('pln', __name__)

current_dir = os.path.dirname(__file__) 
model_path = os.path.join(current_dir, 'modelo_pln.pkl')
vectorizer_path = os.path.join(current_dir, 'vectorizer.pkl')

with open(model_path, 'rb') as file:
    modelo = pickle.load(file)

with open(vectorizer_path, 'rb') as file:
    vectorizer = pickle.load(file)

@pln_blueprint.route('/', methods=['POST'])
def pln_model():
    data = request.get_json()
    texto = data.get('input')

    if not texto:
        return jsonify({'error': 'Nenhum texto fornecido'}), 400

    # Pré-processar o texto
    texto = preprocess_text(texto)

    # Vetorizar o texto usando o vectorizer treinado
    texto_vetorizado = vectorizer.transform([texto])

    # Fazer a previsão
    resultado = modelo.predict(texto_vetorizado)

    return jsonify({'resultado': resultado[0]})

@pln_blueprint.route('/query', methods=['POST'])
def regulation_pln():
    data = request.get_json()
    input = data.get('input')
    response, status_code = pln_query_pipeline(input)
    return jsonify(response), status_code

@pln_blueprint.route('', methods=['GET'])
def test_pln_route():
    return f"It's working"

#Tagguing Service
@pln_blueprint.route('/tag', methods=['POST'])
def tagguing_service():
    data = request.get_json()
    result = data.get('plainText')
    result = preprocess_tagguing(result)
    return result

#Tagguing Service
@pln_blueprint.route('/associated', methods=['POST'])
def associated_service():
    data = request.get_json()
    input = data.get('plainText')
    regulation, query = associated_pipeline(input)
    response = {
        'regulation': regulation,
        'query': query
    }
    return jsonify(response), 200

