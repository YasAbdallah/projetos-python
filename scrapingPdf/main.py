from PyPDF2 import PdfReader
import openpyxl
from tkinter import filedialog


pasta = filedialog.askopenfilename(title="Onde está salvo o arquivo .PDF? - Desenvolvido por: Yasser Abdallah.")
pdfReader = PdfReader(pasta)
array = [
    ['Item material', 'Unidade fornecimento', 'Quantidade', 'Almoxarifado']
]
for pag in range(len(pdfReader.pages)):
    page = pdfReader.pages[pag]
    extract = page.extract_text().split('\n')
    for x in extract:
        if "9796 -" in x:
            edit = x.split('-')
            nomeProduto = edit[2].split('  ')
            itemMaterial = edit[1].lstrip()
            produto = nomeProduto[0].lstrip()
        if "MNO" in x:
            edit2 = x.split(' ')
            qnt= edit2[0]
            almox = edit2[1]
            array.append([itemMaterial, produto, qnt, almox])
workbook = openpyxl.Workbook()
sheet = workbook.active
for row in array:
    sheet.append(row)

salvarArquivo = filedialog.askdirectory(title="Onde deseja salvar o arquivo? - Desenvolvido por: Yasser Abdallah.")
workbook.save(f'{salvarArquivo}\\relatorio_inventario_siads_MNO.xls')