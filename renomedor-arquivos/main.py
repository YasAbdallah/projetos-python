import os
from tkinter import filedialog, messagebox, Tk


selectDirectory = ''
soma = 0

if messagebox.askyesno("Deseja selecionar o diretorio raiz. Criado por: Yasser Ibrahim.", "Para continuar selecione o diretorio raiz para verificação dos arquivos que deseja ser renomedo. Clique em cancelar para finalizar."):
    selectDirectory = filedialog.askdirectory()
    root = Tk()
    root.withdraw()
    root.after(4000, root.destroy)
    messagebox.showinfo("Fique tranquilo. Criado por: Yasser Ibrahim.", f"O script está executando, quando terminar te avisarei.", master=root)

    for root, dirs, files in os.walk(selectDirectory):
        for file in files:
            if 'Documentos Aduaneiros - Outros - ' in file:
                os.rename(os.path.join(root, file), os.path.join(root, f"{file[33:-15]}{file[-4:]}"))
                soma += 1

root = Tk()
root.withdraw()
root.after(5000, root.destroy)
messagebox.showinfo("Fim do script! Criado por: Yasser Ibrahim.", f"Script Finalizado! Foram renomeados {soma} arquivos. Até a próxima.", master=root)