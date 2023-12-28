import os

user = os.getlogin()

pastas = ['C:\\Windows\\Temp', f'C:\\Users\\{user}\\AppData\\Local\\Temp', 'C:\\Windows\\Prefetch']

for i in pastas:
    try:
        arqs = os.listdir(i)
        for arq in arqs:
            try:
                #print(os.path.join(i, arq))
                os.remove(os.path.join(i, arq))
            except Exception as e:
                print('Sem permissão.', e)
    except:
        pass

print("Fim")
input("Aperte qualquer tecla para finalizar.")
