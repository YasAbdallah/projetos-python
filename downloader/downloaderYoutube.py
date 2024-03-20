from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip
import os
from time import sleep
import datetime
import PySimpleGUI as sg


def conversor(caminho):
    files = os.scandir(caminho)
    for file in files:
        if ".mp4" in file.name or ".webm" in file.name:
            try:
                with AudioFileClip(os.path.join(caminho, file.name)) as converter:
                    window['-EVENTS-'].update(f"Convertendo áudio para mp3")
                    window.refresh()
                    converter.write_audiofile(os.path.join(caminho, f'{file.name[:file.name.rfind(".")+1]}mp3'), logger=None)
            except Exception as e:
                sg.PopupError("Ocorreu um erro ao tentar converter o áudio: ", e)
            else:
                window['-EVENTS-'].update(f"Conversão concluida.")
                window.refresh()
                sleep(1)
                os.remove(os.path.join(caminho, file.name))

def infoVideo(objVideo):
    window['-TITULO-'].update(f"Título: {objVideo.title}")
    window['-VISUALIZACAO-'].update(f"Views: {objVideo.views}")
    window['-DURACAO-'].update(f"Duração do Vídeo: {str(datetime.timedelta(seconds=objVideo.length))}")
    window.refresh()

def downloadPlaylist(objVideo, qualidade, audioOrVideo=0):
    """
    :param objVideo: variavel com as informações do link para download
    :param qualidade: Qualidade do Áudio ou do Vídeo que deve ser feito o download.
    :param audioOrVideo: Definido com o padrão 0 para vídeo, no caso que querer música é 1.
    """
    for video in objVideo.videos:
        try:
            window['-EVENTS-'].update(f"Iniciando Download.")
            window.refresh()
            if audioOrVideo == 1:
                objVideo.streams.filter(only_audio=True, abr=qualidade).first().download(output_path=window['-GETPATH-'].get())
                conversor(window['-GETPATH-'].get())
            else:
                objVideo.streams.filter(file_extension='mp4', res=qualidade).first().download(output_path=window['-GETPATH-'].get())
        except Exception as e:
            sg.Popup(f"Ocorreu um erro ao tentar baixar a playlist.")
        else:
            window['-EVENTS-'].update(f"Download da playlist efetuada com sucesso!")
            window.refresh()

def downloadUnico(objVideo, qualidade, audioOrVideo=0):
    """
    :param objVideo: variavel com as informações do link para download
    :param qualidade: Qualidade do Áudio ou do Vídeo que deve ser feito o download.
    :param audioOrVideo: Definido com o padrão 0 para vídeo, no caso que querer música é 1.
    """
    try:
        window['-EVENTS-'].update(f"Iniciando Download.")
        window.refresh()
        if audioOrVideo == 1:
            window['-EVENTS-'].update(f"Fazendo Download.")
            window.refresh()
            objVideo.streams.filter(only_audio=True, abr=qualidade).first().download(output_path=window['-GETPATH-'].get())
            conversor(window['-GETPATH-'].get())
        else:
            objVideo.streams.filter(file_extension='mp4', res=qualidade).first().download(output_path=window['-GETPATH-'].get())
    except Exception as e:
        sg.PopupError("Ocorreu um erro ao tentar baixar o arquivo. Tente alterar a resolução do vídeo ou a qualidade do áudio.")
    else:
        window['-EVENTS-'].update(f"Download Concluido")
        window['-FIM-'].update(visible=True)
        window.refresh()

