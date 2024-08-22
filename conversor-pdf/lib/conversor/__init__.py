import os
import camelot
import pikepdf
import subprocess
import pandas as pd
from pdf2docx import Converter
from lib.prints import Print
from lib.manipular_pasta import *


class Conversor():
    def __init__(self) -> None:
        self.arquivo_principal = selecionar_arquivo()
        self.caminho_salvar_arquivo = selecionar_caminho()
        self.nome_arquivo = pegar_nome(self.arquivo_principal)
        self.extencao_arquivo = pegar_extencao(self.arquivo_principal)
        self.print = Print()

    def pdf_para_xlsx(self):
        try: 
            self.print.print_colorido("-"*10, "Iniciando Conversão!!!", "-"*10)
            
            tabelas = camelot.read_pdf(self.arquivo_principal, pages='all')

            # Converte cada tabela em uma planilha separada
            with pd.ExcelWriter(f'{self.caminho_salvar_arquivo}\{self.nome_arquivo}.xlsx') as writer:
                for i, tabela in enumerate(tabelas):
                    tabela.df.to_excel(writer, sheet_name=f'Tabela_{i}', index=False)
        except Exception as e:
            self.print.print_vermelho(str(e))


    def pdf_para_word(self):
        try:
            cv = Converter(self.arquivo_principal)
            cv.convert(os.path.join(self.caminho_salvar_arquivo, self.nome_arquivo+".docx"), start=0, end=None)
            cv.close()
        except Exception as e:
            self.print.print_vermelho(str(e))


    def any_para_pdf(self):
        try:
            subprocess.run(['unoconv', '-f', 'pdf', '-o', os.path.join(self.caminho_salvar_arquivo, self.nome_arquivo), self.arquivo_principal])
        except Exception as e:
            self.print.print_vermelho(str(e))


    def desbloquear_pdf(self):
        try:
            with pikepdf.open(self.arquivo_principal, allow_overwriting_input=True) as pdf:
                pdf.save(os.path.join(self.caminho_salvar_arquivo, self.nome_arquivo))
        except Exception as e:
            self.print.print_vermelho(str(e))