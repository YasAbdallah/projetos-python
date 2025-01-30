import os
import sys
import ctypes
from lib.prints import Print
from lib.funcoes import limpar_tela, realizar_ping, main_verificar_conexoes
from src.impressoras_HP import gerar_relatorio_simples_todos, gerar_relatorio_multifuncional_todos, gerar_relatorio_hp_colorido


def escolher_tipo_relatorio_hp():
    caminhos = {
        "simples": os.path.join(os.path.dirname(__file__), "..", "data", "impressora_simples.json"),
        "multifuncional": os.path.join(os.path.dirname(__file__), "..", "data", "impressora_multifuncional.json"),
        "colorida": os.path.join(os.path.dirname(__file__), "..", "data", "impressora_colorida.json"),
    }
    main_verificar_conexoes(caminhos)
    while True:
        relatorio = input("""Como deseja gerar o relatório?
        [1] - Relatório impressoras Simples.
        [2] - Relatório impressoras Multifuncional.
        [3] - Relatório impressoras Colorida.
        [4] - Todos as opções acima.
        [Qualquer botão] - Sair.
        Digite o número da opção: """)
        if relatorio not in ("1", "2", "3", "4"):
            limpar_tela()
            break
        else:
            limpar_tela()
            return relatorio
    return None


def menu_relatorio_HP(opcao_relatorio):
    while True:
        relatorio = opcao_relatorio
        match relatorio:
            case "1":
                limpar_tela()
                printar.print_colorido("Iniciando relatório de impressoras HP Simples...")
                resultado = menu_secundario_hp()
                gerar_relatorio_hp_simples(resultado)
                return printar.print_verde("Relatório gerado com sucesso!")
            case "2":
                limpar_tela()
                printar.print_colorido("Iniciando relatório de impressoras HP Multifuncional...")
                resultado = menu_secundario_hp()
                gerar_relatorio_hp_multifuncional(resultado)
                return printar.print_verde("Relatório gerado com sucesso!")
            case "3":
                limpar_tela()
                printar.print_colorido("Iniciando relatório de impressoras HP Colorida...")
                gerar_relatorio_hp_colorido()
                return printar.print_verde("Relatório gerado com sucesso!")
            case "4":
                limpar_tela()
                printar.print_colorido("Gerando relatório de todas as impressoras...")
                gerar_relatorio_simples_todos()
                gerar_relatorio_multifuncional_todos()
                gerar_relatorio_hp_colorido()
                return printar.print_verde("Relatório gerado com sucesso!")
            case _:
                limpar_tela()
                printar.print_vermelho("Opção inválida. Tente Novamente.")
                break


def menu_secundario_hp():
    while True:
        relatorio = input("""Como deseja gerar o relatório?
        [1] - Relatório impressoras Unitario.
        [2] - Relatório impressoras Todos.
        [Qualquer botão] - Sair.
        Digite o número da opção: """)
        if relatorio not in ("1", "2"):
            limpar_tela()
            break
        else:
            limpar_tela()
            return relatorio
    return None
    

def gerar_relatorio_OKI(opcao_relatorio):
    while True:
        relatorio = opcao_relatorio
        try:
            from src.impressoras_OKI import gerarRelatorioOKI
            gerarRelatorioOKI()
            printar.print_verde("Relatório gerado com sucesso!")
            break
        except Exception as e:
            printar.print_vermelho("Erro ao gerar relatório. Tente Novamente.")
            break
    return printar.print_colorido("Fim do relatório, até a próxima!")


printar = Print()

# Apenas tente habilitar o modo de terminal ANSI se estivermos no Windows
if os.name == 'nt':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

printar.print_colorido("*" * 70, "\n", "Bem vindo ao gerador de relatório de impressora.", "\n", "*" * 70)
printar.print_azul("-" * 30, " Desenvolvido por: Yasser Ibrahim.", "\n \n")

tipo_impressora = None
while True:
    tipo_impressora = input("""Digite o tipo de impressora que deseja gerar o relatório? 
    [1] - Impressoras HP/Canon Colorida.
    [2] - Impressoras OKI.
    [3] - Sair.
    Digite o número da opção: """)

    limpar_tela()

    match tipo_impressora:
        case "1":
            opcao_relatorio = escolher_tipo_relatorio_hp()
            menu_relatorio_HP(opcao_relatorio)
            limpar_tela()
        case "2":
            from src.impressoras_OKI import gerarRelatorioOKI
            gerar_relatorio_OKI()
            limpar_tela()
        case "3":
            printar.print_colorido("Fim do programa, até a próxima!")
            break
        case _:
            printar.print_vermelho("Tipo de impressora inválida. Tente Novamente.")
