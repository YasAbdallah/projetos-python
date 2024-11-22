import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['os', "json", "PIL", 'datetime', "lib.navegacao", "lib.funcoes"]}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Relatório Impressoras HP e Canom. Desenvolvido por: Yasser Ibrahim.',
    version='1.0',
    description='Relatório Impressoras HP e Canom.',
    options={'build.exe': build_exe_options},
    executables=[Executable('src/impressoras_HP.py', base=base, icon="img/icon2.ico")]
)