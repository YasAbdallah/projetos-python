import moviepy.editor as mp
import speech_recognition as sr
import sys, os
from pydub import AudioSegment


def conversor(caminho, remover = True):
    try:
        video = mp.AudioFileClip(caminho)
        video.write_audiofile(caminho[:caminho.rfind(".")+1]+"wav")
        video.close()
        os.remove(caminho) if remover == True else False
    except Exception as e:
        print("Houve um erro ao converter ou o arquivo não existe.")
    else:
        return caminho[:caminho.rfind(".")+1]+"wav"


try:
    path = os.path.join(os.getcwd(), 'textoEmFalaEFalaEmTexto\\audio\\frase.mp3')
    path2 = conversor(path)
    file_audio = sr.AudioFile(path2)
    r = sr.Recognizer()
    with file_audio as source:
        audio_text = r.record(source)
        text = r.recognize_google(audio_text, language='pt-br')
        
        arq = open(os.path.join(os.getcwd(), 'textoEmFalaEFalaEmTexto\\texto\\texto.txt'), 'w')
        arq.write(text)
        arq.close()
        print(text)
        os.remove(path2)
except Exception as e:
    print(e)