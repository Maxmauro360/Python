#Manipulação de arquivos de texto

manipulador = open('arquivo.txt', 'r', encoding='utf-8')
print(f'\Método read():\n')
print(manipulador.readlines()) #cria uma lista com todo conteudo do texto
print(manipulador.read())#puxa todo o texto, faz a leitura
print(manipulador.readline()) #puxa a primeira linha

manipulador = open('arquivo.txt', 'r', encoding='utf-8')
texto = input('Qual termo deseja procurar?: ').lower()
try:
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha= linha.rstrip() #tira o ultimo caracter da linha '\n'
        if texto in linha.lower():
            print(f'o termo foi encontrado!')
            print(linha)
except IOError: #erro de entrada e saida
    print(f'Não foi possivel abrir o arquivo')
else:
    manipulador.close()

    #da pra se ler arquivos de outros diretorios nao necessariamente na mesma pasta do script
    print()


import os

with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
print(os.getcwd())
print(os.listdir())


#escrever em arquivos de textos
import os
textoo= input(f'digite oq quer escrever:')
try:
    os.chdir(r'C:\\Users\\Mauro\\Documents\\Github\\Diretorio') 
    with open('textin.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(textoo)

    print(f'Texto salvo com sucesso!')
        
except IOError:
    print('Tente novamente')

import os
print(os.getcwd())

#Ele cria um pastra vazia se não tiver

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
