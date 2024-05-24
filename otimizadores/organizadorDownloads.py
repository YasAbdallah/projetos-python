import os
from tkinter import filedialog, messagebox


if messagebox.askyesno("Deseja selecionar o diretorio. Criado por: Yasser Ibrahim.", "Para continuar selecione o diretorio a qual deseja organizar ou clique em cancelar para finalizar o script."):
    pasta_selecionada = filedialog.askdirectory()
    arquivos = os.scandir(pasta_selecionada)

    for arquivo in arquivos:
        if "ini" not in arquivo.name and '.' in arquivo.name:
            if not os.path.exists(os.path.join(pasta_selecionada, arquivo.name[arquivo.name.rfind('.')+1:])):
                os.mkdir(os.path.join(pasta_selecionada, arquivo.name[arquivo.name.rfind('.')+1:]))
            try:
                os.rename(os.path.join(pasta_selecionada, arquivo.name), os.path.join(pasta_selecionada, arquivo.name[arquivo.name.rfind('.')+1:], arquivo.name))
            except FileExistsError as e:
                print(f'O arquivo {arquivo.name} já existe na pasta. Revise o arquivo.')
input("Fim do script! Script Finalizado! Aperte qualquer tecla para sair")
