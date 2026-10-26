a = int(input('nota:'))

if (a>=7 or a <= 10):
    if(a>=7):
        print('Aprovado!')
    elif(6>=a>=5):
        print('Recuperação!')
    else:
     print('Reprovado!')

#ex010
soma = 0
contador = 0
lista = []
while True:
    k = int(input('Digite uns numeros:'))

    if(k == 0):
        print('Acabou a mamata')
        break
    if (k>0 or k<0):
        soma += k
        contador += 1
        lista.append(k)
print(f'sua soma é: {soma}')
print(f'a quantidade é:{contador}')
print(f'os valores somados foram: {lista}')