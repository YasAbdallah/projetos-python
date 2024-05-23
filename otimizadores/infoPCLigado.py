import smtplib
import calendar
from datetime import date, datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd
    def conectarServidor(self):
        try:
            server = smtplib.SMTP(host='smtp.office365.com', port=587)
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.email, self.pwd)
            return server
        except Exception as e:
            print('Erro ao conectar ao servidor de email. Verifique se o email ou a senha estão corretas, caso estejam entre em  contato com o administrador.')

    
    def enviarEmail(self, server):
        qntDias = calendar.monthrange(date.today().year, date.today().month)[1]
        # 2- Montando corpo do email
        corpo = f"<h1>O NoteBook foi ligado as {datetime.now()}</h1>"

        email_message = MIMEMultipart()
        email_message['From'] = self.email
        
        email_message['Subject'] = 'Computador foi ligado.'
        email_message.attach(MIMEText(corpo, 'html', 'utf-8'))
        
        server.sendmail(email_message['From'], self.email, email_message.as_string())
        server.close()