# verificador.py

import requests
from config import settings
from utils import log_info, log_error

def verificar_email_truemail(email):
    params = {
        "email": email,
        "apiKey": settings.API_KEY_TRUEMAIL
    }
    try:
        response = requests.get(settings.API_URL_TRUEMAIL, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'result' in data:
            if data['result'] == "valid":
                log_info(f"Email {email} verificado com sucesso.")
                return {"status": True, "message": "Email válido"}
            else:
                log_info(f"Email {email} é inválido. Razão: {data.get('reason', 'Desconhecido')}")
                return {"status": False, "message": data.get("reason", "Desconhecido")}
        else:
            log_error(f"Resposta inesperada da API para o e-mail {email}.")
            return {"status": False, "message": "Resposta inesperada da API"}
    except requests.RequestException as e:
        log_error(f"Erro ao verificar o e-mail {email}: {e}")
        return {"status": False, "message": str(e)}

def is_disposable_domain(email):
    # Aqui, você pode adicionar uma lista de domínios descartáveis ou usar uma API para verificar.
    disposable_domains = ["tempmail.com", "mailinator.com"]
    domain = email.split('@')[-1]
    return domain in disposable_domains

def extract_domain_from_email(email):
    return email.split('@')[-1]

def verify_domain(domain):
    # Aqui, você pode adicionar lógica para verificar se um domínio é válido ou não.
    # Por exemplo, usando uma API ou uma lista predefinida.
    valid_domains = ["joseok.tech", "gmail.com", "yahoo.com"]
    return domain in valid_domains
