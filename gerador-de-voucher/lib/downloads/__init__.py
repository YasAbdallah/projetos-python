import os
import logging
from time import sleep
from zipfile import ZipFile
from urllib.request import urlretrieve
from lib.funcoes import configurar_logger


class Download:


    def __init__(self, url, path_download, path_descompactar):
        """

        Args:
            url (String): Recebe a url para download do Edge webDriver mais recente
            path_download (String): Path para download do Driver
            path_descompactar (String): Path onde irá descompactar o Driver
        """
        self.url = url
        self.path_download = path_download
        self.path_descompactar = path_descompactar
        self.arquivo = ''
        self.logger = configurar_logger(nome_logger="Download_Driver", arquivo_log=os.path.abspath(os.path.join('data', "logs", "download_driver.log")), nivel=logging.DEBUG)


    def download(self):
        """Realiza  download o EDGE WebDriver.

        Returns:
            Object: Arquivo baixado.
        """
        try:
            self.logger.info("Realizando download do driver.")
            local_filename, headers = urlretrieve(self.path_download)
            down = open(local_filename)
            down.close()
            return self.descompactar()
        except Exception as e:
            self.logger.error(f"Erro ao tentar realizar download do driver: {e}")
        return None
    

    def descompactar(self):
        """Descompactador de zip

        Returns:
            Object: Arquivo escompactado.
        """
        try:
            self.logger.info("Descompactando o driver.")
            self.arquivo = [os.path.join(d, a[0]) for d, f, a in os.walk(self.path_descompactar)]
            desc = ZipFile(self.arquivo[0])
            desc.extractall(self.path_descompactar)
            desc.close()
            sleep(3)
            return self.deletaZip()
        except Exception as e:
            self.logger.error(f"Erro ao tentar descompactar o driver: {e}")
        return None


    def deletaZip(self):
        """Deletar arquivo zip

        Returns:
            Object: Arquivo zip deletado
        """
        try:
            return os.remove(self.arquivo[0])
        except Exception as e:
            self.logger.error(f"Erro ao tentar o arquivo compactado do driver: {e}")
        return None
