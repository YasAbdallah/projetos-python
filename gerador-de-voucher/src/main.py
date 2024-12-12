import os
import json
import lib.funcoes as fc
from lib.email import Email
from lib.navegacao import Navegar

fc.menssagem("Bem-vindo ao gerador de voucher.", "Iniciando Gerador de voucher", 3000)

caminho_driver = os.path.join("C:\\", "scripts", "webDriver")
if not os.path.exists(caminho_driver):
    os.makedirs(caminho_driver)

login_email = {'username': 'issoNaoEUmEmail@valido.com', 'pwd':'semSenhaPorAquiTambem'}

senha_wifi = fc.gerar_senha_wifi()

with open(os.path.join("data","xpath03.json"), "r", encoding="utf-8") as xpath:
    xpath = json.load(xpath)
# Primeiro faz a automação de navegação e criação de um novo Voucher
driver = Navegar(site='https://localhost:8080/manage/account/', caminho_driver=caminho_driver, xpaths=xpath)

# Após o voucher ser gerado, criar o PDF para anexo ao email
fc.menssagem("Gerando PDF.", "Gerando PDF para anexo do email", 2000)

gerar_pdf = fc.criar_PDF(senha_wifi)

# Conectando ao servidor de email 
conectar = Email(email=login_email['username'], pwd=login_email['pwd'], voucher=senha_wifi)

fc.menssagem("Quase lá!.", "Conectanto ao servidor de email", 2000)
conn = conectar.conectar_servidor()
fc.menssagem("Tudo pronto!", "Enviando E-mail", 2000)
conectar.enviar_email(conn)

fc.menssagem("Pronto!!!!", "Tudo certo, aproveite o wi-fi com o voucher novo!", 2000)
