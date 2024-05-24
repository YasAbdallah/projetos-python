import os

usuario = os.getlogin()

pastas = ['C:\\Windows\\Temp', f'C:\\Users\\{usuario}\\AppData\\Local\\Temp', 'C:\\Windows\\Prefetch']

for pasta in pastas:
    try:
        arquivos = os.listdir(pasta)
        for arquivo in arquivos:
            try:
                os.remove(os.path.join(pasta, arquivo))
            except Exception as e:
                print('Sem permissão.', e)
    except Exception as e:
        print(e)

print("Fim")
input("Aperte qualquer tecla para finalizar.")
