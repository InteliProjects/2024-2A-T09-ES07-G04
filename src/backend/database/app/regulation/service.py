from .models import Regulation, Tag, RegulationTags, DocumentType, RegulationBacklink, db
from ..regulator.models import Organization
from sqlalchemy import text
import requests
import html
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError


def format_text(regulation):
    text = html.unescape(regulation)
    date = datetime.strptime(regulation["publicationDate"], "%d/%m/%Y %H:%M")
    regulation["publicationDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
    regulation["documentNumber"] = text["documentNumber"].replace('.', '')
    regulation["xmlText"] = text["xmlText"].replace('\xa0', '&nbsp;').replace('\n', '<br>')
    regulation["plainText"] = text["plainText"].replace('\xa0', '').replace('\n', '')
    return regulation

class DatabaseException(Exception):
    def __init__(self, message="Database transaction failed"):
        self.message = message
        super().__init__(self.message)
        
class RegulationService:
    @staticmethod
    def get_regulation_by_id(id):
        regulation = Regulation.query.get(id)
        if regulation:
            return regulation.to_dict() 
        return None

    @staticmethod
    def get_all_regulations():
        regulations = Regulation.query.all()
        return [regulation.to_dict() for regulation in regulations]
    
    @staticmethod
    def create_regulation(data):
        try:
            if not data['xmlText']:
                data['xmlText'] = 'Regulamentação indisponível. Acesse o link da plataforma oficial.'

            if not data['plainText']:
                data['plainText'] = 'Regulamentação indisponíve. Acesse o link da plataforma oficial.'

            data = format_text(data)

            document_name = data["documentType"]
            query = f"""
            SELECT
                documenttype.id
            FROM
                documenttype
            WHERE
                documenttype.name ILIKE '{document_name}'
            """

            documenttypeid = RegulationService.execute_sql_query(query)
            documenttypeid = documenttypeid[0]['id']

            organization = data["organization"]

            query = f"""
            SELECT
                organization.id
            FROM
                organization
            WHERE
                organization.name ILIKE '{organization}'
            """

            organizationid = RegulationService.execute_sql_query(query)
            
            if not organizationid:
                new_organization = Organization(
                    name=organization
                )
                db.session.add(organization)
                db.session.commit()
                organizationid = new_organization.id
            else:
                organizationid = organizationid[0]['id']

            new_regulation = Regulation(
                regulatorid=1,
                documenttypeid=documenttypeid,
                documentnumber=data['documentNumber'],
                publicationdate=data['publicationDate'],
                topic=data['topic'],
                organizationid=organizationid,
                status=True,
                documenturl=data['documentURL'],
                xmltext=data['xmlText'],  
                plaintext=data['plainText'],

            )
            db.session.add(new_regulation)
            db.session.flush()
            regulation_id = new_regulation.id

            # Tagguing Service
            plainText = data['plainText']
            tagguing_response = requests.post('http://localhost:5000/pln/tag', json={'plainText': plainText})
            tagguing_response = tagguing_response.json()            


            tags = Tag.query.all()
            tags = [tag.to_dict() for tag in tags]

            ids = []
            for tag_name in tagguing_response:
                for tag in tags:
                    if tag_name == tag['name']:
                        ids.append(tag['id'])

            for tagid in ids:
                regulationtags = RegulationTags(
                    regulationid=regulation_id,
                    tagid=tagid
                )
                db.session.add(regulationtags)

            plaintext = data['plainText']
            response_associated = requests.post('http://localhost:5000/pln/associated', json={'plainText': plaintext})

            if response_associated.status_code == 200:
                data = response_associated.json()
                regulation = data.get('regulation')
                query = data.get('query')
                print(regulation, query)
            else:
                print(f"Erro na requisição: {response_associated.status_code}")

            norms_in_database = RegulationService.execute_sql_query(query)

            for norm in regulation:
                matching_norm = next(
                    (db_norm for db_norm in norms_in_database if db_norm['documentnumber'] == norm['documentnumber'] and db_norm['name'] == norm['documenttype']),
                    None
                )

                if matching_norm is not None:
                    print("diferente de none, id: ", matching_norm['id'])
                    new_regulationBackLink = RegulationBacklink(
                        sourceregulationid=regulation_id,
                        targetregulationid=matching_norm['id'],  
                    )
                    print(f"Norma encontrada no banco: {norm['documentnumber']}, criando backlink com target_regulation = {matching_norm['id']}")
                    
                else:
                    base_url = "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo={}&numero={}"
                    url_document_type = norm['documenttype'].replace(" ", "%20")
                    url_document_number = norm['documentnumber']
                    url = base_url.format(url_document_type, url_document_number)
                    new_regulationBackLink = RegulationBacklink(
                        sourceregulationid=regulation_id,
                        documenturl=url,
                        documentname=f"{norm['documenttype']} nº {norm['documentnumber']}"
                    )
                    print(f"Norma não encontrada no banco: {norm['documentnumber']}, criando backlink com documenturl = {url}")

                db.session.add(new_regulationBackLink)

            db.session.commit()

            return new_regulation.to_dict()

        except (SQLAlchemyError, requests.exceptions.RequestException) as e:
            db.session.rollback()
            raise DatabaseException(f"An error occurred while saving regulation: {str(e)}")

    @staticmethod
    def execute_sql_query(sql_code):
        try:
            with db.engine.connect() as connection:
                result = connection.execute(text(sql_code))
                columns = result.keys()
                return [dict(zip(columns, row)) for row in result.fetchall()]
        except Exception as e:
            return {"error": str(e)}
        