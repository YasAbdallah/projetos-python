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
    pasta_audio = os.path.join(os.getcwd(), 'audio\\frase.mp3')
    converter_arquivo_audio = conversor(pasta_audio)
    arquivo_audio = sr.AudioFile(converter_arquivo_audio)
    recognizer = sr.Recognizer()
    with arquivo_audio as source:
        audio_texto = recognizer.record(source)
        texto = recognizer.recognize_google(audio_texto, language='pt-br')
        
        with open(os.path.join(os.getcwd(), 'texto\\texto.txt'), 'w') as arquivo:
            arquivo.write(texto)
        os.remove(converter_arquivo_audio)
except Exception as e:
    print(e)