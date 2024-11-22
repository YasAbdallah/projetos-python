import os
import json
import lib.funcoes as fc
from lib.email import Email
from lib.navegacao import Navegar

fc.menssagem("Bem-vindo ao gerador de voucher.", "Iniciando Gerador de voucher", 3000)

caminhoDriver = os.path.join("C:\\", "scripts", "webDriver")
if not os.path.exists(caminhoDriver):
    os.makedirs(caminhoDriver)

loginEmail = {'username': 'issoNaoEUmEmail@valido.com', 'pwd':'semSenhaPorAquiTambem'}

senhaWifi = fc.gerar_senha_wifi()

with open(os.path.join("data","xpath03.json"), "r", encoding="utf-8") as xpath:
    xpath = json.load(xpath)
# Primeiro faz a automação de navegação e criação de um novo Voucher
driver = Navegar(site='https://localhost:8080/manage/account/', caminhoDriver=caminhoDriver, xpaths=xpath)

# Após o voucher ser gerado, criar o PDF para anexo ao email
fc.menssagem("Gerando PDF.", "Gerando PDF para anexo do email", 2000)

gerarPDF = fc.criar_PDF(senhaWifi)

# Conectando ao servidor de email 
conectar = Email(email=loginEmail['username'], pwd=loginEmail['pwd'], voucher=senhaWifi)

fc.menssagem("Quase lá!.", "Conectanto ao servidor de email", 2000)
conn = conectar.conectar_servidor()
fc.menssagem("Tudo pronto!", "Enviando E-mail", 2000)
conectar.enviar_email(conn)

fc.menssagem("Pronto!!!!", "Tudo certo, aproveite o wi-fi com o voucher novo!", 2000)
