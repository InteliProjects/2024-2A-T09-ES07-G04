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

class ScrapingService:
    @staticmethod
    def scraping_bacen(base_url: str):
        # Inicialização
        yesterday = datetime.now() - timedelta(days=1)
        date = yesterday.strftime("%d/%m/%Y")

        search_url = base_url.format(dataInicioBusca=date, dataFimBusca=date)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        try:
            driver.get(search_url)
            driver.implicitly_wait(10)

            wait = WebDriverWait(driver, 20)
            found_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.encontrados")))
            norms = found_div.find_elements(By.XPATH, ".//ol/li")

            # Expressão regular para extrair o tipo e número do documento
            regex = r"(?P<documentType>[\w\s]+)\s*n°\s*(?P<documentNumber>[\d\.]+)"

            # Iterar sobre cada norma encontrada
            for norm in norms:
                try:
                    # Extrair o título e o link
                    link_element = WebDriverWait(norm, 10).until(
                        EC.presence_of_element_located((By.XPATH, ".//a"))
                    )
                    full_text = link_element.text
                    link_href = link_element.get_attribute("href")

                    norm_text_lines = norm.text.split('\n')
                    document_datetime, subject, responsible = None, None, None

                    for line in norm_text_lines:
                        if "Data/Hora Documento:" in line:
                            document_datetime = line.replace("Data/Hora Documento:", "").strip()
                        elif "Assunto:" in line:
                            subject = line.replace("Assunto:", "").strip()
                        elif "Responsável:" in line:
                            responsible = line.replace("Responsável:", "").strip()

                    # Aplicar regex para capturar o tipo e número do documento
                    match = re.search(regex, full_text)

                    if match:
                        document_type = match.group("documentType").strip()
                        document_number = match.group("documentNumber").strip()

                        # Extrair o texto da norma
                        xml_text, plain_text = ScrapingService.extract_norm_text(link_href)

                        # Criar o dicionário JSON
                        norm_json = {
                            "regulator": "BACEN",
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

                        print(norm_json)
                        return norm_json

                        # # Enviar a norma para RabbitMQ e verificar o sucesso
                        # success = ScrapingService.send_to_rabbitmq(norm_json)

                        # if success:
                        #     print(f"Norm sent successfully: {document_type} {document_number}")
                        # else:
                        #     print(f"Failed to send norm: {document_type} {document_number}")
                        #     break  # Parar o processo se o envio falhar

                        # driver.back()

                except Exception as e:
                    print(f"Error processing a norm: {e}")

        finally:
            # Fechar o driver no final
            driver.quit()

    @staticmethod
    def extract_norm_text(url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        try:
            driver.get(url)
            driver.implicitly_wait(10)

            # Encontrar todos os divs com classe começando com 'ExternalClass'
            content_divs = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class^='ExternalClass']"))
            )

            xml_content = ""
            plain_text = ""

            for div in content_divs:
                html = div.get_attribute('outerHTML')
                soup = BeautifulSoup(html, 'html.parser')

                p_tags = soup.find_all('p')
                for p in p_tags:
                    xml_content += str(p)
                    plain_text += p.get_text(separator='\n').strip() + "\n\n"

            if not xml_content and not plain_text:
                print("No <p> tags found in any ExternalClass div.")
                return None, None

            return xml_content.strip(), plain_text.strip()

        except Exception as e:
            print(f"Error extracting text from <p> tags: {e}")
            return None, None
        finally:
            # Fechar o driver após a extração
            driver.quit()

    @staticmethod
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