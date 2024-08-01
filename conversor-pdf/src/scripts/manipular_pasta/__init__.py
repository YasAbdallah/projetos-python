from pathlib import Path
import tkinter as tk
from tkinter import filedialog


def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()
    arquivo = filedialog.askopenfilename()
    return arquivo


def selecionar_caminho():
    root = tk.Tk()
    root.withdraw()
    caminho_arquivo = filedialog.askdirectory()
    return caminho_arquivo

def pegar_nome(diretorio):
    path = Path(diretorio)
    for x in (".pdf", '.doc', '.docx', ".xls", "xlsx"):
        if x in path.name:
            nome = str(path.name).replace(x, '')
    return nome

def pegar_extencao(diretorio):
    path = Path(diretorio)
    for x in (".pdf", '.doc', '.docx', ".xls", "xlsx"):
        if x in path.name:
            str(path.name).replace(path.name, '')
    return str(path)