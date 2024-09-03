import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviar_email():
    corpo_email = """
    <p>Olá User</p>
    <p>Segue meu email automático</p>
    """

    # Cria a mensagem
    msg = MIMEMultipart()
    msg['Subject'] = "assunto"
    msg['From'] = 'remetente'
    msg['To'] = 'destinatario'
    password = 'senha'  # Defina sua senha aqui

    # Anexa o corpo do email
    msg.attach(MIMEText(corpo_email, 'html'))

    # Conecta ao servidor SMTP e envia o email
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

    print('Email enviado!')


enviar_email()
