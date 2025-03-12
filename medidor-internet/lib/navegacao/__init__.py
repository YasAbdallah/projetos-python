import os
import json
import logging
from time import sleep
from selenium import webdriver
from lib.downloads import Download
from lib.funcoes import configurar_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service


class Navegar:


    def __init__(self, site, caminho_driver, xpaths):
        """
        :param site: Informar o site que o sistema deve fazer a navegação
        :param caminho_drive: O caminho onde está localizado o webDriver do navegador
        :param url_web_driver: Informar o site onde é feito o download
        :param xpath: Informar um dicionario com o xpath e do que deseja ser feito. No caso do click apenas uma string vazia ''
        """
        self.site = site
        self.caminho_driver = caminho_driver
        self.versao_driver = [f for d, f, a in os.walk('C:\\Program Files (x86)\\Microsoft\\Edge\\Application')][0][0]
        self.url_web_driver = f"https://msedgedriver.azureedge.net/{self.versao_driver}/edgedriver_win64.zip"
        self.xpaths = xpaths
        self.driver = ''
        self.logger = configurar_logger(nome_logger="navegador_auto", arquivo_log=os.path.abspath(os.path.join("data", "logs", "navegador_auto.log")), nivel=logging.DEBUG)


    def abrir_navegador(self):
        try:
            self.logger.info("Instanciando o navegador.")
            opcoes = webdriver.EdgeOptions()
            self.driver = webdriver.Edge(options=opcoes)
        except Exception as e:
            self.logger.error(f"Ocorreu um erro ao tentar abrir Navegador Automatico.")
            self.logger.info("Realizando download do Driver mais recente.")
            download = Download(self.url_web_driver, self.caminho_driver, self.caminho_driver)
            download.download()
        return None


    def navegar(self, tempo=3):
        try:
            self.logger.info(f"Iniciando Navegação para o site: {self.site}")
            self.driver.get(self.site)
            for xpath, texto in self.xpaths.items():
                sleep(tempo)
                if texto != '':
                    self.escrever(xpath=xpath, texto=texto)
                else:
                    self.clicar(xpath=xpath)
        except Exception as e:
           self.logger.error(f"Erro a navegar pelo site {self.site}. O xpath {xpath} não foi encontrado. A ação foi - {texto} - .")
        return None
    

    def escrever(self, xpath, texto):
        try:
            self.logger.info(f"Preenchendo input em: {xpath}")
            self.driver.find_element(By.XPATH, xpath).send_keys(Keys.CONTROL + 'a')
            return self.driver.find_element(By.XPATH, xpath).send_keys(texto)
        except Exception as e:
            self.logger.error(f"O xpath {xpath} não foi encontrado. Não foi possivel preencher o campo de texto.")
        return None
    

    def capturar_texto(self, xpath):
        try:
            self.logger.info(f"capturando texto em: {xpath}")
            captura_texto = self.driver.find_element(By.XPATH, xpath).text
            return captura_texto
        except Exception as e:
            self.logger.error(f"O xpath {xpath} não foi encontrado. Não foi possivel capturar texto.")
        return None

    def atualizar_tela(self):
        try:
            self.logger.info("Atualizando tela.")
            return self.driver.refresh()
        except Exception as e:
            self.logger.error(f"Erro ao tentar atualizar tela.")

    def clicar(self, xpath):
        try:
            self.logger.info(f"Clicando em {xpath}")
            return self.driver.find_element(By.XPATH, xpath).click()
        except Exception as e:
            self.logger.error(f"O xpath {xpath} não foi encontrado. Não foi possivel clicar.")
        return None


    def fechar_navegador(self):
        try:
            self.logger.info("Fechando navegador.")
            return self.driver.quit()
        except Exception as e:
            self.logger.error(f"Erro ao tentar fechar navegador.")
        return None