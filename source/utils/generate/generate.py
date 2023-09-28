# gerador.py

import random
import string

def gerar_string_aleatoria(tamanho=10, caracteres=None):
    """
    Gera uma string aleatória.
    
    Args:
    - tamanho (int): O tamanho da string a ser gerada.
    - caracteres (str, optional): Conjunto de caracteres a serem usados para gerar a string.

    Returns:
    - str: A string aleatória gerada.
    """
    if caracteres is None:
        caracteres = string.ascii_lowercase + string.digits
    return ''.join(random.choice(caracteres) for i in range(tamanho))

def gerar_nome_usuario(tamanho=8):
    """
    Gera um nome de usuário aleatório.
    
    Args:
    - tamanho (int): O tamanho do nome de usuário a ser gerado.

    Returns:
    - str: O nome de usuário aleatório gerado.
    """
    return gerar_string_aleatoria(tamanho)

def gerar_email(dominio="joseok.tech", tamanho=10):
    """
    Gera um e-mail aleatório.
    
    Args:
    - dominio (str): O domínio do e-mail.
    - tamanho (int): O tamanho do nome do e-mail a ser gerado.

    Returns:
    - str: O e-mail aleatório gerado.
    """
    nome_email = gerar_string_aleatoria(tamanho)
    return f"{nome_email}@{dominio}"

def gerar_senha(tamanho=12, caracteres_especiais=True, digitos=True, maiusculas=True):
    """
    Gera uma senha aleatória.
    
    Args:
    - tamanho (int): O tamanho da senha a ser gerada.
    - caracteres_especiais (bool): Se deve incluir caracteres especiais na senha.
    - digitos (bool): Se deve incluir dígitos na senha.
    - maiusculas (bool): Se deve incluir letras maiúsculas na senha.

    Returns:
    - str: A senha aleatória gerada.
    """
    caracteres = string.ascii_lowercase
    if maiusculas:
        caracteres += string.ascii_uppercase
    if digitos:
        caracteres += string.digits
    if caracteres_especiais:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    while (
        len(senha) < tamanho or
        not any(c.isupper() for c in senha) or
        not any(c.isdigit() for c in senha) or
        not any(c in string.punctuation for c in senha)
    ):
        senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    return senha
