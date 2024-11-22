import os
import logging
import smtplib
import calendar
from email import encoders
from datetime import date, timedelta
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from lib.funcoes import configurar_logger
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader


class Email:
    def __init__(self, email, pwd, voucher):
        self.email = email
        self.pwd = pwd
        self.voucher = voucher
        self.caminho = os.path.abspath(os.path.join('data'))
        self.logger = configurar_logger(nome_logger="Email", arquivo_log=os.path.abspath(os.path.join('data', "logs", "email.log")), nivel=logging.DEBUG)

    def conectar_servidor(self):
        try:
            self.logger.info("Iniciando conexão ao servidor SMTP")
            server = smtplib.SMTP(host='smtp.office365.com', port=587)
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.email, self.pwd)
            return server
        except smtplib.SMTPAuthenticationError as e:
            self.logger.error(f'Erro de autenticação. Verifique o e-mail ou a senha. {str(e)}')
        except Exception as e:
            self.logger.error(f"Erro ao conectar ao servidor SMTP: {str(e)}")
        return None

    def criar_conteudo_email(self):
        try:
            self.logger.info("Criando corpo do Email.")
            quantidade_total_dias = calendar.monthrange(date.today().year, date.today().month)[1]
            mes_atual = date.today().month
            data_validade = format(date.today() + timedelta(quantidade_total_dias), "%d/%m/%Y")

            env  = Environment(loader=FileSystemLoader(os.path.join('data')))
            template = env.get_template("corpo_email.html")

            return template.render(mes=mes_atual, senha=self.voucher, validade=data_validade)
        except Exception as e:
            self.logger.error(f"Erro ao criar corpo do Email: {str(e)}")
        return None
    
    def preparar_anexo(self, nome_arquivo="senha_wifi.pdf"):
        try:
            self.logger.info("Preparando arquivo de anexo para o email.")
            with open(os.path.join(self.caminho, "imagem_senha", nome_arquivo), 'rb') as attachment:
                att = MIMEBase('application', 'octet-stream')
                att.set_payload(attachment.read())
                encoders.encode_base64(att)
                att.add_header('Content-Disposition', f'attachment; filename={nome_arquivo}')
            return att
        except FileNotFoundError:
            self.logger.error(f'Erro: Arquivo {nome_arquivo} não foi encontrado.')
        except Exception as e:
            self.logger.error(f"Erro ao preparar arquivo de anexo: {str(e)}")
        return None

    def enviar_email(self):
        self.logger.info("Iniciando Envio de email")

        conteudo_html = self.criar_conteudo_email()
        anexo = self.preparar_anexo()
        
        if anexo is None:
            return  # Anexo não foi encontrado, não prossegue
        try:
            self.logger.info("Abrindo lista de emails.")
            with open(os.path.join(self.caminho, "emails", "email.txt"), 'r') as emails_file:
                emails = [x.strip() for x in emails_file.readlines()]
                
            # Conectar ao servidor de email
            server = self.conectar_servidor()
            if server is None:
                return
            
            for destinatario in emails:
                self.logger.info(f"Montando email para {destinatario}")

                email_message = MIMEMultipart()
                email_message['From'] = self.email
                email_message['To'] = destinatario
                email_message['Subject'] = "Acesso Wi-Fi para Visitantes – Informações de Senha (E-mail Automático, Não Responder)"
                email_message.attach(MIMEText(conteudo_html, "html", "utf-8"))
                email_message.attach(anexo)
                
                print(f"Enviando e-mail para {destinatario}")
                server.sendmail(self.email, destinatario, email_message.as_string())

            server.quit()
            self.logger.info("Envio de Email FINALIZADO.")
            
        except Exception as e:
            self.logger.error(f'Erro no envido de e-mail: {str(e)}')
