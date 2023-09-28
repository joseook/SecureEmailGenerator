# main.py

from source.utils.generate import generate, verify
from utils import criptografar_dados, descriptografar_dados
from styles import main_window


def gerar_e_verificar_emails(quantidade=10, usar_tempmail=False, criptografar=False):
    emails_verificados = []

    for _ in range(quantidade):
        if usar_tempmail:
            email = verify.gerar_email_temporario()
            senha = "N/A"  # E-mails temporários não têm senha associada
            resultado = True  # E-mails temporários são sempre válidos
        else:
            email = generate.gerar_email()
            senha = generate.gerar_senha()
            resultado = verify.verificar_email_truemail(email)

        if criptografar:
            email = criptografar_dados(email)
            senha = criptografar_dados(senha)

        emails_verificados.append((email, senha, resultado))

    return emails_verificados

def main():
    print("Bem-vindo ao Gerador e Verificador de E-mails!")
    print("Opções:")
    print("1. Iniciar a interface gráfica (GUI)")
    print("2. Gerar e verificar e-mails (opção avançada)")
    
    escolha = input("Escolha uma opção (1/2): ")

    if escolha == '1':
        main_window.run()
    elif escolha == '2':
        quantidade = int(input("Quantos e-mails você deseja gerar e verificar? "))
        usar_tempmail = input("Deseja usar e-mails temporários? (s/n): ").lower() == 's'
        criptografar = input("Deseja criptografar os dados localmente? (s/n): ").lower() == 's'

        emails_verificados = gerar_e_verificar_emails(quantidade, usar_tempmail, criptografar)

        print("\nResultados:")
        for email, senha, resultado in emails_verificados:
            status = "Válido" if resultado else "Inválido"
            print(f"Email: {email} | Senha: {senha} | Status: {status}")

if __name__ == "__main__":
    main()
