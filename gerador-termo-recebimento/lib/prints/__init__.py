from random import randrange


class Print():
    def __init__(self) -> None:
        self.__frase = ""

    def print_colorido(self, *args):
        for texto in args:
            for letra in texto:
                self.__frase += f"\033[0;3{randrange(1, 4)}m{letra}\033[m"
        print(self.__frase)
        self.__frase = ""

    def print_vermelho(self, *args):
        for texto in args:
            for letra in texto:
                self.__frase += f"\033[31m{letra}\033[m"
        print(self.__frase)
        self.__frase = ""

    def print_preto(self, *args):
        for texto in args:
            for letra in texto:
                self.__frase += f"\033[30m{letra}\033[m"
        print(self.__frase)
        self.__frase = ""

    def print_verde(self, *args):
        for texto in args:
            for letra in texto:
                self.__frase += f"\033[32m{letra}\033[m"
        print(self.__frase)
        self.__frase = ""

    def print_amarelo(self, *args):
        for texto in args:
            for letra in texto:
                self.__frase += f"\033[33m{letra}\033[m"
        print(self.__frase)
        self.__frase = ""

    def print_azul(self, *args):
        for texto in args:
            for letra in texto:
                self.__frase += f"\033[34m{letra}\033[m"
        print(self.__frase)
        self.__frase = ""

    def print_magenta(self, *args):
        for texto in args:
            for letra in texto:
                self.__frase += f"\033[35m{letra}\033[m"
        print(self.__frase)
        self.__frase = ""

    def print_ciano(self, *args):
        for texto in args:
            for letra in texto:
                self.__frase += f"\033[36m{letra}\033[m"
        print(self.__frase)
        self.__frase = ""
