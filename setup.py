import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['os'], 'includes': ['tkinter']}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Downloader de Videos do Youtube. Criado por: Yasser Ibrahim.',
    version='1.0',
    description='Downloader de Videos do Youtube.',
    options={'build.exe': build_exe_options},
    executables=[Executable('downloaderYoutube.py', base=base)]
)