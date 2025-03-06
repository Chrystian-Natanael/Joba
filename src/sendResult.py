import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email():
    remetente = "seuemail@gmail.com"
    senha = "suasenha"
    destinatario = "destino@gmail.com"
    
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = "Vagas do Dia"

    corpo = "Segue a lista de vagas em anexo."
    msg.attach(MIMEText(corpo, "plain"))

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatario, msg.as_string())
    servidor.quit()

enviar_email()
