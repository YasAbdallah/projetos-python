from lib.navegacao import Navegar
from lib.funcoes import *
from time import sleep
import os

caminhoDriver = "D:\Temp\scripts\webdriver"
site = 'https://sa3.receita.fazenda/php/inicio2.php'

xpath = {
    '//a[@title="Acessar com o PIN"]': "",
    '//a[@title="Abrir Solicitação no SoliCorp" or text()="SoliCorp - Abrir Solicitação" or @title="SoliCorp - Abrir Solicitação"]': "",
    '//a[text() = "Governança de TI" or text() = "Atendimento de TI da RFB"]': "",
    'chamados': {
        '//table[@id="grid_rs_1"]/tbody/tr/td[1]/a': "",
        '//select/option[text()="Atendimento remoto a computador/notebook ou periféricos e a instalação de software" or @value="297"]': "",
        '//input[@name="chave_atendimento"]': palavraAleatoria(),
        '//textarea[@name="tx_solicitacao"]': "",
        '//button[@title="Confirmar"]': ""
    },
}

    

mensagem(msg = "Iniciando abertura de chamados", tempo = 1500)

if not os.path.exists(caminhoDriver):
    os.mkdir(caminhoDriver)

driver = Navegar(caminhoDriver=caminhoDriver)
driver.abrirSite(url=site)
sleep(3)
for key, value in xpath.items():
    sleep(3)
    if key == "chamados":
        with open("../data/chamados.txt", encoding="utf-8") as listaChamados:
            for chamado in listaChamados.readlines():
                for keyChamado, valueChamado in xpath['chamados'].items():
                    sleep(3)
                    driver.navegar(keyChamado, chamado) if keyChamado == '//textarea[@name="tx_solicitacao"]' else driver.navegar(keyChamado, valueChamado)
    driver.navegar(key, value) if value != "" else driver.navegar(key)

driver.fecharNavegador()
mensagem(msg = "Abertura de chamados finalizado", tempo = 3000)