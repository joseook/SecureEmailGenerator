# utils.py

import logging
import re
import csv
from cryptography.fernet import Fernet

logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def validar_formato_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.match(regex, email)

def salvar_csv(filename, data):
    try:
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except Exception as e:
        log_error(f"Erro ao salvar CSV: {e}")

def ler_csv(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    except Exception as e:
        log_error(f"Erro ao ler CSV: {e}")
        return []

def criptografar_dados(dados, chave):
    f = Fernet(chave)
    return f.encrypt(dados.encode()).decode()

def descriptografar_dados(dados_criptografados, chave):
    f = Fernet(chave)
    return f.decrypt(dados_criptografados.encode()).decode()

