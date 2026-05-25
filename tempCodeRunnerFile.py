import os
textoo= input(f'Digite algumas frutas')
try:
    lista = []
    lista.append(textoo)
    os.chdir(r'C:\\Users\\Mauro\\Documents\\Github\\Diretorio') 
    with open('frutas.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(textoo)

    print(f'Texto salvo com sucesso!')
        
except IOError:
    print('Tente novamente')