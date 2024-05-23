from pytube import YouTube, Playlist
from random import randrange
from tkinter import filedialog
from time import sleep
from moviepy.editor import AudioFileClip
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError, URLError


def printColorido(palavras):
    frase = ''
    for letra in palavras:
        frase += f"\033[0;3{randrange(1, 4)}m{letra}\033[m"
    print(frase)

def conversor(caminho):
    files = os.scandir(caminho)
    for file in files:
        if ".mp4" in file.name or ".webm" in file.name:
            try:
                print(f"Convertendo {file.name} para mp3")
                video = AudioFileClip(os.path.join(caminho, file.name))
                video.write_audiofile(os.path.join(caminho, f'{file.name[:file.name.rfind(".")+1]}mp3'))
                video.close()
            except Exception as e:
                print(e)
            else:
                print(file.name)
                os.remove(os.path.join(caminho, file.name))
                print("Arquivo convertido com Sucesso!")

def resolucao():
    while True:
        printColorido("*"*60)
        print("""
        Selecione a resolução:
            
        Digite [1] Para -  144p.
        Digite [2] Para -  360p.
        Digite [3] Para -  720p.
        Digite [4] Para -  1080p.\n""")
        resolucao = int(input("Digite Aqui: "))

        match resolucao:
            case 1:
                return "144p"
            case 2:
                return "360p"
            case 3:
                return "720p"
            case 4:
                return "1080p"
            case _:
                print("Valor invalido. Tente novamente.")

def qualidadeAudio():
    while True:
        printColorido("*"*60)
        print("""
        Selecione a qualidade do áudio:
            
        Digite [1] Para -  48kbps.
        Digite [2] Para -  50kbps.
        Digite [3] Para -  70kbps.
        Digite [4] Para -  128kbps.
        Digite [5] Para -  160kbps.\n""")
        audio = int(input("Digite Aqui: "))

        match audio:
            case 1:
                return "48kbps"
            case 2:
                return "50kbps"
            case 3:
                return "70kbps"
            case 4:
                return "128kbps"
            case 5:
                return "160kbps"
            case _:
                print("Valor invalido. Tente novamente.")

printColorido(('***'*20))
print('    ' + '*-_*_-'*2 + '  Bem-vindo ao Downloader  ' + '*-_*_-'*2 + '    ')
print("Criado Por: Yasser Ibrahim Abdallah Vaz Condoluci!")
printColorido(('***'*20))
print("\n\nAtenção! Para efetuar o download de uma playlist, certifique-se que o link é de uma playlist mesmo.")
print("Para ter certeza que é uma playlist siga os passos a seguir:")
print('''
1 - Em sua playlist clique nos três pontos acima da lista de vídeos e clique em "GUARDAR PLAYLIST NA BIBLIOTECA".
2 - Ao lado da logo do Youtube, clique no icone com três barras e depois em "mostrar mais".
3 - Quando clicar em "Mostrar mais" aparecerá uma lista das playslist salvas, procure a playlist desejada e copie o link dela.
''')
while True:
    print('\n\n\n')
    link = str(input('Copie o link do video ou ta playlist que deseja baixar aqui: '))
    print('\n\n')

    while True:
        printColorido('*'*60)
        opcoes = int(input('Deseja baixar o video ou audio?\n Digite [1] Para Vídeo | [2] para áudio: '))
        print('\n\n')
        match opcoes:
            case 1:
                res = resolucao()
                break
            case 2:
                som = qualidadeAudio()
                break
            case _:
                print("Valor invalido. Tente Novamente.")


    caminho = filedialog.askdirectory(title="Onde deseja Salvar?")

    if 'playlist' in link:
        playlist = Playlist(link)
        for video in playlist.videos:
            try:
                print(f"Baixando {video.title}")
                video.streams.filter(file_extension='mp4', res=res).first().download(output_path=caminho) if opcoes == 1 else  video.streams.filter(only_audio=True, abr=som).first().download(output_path=caminho)
            except:
                print(f"Ocorreu um erro ao baixar o {'video' if opcoes == 1 else 'áudio'}.")
            else:
                printColorido("*"*60)
                print(f"Download do {'video' if opcoes == 1 else 'áudio'} efetuado com sucesso!")
                conversor(caminho) if opcoes == 2 else ''
    elif 'list' in link:
        try:
            html = urlopen(link)
            bs = BeautifulSoup(html.read(), 'html.parser')

            for child in bs.find_all('ytd-playlist-panel-video-renderer', {'id': 'playlist-items'}):
                print(child.attrs['href'])
        except Exception as e:
            print(e)
    else:
        unico = YouTube(link)
        try:
            print(f"Baixando {unico.title}")
            unico.streams.filter(file_extension='mp4', res=res).first().download(output_path=caminho) if opcoes == 1 else  unico.streams.filter(only_audio=True, abr=som).first().download(output_path=caminho)
        except:
            print(f"Ocorreu um erro ao baixar o {'video' if opcoes == 1 else 'áudio'}.")
        else:
            printColorido("*"*60)
            print(f"Download do {'video' if opcoes == 1 else 'áudio'} efetuado com sucesso!")
            conversor(caminho) if opcoes == 2 else ''
    
    continuar = input('Deseja Baixar mais alguma coisa? [s - Para continuar | n - Para sair]')
    if 's' in continuar:
        continue
    else:
        printColorido("*"*60)
        print("\n\nFim!")
        input("Aperte ENTER para finalizar.")
        break