import gtts
from playsound import playsound
from time import sleep
import os

texto = """Insira seu texto aqui"""

caminho = os.path.join(os.getcwd(), 'textoEmFalaEFalaEmTexto\\audio\\frase.mp3')
try:
    frase = gtts.gTTS(texto, lang="pt-br")
    frase.save(caminho)
    playsound(caminho)
except Exception as e:
    print(e)
print("Feito!!!")