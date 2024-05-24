import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['os'], 'includes': ['tkinter', 'PyPDF2', 'openpyxl'], 'add_to_path': True}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Scraping PDF SIADS. Criado por: Yasser Ibrahim.',
    version='1.0',
    description='Feito para procurar itens da unidade de Mundo Novo.',
    author='Yasser Ibrahim Abdallah Vaz Condoluci.',
    options={'build.exe': build_exe_options},
    executables=[Executable('main.py', base=base, icon='icon.ico', target_name='Scraping_SIADS_PDF.exe')]
)