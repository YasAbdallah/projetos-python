import os
import json
from time import sleep
from PIL import ImageGrab
from datetime import datetime
from calendar import monthrange
from lib.navegacao import Navegar
from lib.funcoes import fazer_planilha, fazer_documento_word, pasta_existente


data_atual = datetime.now()

# Criação de diretórios
PATH_DRIVER = os.path.join("C:\\", "scripts", "webDriver")
PATH_DADOS_PRINCIPAL = os.path.join(os.path.dirname(__file__), "..", "data", "internet")
PATH_DADOS_MENSAL = os.path.join(PATH_DADOS_PRINCIPAL, f"{data_atual.year}", f"{data_atual.month}")
PATH_DADOS_PRINTS = os.path.join(PATH_DADOS_MENSAL, "prints", f"{data_atual.day}")
PATH_DADOS_EXCEL = os.path.join(PATH_DADOS_MENSAL, "Controle mensal de velocidade.xlsx")
PATH_DADOS_WORD = os.path.join(PATH_DADOS_MENSAL, f"{data_atual.month}-{data_atual.year}(Medicoes de Velocidade).docx")

# Verificação e criação de diretórios
pasta_existente(PATH_DRIVER)
pasta_existente(PATH_DADOS_PRINCIPAL)
pasta_existente(PATH_DADOS_MENSAL)
pasta_existente(PATH_DADOS_PRINTS)


# monthrange retorna o último dia do mês, basta setá-lo na data e pronto
ultimo_dia = str(data_atual.replace(day=monthrange(data_atual.year, data_atual.month)[1])).split("-")[-1]
quantidade_dias_mes = str(ultimo_dia).split(" ")[0]

try:
    with open(os.path.join("data", "speedTest.json"), "r", encoding="utf-8") as xpath:
        xpath = json.load(xpath)
    driver = Navegar(site='https://www.speedtest.net/', caminho_driver=PATH_DRIVER, xpaths=xpath)
    driver.abrir_navegador()
    driver.navegar(tempo=3)
    sleep(60)
    driver.atualizar_tela()
    sleep(10)
    chaves = list(xpath.keys())
    speedtest_download = str(driver.capturarTexto(chaves[-2]))
    speedtest_upload = str(driver.capturarTexto(chaves[-1]))
    
    imagem = ImageGrab.grab()
    imagem.save(os.path.join(PATH_DADOS_PRINT_SPEEDTEST, 'speedTeste.png'))
except Exception as e:
    print("Ocorreu um erro ao tentar medir a velocidade da internet do site SpeedTest.", e)
finally:
    driver.fechar_navegador()

try:
    with open(os.path.join("data", "minhaConexao.json"), "r", encoding="utf-8") as xpath:
        xpath = json.load(xpath)
    driver = Navegar(site='https://www.minhaconexao.com.br/', caminho_driver=PATH_DRIVER, xpaths=xpath)
    driver.abrir_navegador()
    driver.navegar(tempo=3)
    sleep(60)
    chaves = list(xpath.keys())
    minha_conexao_download = str(driver.capturarTexto(chaves[-2])).split(" ")[0]
    minha_conexao_upload = str(driver.capturarTexto(chaves[-1])).split(" ")[0]
    # Aqui precisa atualizar a tela antes de tirar print.
    driver.atualizar_tela()
    sleep(10)
    imagem = ImageGrab.grab()
    imagem.save(os.path.join(PATH_DADOS_PRINT_MINHACONEXAO, 'minhaConexao.png'))
except Exception as e:
    print(f"Ocorreu um erro ao tentar medir a velocidade da internet no site Minha Conexao. {e}")
finally:
    driver.fechar_navegador()

# Preencher a planilha com os dados
fazer_planilha(PATH_DADOS_EXCEL, data_atual, quantidade_dias_mes, minha_conexao_download, minha_conexao_upload, speedtest_download, speedtest_upload)

# Preencher o arquivo word com os prints da tela
fazer_documento_word(PATH_DADOS_WORD, PATH_DADOS_PRINTS, data_atual, quantidade_dias_mes)