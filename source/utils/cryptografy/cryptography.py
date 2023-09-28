from cryptography.fernet import Fernet

def gerar_chave_criptografia():
    return Fernet.generate_key()

def criptografar(dados, chave):
    f = Fernet(chave)
    return f.encrypt(dados.encode()).decode()

def descriptografar(dados_criptografados, chave):
    f = Fernet(chave)
    return f.decrypt(dados_criptografados.encode()).decode()

def gerar_hash_senha(senha, salt="SALT_FOR_HASH"):
    import hashlib
    return hashlib.sha256((senha + salt).encode()).hexdigest()
