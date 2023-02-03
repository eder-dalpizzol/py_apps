import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send_email(to, subject, pdf_file):
    # Endereço e senha do remetente
    gmail_user = "dalpizzol.eder@gmail.com"
    gmail_password = ""

    # Conteúdo da mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = COMMASPACE.join([to])
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    # Adiciona o corpo da mensagem como texto simples
    msg.attach(MIMEText("Arquivo PDF anexado."))

    # Adiciona o arquivo PDF como anexo
    with open(pdf_file, "rb") as f:
        part = MIMEApplication(f.read(), Name=pdf_file)
    part['Content-Disposition'] = 'attachment; filename="%s"' % pdf_file
    msg.attach(part)

    # Envia a mensagem de e-mail
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to, msg.as_string())
    server.close()

# Executa a função se este arquivo for executado diretamente
if __name__ == "__main__":
    # Endereço de e-mail do destinatário
    to = "dalpizzol.eder@gmail.com"

    # Assunto da mensagem de e-mail
    subject = "Arquivo PDF"

    # Nome do arquivo PDF
    pdf_file = "sophia_ll.pdf"

    send_email(to, subject, pdf_file)
