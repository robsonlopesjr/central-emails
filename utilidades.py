from email.message import EmailMessage
import smtplib
import ssl


def enviar_email(email_usuario, destinatarios, titulo, corpo, senha_app):
    """
    Função para enviar o E-mail usando o provedor do Gmail

    :param email_usuario: str
    :param destinatarios: str
    :param titulo: str
    :param corpo: str
    :param senha_app: str
    :return:
    """
    message_email = EmailMessage()
    message_email["From"] = email_usuario
    message_email["To"] = destinatarios
    message_email["Subject"] = titulo
    message_email.set_content(corpo)

    safe = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
        smtp.login(email_usuario, senha_app)
        smtp.sendmail(email_usuario, destinatarios, message_email.as_string())