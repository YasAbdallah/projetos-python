from moviepy.editor import AudioFileClip
from tkinter import filedialog, messagebox
import os

def conversor(caminho, remover):
    try:
        video = AudioFileClip(caminho)
        video.write_audiofile(caminho[:caminho.rfind(".")+1]+"mp3")
        video.close()

        os.remove(caminho) if remover == True else False
    except:
        print("Houve um erro.")
    else:
        print("Convertido com sucesso!")

def pesquisa(caminho):
    files = os.scandir(caminho)
    deletar = False
    if messagebox.showinfo(title='Deletar os arquivos?', message="Deseja deletar os arquivos Originais?"):
        deletar = True
    for file in files:
        match file.name[file.name.rfind(".")+1:]:
            case "mp4":
                conversor(os.path.join(caminho, file.name), deletar)
            case "webm":
                conversor(os.path.join(caminho, file.name), deletar)
            case "wav":
                conversor(os.path.join(caminho, file.name), deletar)
            case "wma":
                conversor(os.path.join(caminho, file.name), deletar)
            case "avi":
                conversor(os.path.join(caminho, file.name), deletar)
            case _:
                pass

print("""
O conversor só converte audio com as extensões:
      
1 - .mp4
2 - .webm
3 - .wav
4 - .wma
5 - .avi
""")
input("\nAperte qualquer tecla para continuar.")

caminho = filedialog.askdirectory(title="Onde deseja Salvar?")

pesquisa(caminho)
