import pymsgbox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import shutil
import subprocess
import os

def mensagem(titulo, texto, tempo=3):
    """Popup informativo

    Args:
        titulo (String): Mensagem de título do popup.
        texto (String): Mensagem do corpo do popup.
        tempo (int, optional): Tempo em segundos. Defaults to 3000.

    Returns:
        pymsgbox: Popup com mensagem.
    """
    dev = " Desenvolvido por: Yasser Ibrahim."
    return pymsgbox.alert(text=texto, title=titulo + dev, timeout=(tempo*1000))


def criarPDFMultifuncional(**kwargs):
    """Gerador de pdf
    Utilizar um Dicionario de dados.
    """
    args = [value for key, value in kwargs.items()]
    cnv = canvas.Canvas(args[30], pagesize=A4)

    pdfmetrics.registerFont(TTFont('arial', 'arial.ttf'))
    pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))

    cnv.setFont('Arial-Bold', 12)
    cnv.drawString(mm2p(14), mm2p(285), f"Relatório de uso ({args[0]})")

    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(275), args[1])
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(265), f"Nome do produto: {args[2]}")
    cnv.drawString(mm2p(14), mm2p(255), f"Número do produto: {args[3]}")
    cnv.drawString(mm2p(14), mm2p(245), f"Número de série: {args[4]}")

    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(235), "Digit:")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(230), f"Imagens digitalizadas para host(alimentador de")
    cnv.drawString(mm2p(14), mm2p(225), f"documentos): {args[5]}")
    cnv.drawString(mm2p(14), mm2p(220), f"Imagens digitalizadas para host(Vidro do scanner): {args[6]}")
    cnv.drawString(mm2p(115), mm2p(225), f"Imagens digitalizadas p/ email: {args[7]}")
    cnv.drawString(mm2p(115), mm2p(220), f"Imagens digitalizadas para pasta na rede: {args[8]}")

    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(210), "Copiar")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(205), f"Imagens digitalizadas(alimentador de documentos): {args[9]}")
    cnv.drawString(mm2p(14), mm2p(200), f"Imagens digitalizadas(Vidro do scanner): {args[10]}")
    cnv.drawString(mm2p(115), mm2p(205), f"Páginas totais: {args[11]}")

    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(190), "Fax")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(185), f"Imagens digitalizadas(alimentador de documentos): {args[12]}")
    cnv.drawString(mm2p(14), mm2p(180), f"Imagens digitalizadas(Vidro do scanner): {args[13]}")
    cnv.drawString(mm2p(115), mm2p(185), f"Total faxes enviados: {args[14]}")
    cnv.drawString(mm2p(115), mm2p(180), f"Total faxes enciados (enviados do computador): {args[15]}")

    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(170), "Mecanismo impr")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(165), f"Total de páginas impressas: {args[16]}")
    cnv.drawString(mm2p(14), mm2p(160), f"Total pág. impressas (frente/verso): {args[17]}")
    cnv.drawString(mm2p(14), mm2p(155), f"Total páginas impressas (modo econômico):{ args[18]}")
    cnv.drawString(mm2p(115), mm2p(165), f"Total de págs. do mecanismo*: {args[19]}")
    cnv.drawString(mm2p(115), mm2p(160), f"Total congest: {args[20]}")
    cnv.drawString(mm2p(115), mm2p(155), f"Total falhas coleta: {args[21]}")
    cnv.setFont('arial', 6)
    cnv.drawString(mm2p(14), mm2p(150), f"*A contagem total de páginas do mecanismo nunca é redefinida e representa o número total de páginas processadas pela impressora ao longo de sua vida útil.")

    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(145), "Mecanismo do scanner")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(140), f"Páginas totais (Alimentador de documentos): {args[22]}")
    cnv.drawString(mm2p(14), mm2p(135), f"Páginas totais (Vidro do scanner): {args[23]}")
    cnv.drawString(mm2p(115), mm2p(140), f"Total congest:{ args[24]}")
    
    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(125), "Imprimir/Copiar/Fax")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(120), f"Tamanho mídia")
    cnv.drawString(mm2p(55), mm2p(120), f"Unids")
    cnv.drawString(mm2p(90), mm2p(120), f"Contagem Total de páginas")
    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(118), "_"*90)
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(112), f"U.S Carta")
    cnv.drawString(mm2p(55), mm2p(112), f"1.0")
    cnv.drawString(mm2p(90), mm2p(112), f"{args[25]}")
    cnv.drawString(mm2p(14), mm2p(106), f"ISO e JIS A4")
    cnv.drawString(mm2p(55), mm2p(106), f"1.0")
    cnv.drawString(mm2p(90), mm2p(106), f"{args[26]}")

    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(98), "Copiar")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(93), f"Tamanho mídia")
    cnv.drawString(mm2p(55), mm2p(93), f"Unids")
    cnv.drawString(mm2p(90), mm2p(93), f"Contagem Total de páginas")
    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(90), "_"*90)
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(84), f"Todas")
    cnv.drawString(mm2p(55), mm2p(84), f"-")
    cnv.drawString(mm2p(90), mm2p(84), f"{args[27]}")

    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(75), "Fax")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(70), f"Tamanho mídia")
    cnv.drawString(mm2p(55), mm2p(70), f"Unids")
    cnv.drawString(mm2p(90), mm2p(70), f"Contagem Total de páginas")
    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(68), "_"*90)
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(62), f"Todas")
    cnv.drawString(mm2p(55), mm2p(62), f"-")
    cnv.drawString(mm2p(90), mm2p(62), f"{args[28]}")

    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(55), "Impressões equilaventes a A4")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(90), mm2p(50), f"Contagem Total de páginas")
    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(48), "_"*90)
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(42), f"Imprimir/Copiar/Fax")
    cnv.drawString(mm2p(90), mm2p(42), f"{args[29]}")

    cnv.save()
    shutil.move(args[-2], args[-1]+args[-2])


