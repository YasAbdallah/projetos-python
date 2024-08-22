from datetime import datetime
from lib.navegacao import Navegar
from lib.funcoes import mensagem, criarPDFSimples, criarPDFMultifuncional, abrir_pasta
from time import sleep
from PIL import ImageGrab
import os

site_impressoras_multifuncional = {
    "EGC":"",
    "EVR primeiro andar":"",
    "EAD":"",
    "Gabinete":"",
    "EMA Chefia":"",
    "EMA Contagem":"",
    "EVR Bagagem":"",
    
}

site_impressora_colorida = {"EGC Colorida":"",}

site_impressoras_simples = {
    "EMA Destinação":"",
    "CAC": "",
    "SOATA":"",
    "EVR Bagagem_2":"",
}

diretorio_webDriver = ".\\webdriver\\"

diretorio_rede_salvar_pdf = f"C:\\Users\\{os.getlogin()}\\Downloads\\_Relatorios_impressoras_HP\\{datetime.today().month - 1}\\"

if not os.path.exists(diretorio_rede_salvar_pdf): 
    os.makedirs(diretorio_rede_salvar_pdf)

data_hoje = f"{datetime.today().day}-{datetime.today().month}-{datetime.today().year}"

mensagem("Iniciando Geração de relatório.", "A geração de relatório está iniciando. A captura dos dados dura, em média, 7 minutos. Fique a vontade para fazer outra coisa enquanto o relatório é gerado", tempo=5)

driver = Navegar(caminhoDriver=diretorio_webDriver)

for setor, site in site_impressoras_simples.items():
    driver.abrirSite(site)
    mensagem("Iniciando captira dos dados.", f"Iniciando captura dos dados do setor: {setor}")
    # Acessando o site da impressora
    driver.clicar("//button[@id='details-button']")
    driver.clicar("//a[@id='proceed-link']")
    driver.clicar("//button[@class='gui-action-btn']")
    # Fazendo login
    driver.clicar("//a[@class='login']")
    driver.escrever("//input[@type='password']", "irf@$3004")
    driver.clicar("//button[@class='gui-action-btn']")
    # Acessar pagina para relatório
    sleep(3)
    driver.clicar("//a[@id='top-cat-Tools']")

    #Informações do produto
    driver.clicar("//div[@aria-label='Informações do produto']")
    driver.clicar("//a[@id='nav-pgDevInfo']")
    sleep(3)
    nome_produto = str(driver.capturarTexto("//table[@id='appDevInfo-printerInfo-tbl-Tbl']/tbody/tr[1]/td[2]"))
    numero_produto = str(driver.capturarTexto("//table[@id='appDevInfo-printerInfo-tbl-Tbl']/tbody/tr[2]/td[2]"))
    numero_serie = str(driver.capturarTexto("//table[@id='appDevInfo-printerInfo-tbl-Tbl']/tbody/tr[3]/td[2]"))

    driver.clicar("//div[@aria-label='Relatórios']")
    driver.clicar("//a[@id='nav-pgBizUsageReport']")

    sleep(3)
    # Mecanismo de impressão
    mecanismo_total_impresso = str(driver.capturarTexto("//table[@id='appUsageReport-media-type-ph-Tbl']/tbody/tr[2]/td[2]"))
    mecanismo_total_frente_verso = str(driver.capturarTexto("//table[@id='appUsageReport-media-type-ph-Tbl']/tbody/tr[4]/td[2]"))
    mecanismo_total_modo_economico = str(0) 
    mecanismo_total_pags = str(driver.capturarTexto("//table[@id='appUsageReport-media-type-ph-Tbl']/tbody/tr[1]/td[2]"))
    mecanismo_total_congestionado = str(driver.capturarTexto("//table[@id='appUsageReport-media-type-ph-Tbl']/tbody/tr[5]/td[2]"))
    mecanismo_total_falhas = str(driver.capturarTexto("//table[@id='appUsageReport-media-type-ph-Tbl']/tbody/tr[6]/td[2]"))
    iso_e_jis_a4_contagem_total = str(driver.capturarTexto("//table[@id='appUsageReport-media-size-print-ph-Tbl-Tbl']/tbody/tr[2]/td[3]"))

    # Tabela 9 Fax
    impressao_equilavente_a4 = str(driver.capturarTexto("//table[@id='appUsageReport-media-a4-equiv-ph-Tbl']/tbody/tr[1]/td[2]"))

    mensagem("Captura de dados.", f"Captura de dados do setor {setor} finalizado.")
    mensagem("Criação de PDF", "Iniciando a criação do PDF da impressora.")
    
    criarPDFSimples(
    setor=setor, 
    modelo='HP LaserJet Pro 4003 series', 
    nome_impressora=nome_produto, 
    numero_produto=numero_produto, 
    numero_serie=numero_serie,
    mecan_total_impresso = mecanismo_total_impresso,
    mecan_total_frente_verso = mecanismo_total_frente_verso,
    mecn_total_modo_economico = mecanismo_total_modo_economico, 
    mecan_total_pags = mecanismo_total_pags,
    mecan_total_congestionado = mecanismo_total_congestionado,
    mecan_total_falhas = mecanismo_total_falhas,
    iso_e_jis_a4_contagem_total = iso_e_jis_a4_contagem_total,
    impressao_equilavente_a4 = impressao_equilavente_a4,
    nome_arquivo = f"Relatorio_impressora_HP_{setor}_simples.pdf",
    diretorio_salvar = diretorio_rede_salvar_pdf)

    mensagem("Criação de PDF.", f"PDF do setor {setor} finalizado.")

