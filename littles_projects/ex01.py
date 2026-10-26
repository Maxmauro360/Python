#ex01

import math
a = int(input('escolha um numero:'))
b = int(input('escolha outro numero:'))
c = a + b
print(f'sua soma é {c}')
print(f'o dobro desse numero é:', c*2)
print(f'o triplo desse numero é:', c*3)
print(f'a raiz desse numero é:', round(int(math.sqrt(c)))  )
print(f'a metade desse numero é: {c/2:.0f}') 

if (a > b):
    print(f'{a} é maior que {b}')
elif (a == b):
    print(f'{a} é igual a {b}')
else:
    print(f'{a} é menor que {b}')


#ex02

idade = 21
carteira = 'desabilitado'
resultado =(idade >= 18) and (carteira == 'habilitado')
#resultado =(idade >= 18) and (carteira == 'desabilitado')
print (f'Pode pegar o carro? {resultado}')

cat = 'saiu'
dog = 'saiu'
k = (dog == 'entrou') or (cat== 'entrou')
print(f'algum pet saiu?{k}')

#ex03

x = 10
y = 20
z = c
if(c <= 20 and c>=10):
    print(f'{c} está entre {x} e {y}')
else:
    print(f'{z} não está entre {x} e {y} ')

#ex04

k = int(input('Digite um numero:'))
if (k < 0 or k >100):
    if (k < 0):
        print('É negativo')
    elif(k>100):
        print('É maior que 100')
    else:
        print('Está entre 0 e 100')