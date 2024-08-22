from selenium import webdriver
from selenium.webdriver.common.by import By
from lib.download import Download
import os


class Navegar:
    def __init__(self, caminhoDriver):
        """Descrição:
            Essa Classe é para fazer a navegação e preencher dados de forma automática. 

        Args:
            caminhoDriver (String): Path (caminho destino) para onde está localizado o WebDriver para abertura do navegador.
            versaoWebDriver (String): Pega o caminho padrão onde é instalado o MSEdge para pegar a versão mais recente do navegador para download do WebDriver compatível.
            urlWebDriver (String): URL do site do MSEdgeDriver para download do WebDriver mais recente compatível com o navegador instalado.
        """
        self.driver = ''
        self.pathWebDriver = caminhoDriver
        self.versaoWebDriver = [f for d, f, a in os.walk('C:\\Program Files (x86)\\Microsoft\\Edge\\Application')][0][0]
        self.urlWebDriver = f"https://msedgedriver.azureedge.net/{self.versaoWebDriver}/edgedriver_win64.zip"

    def abrirSite(self, url):
        """Descrição:
            Abre o navegado direto no site alvo. Caso ocorra algum erro, faz download o WebDriver mais recente compatível com o navegador instalado e tenta novamente. 

        Args:
            url (String): Recebe a url do site que deseja navegar para obter dados.
        """
        try:
            opcoes = webdriver.EdgeOptions()
            self.driver = webdriver.Edge(options=opcoes)
            self.driver.maximize_window()
            return self.driver.get(url)
        except Exception as e:
            download = Download()
            download.download(self.pathWebDriver)
            download.descompactarZip(self.pathWebDriver)
            download.deletarZip()
            self.abrirSite()
            
    
    def clicar(self, xpath):
        """Descrição:
            Realiza a navegação no site.

        Args:
            xpath (String): Xpath dos buttons, selects, etc.
        """
        try:
            self.driver.find_element(By.XPATH, xpath).click() if self.driver.find_element(By.XPATH, xpath) else ""
        except Exception as e:
            print("Erro ao tentar clicar")
            pass


    def escrever(self, xpath, texto):
        """Descrição:
            Preenche os campos de texto.

        Args:
            xpath (String): Xpath de inputs.
            texto (String): Texto para preencher os inputs.
        """
        try:
            self.driver.find_element(By.XPATH, xpath).send_keys(texto) if self.driver.find_element(By.XPATH, xpath) else None
        except Exception as e:
            print("Erro ao tentar escrever.")
            pass


    def capturarTexto(self, xpath):
        try:
            if self.driver.find_element(By.XPATH, xpath):
                self.driver.implicitly_wait(3)
                return self.driver.find_element(By.XPATH, xpath).text
        except Exception as e:
            print("Erro ao tentar capturar texto")
            pass

    def fecharNavegador(self):
        try:
            self.driver.close()
        except Exception as e:
            print("Ocorreu um erro ao tentar fechar o navegador.", e)
            pass
