from PyPDF2 import PdfReader
import json
from tkinter import filedialog
import re


leitor_pdf = PdfReader("C:\\Users\\05916892195\\Documents\\GitHub\\projetos-python\\scraping-pdf\\arquivos\\pdf\\lista_materiais.pdf")
conteudo_tradado = list()
for pagina in range(len(leitor_pdf.pages)):
    pagina_pdf = leitor_pdf.pages[pagina]
    extrair_conteudo = pagina_pdf.extract_text().split('\n')
    for conteudo in extrair_conteudo:
        if conteudo.find("MINISTERIO DA FAZENDA") == -1:
            if conteudo.find("DELEGACIA") == -1:
                if conteudo.find("CATALOGO DE MATERIAIS PERSONALIZADO") == -1:
                    if conteudo.find("CONTA CONTABIL") == -1:
                        if conteudo.find("DATA DA PERSONALIZACAO") == -1:
                            if conteudo.find("UNIDADE DE FORNECIMENTO") == -1:
                                try:
                                    re_compile = re.compile(r"((^[0-9]*)\-([0-9]*))")
                                    result = re_compile.search(conteudo)
                                    codigo = "".join(result.group(1).split("-")[:]) if len(result.group(1)) == 10 else ""
                                    descricao = " ".join(conteudo.split('-')[2:]) if len(conteudo.split('-')) > 3 else " ".join(conteudo.split('-')[2:])
                                    #TODO: Remover listas vazias
                                    nome_produto = " ".join(descricao.replace('"', '').replace(",", "").lstrip().split(' ')[0:2])
                                    if codigo != "" and nome_produto[0:2] != "" and descricao != "":
                                        descricao = descricao[:-2] if ',' in descricao[::-1] else descricao
                                        conteudo_tradado.append({"codigo": codigo, "produto": nome_produto.lower(), "descricao": descricao.replace('"', '').lstrip().lower(), "saldo":0}) 
                                except Exception as e:
                                    pass
    print("*"*10, f" Fim pagina {pagina+1} ", "*"*10)
with open("dados.json", 'w') as arquivo:
    arquivo.write(json.dumps(conteudo_tradado))
    