import os
from time import sleep
from PIL import ImageGrab
from lib.prints import Print
from datetime import datetime
from lib.navegacao import Navegar
from lib.funcoes import mensagem, criarPDFSimples, criarPDFMultifuncional, abrir_pasta, limpar_tela, realizar_ping, ler_dados


printar = Print()
diretorio_webDriver = ".\\webdriver\\"
login_impressora = ['administrator', "irf@$3004"]

diretorio_rede_salvar_pdf = f"C:\\Users\\{os.getlogin()}\\Downloads\\_Relatorios_impressoras_HP\\{datetime.today().month}\\"

if not os.path.exists(diretorio_rede_salvar_pdf): 
    os.makedirs(diretorio_rede_salvar_pdf)

data_hoje = f"{datetime.today().day}-{datetime.today().month}-{datetime.today().year}"

driver = Navegar(caminhoDriver=diretorio_webDriver)


def capturar_tela(diretorio_salvar_pdf, nome_arquivo):
    img = ImageGrab.grab()
    img.save(os.path.join(diretorio_salvar_pdf, nome_arquivo))
    return True


def salvar_PDF_multifuncional(setor, info_impressora, diretorio_rede_salvar_pdf=diretorio_rede_salvar_pdf):
    nome_setor = str(setor).replace(",", "_").replace(".", "_").replace(" ", "").replace(":","")
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
    printar.print_verde(f"PDF do setor {setor} finalizado.")
    return True

def salvar_PDF_simples(setor, info_impressora, diretorio_rede_salvar_pdf=diretorio_rede_salvar_pdf):
    nome_setor = str(setor).replace(",", "_").replace(".", "_").replace(" ", "").replace(":","")
    criarPDFSimples(
        setor=setor, 
        modelo='HP LaserJet Pro 4003 series', 
        nome_impressora=info_impressora[0],
        numero_produto=info_impressora[1],
        numero_serie=info_impressora[2], 
        mecan_total_impresso=info_impressora[3], 
        mecan_total_frente_verso=info_impressora[4],
        mecn_total_modo_economico=info_impressora[5], 
        mecan_total_pags=info_impressora[6], 
        mecan_total_congestionado=info_impressora[7],
        mecan_total_falhas=info_impressora[8], 
        iso_e_jis_a4_contagem_total=info_impressora[9], 
        impressao_equilavente_a4=info_impressora[10], 
        nome_arquivo=f"Relatorio_impressora_HP_{nome_setor}_simples.pdf", 
        diretorio_salvar=diretorio_rede_salvar_pdf
    )
    printar.print_verde(f"PDF do setor {setor} finalizado.")
    return True

# Impressora Colorida
def gerar_relatorio_hp_colorido(login_impressora=login_impressora):
    limpar_tela()
    dados_impressora_colorida = ler_dados(os.path.join(os.path.dirname(__file__), "..", "data", "impressora_colorida.json"))
    for setor, site in dados_impressora_colorida[0]["sites"].items():
        driver.abrirSite(site)
        for key, value in dados_impressora_colorida[1]["xpath"].items():
            if "clicar" in (key, value):
                driver.clicar(value) if "clicar" in key else driver.clicar(key)
            if "escrever" in (key, value):
                driver.escrever(value, login_impressora[0]) if "escrever" in key else driver.escrever(key, login_impressora[0])
        capturar_tela(diretorio_rede_salvar_pdf, "Relatorio_impressora_CANON_EGC.pdf")
        driver.fecharNavegador()

# Impressoras Multifuncional
def gerar_relatorio_multifuncional_todos(login_impressora=login_impressora):
    limpar_tela()
    dados_impressora_multifuncional = ler_dados(os.path.join(os.path.dirname(__file__), "..", "data", "impressora_multifuncional.json"))
    contador = 0
    for setor, site in dados_impressora_multifuncional[0]["sites"].items():
        info_impressora = []
        driver.abrirSite(site)
        printar.print_colorido(f"Iniciando captura dos dados do setor: {setor}")
        for key, value in dados_impressora_multifuncional[1]["xpath"].items():
            if "clicar" in (key, value):
                driver.clicar(value) if "clicar" in key else driver.clicar(key)
            if "escrever" in (key, value):
                driver.escrever(value, login_impressora[1]) if "escrever" in key else driver.escrever(key, login_impressora[1])
            if "capturarTexto" in (key, value):
                info_impressora.append(str(driver.capturarTexto(key)))
        printar.print_verde(f"Captura de dados do setor {setor} finalizado.")
        printar.print_colorido("_"*50)
        printar.print_colorido("Iniciando a criação do PDF da impressora.")
        salvar_PDF_multifuncional(setor, info_impressora)
        printar.print_colorido("_"*50)
        printar.print_magenta("Fechando Navegador.")
        driver.fecharNavegador()
        contador += 1
    printar.print_verde(f"Processo finalizado. Foram gerados {contador} relatórios.")
    return