# Escolha da cor do tema
sg.theme("DarkBlue14")
# Desenhando o layout do app
cabecalho = [
    [
        sg.Text("Insira a URL: "), sg.Input(key='-URLVIDEO-', size=(80, 1), do_not_clear=True),
        sg.Frame('',
            [
                [
                    sg.Image(
                        source=("./img/baixar.png"),
                        key="-DOWNLOAD-",
                        size=(32,32),
                        enable_events=True,
                        
                    ),
                ]
            ],
        ),
        
    ],
    [sg.HorizontalSeparator(),],
]
corpo = [
    [
        sg.Frame("",
            [
                [
                    # Coluna de seleção de qualidade de video ou audio.
                    sg.Column(justification="top", layout=[
                        [
                            sg.Radio("Video", "typeDown", default=True, key="cbox_video", enable_events=True), 
                            sg.Radio("Áudio", "typeDown", default=False, key="cbox_audio", enable_events=True)
                        ],
                        [
                            sg.Column([
                                [
                                    # Qualidade de video
                                    sg.Frame(
                                        "Qualidades do Video: ",
                                        [
                                            [sg.Radio('240p', 'r_vQuality', default=False, key="240p", enable_events=True)],
                                            [sg.Radio('360p', 'r_vQuality', default=False, key="360p", enable_events=True)],
                                            [sg.Radio('480p', 'r_vQuality', default=False, key="480p", enable_events=True)],
                                            [sg.Radio('720p', 'r_vQuality', default=False, key="720p", enable_events=True)],
                                            [sg.Radio('1080p', 'r_vQuality', default=False, key="1080p", enable_events=True)]
                                        ],
                                        key="-FRAMEVIDEO-",
                                        visible=True
                                    ),
                                    # Qualidade de audio
                                    sg.Frame(
                                        "Qualidades do Áudio: ",
                                        [
                                            [sg.Radio('48kbps', 'r_aQuality', default=False, key="48kbps", enable_events=True)],
                                            [sg.Radio('50kbps', 'r_aQuality', default=False, key="50kbps", enable_events=True)],
                                            [sg.Radio('70kbps', 'r_aQuality', default=False, key="70kbps", enable_events=True)],
                                            [sg.Radio('128kbps', 'r_aQuality', default=False, key="128kbps", enable_events=True)],
                                            [sg.Radio('160kbps', 'r_aQuality', default=False, key="160kbps", enable_events=True)],
                                        ],
                                        key="-FRAMEAUDIO-",
                                        visible=False
                                    )
                                ],
                            ])
                        ],
                    ]),
                    # Separando os blocos
                    sg.VerticalSeparator(),
                    #Futuro visualizados do video
                    #Caminho para salvar arquivo
                    sg.Column([
                        [
                            sg.Column([
                                [
                                    sg.Frame(
                                        "Informações",
                                        [
                                            [sg.Text("Título: ", enable_events=True, key="-TITULO-")],
                                            [sg.Text("Visualizações: ", enable_events=True, key="-VISUALIZACAO-")],
                                            [sg.Text("Duração do Vídeo: ", enable_events=True, key="-DURACAO-")],
                                            [],
                                            [],
                                            [sg.Text("", enable_events=True, key="-EVENTS-",font=("Arial", 16)), 
                                            sg.Image(source=("./img/certo.png"), key="-FIM-", size=(32,32), enable_events=True, visible=False)],
                                        ]
                                    )
                                ],
                            ]),
                        ],
                        [sg.HorizontalSeparator()],
                        [
                            sg.Text("Onde Deseja Salvar o arquivo: ", pad=((0,0),(0,0))),
                        ],
                        [
                            sg.Input(key="-GETPATH-", enable_events=True, pad=((0,0),(0,0))), sg.FolderBrowse(button_text="Procurar", key="-GETFOLDER-")
                        ],
                    ])
                ]
            ],
            element_justification="center"
        ),
    ],
]
rodape = [
    [
        sg.Text("Desenvolvido por:", font=("Franklin Gotic", 12), pad=((450, 0), (100, 0))),
        sg.Text("Yasser Ibrahim.", font=("Freestyle Script", 16), pad=((0, 0), (100, 0))),
    ],
]
layout = [
    [cabecalho],
    [corpo],
    [rodape]
]

window = sg.Window("Downloader de videos do Youtube", layout=layout, margins=(3, 3), size=(750, 430), element_justification="center")
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'cbox_video':
        window['-FRAMEVIDEO-'].update(visible=True)
        window['-FRAMEAUDIO-'].update(visible=False)

    if event == 'cbox_audio':
        window['-FRAMEAUDIO-'].update(visible=True)
        window['-FRAMEVIDEO-'].update(visible=False)

    if event == "-GETFOLDER-":
        window['-GETPATH-'].update(values=values['-GETFOLDER-'])


    if window['-URLVIDEO-'].get() != '':
        infoVideo(YouTube(window['-URLVIDEO-'].get()))
    elif window['-URLVIDEO-'].get() == '':
        window['-TITULO-'].update("Título: ")
        window['-VISUALIZACAO-'].update("Visualizações: ")
        window['-DURACAO-'].update("Duração do Vídeo: ")

    # Pegando qualidade de vídeo
    if event == "240p" or event == "360p" or event == "480p" or event == "720p" or event == "1080p":
        tipoDownload = '-cbox_video-'
        qualidade = event

    # Pegando qualidade de áudio
    if event == "48kbps" or event == "50kbps" or event == "70kbps" or event == "128kbps" or event == "160kbps":
        tipoDownload = '-cbox_audio-'
        qualidade = event

    #Botão de para fazer Download
    if event == '-DOWNLOAD-':
        if window['-URLVIDEO-'].get() == '':
            sg.Popup("Link do vídeo está vazia. Preencha para continuar.")
        elif window['-GETPATH-'].get() == '':
            sg.Popup("Você não escolheu onde deseja salvar. Escolha uma pasta para continuar.")
        else:
            if tipoDownload == '-cbox_video-':
                if 'playlist' in window['-URLVIDEO-'].get():
                    downloadPlaylist(Playlist(window['-URLVIDEO-'].get()), qualidade)
                else:
                    downloadUnico(YouTube(window['-URLVIDEO-'].get()), qualidade)
            
            if tipoDownload == '-cbox_audio-':
                if 'playlist' in window['-URLVIDEO-'].get():
                    downloadPlaylist(Playlist(window['-URLVIDEO-'].get()), qualidade, 1)
                else:
                    downloadUnico(YouTube(window['-URLVIDEO-'].get()), qualidade, 1)
window.close()