#ex1
#while True:
#    x = int(input('digite o numero:'))
 #   if (x %2 == 0):
  #      print('É par')
   # else:
    #    print ('É impar')
     #   break

#ex02

def numero (a,b):
    if a > b:
          print(f'O numero {a} é maior que {b}')
    elif b>a:
         print(f'O numero {a} é menor que {b}')
    else:
        print('são iguais')

while True:
    a = int(input())
    b = int(input())
    numero(a,b)

    #nessas condiçoes, o laço acontece varias vezes, sem ter a quebra

#03
def notas(nota):
    if nota >= 7:
        return 'aprovado'
    elif 5 <= nota <7:
        return 'recuperação'
    else:
        return  'reprovado'
if __name__== '__main__':
    try:
        if 0 <= nota <=10:
            print(notas(nota))
        else:
            print('nota inválida')
    except ValueError:
        print('Digite um numero valido:')

while True:
    nota = int(input('Digite a nota:'))
    notas(nota)

#ex04
def cadastro (usuario, senha):
    if usuario == 'admin' and senha == '12345':
        return 'Pode entrar'
    if usuario == 'admin' and senha != '12345':
        print('senha incorreta')
    elif usuario != 'admin' and senha == '12345':
        print('usuario incorreto')
    else:
        return 'Tente outra vez'
if __name__=='__main__':
    while True:
        usuario = input('Digite seu usuário:')
        senha = input('Digite sua senha:')


        resultado =(cadastro (usuario, senha))
        print(resultado)

#nivel 2 ex01
for i in range(1,11):
    print(sum(i))
    
#ex02
    print(sum(range(1,11)))
#ou

soma = 0
for i in range (1,11):
    soma += i
    print(f'soma até {i} é: {soma}')

#03
def numeros(numero):
        if numero == 0:
            return 'parou'
        else:
            return f'voce digitou:{numero}'
    
if __name__=='__main__':       
    while True:
        numero = int(input('digite numeros:'))
        if numero == 0:
            break
    print(numeros(numero))

#04
def tabuadas(a):
    if a == 0:
        return 'Multiplicação por 0 é 0'
    
    lista = []
    for b in range (1,11):
       lista.append(f'{a} x {b} = {a*b}')

    return lista
if __name__== '__main__':
    while True:
        a = int(input('Digite um numero ou "-1" para sair:'))
        if a== -1:
            print('parou')
            break
        for linha in tabuadas(a):
            print(linha)

#nivel3 001
def nomes(qdt):
    lista=[]

    for nome in range(qdt):
        nome = input('Digite um nome:')
        lista.append(nome)
    return lista
if __name__== '__main__':
    print(nomes(6))

#ex02
    import random

def numeros(qdt):
    lista= []
    for i in range(qdt):
        n = random.randint(1,51)
        lista.append(n)
    return lista
if __name__=='__main__':
    print(numeros(6))

#ex03

lista =[]
def palavras(qdt):
     for nome in range(qdt):
         nome= input('digite uma palavra: \n')
         lista.append(nome)
     for palavra in lista:
         contador = 0
         for letra in palavra:
             if letra.lower() in 'aeiou':
                contador +=1
         print(f'A palavra "{palavra} tem "{contador}" vogais')
     return lista

if __name__=='__main__':
     print(palavras(1))
    

