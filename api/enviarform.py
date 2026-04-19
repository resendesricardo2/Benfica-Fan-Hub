import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("MAIL_USER")
password = os.getenv("MAIL_PASS")
host = os.getenv("MAIL_HOST")
port = int(os.getenv("MAIL_PORT"))

def enviar_email(nome, email, mensagem):
    corpo = f"""
    Novo Formulário de Contacto

    Nome Completo: {nome}
    Email: {email}

    Mensagem:
    {mensagem}
    """

    msg = MIMEText(corpo)
    msg["Subject"] = "Novo Formulário de Contacto"
    msg["From"] = "teu_email@gmail.com"
    msg["To"] = "destino@gmail.com"

    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()