import pymsgbox
from random import randint

def mensagem(msg, titulo = "", tempo = 3000):
    """

    :param msg: Deve ser Digitado a mensagem que vai no corpo do popup.
    :param titulo: Pode ser Digitado uma mensagem no título do popup.
    :param tempo: Pode ser informa o tempo que o popup vai ficar na tela. Por padrão são 3 segundos ou 3000 milésimos.
    :return: Retorna popup na tela do usuário com a mensagem.
    """
    dev  = " Desenvolvido por: Yasser Ibrahim."
    return pymsgbox.alert(text=msg, title=titulo + dev, timeout=tempo)


def confirmar(msg, titulo = "",):
    """

    :param msg: Deve ser Digitado a mensagem que vai no corpo do popup.
    :param titulo: Pode ser Digitado uma mensagem no título do popup.
    :return: Retorna popup na tela do usuário com a mensagem.
    """
    dev  = " Desenvolvido por: Yasser Ibrahim."
    return pymsgbox.confirm(text=msg, title=titulo + dev)

def palavraAleatoria():
    """
    
    :return: Retona uma palavra aleatória do dicionario que conteina mais que 5 letras.
    """
    linhas = []
    with open('../data/palavras.txt', encoding="utf8") as file:
        linhas.append(file.readlines())

    if len(linhas[0][randint(0, len(linhas[0])-1)]) < 5:
        palavraAleatoria()
    else:
        return linhas[0][randint(0, len(linhas[0])-1)]