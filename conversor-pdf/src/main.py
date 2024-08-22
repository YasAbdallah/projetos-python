from lib.prints import Print
from lib.conversor import Conversor

texto = Print()

texto.print_colorido("-"*99, "\n",">"*38, " Conversor de arquivos ", "<"*38, "\n", "-"*99)
print((" "*62), "Desenvolvido por: Yasser Ibrahim.")
texto.print_colorido("-"*99, "\n"*3)
while True:
    print("""
    Selecione uma das opções: 
    |    ---------------------------------------------------------------------------------------------    |   
    |    Digite [1] para - DOC|DOCX -> PDF.                                                               |
    |            *Esta opção converte documentos word com terninação .doc e .docx para arquivos .pdf.     |
    |    ---------------------------------------------------------------------------------------------    |
    |    Digite [2] para - XLS|XLSX -> PDF.                                                               |
    |            *Esta opção converte planilhas com terninação .xls e .xlsx para .pdf.                    |
    |    ---------------------------------------------------------------------------------------------    |
    |    Digite [3] para - PDF -> DOC|DOCX.                                                               |
    |            *Esta opção converte arquivos PDF para documentos word com terminação .doc e .docx.      |
    |    ---------------------------------------------------------------------------------------------    |
    |    Digite [4] para - PDF -> XLS|XLSX.                                                               |
    |            *Esta opção converte arquivos PDF para planilhas com terminação .xls e .xlsx.            |
    |    ---------------------------------------------------------------------------------------------    |
    |    Digite [5] para - PDF -> CSV.                                                                    |
    |            *Esta opção converte arquivos PDF para planilhas com terminação CSV.                     |
    |    ---------------------------------------------------------------------------------------------    |
    |    Digite [6] para - Desbloquear PDF(Para impressão).                                               |
    |    ---------------------------------------------------------------------------------------------    |
    |    Digite [0] para - Finalizar o programa.                                                          |
    |    ---------------------------------------------------------------------------------------------    |
    """)
    match input("Digite aqui o que deseja fazer [1 - 4]: "):
        case '1':
            conversor = Conversor()
            conversor.any_para_pdf()
        case '2':
            conversor = Conversor()
            conversor.any_para_pdf()
        case '3':
            conversor = Conversor()
            conversor.pdf_para_word()
        case '4':
            conversor = Conversor()
            conversor.pdf_para_xlsx()
        case '5':
            conversor = Conversor()
            conversor.pdf_para_csv()
        case '6':
            conversor = Conversor()
            conversor.desbloquear_pdf()
        case '0':
            break
        case _:
            texto.print_vermelho("Digite uma opção valida.")

texto.print_azul("Finalizando o programa! Até a próxima")

"""

selecao_arquivo = [
    [sg.Text("Selecione o arquivo que deseja converter:", background_color="#000", font=("Times new roman", 14))],
    [sg.Input("", size=(50, 20), disabled=True), sg.FileBrowse("Selecionar")],
]
selecao_convercao = [
    [sg.Text("Converter em:", background_color="#000", font=("Times new roman", 14))],
    [sg.Combo(['pdf -> xlsx', 'pdf -> doc', 'pdf -> docx', 'doc -> pdf', 'xlsx -> pdf', 'Desbloquear PDF'], default_value='Escolha uma opção', size=(25, 15), key="-SELECIONAR_CONVERSOR-")]
]
layout = [
    [
        sg.Frame(
            title="",
            layout=[
                [sg.Column(selecao_arquivo, background_color="#000"),
                sg.Column(selecao_convercao, background_color="#000", pad=((50,0),(0,0)))],
                [
                    sg.Text("Onde deseja salvar o arquivo convertido:"),
                    sg.Input("", disabled=True), sg.FolderBrowse("Buscar")]
            ],
            background_color="#000", vertical_alignment='center')
    ],
    [
        sg.Frame(
            title="",
            layout=[
                [
                    sg.Text(key="-OUTPUT-")
                ]
            ],
            size=(500,500),
            background_color="#000"
        )
    ],
    [sg.Button("Converter"), sg.Button("Limpar"), sg.Button("Sair")]
]

sg.theme('Black')
window = sg.Window("Conversor de arquivos. Desenvolvido por: Yasser Ibrahim.", layout, resizable=True, size=(1024, 768))

while True:
    event, value = window.read()
    print(value)
    if event in (sg.WIN_CLOSED, "Sair"):
        break
    if event == "converter":
        nome_arquivo = pegar_nome_arquivo(value['Buscar'])
        match value['-SELECIONAR_ARQUIVO-']:
            case 'pdf -> xlsx':
                converter_pdf_para_planilha(value['Buscar'], value['Selecionar'], nome_arquivo)
            case 'pdf -> doc':
                converter_pdf_para_doc(value['Buscar'], value['Selecionar'], nome_arquivo)
            case 'pdf -> docx':
                converter_pdf_para_doc(value['Buscar'], value['Selecionar'], nome_arquivo)
            case 'doc -> pdf':
                converter_para_pdf(value['Buscar'], value['Selecionar'], nome_arquivo)
            case 'xlsx -> pdf':
                converter_para_pdf(value['Buscar'], value['Selecionar'], nome_arquivo)
            case 'Desbloquear PDF':
                desbloquear_pdf(value['Buscar'], value['Selecionar'], nome_arquivo)
            case _:
                window["-OUTPUT-"].update("Selecione um tipo de arquivo para conversão.")
    if event == "Limpar":
        window['-CAMINHO_ARQUIVO-'].update('')
window.close()"""