driver.abrirSite(site_impressora_colorida['EGC Colorida'])

driver.clicar("//button[@id='details-button']")
driver.clicar("//a[@id='proceed-link']")
driver.escrever("//input[@id='USERNAME']", "administrator")
driver.clicar("//button[@name='LoginButton']")
driver.clicar("//span[text()='Controlo estado/Cancelar']")
driver.clicar("//a[text()='Verificar Contador ']")
img = ImageGrab.grab()
img.save(os.path.join(diretorio_rede_salvar_pdf, "Relatorio_impressora_CANON_EGC.pdf"))


for setor, site in site_impressoras_multifuncional.items():
    driver.abrirSite(site)
    mensagem("Iniciando captira dos dados.", f"Iniciando captura dos dados do setor: {setor}")
    # Acessando o site da impressora
    driver.clicar("//button[@id='details-button']")
    driver.clicar("//a[@id='proceed-link']")
    driver.clicar("//button[@class='gui-action-btn']")
    # Fazendo login
    driver.clicar("//a[@class='login']")
    driver.escrever("//input[@type='password']", "irf@$3004")
    driver.clicar("//button[@class='gui-action-btn']")
    # Acessar pagina para relatório
    sleep(3)
    driver.clicar("//a[@id='top-cat-Tools']")

    #Informações do produto
    driver.clicar("//div[@aria-label='Informações do produto']")
    driver.clicar("//a[@id='nav-pgDevInfo']")
    nome_produto = str(driver.capturarTexto("//table[@id='appDevInfo-printerInfo-tbl-Tbl']/tbody/tr[1]/td[2]"))
    numero_produto = str(driver.capturarTexto("//table[@id='appDevInfo-printerInfo-tbl-Tbl']/tbody/tr[2]/td[2]"))
    numero_serie = str(driver.capturarTexto("//table[@id='appDevInfo-printerInfo-tbl-Tbl']/tbody/tr[3]/td[2]"))

    driver.clicar("//div[@aria-label='Relatórios']")
    driver.clicar("//a[@id='nav-pgBizUsageReport']")

    sleep(3)
    # Digitalização
    digitalizar_alimentadora_auto = str(driver.capturarTexto("//table[@id='appUsageReport-scan-app-ph-Tbl']/tbody/tr[2]/td[2]"))
    digitalizar_mesa = str(driver.capturarTexto("//table[@id='appUsageReport-scan-app-ph-Tbl']/tbody/tr[1]/td[2]"))
    digitalizar_email = str(driver.capturarTexto("//table[@id='appUsageReport-scan-app-ph-Tbl']/tbody/tr[3]/td[2]"))
    digitalizar_pasta_rede = str(driver.capturarTexto("//table[@id='appUsageReport-scan-app-ph-Tbl']/tbody/tr[4]/td[2]"))
    # Copiadora
    copia_alimentador_auto = str(driver.capturarTexto("//table[@id='appUsageReport-copy-ph-Tbl']/tbody/tr[2]/td[2]"))
    copia_mesa_scanner = str(driver.capturarTexto("//table[@id='appUsageReport-copy-ph-Tbl']/tbody/tr[1]/td[2]"))
    copia_total = str(driver.capturarTexto("//table[@id='appUsageReport-copy-ph-Tbl']/tbody/tr[3]/td[2]"))
    # Fax
    fax_alimentadora_auto = str(driver.capturarTexto("//table[@id='appUsageReport-fax-app-ph-Tbl']/tbody/tr[2]/td[2]"))
    fax_mesa_scanner = str(driver.capturarTexto("//table[@id='appUsageReport-fax-app-ph-Tbl']/tbody/tr[1]/td[2]"))
    fax_total_enviado = str(driver.capturarTexto("//table[@id='appUsageReport-fax-app-ph-Tbl']/tbody/tr[4]/td[2]"))
    fax_total_computador = str(driver.capturarTexto("//table[@id='appUsageReport-fax-app-ph-Tbl']/tbody/tr[5]/td[2]"))
    # Mecanismo de impressão
    mecanismo_total_impresso = str(driver.capturarTexto("//table[@id='appUsageReport-media-type-ph-Tbl']/tbody/tr[2]/td[2]"))
    mecanismo_total_frente_verso = str(driver.capturarTexto("//table[@id='appUsageReport-media-type-ph-Tbl']/tbody/tr[4]/td[2]"))
    mecanismo_total_modo_economico = str(0) 
    mecanismo_total_pags = str(driver.capturarTexto("//table[@id='appUsageReport-media-type-ph-Tbl']/tbody/tr[1]/td[2]"))
    mecanismo_total_congestionado = str(driver.capturarTexto("//table[@id='appUsageReport-media-type-ph-Tbl']/tbody/tr[5]/td[2]"))
    mecanismo_total_falhas = str(driver.capturarTexto("//table[@id='appUsageReport-media-type-ph-Tbl']/tbody/tr[6]/td[2]"))
    # Mecanismo scanner
    scanner_total_alimentador_auto = str(driver.capturarTexto("//table[@id='appUsageReport-scanner-ph-Tbl']/tbody/tr[1]/td[2]"))
    scanner_total_mesa_scanner = str(driver.capturarTexto("//table[@id='appUsageReport-scanner-ph-Tbl']/tbody/tr[3]/td[2]"))
    scanner_total_consegtionado = str(driver.capturarTexto("//table[@id='appUsageReport-scanner-ph-Tbl']/tbody/tr[4]/td[2]"))
    # Tabela 6 imprimir/copiar/fax
    us_carta_contagem_total = str(driver.capturarTexto("//table[@id='appUsageReport-media-size-print-ph-Tbl-Tbl']/tbody/tr[1]/td[3]"))
    iso_e_jis_a4_contagem_total = str(driver.capturarTexto("//table[@id='appUsageReport-media-size-print-ph-Tbl-Tbl']/tbody/tr[2]/td[3]"))
    # Tabela 7 Copiar
    copiar_todas = str(driver.capturarTexto("//table[@id='appUsageReport-media-size-copy-ph-Tbl-Tbl']/tbody/tr[1]/td[3]"))
    # Tabela 8 Fax
    fax_todas = str(driver.capturarTexto("//table[@id='appUsageReport-media-size-fax-ph-Tbl-Tbl']/tbody/tr[1]/td[3]"))
    # Tabela 9 Fax
    impressao_equilavente_a4 = str(driver.capturarTexto("//table[@id='appUsageReport-media-a4-equiv-ph-Tbl']/tbody/tr[1]/td[2]"))
    

    mensagem("Captura de dados.", f"Captura de dados do setor {setor} finalizado.")
    mensagem("Criação de PDF", "Iniciando a criação do PDF da impressora.")
    criarPDFMultifuncional(
    setor=setor, 
    modelo='HP LaserJet Pro MFP 4103 series', 
    nome_impressora=nome_produto, 
    numero_produto=numero_produto, 
    numero_serie=numero_serie,
    digit_alimentador_auto = digitalizar_alimentadora_auto,
    digit_mesa_scanner = digitalizar_mesa,
    digit_email = digitalizar_email,
    digit_pasta_rede = digitalizar_pasta_rede,
    copia_alimentador_auto = copia_alimentador_auto,
    copia_mesa_scanner = copia_mesa_scanner,
    copia_total = copia_total,
    fax_alimentadora_auto = fax_alimentadora_auto,
    fax_mesa_scanner = fax_mesa_scanner,
    fax_total_enviado = fax_total_enviado,
    fax_total_computador = fax_total_computador,
    mecan_total_impresso = mecanismo_total_impresso,
    mecan_total_frente_verso = mecanismo_total_frente_verso,
    mecn_total_modo_economico = mecanismo_total_modo_economico, 
    mecan_total_pags = mecanismo_total_pags,
    mecan_total_congestionado = mecanismo_total_congestionado,
    mecan_total_falhas = mecanismo_total_falhas,
    scanner_total_alimentador_auto = scanner_total_alimentador_auto,
    scanner_total_mesa_scanner = scanner_total_mesa_scanner,
    scanner_total_consegtionado = scanner_total_consegtionado,
    us_carta_contagem_total = us_carta_contagem_total,
    iso_e_jis_a4_contagem_total = iso_e_jis_a4_contagem_total,
    copiar_todas = copiar_todas,
    fax_todas = fax_todas,
    impressao_equilavente_a4 = impressao_equilavente_a4,
    nome_arquivo=f"Relatorio_impressora_HP_{setor}_multifuncional.pdf",
    diretorio_salvar = diretorio_rede_salvar_pdf)

    mensagem("Criação de PDF.", f"PDF do setor {setor} finalizado.")

mensagem("Tudo pronto.", f"Verfique se foram feitos todos os relatórios das impressoras.")

abrir_pasta(caminho_do_arquivo=diretorio_rede_salvar_pdf)

mensagem("Finalizando", f"Finalizando Gerador de relatório. Até a próxima.")