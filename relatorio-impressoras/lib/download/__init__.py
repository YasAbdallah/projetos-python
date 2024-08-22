from urllib.request import urlretrieve
from zipfile import ZipFile
import os


class Download:
    """Classe Download foi desenvolvida para fazer download de WebDriver para automações web.
    Seu objetivo é automatizar o download e descompactar o arquivo .zip e deletar após a descompactação em uma pasta especifica.
    """
    def __init__(self):
        self.pathDownload = ''
        self.pathDescompactar = ''
        self.arquivoZip = ''

    def download(self, pathDownload):
        """Descrição:
            Faz download do arquivo .zip e salva em uma pasta.

        Args:
            pathDownload (String): Caminho onde será salvo o arquivo .zip do WebDriver.
        """
        try:
            self.pathDownload = pathDownload
            local_filename, headers = urlretrieve(pathDownload)
            down = open(local_filename)
            down.close()
        except Exception as e:
            pass

    def descompactarZip(self, pathDescompactar):
        """Descrição:
            Descompactar o arquivo .zip do WebDriver.

        Args:
            pathDescompactar (String): Caminho onde foi salvo o arquivo .zip do WebDriver.
        """
        try:
            self.arquivo = [os.path.join(d, a[0]) for d, f, a in os.walk(pathDescompactar)]
            desc = ZipFile(self.arquivo[0])
            desc.extractall(pathDescompactar)
            desc.close()
        except Exception as e:
            pass

    def deletarZip(self):
        """Descrição:
            Deletar o arquivo .zip após a descompactação.
        """
        try:
            os.remove(self.arquivo[0])
        except Exception as e:
            pass
