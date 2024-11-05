import spacy
import re
import pickle
import os
from datetime import datetime, timedelta
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import spacy
import json

# Baixar e carregar o modelo de linguagem para português (uma vez)
# spacy.cli.download("pt_core_news_sm")
nlp = spacy.load("pt_core_news_sm")

# Caminho absoluto para o modelo e o vectorizer
current_dir = os.path.dirname(__file__)  # Diretório atual do script
model_path = os.path.join(current_dir, 'modelo_pln.pkl')
vectorizer_path = os.path.join(current_dir, 'vectorizer.pkl')

# Carregar o modelo e o vectorizer
with open(model_path, 'rb') as file:
    modelo = pickle.load(file)

with open(vectorizer_path, 'rb') as file:
    vectorizer = pickle.load(file)

# Dicionário de palavras-chave por TAG (podem ser as mesmas ou outras relevantes)
tags_keywords = {
    'segurança': 'segurança proteção cibersegurança risco criptografia firewall',
    'auditoria interna': 'auditoria fiscalização controle interno verificação conformidade',
    'governança corporativa': 'governança conselho decisão corporativa transparência ética',
    'gestão de riscos': 'risco gestão mitigação avaliação de risco contingência prevenção',
    'regulamentação bancária': 'regulamentação bancária compliance lei supervisão financeira',
    'proteção de dados': 'dados privacidade proteção GDPR LGPD confidencialidade segurança digital',
    'fraude financeira': 'fraude esquema desvio financeiro manipulação auditoria investigação',
    'conformidade ambiental': 'compliance ambiental sustentabilidade regulamento verde ecofriendly',
    'responsabilidade social': 'responsabilidade social ética comunidade impacto positivo inclusão'
}

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def gemini_chat_tag(input):
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=GEMINI_API_KEY)

    tags = "Manual de crédito rural (MCR), Sistema de Pagamentos, Consórcio, Open Finance, Câmbio, Crédito Externo, Capital Estrangeiro, Certificação, Compensação, Composição Societária, Conglomerado Prudencial, Valores Mobiliários, Derivativos, FGC, Fundos de Investimento, Lavagem, Operações de Câmbio, Operações de Crédito, Pix, Sistema de Informações de Créditos, SELIC, Regulamento)"

    context = f"""
    Você é um especialista em relacionar em porcentagem textos com tags

    Nossa lista de TAGS: {tags}

    Exemplo de entrada do usuário:
    (algum texto falando sobre MCR, sistema de pagamentos e Open Finance)

    Seu output:
    MCR, Sistema de Pagamentos, Open Finance

    Siga essas regras a risca:
    - retorne apenas as TAGS relacionadas e nada mais.
    - separe por vírgula as TAGS
    - não finalize com "."
    """
    # Create the model
    generation_config = {
    "temperature": 0.8,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    gemini = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    system_instruction=context,
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    response = gemini.generate_content(f"""{input}""")
    print(response.text)
    return response.text

def gemini_chat(input):
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=GEMINI_API_KEY)

    lista_tipos = [
        "Manual de crédito rural (MCR)", "Sistema de Pagamentos", "Consórcio", "Open Finance", "Câmbio","Crédito Externo", "Capital Estrangeiro", "Certificação, Compensação", "Composição Societária", "Conglomerado Prudencial", "Valores Mobiliários", "Derivativos", "FGC", "Fundos de Investimento", "Lavagem", "Operações de Câmbio", "Operações de Crédito", "Pix", "Sistema de Informações de Créditos", "SELIC", "Regulamento","BACEM","DEMAB","Ato de Diretor", "Ato Normativo Conjunto", "Ato do Presidente", "Carta Circular", "Circular", "Comunicado", "Comunicado Conjunto", "Decisão Conjunta", "Instrução Normativa BCB", "Instrução Normativa Conjunta", "Portaria Conjunta", "Resolução BCB", "Resolução CMN", "Resolução Conjunta", "Resolução Coremec", "Regulação Financeira", "Fiscalização financeira", "Governança regulatoria", "Fiscalização Interna", "Circular", "Governança", "Financial Services"
    ]

    context = f"""
    Você é um especialista em identificar a inteção do usuário e corrigir texto.

    lista com as palavaras corretas que temos no nosso banco: {lista_tipos}

    Exemplo de Input do usuário:
    Eu quero o comunicadu número quarenta e dois mill

    Seu output:
    Eu quero o comunicado n° 42000

    Siga essas instruções a risca:
    - Retorne apenas a frase corrigida sem nenhuma informação adicional
    - Nuemro com ponto, retorne apenas o numero (42.031 -> 42031)
    - Não remova informações do usuário. Apenas corrija o português e analise se ele quer usar alguma das palavras do nosso banco de palavras

    """

    # Create the model
    generation_config = {
    "temperature": 0.8,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    gemini = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    system_instruction=context,
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    response = gemini.generate_content(f"""{input}""")
    print(response.text)
    return response.text

# Função para separar as sentenças
def extract_sentences(doc):
    sentences = [sent for sent in doc.sents]  # A função retorna spans (conjuntos de tokens)
    return sentences

# Função para separar em tokens (palavras)
def tokenize(sentences):
    tokens = []
    for sentence in sentences:
        # Retorna tokens diretamente como objetos spaCy
        sentence_tokens = [token for token in sentence]  # Mantém os objetos Token
        tokens.extend(sentence_tokens)
    return tokens

# Função para remover stop words
def extract_stop_words(tokens):
    # Verifica se é um objeto Token e não string
    doc = nlp(" ".join(tokens))
    words_filtered = [token.text for token in doc if not token.is_stop]
    return words_filtered

# Função para lematizar as palavras
def extract_lemmatizer(tokens):
    # Lematiza se for objeto Token
    lemmatized_words = [token.lemma_ for token in tokens]
    return lemmatized_words

# Função para remover pontuação
def rem_pontuacao(tokens):
    # Remove pontuação se for objeto Token
    words_no_punctuation = [token for token in tokens if token not in string.punctuation]
    return words_no_punctuation

# Função para POS tagging
def pos_tagging(tokens):
    # Recebe objetos Token e extrai tags POS e dependências
    pos_tags = [(token.text, token.pos_, token.dep_) for token in tokens]
    return pos_tags

# Função de pré-processamento do texto
def preprocess_text(text):
    doc = nlp(text.lower())
    
    # Extração de sentenças
    resultado = extract_sentences(doc)

    # Tokenização
    tokens = tokenize(resultado)

    # POS tagging
    pos_tags = pos_tagging(tokens)

    # Remover stop words
    # tokens = extract_stop_words(tokens)

    # Remover pontuação
    tokens = rem_pontuacao(tokens)

    # Lematização
    # tokens = extract_lemmatizer(tokens)
    # Transformar os tokens em strings antes de concatenar
    tokens = ' '.join([token.text for token in tokens])
    return tokens  # Concatenar os tokens para formar uma string processada

# Função para processar datas
def processar_data(expressao_data):
    if expressao_data is None:
        return None

    hoje = datetime.today()

    if expressao_data.lower() == "semana passada" or "semana passado":
        data_inicial = hoje - timedelta(days=hoje.weekday() + 7)
        data_final = data_inicial + timedelta(days=6)
        return f"{data_inicial.date()} até {data_final.date()}"

    elif expressao_data.lower() == "mês passado":
        primeiro_dia_mes = hoje.replace(day=1)
        ultimo_dia_mes_passado = primeiro_dia_mes - timedelta(days=1)
        primeiro_dia_mes_passado = ultimo_dia_mes_passado.replace(day=1)
        return f"{primeiro_dia_mes_passado.date()} até {ultimo_dia_mes_passado.date()}"

    elif expressao_data.lower() == "ano passado":
        ano_passado = hoje.year - 1
        return f"01/01/{ano_passado} até 31/12/{ano_passado}"

    elif expressao_data.lower() == "hoje":
        return hoje.strftime("%d/%m/%Y")

    elif expressao_data.lower() == "ontem":
        ontem = hoje - timedelta(days=1)
        return ontem.strftime("%d/%m/%Y")

    elif expressao_data.lower() == "próxima semana":
        inicio_semana_proxima = hoje + timedelta(days=(7 - hoje.weekday()))
        fim_semana_proxima = inicio_semana_proxima + timedelta(days=6)
        return f"{inicio_semana_proxima.date()} até {fim_semana_proxima.date()}"

    # Captura padrões como "julho de 2023" ou "dezembro de 2022"
    elif re.match(r"(janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro) de \d{4}", expressao_data.lower()):
        # Mapeia os meses para números
        meses = {
            "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4, "maio": 5, "junho": 6,
            "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12
        }
        partes = expressao_data.lower().split(" de ")
        mes = meses[partes[0]]
        ano = int(partes[1])
        primeiro_dia = datetime(ano, mes, 1)
        if mes == 12:
            ultimo_dia = datetime(ano, mes, 31)
        else:
            ultimo_dia = datetime(ano, mes + 1, 1) - timedelta(days=1)
        return f"{primeiro_dia.date()} até {ultimo_dia.date()}"

    elif re.match(r"\d{1,2}/\d{1,2}/\d{4}", expressao_data):
        return expressao_data  # Retorna a data no formato dd/mm/yyyy

    return expressao_data

# Função para enriquecer ainda mais a extração de entidades com regex
def extrair_entidades_regex(texto):
    entidades = {
        'regulator': 'BACEN',
        'type': None,
        'number':None,
        'topic':None,
        'date': None,
        'organization': None,
        'tag': None,
    }

    # Padrões regex ainda mais ricos
    padrao_regulator = r"\b(BACEM)\b"

    padrao_type = r"\b(Ato de Diretor|Ato Normativo Conjunto|Ato do Presidente|Carta Circular|Circular|Comunicado|Comunicado Conjunto|Decisão Conjunta|Instrução Normativa BCB|Instrução Normativa Conjunta|Portaria Conjunta|Resolução BCB|Resolução CMN|Resolução Conjunta|Resolução Coremec)\b"

    #ANALISAR LÓGICA PARA OS TÓPICOS
    padrao_topic = r"\b(Divulga a Taxa Básica Financeira)\b"

    padrao_organization = r"\b(DEMAB)\b"

    #Adicionar lógica para buscar normas revogadas

    padrao_tag = r"\b(Manual de crédito rural (MCR)|Sistema de Pagamentos|Consórcio|Open Finance|Câmbio|Crédito Externo|Capital Estrangeiro|Certificação|Compensação|Composição Societária|Conglomerado Prudencial|Valores Mobiliários|Derivativos|FGC|Fundos de Investimento|Lavagem|Operações de Câmbio|Operações de Crédito|Pix|Sistema de Informações de Créditos|SELIC|Regulamento)\b"

    padrao_date = r"\b(de hoje|ultimo dia|semana passada|semana passdo|mês passado|ano passado|hoje|ontem|próxima semana|dezembro de \d{4}|janeiro de \d{4}|fevereiro de \d{4}|março de \d{4}|abril de \d{4}|maio de \d{4}|junho de \d{4}|julho de \d{4}|agosto de \d{4}|setembro de \d{4}|outubro de \d{4}|novembro de \d{4}|\d{1,2}/\d{1,2}/\d{4})\b"

    padrao_number = r"\b\d+\b"

    regulator = re.search(padrao_regulator, texto, re.IGNORECASE)
    if regulator:
        entidades['regulator'] = regulator.group(0)

    type = re.search(padrao_type, texto, re.IGNORECASE)
    if type:
        entidades['type'] = type.group(0)  # Mantém o formato original do texto

    number = re.search(padrao_number, texto, re.IGNORECASE)
    if number:
        entidades['number'] = number.group(0)

    topic = re.search(padrao_topic, texto, re.IGNORECASE)
    if topic:
        entidades['topic'] = topic.group(0)

    date = re.search(padrao_date, texto, re.IGNORECASE)
    if date:
        entidades['date'] = processar_data(date.group(0))

    organization = re.search(padrao_organization, texto, re.IGNORECASE)
    if organization:
        entidades['organization'] = organization.group(0)

    tag = re.search(padrao_tag, texto, re.IGNORECASE)
    if tag:
        entidades['tag'] = tag.group(0)

    return entidades

def construir_query(dados):
    # Começa a construção da query
    query = f"""    
    SELECT
        regulation.*,
        regulator.name AS regulator_name,
        regulator.scrapingurl AS regulator_scrapingurl,
        organization.name AS organization_name,
        documenttype.name AS documenttype_name,
        COALESCE(ARRAY_AGG(tag.name) FILTER (WHERE tag.name IS NOT NULL), ARRAY[]::text[]) AS tags
    FROM
        regulation
    LEFT JOIN
        regulator ON regulation.regulatorid = regulator.id
    LEFT JOIN
        documenttype ON regulation.documenttypeid = documenttype.id
    LEFT JOIN
        organization ON regulation.organizationid = organization.id
    LEFT JOIN
        regulationtags ON regulation.id = regulationtags.regulationid
    LEFT JOIN
        tag ON tag.id = regulationtags.tagid

    WHERE
    
    """
    
    # Lista para armazenar condições
    condicoes = []
    
    # Verifica cada campo e adiciona a condição se não for None
    if dados['regulator'] is not None:
        condicoes.append(f" regulator.name ILIKE '{dados['regulator']}'")
    
    if dados['type'] is not None:
        condicoes.append(f" documenttype.name ILIKE '{dados['type']}'")

    if dados['number'] is not None:
        condicoes.append(f" regulation.documentnumber = '{dados['number']}'")

    # if dados['topic'] is not None:
    #     condicoes.append(f" topic ILIKE = '{dados['topic']}'")

    # if dados['date'] is not None:
    #     condicoes.append(f" publicationdate ILIKE '{dados['date']}'")

    if dados['organization'] is not None:
        condicoes.append(f" organization.name ILIKE '{dados['organization']}'")
    
    if dados['tag'] is not None:
        condicoes.append(f" tag.name ILIKE '{dados['tag']}'")

    if condicoes:
        query += " AND".join(condicoes)
    else:
        query = query.replace(" WHERE", "")  # Remove o WHERE se não houver condições

        # Adiciona o GROUP BY para garantir que as colunas não agregadas sejam agrupadas
    query += """
    GROUP BY
        regulation.id,
        regulator.name,
        regulator.scrapingurl,
        organization.name,
        documenttype.name;
    """
    
    return query

# Função para identificar entidades
def entidades(nova_frase_processada):
    entidades = extrair_entidades_regex(nova_frase_processada)  # Extrai as entidades usando regex
    return entidades

def pln_query(input):
    nova_frase_vec = vectorizer.transform([input])
    predicao_nova_frase = modelo.predict(nova_frase_vec)
    if predicao_nova_frase == 'consulta_normativa':
        ent = entidades(input)
        return ent, 200
    else:
        return 'Perdão, não posso responder a esse tipo de pergunta.', 400

def pln_query_pipeline(input):
    input = gemini_chat(input)
    result, status_code = pln_query(input)
    if status_code == 400:
        return result, status_code
    
    result = construir_query(result)

    #Request for Regulations Service Query
    result = requests.post('http://localhost:5002/regulations/query', json={'input': result})
    result.raise_for_status() 
    result = result.json()

    # result = RegulationService.execute_sql_query(result)
    result = {
        "regulations": result,
        "quantity": len(result)
    }

    return result, status_code

def tag_process(document):  
    print("2")
     # Vetorização usando TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    # Combinar o documento e as TAGs em uma lista
    corpus = [document] + list(tags_keywords.values())
    # Ajustar o TF-IDF no corpus
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    # Cálculo da similaridade do cosseno entre o documento e as TAGs
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    # Associar os valores de similaridade com as TAGs
    tags_similarities = {tag: similarity for tag, similarity in zip(tags_keywords.keys(), cosine_similarities)}
    # Ordenar as TAGs por similaridade (da maior para a menor)
    sorted_tags = sorted(tags_similarities.items(), key=lambda x: x[1], reverse=True)
    # Exibir os resultados
    for tag, similarity in sorted_tags:
        print(f"{tag}: {similarity:.2f}")

    sorted_tags = dict(sorted_tags)
    tags = list(sorted_tags.keys())

    return tags

# Text preprocessing function
def preprocess_tagguing(input):
    # # Convert the text to lowercase and create a spaCy doc object
    # doc = nlp(text.lower())
    # # Sentence extraction
    # sentences = extract_sentences(doc)
    # tokens = tokenize(sentences)
    # lem = extract_lemmatizer(tokens)
    # rem = rem_pontuacao(lem)
    # resultado = extract_stop_words(rem)
    # print("1")
    # resultado = " ".join(resultado) 
    # resultado = tag_process(resultado)
    resultado = gemini_chat(input)
    print("resultado antes: ", resultado)
    resultado = [item.strip() for item in resultado.split(',')] 
    print(resultado)
    return resultado

# NORMAS ASSOCIADAS ##
def associate_gemini_chat(input):
    associate_types = [
        "Ato de Diretor", "Ato Normativo Conjunto", "Ato do Presidente", 
        "Carta Circular", "Circular", "Comunicado", "Comunicado Conjunto", 
        "Decisão Conjunta", "Instrução Normativa BCB", "Instrução Normativa Conjunta", 
        "Portaria Conjunta", "Resolução BCB", "Resolução CMN", "Resolução Conjunta", 
        "Resolução Coremec"
        
    ]

    associate_context = f"""
        Você é um especialista em identificar normas e regulamentos citados nos textos.

        lista com as palavras-chaves de tipos de regulamentos da BACEN: {associate_types}

        Exemplo de texto da regulamentação:
        A Diretoria Colegiada do Banco Central do Brasil, no uso de suas atribuições, com fundamento no art. 143 do Regimento Interno, anexo à Resolução BCB nº 340, de 21 de setembro de 2023, e no art. 10, caput, inciso XIV, da Lei nº 4.595, de 31 de dezembro de 1964, e tendo em vista o disposto no Voto 170/2024–BCB, de 2 de outubro de 2024,

        Seu output:
        [
            {{
                "documenttype": "Resolução BCB",
                "documentnumber": 340,
                "publicationdate": "2023-09-21"
            }}
        ]

        Siga essas instruções a risca:
        - Retorne regulamentos SE E SOMENTE SE o tipo estiver na lista de tipos de regulamentos da BACEN
        - Retorne apenas a lista de normas e regulamentos citados no texto
        - Numero com ponto, retorne apenas o numero (42.031 -> 42031)

    """

    GEMINI_API_KEY_ASSOCIATED = os.getenv('GEMINI_API_KEY_ASSOCIATED')
    genai.configure(api_key=GEMINI_API_KEY_ASSOCIATED)

    # Create the model
    associate_generation_config = {
    "temperature": 0.8,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    associate_gemini = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    system_instruction=associate_context,
    generation_config=associate_generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    associate_chat_session = associate_gemini.start_chat(
    history=[
    ]
    )
    response = associate_gemini.generate_content(f"""Regulação: {input}""")
    print(response.text)
    
    # Tente converter a resposta de texto em um objeto Python (dicionário ou lista)
    try:
        # Remove caracteres indesejados como '```json' e '```' se necessário
        clean_response = response.text.strip('```json\n').strip('```').strip()
        return json.loads(clean_response)  # Converte a string JSON em um dicionário ou lista
    except json.JSONDecodeError:
        print("Erro ao decodificar a resposta JSON.")
        return None  # Retorna None se a conversão falhar

def associated_pipeline(input):
    regulation = associate_gemini_chat(input)
    # Começa a construção da query
    query = f"""    
    SELECT
        regulation.id,
        documenttype.name,
        regulation.documentnumber
    FROM
        regulation
        JOIN documenttype on documenttype.id = regulation.documenttypeid
    WHERE
    """
    
    # Lista para armazenar condições de cada regulamento
    condicoes = []
    
    # Loop sobre cada item da lista de dados
    for dados in regulation:
        # Verifica se os campos não são None e monta a condição para cada regulamento
        condicao = []
        
        if 'documenttype' in dados and dados['documenttype'] is not None:
            condicao.append(f"documenttype.name ILIKE '{dados['documenttype']}'")
        
        if 'documentnumber' in dados and dados['documentnumber'] is not None:
            condicao.append(f"regulation.documentnumber = {dados['documentnumber']}")
        
        if 'publicationdate' in dados and dados['publicationdate'] is not None:
            condicao.append(f"regulation.publicationdate::date = '{dados['publicationdate']}'")

        if condicao:
            condicoes.append(f"({' AND '.join(condicao)})")
    
    if condicoes:
        query += " OR ".join(condicoes)
    else:
        query = None

    return regulation, query