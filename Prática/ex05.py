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
    
    for b in range (1,11):
        print(f'{a} x {b} = {a*b}')
if __name__== '__main__':
    while True:
        a = int(input('Digite um numero:'))
        break
    print(tabuadas(a))

    
