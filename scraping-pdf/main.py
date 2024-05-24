from PyPDF2 import PdfReader
import openpyxl
from tkinter import filedialog


pasta = filedialog.askopenfilename(title="Onde está salvo o arquivo .PDF? - Desenvolvido por: Yasser Abdallah.")
leitor_pdf = PdfReader(pasta)
cabecalho_planilha = [
    ['Item material', 'Unidade fornecimento', 'Quantidade', 'Almoxarifado']
]
for pagina in range(len(leitor_pdf.pages)):
    pagina_pdf = leitor_pdf.pages[pagina]
    extrair_conteudo = pagina_pdf.extract_text().split('\n')
    for conteudo in extrair_conteudo:
        if "9796 -" in conteudo:
            separa_traco = conteudo.split('-')
            nome_produto = separa_traco[2].split('  ')
            item_material = separa_traco[1].lstrip()
            produto = nome_produto[0].lstrip()
        if "MNO" in conteudo:
            separa_espaco = conteudo.split(' ')
            quantidade = separa_espaco[0]
            almxarifado = separa_espaco[1]
            cabecalho_planilha.append([item_material, produto, quantidade, almxarifado])
planilha = openpyxl.Workbook()
aba_planilha = planilha.active
for linha in cabecalho_planilha:
    aba_planilha.append(linha)

salvar_arquivo = filedialog.askdirectory(title="Onde deseja salvar o arquivo? - Desenvolvido por: Yasser Abdallah.")
planilha.save(f'{salvar_arquivo}\\relatorio_inventario_siads_MNO.xls')