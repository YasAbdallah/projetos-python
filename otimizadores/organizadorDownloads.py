import os
from tkinter import filedialog, messagebox


if messagebox.askyesno("Deseja selecionar o diretorio. Criado por: Yasser Ibrahim.", "Para continuar selecione o diretorio a qual deseja organizar ou clique em cancelar para finalizar o script."):
    selectedFile = filedialog.askdirectory()
    files = os.scandir(selectedFile)

    for file in files:
        if "ini" not in file.name and '.' in file.name:
            if not os.path.exists(os.path.join(selectedFile, file.name[file.name.rfind('.')+1:])):
                os.mkdir(os.path.join(selectedFile, file.name[file.name.rfind('.')+1:]))
            try:
                os.rename(os.path.join(selectedFile, file.name), os.path.join(selectedFile, file.name[file.name.rfind('.')+1:], file.name))
            except FileExistsError as e:
                print(f'O arquivo {file.name} já existe na pasta. Ele será ignorado.')
input("Fim do script! Script Finalizado! Aperte qualquer tecla para sair")
