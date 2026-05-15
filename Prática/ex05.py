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
    lista = numeros(6)
    print(lista)
    print(max(lista))

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
    

lista = []
def contador_vogal(qdt):
    for nome in range(qdt):
        nome = input('Nome aqui:\n')
        lista.append(nome)
    for nome in lista:
        contador =0
        for vogal in nome:
            if vogal.lower() in 'aeiou':
                contador += 1
        print(f'{nome} tem {contador} vogais')
    return lista
if __name__== '__main__':
    print(contador_vogal(1))


#ex04
listinha= []
def palavra_invertida(qtde):
    for nome in range(qtde):
        nome= input('Aqui:')
        listinha.append(nome)
    resultado=[]
    for nome in listinha:
        resultado.append(nome[::-1])
    return resultado
if __name__== '__main__':
    print(palavra_invertida(1))





guarda_roupa= []
def armario(qdt):
    for roupas in range(qdt):
        roupas = input('O que tem?:')
        guarda_roupa.append(roupas)

    resultado= []
    roupa_inversa=[]

    for roupas in guarda_roupa:
        vogais=0
        for vogal in roupas:
            if vogal.lower() in 'aeiou':
                vogais += 1
        resultado.append(f'{roupas} tem {vogais} vogais')
        roupa_inversa.append(roupas[::-1])

    return resultado, roupa_inversa
if __name__== '__main__':
    resultado, roupa_inversa =armario(2) 
    print(resultado)
    print(roupa_inversa)


#nivel4 01
lista=[]
def matematica():
    num1= int(input('Digite um numero aqui:'))
    num2= int(input('Digite outro numero aqui:'))
    operação = input('Digite a operação aqui (+,-,*,/):')
    
    match operação:
        case '+':
            res = num1 + num2
        case '-':
            res= num1 - num2
        case '*':
            res = num1* num2
        case '/':
            res= num1 / num2
        case _:
            return 'Operação inválida'
    return res
if __name__=='__main__':
    print(matematica())

#nivel5- Dicionarios, tuplas, sets..

dicionario= [  
    {  
        'nome': 'Matheus',  
        'idade':21,  
        'escolaridade': 'Tecnico',
    },
    {
        'nome': 'Max',
        'idade':21,
        'escolaridade': 'Tecnico',
    },
    {
        'nome': 'julia',
        'idade': 17,
        'escolaridade': 'Ensino médio'
    }
]

def cadastro(nome_busca):
    for pessoa in dicionario:
        if pessoa['nome'].lower() == nome_busca.lower():
            return pessoa
    return None

if __name__== '__main__':
    nome = input('Digite o nome:')
    resultado = cadastro(nome)
    if resultado:
        print(resultado)
    else:
        print('Pessoa não encontrada')






listagem = [
    {
        'objeto': 'caneta',
        'tamanho': 'pequeno',
        'medida': 20
    },
    {
        'objeto': 'caderno',
        'tamanho': 'medio',
        'medida': 30
    },
    {
        'objeto': 'borracha',
        'tamanho':'miuda',
        'medida': 5
    }   
]

def escola(material):
    for utensilio in listagem:
        if utensilio['objeto'].lower() == material.lower():
            return utensilio
    return None

if __name__== '__main__':
    objeto = input('Digite o nome:')
    resultado = escola(objeto)
    if resultado:
        print(resultado)
    else:
        print('Objeto não encontrado')

      
    
#nivel 5- contar letras unicas

def nomes():
    lista = []

    for i in range(2):
        nome = input(f'Digite o {i+1}º nome:')
        lista.append(nome)

    total_vogais= 0
    resultado =[] #se prestar bastante atenção, está identado diretamente no def 'nomes()'

    for nome in lista:
        total_letras = len(nome)

        letras_unicas = set(nome.lower())

        for letra in nome.lower():
            if letra in 'aeiou':
                total_vogais += 1
    
        resultado.append(f'Nome: {nome}')
        resultado.append(f'Letras unicas: {letras_unicas}')
        resultado.append(f'Total de letras: {total_letras}')
        resultado.append(f'Quantidade de vogais: {total_vogais}')

    return lista, resultado

if __name__== '__main__':
    resultados = nomes()
    for item in resultados:
        print(item)


#nivel 5- criaçao de tuplas

def localização ():

    coordenadas= []
    for i in range(2):
        x= int(input(f'{i+1}ºDigite a abscissa aqui:'))
        y= int(input(f'{i+1}ºDigite a ordenada aqui:'))
        coordenadas.append((x,y))

    coordenada_xy=[]

    for x, y in coordenadas:
        if x==y :
            coordenada_xy.append(f'({x},{y}) são equidistantes')

        else:
            coordenada_xy.append(f'({x},{y}) não são equidistantes')
    
    return coordenada_xy

if __name__== '__main__':
    resultado = localização()
    print(resultado)

#jogo de adivinhação
def adivinhaçao():
    import random

    escolhido = random.randint(1,51)
    tentativas=[]

    for i in range (5):
            suposiçao = int(input(f'Digite o numero aqui: '))    
            tentativas.append(suposiçao) 

            if suposiçao > escolhido:
                print('Numero alto')

            elif suposiçao < escolhido:
                print('Numero baixo')

            if escolhido == suposiçao:
                print(f'Você acertou!')
                return escolhido, tentativas
            
            elif suposiçao > random.randint(1,51) or suposiçao < random.randint(1,51):
                print('Passou das possibilidades')
                    
            else:
                    print('Você errou, tente novamente!')
   
    return escolhido,tentativas

if __name__== '__main__':
    escolhido, tentativas = adivinhaçao()
    print(f'O numero escolhido foi: {escolhido}')
    print(f'As tentativas foram: {tentativas}')


#cadastro bancario
    contas =[]

def criar_conta():
    

    for i in range():
        usuario = input('Crie o usuario aqui: ')
        senha = input ('Crie a senha aqui: ')

        conta = {
            'usuário': usuario,
             'senha': senha,
             'saldo': 0
        }
        contas.append(conta)

        return 'Conta Criada!'
    
    def login():
        usuario= input('Usuário: ')
        senha = input('Senha: ')

        for conta in contas:
            usuario_salvo = conta[0]
            senha_salva = conta[1]

            if usuario == usuario_salvo and senha== senha_salva:
                return 'Login realizado!'
            
                menu_banco(conta)
            else:
                return 'Usuário ou senha incorretos'
            
    def menu_banco(conta):

        usuario = conta[0]
        senha = conta[1]
        saldo = conta[2]

        while true:
            print('1- Depositar')
            print('2- Sacar')
            print('3- Ver saldo')
            print('4- Sair')

            opçao= int(input('Acessar: ')) 

            if opçao == '1':
                valor = float(input('Valor do depósito: '))
                saldo += valor

                print(f'Seu saldo é de: {saldo}')

            elif opçao== '2':
                valor = float(input('Valor do saque: '))

                if valor <= saldo:
                    saldo -= valor

                    print(f'Seu saldo é de: {saldo}')
                else:
                    return 'Saldo insuficente'
                
            elif opçao =='3':
                print(f'Saldo: {saldo}')

            elif opçao== '4':
                return 'Saindo...'
                break
                
            else:
                return 'Opção inválida'
            
if __name__== '___main__':
    resultado = criar_conta()
    print(resultado)


    
            
        
        




      

    
        


































    
