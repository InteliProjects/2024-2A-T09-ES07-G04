from flask import Blueprint, jsonify, request
from .service import RegulationService
import requests
import pika
import json
from threading import Thread

regulation_blueprint = Blueprint('regulations', __name__)

@regulation_blueprint.route('', methods=['GET'])
def get_all_regulations():
    regulations = RegulationService.get_all_regulations()
    return jsonify(regulations)

@regulation_blueprint.route('/<int:id>', methods=['GET'])
def get_regulation_by_id(id):
    regulation = RegulationService.get_regulation_by_id(id)
    if regulation:
        return jsonify(regulation)
    else:
        return jsonify({'error': 'Regulamento não encontrado'}), 400


@regulation_blueprint.route('', methods=['POST'])
def create_regulation():
    data = request.get_json()  
    try:
        new_regulation = RegulationService.create_regulation(data)
        return jsonify(new_regulation), 201 
    except KeyError as e:
        return jsonify({'error': f'Missing field: {e}'}), 400 
    except Exception as e:
        return jsonify({'error': str(e)}), 500 
    
# Execute SQL Query
@regulation_blueprint.route('/query', methods=['POST'])
def execute_sql_query():
    data = request.get_json()
    if 'input' in data:
        query_text = data['input']
        result = RegulationService.execute_sql_query(query_text)
        return jsonify(result)
    else:
        return jsonify({'error': 'Faltando o campo text no corpo da requisição'}), 400


def start_rabbitmq_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declaração da fila
    channel.queue_declare(queue='scraping_queue', durable=False)

    def callback(ch, method, properties, body):
        regulation_url = 'http://localhost:5002/regulations'
        print(f"Response: {body}")

        try:
            body_str = body.decode('utf-8')
            body_json = json.loads(body_str)
            webhook_response = requests.post(regulation_url, json=body_json)
            webhook_response.raise_for_status()

            print("Webhook processado com sucesso")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        except requests.exceptions.RequestException as e:
            print(f"Falha no webhook, erro: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Erro ao processar mensagem: {str(e)}")
            ch.basic_nack(delivery_tag=method.delivery_tag)

    # Consumidor de mensagens do RabbitMQ
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='scraping_queue', on_message_callback=callback)


    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

# Rodar o consumidor RabbitMQ em uma thread separada
rabbitmq_thread = Thread(target=start_rabbitmq_consumer)
rabbitmq_thread.start()
