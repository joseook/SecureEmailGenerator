# main_window.py

import tkinter as tk
from tkinter import messagebox, filedialog

from source.utils.generate import generate, verify
from . import menu_style
from utils import tempmail

def gerar_e_exibir():
    email = generate.gerar_email()
    senha = generate.gerar_senha()
    resultado = verify.verificar_email_truemail(email)
    
    if resultado:
        email_var.set(email)
        senha_var.set(senha)
    else:
        email_var.set("E-mail não verificado")
        senha_var.set("")
        messagebox.showerror("Erro", "E-mail não verificado. Tente novamente.")

def gerar_e_exibir_tempmail():
    email_temp = tempmail.gerar_email_temporario()
    email_var.set(email_temp)
    senha_var.set("N/A")  # Como é um e-mail temporário, não temos uma senha associada

def copiar_senha():
    app.clipboard_clear()
    app.clipboard_append(senha_var.get())
    app.update()
    messagebox.showinfo("Senha Copiada", "Senha copiada com sucesso!")

def baixar_dados():
    dados = f"Email: {email_var.get()}\nSenha: {senha_var.get()}"
    local_arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if local_arquivo:
        with open(local_arquivo, 'w') as file:
            file.write(dados)
        messagebox.showinfo("Dados Salvos", f"Email e senha salvos com sucesso em {local_arquivo}!")

def inicializar_gui():
    global app, email_var, senha_var
    app = tk.Tk()
    app.title("Gerador de Email e Senha Aleatorias")
    app.geometry("800x600")
    app.configure(bg=menu_style.BACKGROUND_COLOR)

    # Variáveis para armazenar e exibir email e senha
    email_var = tk.StringVar()
    senha_var = tk.StringVar()

    # Título
    titulo = tk.Label(app, text="Generate Mail and Password Random", font=menu_style.TITLE_FONT, bg=menu_style.BACKGROUND_COLOR, fg=menu_style.TEXT_COLOR)
    titulo.pack(pady=40)

    # Campo de entrada para exibir o email
    entrada_email = tk.Entry(app, textvariable=email_var, font=menu_style.INPUT_FONT, bg=menu_style.INPUT_COLOR, fg=menu_style.TEXT_COLOR, justify="center", width=30, borderwidth=0)
    entrada_email.pack(pady=20)

    # Campo de entrada para exibir a senha
    entrada_senha = tk.Entry(app, textvariable=senha_var, font=menu_style.INPUT_FONT, bg=menu_style.INPUT_COLOR, fg=menu_style.TEXT_COLOR, justify="center", width=30, borderwidth=0)
    entrada_senha.pack(pady=20)

    # Botão para copiar a senha
    botao_copiar = tk.Button(app, text="Copy", font=menu_style.BUTTON_FONT, bg=menu_style.BUTTON_COLOR, fg=menu_style.TEXT_COLOR, command=copiar_senha)
    botao_copiar.pack(pady=10)

    # Botão para gerar a senha
    botao_gerar = tk.Button(app, text="Generate Password", font=menu_style.BUTTON_FONT, bg=menu_style.BUTTON_COLOR, fg=menu_style.TEXT_COLOR, command=gerar_e_exibir)
    botao_gerar.pack(pady=20)

    # Botão para gerar e-mail temporário
    botao_tempmail = tk.Button(app, text="Generate Temp Email", font=menu_style.BUTTON_FONT, bg=menu_style.BUTTON_COLOR, fg=menu_style.TEXT_COLOR, command=gerar_e_exibir_tempmail)
    botao_tempmail.pack(pady=20)

    # Botão para baixar email e senha
    botao_baixar = tk.Button(app, text="Download Data", font=menu_style.BUTTON_FONT, bg=menu_style.BUTTON_COLOR, fg=menu_style.TEXT_COLOR, command=baixar_dados)
    botao_baixar.pack(pady=20)

def run():
    inicializar_gui()
    app.mainloop()
