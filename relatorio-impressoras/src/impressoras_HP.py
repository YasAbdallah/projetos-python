import os
import json
from time import sleep
from PIL import ImageGrab
from datetime import datetime
from lib.navegacao import Navegar
from lib.funcoes import mensagem, criarPDFSimples, criarPDFMultifuncional, abrir_pasta

diretorio_webDriver = ".\\webdriver\\"
login_impressora = ['administrator', "irf@$3004"]

diretorio_rede_salvar_pdf = f"C:\\Users\\{os.getlogin()}\\Downloads\\_Relatorios_impressoras_HP\\{datetime.today().month - 1}\\"

if not os.path.exists(diretorio_rede_salvar_pdf): 
    os.makedirs(diretorio_rede_salvar_pdf)

data_hoje = f"{datetime.today().day}-{datetime.today().month}-{datetime.today().year}"

mensagem("Iniciando Geração de relatório.", "A geração de relatório está iniciando. A captura dos dados dura, em média, 7 minutos. Fique a vontade para fazer outra coisa enquanto o relatório é gerado", tempo=5)

driver = Navegar(caminhoDriver=diretorio_webDriver)

# Impressora Colorida
with open(os.path.join(os.path.dirname(__file__), "..", "data", "impressora_colorida.json"), encoding="utf-8") as impressora_colorida:
    data = json.load(impressora_colorida)
    for setor, site in data[0]["sites"].items():
        driver.abrirSite(site)
        for key, value in data[1]["xpath"].items():
            if "clicar" in (key, value):
                driver.clicar(value) if "clicar" in key else driver.clicar(key)
            if "escrever" in (key, value):
                driver.escrever(value, login_impressora[0]) if "escrever" in key else driver.escrever(key, login_impressora[0])
    img = ImageGrab.grab()
    img.save(os.path.join(diretorio_rede_salvar_pdf, "Relatorio_impressora_CANON_EGC.pdf"))

# Impressoras Multifuncional
with open(os.path.join(os.path.dirname(__file__), "..", "data", "impressora_multifuncional.json"), encoding="utf-8") as impressora_multifuncional:
    data = json.load(impressora_multifuncional)
    for setor, site in data[0]["sites"].items():
        nome_setor = str(setor).replace(str(setor)[-17:], "")
        info_impressora = []
        driver.abrirSite(site)
        mensagem("Iniciando captira dos dados.", f"Iniciando captura dos dados do setor: {setor}")
        for key, value in data[1]["xpath"].items():
            if "clicar" in (key, value):
                driver.clicar(value) if "clicar" in key else driver.clicar(key)
            if "escrever" in (key, value):
                driver.escrever(value, login_impressora[1]) if "escrever" in key else driver.escrever(key, login_impressora[1])
            if "capturarTexto" in (key, value):
                info_impressora.append(str(driver.capturarTexto(key)))
        mensagem("Captura de dados.", f"Captura de dados do setor {setor} finalizado.")
        mensagem("Criação de PDF", "Iniciando a criação do PDF da impressora.")
        
        criarPDFMultifuncional(
            setor=setor, 
            modelo='HP LaserJet Pro MFP 4103 series',
            nome_impressora=info_impressora[0], 
            numero_produto=info_impressora[1], 
            numero_serie=info_impressora[2],
            digit_alimentador_auto=info_impressora[3], 
            digit_mesa_scanner=info_impressora[4], 
            digit_email=info_impressora[5], 
            digit_pasta_rede=info_impressora[6],
            copia_alimentador_auto=info_impressora[7], 
            copia_mesa_scanner=info_impressora[8], 
            copia_total=info_impressora[9], 
            fax_alimentadora_auto=info_impressora[10], 
            fax_mesa_scanner=info_impressora[11], 
            fax_total_enviado=info_impressora[12], 
            fax_total_computador=info_impressora[13], 
            
            mecan_total_impresso=info_impressora[14],
            mecan_total_frente_verso=info_impressora[15], 
            mecan_total_modo_economico=0, 
            mecan_total_pags=info_impressora[16], 
            mecan_gtotal_conestionado=info_impressora[17], 
            mecan_total_falhas=info_impressora[18],

            scanner_total_alimentador_auto=info_impressora[19], 
            scanner_total_mesa_scanner=info_impressora[20], 
            scanner_total_consegtionado=info_impressora[21],
            us_carta_contagem_total=info_impressora[22], 
            iso_e_jis_a4_contagem_total=info_impressora[23], 
            copiar_todas=info_impressora[24], 
            fax_todas=info_impressora[25],
            impressao_equilavente_a4=info_impressora[26], 
            nome_arquivo=f"Relatorio_impressora_HP_{nome_setor}_multifuncional.pdf", diretorio_salvar=diretorio_rede_salvar_pdf
        )
        del info_impressora
        mensagem("Criação de PDF.", f"PDF do setor {setor} finalizado.")

# Impressoras Simples
with open(os.path.join(os.path.dirname(__file__), "..", "data", "impressora_simples.json"), encoding="utf-8") as impressora_simples: 
    data = json.load(impressora_simples)
    for setor, site in data[0]["sites"].items():
        nome_setor =str(setor).replace(str(setor)[-17:], "")
        info_impressora = []
        driver.abrirSite(site)
        mensagem("Iniciando captira dos dados.", f"Iniciando captura dos dados do setor: {nome_setor}")
        for key, value in data[1]["xpath"].items():
            if "clicar" in (key, value):
                driver.clicar(value) if "clicar" in key else driver.clicar(key)
            if "escrever" in (key, value):
                driver.escrever(value, login_impressora[1]) if "escrever" in key else driver.escrever(key, login_impressora[1])
            if "capturarTexto" in (key, value):
                info_impressora.append(str(driver.capturarTexto(key)))

        mensagem("Captura de dados.", f"Captura de dados do setor {setor} finalizado.")
        mensagem("Criação de PDF", "Iniciando a criação do PDF da impressora.")
        criarPDFSimples(setor=setor, modelo='HP LaserJet Pro 4003 series', nome_impressora=info_impressora[0],
            numero_produto=info_impressora[1], numero_serie=info_impressora[2], mecan_total_impresso=info_impressora[3], mecan_total_frente_verso=info_impressora[4],
            mecn_total_modo_economico=info_impressora[5], mecan_total_pags=info_impressora[6], mecan_total_congestionado=info_impressora[7], 
            mecan_total_falhas=info_impressora[8], iso_e_jis_a4_contagem_total=info_impressora[9], impressao_equilavente_a4=info_impressora[10], nome_arquivo=f"Relatorio_impressora_HP_{nome_setor}_simples.pdf", diretorio_salvar=diretorio_rede_salvar_pdf
        )
        del info_impressora
        mensagem("Criação de PDF.", f"PDF do setor {setor} finalizado.")     

mensagem("Tudo pronto.", f"Verfique se foram feitos todos os relatórios das impressoras.")

abrir_pasta(caminho_do_arquivo=diretorio_rede_salvar_pdf)

mensagem("Finalizando", f"Finalizando Gerador de relatório. Até a próxima.")