def gerar_relatorio_multifuncional_unitario(login_impressora=login_impressora):
    limpar_tela()
    dados_impressora_multifuncional = ler_dados(os.path.join(os.path.dirname(__file__), "..", "data", "impressora_multifuncional.json"))
    dados = [(setor, site) for setor, site in dados_impressora_multifuncional[0]["sites"].items()]
    info_impressora = []
    while True:
        printar.print_colorido("Qual impressora deseja gerar o relatório?")
        impressora = int(input(f"""
        [1] - {dados[0][0]} - {dados[0][1]};
        [2] - {dados[1][0]} - {dados[1][1]};
        [3] - {dados[2][0]} - {dados[2][1]};
        [4] - {dados[3][0]} - {dados[3][1]};
        [5] - {dados[4][0]} - {dados[4][1]};
        [6] - {dados[5][0]} - {dados[5][1]};
        [7] - {dados[6][0]} - {dados[6][1]};
        Digite uma das opções: """))

        if impressora not in (1, 2, 3, 4, 5, 6, 7):
            printar.print_vermelho("Opção inválida. Tente novamente.")
        else:             
            driver.abrirSite(dados[impressora-1][1])
            printar.print_colorido(f"Iniciando captura dos dados do setor: {dados[impressora-1][0]}")
            for key, value in dados_impressora_multifuncional[1]["xpath"].items():
                if "clicar" in (key, value):
                    driver.clicar(value) if "clicar" in key else driver.clicar(key)
                if "escrever" in (key, value):
                    driver.escrever(value, login_impressora[1]) if "escrever" in key else driver.escrever(key, login_impressora[1])
                if "capturarTexto" in (key, value):
                    info_impressora.append(str(driver.capturarTexto(key)))
            printar.print_verde(f"Captura de dados do setor {dados[impressora-1][0]} finalizado.")
            printar.print_colorido("_"*50)
            printar.print_colorido("Iniciando a criação do PDF da impressora.")        
            salvar_PDF_multifuncional(dados[impressora-1][0], info_impressora)
            printar.print_colorido("_"*50)
            printar.print_azul("Fechando Navegador.")
            driver.fecharNavegador()
            break
    return 

def gerar_relatorio_hp_multifuncional(resultado):
    if resultado == "1":
        gerar_relatorio_multifuncional_unitario()
        printar.print_verde("O Processo foi finalizado.")
        printar.print_amarelo("_"*50)
    else:
        gerar_relatorio_multifuncional_todos()
        printar.print_verde("O Processo foi finalizado.")
        printar.print_amarelo("_"*50)
    return


# Impressoras Simples
def gerar_relatorio_simples_todos(login_impressora=login_impressora):
    limpar_tela()

    dados_impressora_simples = ler_dados(os.path.join(os.path.dirname(__file__), "..", "data", "impressora_simples.json"))
    contador = 0
    for setor, site in dados_impressora_simples[0]["sites"].items():
        info_impressora = []
        driver.abrirSite(site)
        printar.print_colorido(f"Iniciando captura dos dados do setor: {setor}")
        for key, value in dados_impressora_simples[1]["xpath"].items():
            if "clicar" in (key, value):
                driver.clicar(value) if "clicar" in key else driver.clicar(key)
            if "escrever" in (key, value):
                driver.escrever(value, login_impressora[1]) if "escrever" in key else driver.escrever(key, login_impressora[1])
            if "capturarTexto" in (key, value):
                info_impressora.append(str(driver.capturarTexto(key)))
        printar.print_verde(f"Captura de dados do setor {setor} finalizado.")
        printar.print_colorido("_"*50)
        printar.print_colorido("Iniciando a criação do PDF da impressora.")
        salvar_PDF_simples(setor, info_impressora)
        printar.print_colorido("_"*50)
        printar.print_magenta("Fechando Navegador.")
        driver.fecharNavegador()
        contador += 1
    printar.print_verde(f"Processo finalizado. Foram gerados {contador} relatórios.")
    return

def gerar_relatorio_simples_unitario(login_impressora=login_impressora):
    limpar_tela()

    dados_impressora_simples = ler_dados(os.path.join(os.path.dirname(__file__), "..", "data", "impressora_simples.json"))
    dados = [(setor, site) for setor, site in dados_impressora_simples[0]["sites"].items()]
    info_impressora = []
    while True:
        printar.print_colorido("Qual impressora deseja gerar o relatório?")
        impressora = int(input(f"""
        [1] - {dados[0][0]} - {dados[0][1]};
        [2] - {dados[1][0]} - {dados[1][1]};
        [3] - {dados[2][0]} - {dados[2][1]};
        [4] - {dados[3][0]} - {dados[3][1]};
        Digite uma das opções: """))

        if impressora not in (1, 2, 3, 4, 5, 6, 7):
            printar.print_vermelho("Opção inválida. Tente novamente.")
        else:             
            driver.abrirSite(dados[impressora-1][1])
            printar.print_colorido(f"Iniciando captura dos dados do setor: {dados[impressora-1][0]}")
            for key, value in dados_impressora_simples[1]["xpath"].items():
                if "clicar" in (key, value):
                    driver.clicar(value) if "clicar" in key else driver.clicar(key)
                if "escrever" in (key, value):
                    driver.escrever(value, login_impressora[1]) if "escrever" in key else driver.escrever(key, login_impressora[1])
                if "capturarTexto" in (key, value):
                    info_impressora.append(str(driver.capturarTexto(key)))
            printar.print_verde(f"Captura de dados do setor {dados[impressora-1][0]} finalizado.")
            printar.print_colorido("_"*50)
            printar.print_colorido("Iniciando a criação do PDF da impressora.")        
            salvar_PDF_simples(dados[impressora-1][0], info_impressora)
            printar.print_colorido("_"*50)
            printar.print_magenta("Fechando Navegador.")
            driver.fecharNavegador()
            break
    return 

def gerar_relatorio_hp_simples(resultado):
    if resultado == "1":
        limpar_tela()
        gerar_relatorio_simples_unitario()
        printar.print_verde("O Processo foi finalizado.")
        printar.print_amarelo("_"*50)
    else:
        limpar_tela()
        gerar_relatorio_simples_todos()
        printar.print_verde("O Processo foi finalizado.")
        printar.print_amarelo("_"*50)
    return
