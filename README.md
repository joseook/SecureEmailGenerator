# Gerador e Verificador de E-mails

Este projeto é uma ferramenta de Gerador e Verificador de E-mails desenvolvida em Python. Ele permite criar e verificar endereços de e-mail automaticamente, com a capacidade de usar e-mails temporários e criptografar os dados, se necessário.

## Requisitos

- Python 3.x
- Bibliotecas: `requests`, `cryptography`, `tkinter`

## Estrutura do Projeto

```
source/
│
├── config/
│   ├── settings.py
│
├── logs/
│   ├── app.log
│
├── styles/
│   ├── __init__.py
│   ├── main_window.py
│   ├── menu_style.py
│
├── tempmail/
│   ├── __init__.py
│   ├── tempmail.py
│
├── utils/
│   ├── __init__.py
│   ├── cryptografy/
│   │   ├── cryptography.py
│   │
│   ├── generate/
│   │   ├── gerador.py
│   │   ├── verificador.py
│   │
│   ├── utils.py
│
├── main.py
```

## Como Usar

1. **Instalando Dependências**:
   Certifique-se de que todas as bibliotecas necessárias estejam instaladas executando o seguinte comando na pasta raiz do projeto:

   ```bash
   pip install -r requirements.txt
   ```

2. **Iniciando o Projeto**:

   Para iniciar o projeto, execute o seguinte comando na pasta raiz do projeto:

   ```bash
   python main.py
   ```

   Isso abrirá uma interface de linha de comando onde você poderá escolher entre a interface gráfica (GUI) ou a geração e verificação de e-mails avançada.

3. **Interface Gráfica (GUI)**:

   - Escolha a opção "Iniciar a interface gráfica (GUI)" no menu.
   - A interface gráfica permitirá gerar e exibir e-mails e senhas aleatórios.
   - Você pode copiar as senhas geradas clicando no botão "Copy" e salvá-las em um arquivo de texto usando o botão "Download Data".

4. **Geração e Verificação de E-mails Avançada**:

   - Escolha a opção "Gerar e verificar e-mails (opção avançada)" no menu.
   - Siga as instruções para especificar a quantidade de e-mails a serem gerados, se deseja usar e-mails temporários e se deseja criptografar os dados.

## Feedback do Usuário

O projeto permite aos usuários fornecer feedback sobre as recomendações, contribuindo para a melhoria contínua do sistema. O feedback é armazenado em um formato estruturado em um banco de dados para análises futuras.

## Considerações Finais

Este projeto oferece uma base sólida e flexível para o desenvolvimento de sistemas de recomendação de alta qualidade. Você pode personalizar e expandir o sistema adicionando recursos adicionais e ajustando modelos de recomendação conforme necessário.

Aproveite a geração e verificação de e-mails com o Gerador e Verificador de E-mails!

**Observações**: Certifique-se de que os dados necessários, como arquivos CSV e modelos de criptografia, estejam presentes nas pastas apropriadas antes de executar o sistema. Além disso, verifique se os ambientes virtuais Python (venv) estão configurados corretamente para evitar conflitos de dependência.