def criarPDFSimples(**kwargs):
    args = [value for key, value in kwargs.items()]
    cnv = canvas.Canvas(args[-2], pagesize=A4)

    pdfmetrics.registerFont(TTFont('arial', 'arial.ttf'))
    pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))

    cnv.setFont('Arial-Bold', 12)
    cnv.drawString(mm2p(14), mm2p(285), f"Relatório de uso ({args[0]})")

    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(275), args[1])
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(265), f"Nome do produto: {args[2]}")
    cnv.drawString(mm2p(14), mm2p(255), f"Número do produto: {args[3]}")
    cnv.drawString(mm2p(14), mm2p(245), f"Número de série: {args[4]}")
    
    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(235), "Mecanismo impr")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(230), f"Total de páginas impressas: {args[5]}")
    cnv.drawString(mm2p(14), mm2p(225), f"Total pág. impressas (frente/verso): {args[6]}")
    cnv.drawString(mm2p(14), mm2p(220), f"Total páginas impressas (modo econômico):{ args[7]}")
    cnv.drawString(mm2p(115), mm2p(230), f"Total de págs. do mecanismo*: {args[8]}")
    cnv.drawString(mm2p(115), mm2p(225), f"Total congest: {args[9]}")
    cnv.drawString(mm2p(115), mm2p(220), f"Total falhas coleta: {args[10]}")
    cnv.setFont('arial', 6)
    cnv.drawString(mm2p(14), mm2p(210), f"*A contagem total de páginas do mecanismo nunca é redefinida e representa o número total de páginas processadas pela impressora ao longo de sua vida útil.")
    
    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(190), "Imprimir")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(185), f"Tamanho mídia")
    cnv.drawString(mm2p(55), mm2p(185), f"Unids")
    cnv.drawString(mm2p(90), mm2p(185), f"Contagem Total de páginas")
    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(182), "_"*90)
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(175), f"ISO e JIS A4")
    cnv.drawString(mm2p(55), mm2p(175), f"1.0")
    cnv.drawString(mm2p(90), mm2p(175), f"{args[11]}")

    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(160), "Impressões equilaventes a A4")
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(90), mm2p(150), f"Contagem Total de páginas")
    cnv.setFont('Arial-Bold', 10)
    cnv.drawString(mm2p(14), mm2p(148), "_"*90)
    cnv.setFont('arial', 10)
    cnv.drawString(mm2p(14), mm2p(137), f"Imprimir")
    cnv.drawString(mm2p(90), mm2p(137), f"{args[12]}")

    cnv.save()
    shutil.move(args[-2], args[-1]+args[-2])


def mm2p(mm):
    return mm / 0.352777


def abrir_pasta(caminho_do_arquivo):
    if os.path.exists(caminho_do_arquivo):
        subprocess.run(f'explorer /select,"{os.path.abspath(caminho_do_arquivo)}"')
    else:
        print(f"Arquivo {caminho_do_arquivo} não encontrado")
