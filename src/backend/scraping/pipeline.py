from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import datetime, timedelta
import re
import json
from bs4 import BeautifulSoup
import pika

# Supabase connection URI
SUPABASE_DB_URI = os.getenv("DATABASE_URL")

# SQLAlchemy setup
engine = create_engine(SUPABASE_DB_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Regulator(Base):
    __tablename__ = 'regulator'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    scrapingurl = Column(Text, nullable=False)

def get_scraping_url(regulator):
    try:
        url = session.query(Regulator).filter_by(name=regulator).first()
        if url:
            return url.scrapingurl
        else:
            print(f"Regulator '{regulator}' not found in the database.")
            return None
    except Exception as e:
        print(f"Error retrieving configuration: {e}")
        return None

# Function to initialize the driver
def init_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Function to extract norm text from the URL
def extract_norm_text(url, driver):
    driver.get(url)
    driver.implicitly_wait(100)

    try:
        content_divs = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class^='ExternalClass']"))
        )
        xml_content = ""
        plain_text = ""

        for div in content_divs:
            html = div.get_attribute('outerHTML')
            soup = BeautifulSoup(html, 'html.parser')
            p_tags = soup.find_all('p')
            if p_tags:
                for p in p_tags:
                    xml_content += str(p)
                    plain_text += p.get_text(separator='\n').strip() + "\n\n"

        return xml_content.strip(), plain_text.strip()
    except Exception as e:
        print(f"Error extracting text from <p> tags: {e}")
        return None, None

# Function to send data to RabbitMQ
def send_to_rabbitmq(data):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='scraping_queue', durable=False)
        message = json.dumps(data)
        channel.basic_publish(exchange='',
                              routing_key='scraping_queue',
                              body=message,
                              properties=pika.BasicProperties(
                                  delivery_mode=2,
                              ))
        print(f"[x] Scraping data sent to RabbitMQ: {message}")
        connection.close()
        return True
    except Exception as e:
        print(f"Error sending message to RabbitMQ: {str(e)}")
        return False

# Function to scrape norms
def scrape_norms(driver, search_url):
    driver.get(search_url)
    driver.implicitly_wait(100)

    try:
        wait = WebDriverWait(driver, 20)
        found_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.encontrados")))
        norms = found_div.find_elements(By.XPATH, ".//ol/li")
    except Exception as e:
        print(f"Error fetching norms: {e}")
        norms = []
    
    return norms

# Function to parse each norm's details
def parse_norm_details(norm, regex, driver):
    try:
        link_element = WebDriverWait(norm, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//a"))
        )
        full_text = link_element.text
        link_href = link_element.get_attribute("href")
        
        norm_text_lines = norm.text.split('\n')
        document_datetime = None
        subject = None
        responsible = None

        for line in norm_text_lines:
            if "Data/Hora Documento:" in line:
                document_datetime = line.replace("Data/Hora Documento:", "").strip()
            elif "Assunto:" in line:
                subject = line.replace("Assunto:", "").strip()
            elif "Responsável:" in line:
                responsible = line.replace("Responsável:", "").strip()
        
        match = re.search(regex, full_text)
        
        if match:
            document_type = match.group("documentType").strip()
            document_number = match.group("documentNumber").strip()

            xml_text, plain_text = extract_norm_text(link_href, driver)
            
            norm_json = {
                "documentType": document_type,
                "documentNumber": document_number,
                "publicationDate": document_datetime,
                "topic": subject,
                "status": True,
                "organization": responsible,
                "documentURL": link_href,
                "xmlText": xml_text,
                "plainText": plain_text
            }

            return norm_json
    except Exception as e:
        print(f"Error parsing norm details: {e}")
        return None

# Pipeline function to manage the full process
def pipeline():
    regulator = 'BACEN'
    # Get the base URL from the database
    base_url = get_scraping_url(regulator)
    if not base_url:
        return
    
    today = datetime.now()

    if today.weekday() == 0:
        # If it's Monday, set the date to the previous Friday
        target_date = today - timedelta(days=3)
    else:
        # Otherwise, use yesterday's date
        target_date = today - timedelta(days=1)

    date = target_date.strftime("%d/%m/%Y")
    search_url = base_url.format(dataInicioBusca=date, dataFimBusca=date)

    # Initialize the driver
    driver = init_driver()

    # Scrape norms
    norms = scrape_norms(driver, search_url)

    # Regex for document type and number
    regex = r"(?P<documentType>[\w\s]+)\s*n°\s*(?P<documentNumber>[\d\.]+)"

    # Iterate over each norm and send to RabbitMQ
    for norm in norms:
        norm_data = parse_norm_details(norm, regex, driver)
        if norm_data:
            success = send_to_rabbitmq(norm_data)
            driver.back()
            if not success:
                break  # Stop the pipeline if there's an error sending to RabbitMQ

    # Step 6: Close the driver
    driver.quit()

if __name__ == "__main__":
    pipeline()