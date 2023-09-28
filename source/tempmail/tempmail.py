import requests
import logging
from config import settings

# Configurações
BASE_URL = settings.API_URL_TEMPMAIL
HEADERS = {
    "X-RapidAPI-Key": settings.API_KEY_TEMPMAIL,
    "X-RapidAPI-Host": settings.API_HOST_TEMPMAIL
}

# Configuração de logs
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def api_request(endpoint, method="GET"):
    try:
        if method == "GET":
            response = requests.get(endpoint, headers=HEADERS)
        # Adicione outros métodos conforme necessário
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Erro ao acessar {endpoint}. Código de status: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Exceção ao acessar {endpoint}: {e}")
        return None

def gerar_email_temporario():
    endpoint = f"{BASE_URL}/request/domains/"
    domains = api_request(endpoint)
    if domains:
        email = f"{generate_random_string()}@{domains[0]}"
        return email
    return None

def verificar_emails_recebidos(email):
    endpoint = f"{BASE_URL}/request/mail/id/{email}/"
    return api_request(endpoint)

def ler_email(mail_id):
    endpoint = f"{BASE_URL}/request/mail/id/{mail_id}/"
    return api_request(endpoint)

def deletar_email(mail_id):
    endpoint = f"{BASE_URL}/request/delete/id/{mail_id}/"
    return api_request(endpoint)

def generate_random_string(length=10):
    import random
    import string
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
