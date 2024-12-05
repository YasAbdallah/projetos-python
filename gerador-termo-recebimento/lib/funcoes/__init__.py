import os
import re
import shutil
import subprocess

import pymsgbox
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


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


def criarTermoRecebimentoToken(**kwargs):
    args = [value for key, value in kwargs.items()]
    dadosToken = [dados for dados in capturarDadosToken()]
    cnv = canvas.Canvas("Termo de recebimento de midia.pdf", pagesize=A4)

    pdfmetrics.registerFont(TTFont('Liberation Serif', 'LiberationSerif-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Liberation Serif Bold', 'LiberationSerif-Bold.ttf'))

    cnv.setFont('Liberation Serif Bold', 14)
    cnv.rect(x=mm2p(20), y=mm2p(280), width=483, height=20, stroke=1, fill=0)
    cnv.drawString(mm2p(21), mm2p(281), f"TERMO DE RECEBIMENTO DE MÍDIA PARA CERTIFICAÇÃO DIGITAL")

    cnv.setFont('Liberation Serif', 14)
    cnv.drawString(mm2p(38), mm2p(271), f"Nome do Funcionário: {args[0]}")
    cnv.drawString(mm2p(38), mm2p(264), f"CPF: {args[1]}")
    cnv.drawString(mm2p(38), mm2p(257), f"E-mail RFB: {args[2]}")
    cnv.drawString(mm2p(38), mm2p(250), f"Nº do Token: {dadosToken[3][16:]}")

    cnv.setFont('Liberation Serif Bold', 14)
    cnv.drawString(mm2p(18), mm2p(240), "DECLARO: ")
    cnv.setFont('Liberation Serif', 12)
    cnv.drawString(mm2p(22), mm2p(234), "1.  Ter recebido o token conforme informado abaixo onde será armazenado meu certificado")
    cnv.drawString(mm2p(28), mm2p(228), "digital e-CPF – e o manual do usuário.")
    cnv.drawString(mm2p(22), mm2p(222), "2.  Estar ciente da obrigatoriedade de efetivar a troca da senha (PIN) do token antes de efetuar a")
    cnv.drawString(mm2p(28), mm2p(216), "solicitação de emissão do certificado digital e-CPF. ")
    cnv.drawString(mm2p(22), mm2p(210), "3.  Estar ciente que em caso de desligamento da Receita Federal devo adotar as providências ")
    cnv.drawString(mm2p(28), mm2p(204), "necessárias à revogação do certificado digital e-CPF armazenado no token e devolver, ao ")
    cnv.drawString(mm2p(28), mm2p(198), "setor responsável o material recebido.")
    cnv.drawString(mm2p(22), mm2p(192), "4.  Estar ciente das disposições de segurança e de responsabilidade constantes do token")
    cnv.drawString(mm2p(28), mm2p(186), "recebido, devendo zelar pela sua guarda e integridade. Em caso de perda ou roubo informar")
    cnv.drawString(mm2p(28), mm2p(180), "imediatamente o setor responsável por meio de declaração escrita e assinada informando o ")
    cnv.drawString(mm2p(28), mm2p(174), "ocorrido.")


    cnv.setFont('Liberation Serif', 12)
    cnv.rect(x=mm2p(18), y=mm2p(26), width=483, height=400, stroke=1, fill=0)
    espacamento_entrelinhas = 162
    for dados in dadosToken:
        if "Nome do Token" in dados:
            cnv.drawString(mm2p(19), mm2p(espacamento_entrelinhas), f"{dados[0:14]} {args[0]}")
        else:
            cnv.drawString(mm2p(19), mm2p(espacamento_entrelinhas), f"{dados}")
        espacamento_entrelinhas -= 6
    
    cnv.drawString(mm2p(19), mm2p(16), "_____/_____/_____       ________________________")

    cnv.drawString(mm2p(19), mm2p(10), "Data"+ " "*32 + "Assinatura")
    cnv.save()
    shutil.move("Termo de recebimento de midia.pdf", f"C:\\Users\\{os.getlogin()}\\Downloads\\Termo de recebimento de midia.pdf")


def mm2p(mm):
    return mm / 0.352777


def capturarDadosToken():
    array = []
    with open(os.path.join(os.path.dirname(__file__), "..", "..", "data", "data.txt"), encoding="utf-8") as info:
        linhas = info.readlines()
        for linha in linhas:
           array.append(str(linha).encode("latin1").decode("utf-8").removesuffix("\n"))

    return array


def abrir_pasta(caminho_do_arquivo):
    if os.path.exists(caminho_do_arquivo):
        subprocess.run(f'explorer /select,"{os.path.abspath(caminho_do_arquivo)}"')
    else:
        print(f"Arquivo {caminho_do_arquivo} não encontrado")


def verificarNumeroEmString(string):
    return any(char.isdigit() for char in string)


def validarCPF(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join([char for char in cpf if char.isdigit()])

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        print("menos ou mais de 11")
        return False

    # Verifica se todos os dígitos são iguais, o que é um CPF inválido
    if cpf == cpf[0] * 11:
        print("Os numeros são iguais")
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    digito1 = digito1 if digito1 < 10 else 0

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    digito2 = digito2 if digito2 < 10 else 0

    # Verifica se os dígitos verificadores calculados correspondem aos do CPF fornecido
    return cpf[-2:] == f"{digito1}{digito2}"


def verificarEmail(email):

    # Expressão regular para validar o formato do email
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Verifica se o email corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False
    

def abrir_pasta(caminho_do_arquivo):
    if os.path.exists(caminho_do_arquivo):
        subprocess.run(f'explorer /select,"{os.path.abspath(caminho_do_arquivo)}"')
    else:
        print(f"Arquivo {caminho_do_arquivo} não encontrado")
