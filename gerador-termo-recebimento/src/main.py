import os
from lib.funcoes import *
from lib.prints import Print

printar = Print()

printar.print_colorido("*"*70, "\n", "Gerar Termo de recebimento de token.", "\n", "*"*70)

while True:
    nome = input("Digite o nome do Usuário: ")
    if verificarNumeroEmString(nome):
        printar.print_vermelho("Existe um Número no nome que você digitou. Tente Novamente.")
    else:
        break

while True:
    CPF = input("Digite o CPF do Usuário: ")
    if not validarCPF(CPF):
        printar.print_vermelho("CPF invalido. Tente Novamente.")
    else:
        break

while True:
    email = input("Digite o email do Usuário: ")
    if not verificarEmail(email):
        printar.print_vermelho("Email inválido, tente Novamente.")
    else:
        break

while True:
    printar.print_colorido("*"*70)
    printar.print_azul("Para pegar os dados do token siga os passos a seguir:")
    print("     1. Abra o aplicativo safeNet localizado na barra de tarefas. (Icone com um 'S' vermelho)")
    print("     2. Selecione o token no canto esquedo do programa.")
    print("     3. Clique no botão com um icone de lupa e escrito 'Visualizar informações do token' do lado direito do programa.")
    print("     4. Por fim clique em copiar na nova janela que abrir.")
    printar.print_colorido("*"*70)
    printar.print_verde("\nPara continuar, insira as informações que foram copiadas do token no arquivo de texto que irá aparecer na pasta agora!")
    printar.print_verde("Basta apagar todo o conteúdo que houver e colar os novos dados e salvar o arquivo.")
    
    abrir_pasta(caminho_do_arquivo=os.path.join(os.path.dirname(__file__), "..", "data", "data.txt"))

    if input("Para gerar o termo, Digite [\033[33mcontinuar\033[m] sem os colchetes.\n\nDigite Aqui: ").lower() == "continuar":
        break

criarTermoRecebimentoToken(nome=nome, cpf=CPF, email=email)
printar.print_amarelo("Finalizando...")
abrir_pasta(caminho_do_arquivo=os.path.join("C:\\", "Users", f"{os.getlogin()}", "Downloads", "Termo de recebimento de midia.pdf"))
printar.print_colorido("Até a próxima!!!!")