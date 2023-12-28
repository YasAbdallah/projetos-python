from random import choice, randrange


def gerarsenha(qntSenhas, qntCaracter, complexidade):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    especial = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+', '\\', '|', '/', ',', '<', '.', '>', ';', ':', '[', ']', '{', '}']
    caracteres = [letras, [letra.upper() for letra in letras], num, especial]
    for i in range(qntSenhas):
        senha = ''
        x = 0
        for x in range(qntCaracter):
            senha += str(choice(caracteres[randrange(0, complexidade + 1)])) 
        print(f"{i + 1}ª) {senha}\n")

def printColorido(palavras):
    frase = ''
    for letra in palavras:
        frase += f"\033[0;3{randrange(1, 4)}m{letra}\033[m"
    print(frase)

printColorido(('***'*20))
printColorido('    ' + '*-_*_-'*2 + '  Bem-vindo ao gerador de senhas  ' + '*-_*_-'*2 + '    ')
printColorido(('***'*20))
while True:
    qntCaracter = int(input("Quantos caracteres a senha deve ter?\nDigite aqui: "))
    printColorido('---'*20)
    qntSenhas = int(input(f"Quantas senhas de {qntCaracter} caracteres deseja gerar?\nDigite aqui: "))
    printColorido('---'*20)

    while True:
        print("-"*10 + "  Nivel de complexidade da senha  " + "-"*10)
        complexidade = int(input("\nQual nivel de complexidade da sua senha?\n1 - Apenas letras. Ex: AbCDe\n2 - Letras e números. Ex: A1b2C3\n3 - Letras, números e caracteres especiais. Ex: A!1b@2C#.3\n\nDigite aqui: "))
        
        match complexidade:
            case 1:
                printColorido("---"*20)
                gerarsenha(qntSenhas, qntCaracter, complexidade)
                break
            case 2:
                printColorido("---"*20)
                gerarsenha(qntSenhas, qntCaracter, complexidade)
                break
            case 3:
                printColorido("---"*20)
                gerarsenha(qntSenhas, qntCaracter, complexidade)
                break
            case _:
                printColorido("---"*20)
                print("\n\nNivel de complexidade invalida... Tente novamente.")
                printColorido("---"*20)
    if 'n' in str(input('Deseja gerar novas senhas? [S - Para continuar/ N - Para sair]')).lower():
        break
    printColorido('---'*20)

print("\nLembre-se de salvar a(s) senha(s) em um lugar seguro.")
print("\nFim!")
