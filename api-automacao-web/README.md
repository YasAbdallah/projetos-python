# Automação de download e Navegação com WebDriver

Repositório pensado e desenvolvido para automatizar navegação usando selenium e MSEdgeWebDriver.

## Funcionalidades

- Download do arquivo .zip no site da [MSEdgeWebDriver](https://msedgewebdriverstorage.z22.web.core.windows.net/?form=MA13LH).
- Descompactar e deletar o arquivo .zip após download.
- Abrir Navegador automatizado com selenium.
- Navegar entre abas clicando em botões e preenchendo campos de texto.


## Uso/Exemplos - script de abertura de chamados.
#### Obs.: Sem o link e xpaths do sistema utilizado.

```Python
from lib.navegacao import Navegar
from time import sleep
import os

pathWebDriver = "D:\Temp\scripts\webdriver"
site = 'https://siteExemplo.com.br'

xpaths = {
    '//a[@title="Titulo"]': "",
    '//a[@title="Titulo1" or text()="texto referencia"]': "",
    '//a[text() = "texto2" or text() = "texto3"]': "",
    'chamados': {
        '//table[@id="grid_rs_1"]/tbody/tr/td[1]/a': "",
        '//select/option[text()="selectValue" or @value="297"]': "",
        '//input[@name="palavra_senha"]': "Palavra senha",
        '//textarea[@name="tx_solicitacao"]': "Um texto aleatório",
        '//button[@title="Confirmar"]': ""
    },
}

 
if not os.path.exists(caminhoDriver):
    os.mkdir(caminhoDriver)


#Instancia novo objeto
driver = Navegar(caminhoDriver=caminhoDriver)

#Abre o navegador
driver.abreSite(url=site)

sleep(3)
# Inicia varredura pelo dict de Xpath
for key, value in xpaths.items():
    sleep(3)
    if key == "chamados":
        for keyChamado, valueChamado in xpaths['chamados'].items():
            sleep(3)
            driver.navegar(keyChamado, valueChamado)
    driver.navegar(key, value) if value != "" else driver.navegar(key)

driver.fecharNavegador()
```


## Referência

 - [Selenium](https://www.selenium.dev/documentation/)
 - [Urllib](https://docs.python.org/3/library/urllib.html)
 - [Zipfile](https://docs.python.org/3/library/zipfile.html)


## 🛠 Habilidades
Python


## Autor

- [@YasAbdallah](https://www.github.com/YasAbdallah)
