import os
import logging
import pymsgbox
from random import randint
from reportlab.pdfgen import canvas
from wifi_qrcode_generator.generator import wifi_qrcode
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def menssagem(titulo, texto, tempo):
    criador = " Criado Por: Yasser Ibrahim Abdallah Vaz Condoluci."
    return pymsgbox.alert(text=texto, title=titulo + criador, timeout=tempo)

def mm_to_pixel(mm):
    return mm / 0.352777

def criar_PDF(senha):
    caminho = os.path.join("data", "pdf")

    os.makedirs(caminho, exist_ok=True)

    cnv = canvas.Canvas(os.path.join(caminho, "senha_wifi.pdf"), pagesize=A4)

    cnv.rect(mm_to_pixel(1.70), mm_to_pixel(1.70), width=mm_to_pixel(206.18), height=mm_to_pixel(293.18))
    cnv.drawImage(os.path.join(caminho, "imagem_senha", "wifi_logo.png"), mm_to_pixel(30), mm_to_pixel(120), width=mm_to_pixel(150), height=mm_to_pixel(230), preserveAspectRatio=True, mask="auto")
    cnv.drawImage(os.path.join(caminho, "imagem_senha", "qrcode_senha.png"), mm_to_pixel(60), mm_to_pixel(53), width=mm_to_pixel(90), height=mm_to_pixel(150), preserveAspectRatio=True, mask="auto")

    pdfmetrics.registerFont(TTFont('arial', 'arial.ttf'))
    pdfmetrics.registerFont(TTFont('Franklin Gotic', 'framd.ttf'))
    pdfmetrics.registerFont(TTFont('Segoe', 'segoesc.ttf'))

    cnv.setFont('arial', 20)
    cnv.drawString(mm_to_pixel(50), mm_to_pixel(80), "Aponte a câmera do seu celular ou")
    cnv.drawString(mm_to_pixel(52), mm_to_pixel(70), "use a senha para acessar o Wi-Fi.")
    cnv.setFont('arial', 50)
    cnv.drawString(mm_to_pixel(73), mm_to_pixel(35), f"{senha}")

    cnv.setFont('Franklin Gotic', 10)
    cnv.drawString(mm_to_pixel(4), mm_to_pixel(4), "Desenvolvido por: ")
    cnv.setFont('Segoe', 10)
    cnv.drawString(mm_to_pixel(32), mm_to_pixel(4), "Yasser Ibrahim Abdallah Vaz Condoluci.")
    cnv.save()
    
def gerar_qrCode(senha):
    caminho = os.path.join("data", "pdf", "imagem_senha")
    qr_code = wifi_qrcode(
        ssid='Viajantes', 
        hidden=False, 
        authentication_type='WPA', 
        password=senha
    )
    qr_code.print_ascii()
    qr_code.make_image().save(os.path.join(caminho, "qrcode_senha.png"))

def gerar_senha_wifi():
    i = 0
    senha = ''
    for i in range(6):
        senha += str(randint(0, 10))
    return senha

def configurar_logger(nome_logger='app', arquivo_log='app.log', nivel=logging.INFO):
    """
        Configura e retorna um logger para gerenciar logs da aplicação.

        Args:
            nome_logger (str): Nome do logger, usado para identificação.
            arquivo_log (str): Caminho do arquivo onde os logs serão salvos.
            nivel (int): Nível de registro (DEBUG, INFO, WARNING, ERROR, CRITICAL).

        Returns:
            logging.Logger: Objeto logger configurado.
    """
    # Criação do diretório para logs, se necessário.
    diretorio_log = os.path.dirname(arquivo_log)
    if diretorio_log and not os.path.exists(diretorio_log):
        os.makedirs(diretorio_log)

    # Configurar o logger
    logger = logging.getLogger(nome_logger)
    logger.setLevel(nivel)

    #Evitar Múltiplos handlers no logger
    if not logger.handlers:
        #formato do logger
        formato = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        #handler para arquivo
        arquivo_handler = logging.FileHandler(arquivo_log)
        arquivo_handler.setFormatter(formato)
        logger.addHandler(arquivo_handler)

        #Handler para console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formato)
        logger.addHandler(console_handler)

    return logger