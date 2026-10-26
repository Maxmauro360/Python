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
    

    for i in range(1):
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
            usuario_salvo = conta['usuário'] # Aqui foi preciso criar um parametro para conseguir comparar com o input
            senha_salva = conta['senha']

            if usuario == usuario_salvo and senha== senha_salva:
                print('Login realizado!')
            
                menu_banco(conta)
            else:
                return 'Usuário ou senha incorretos'
            
def menu_banco(conta):

        usuario = conta['usuário']
        senha = conta['senha']
        saldo = conta['saldo']

        while True:
            print('1- Depositar')
            print('2- Sacar')
            print('3- Ver saldo')
            print('4- Sair')

            opçao= (input('Acessar: ')) 

            if opçao == '1':
                valor = float(input('Valor do depósito: '))
                conta['saldo'] += valor

                print(f'Seu saldo é de: {saldo}')

            elif opçao== '2':
                valor = float(input('Valor do saque: '))

                if valor <= conta['saldo']:
                    conta['saldo'] -= valor

                    print(f'Seu saldo é de: {conta['saldo']}')
                else:
                    return 'Saldo insuficente'
                
            elif opçao =='3':
                print(f'Saldo: {conta['saldo']}')

            elif opçao== '4':
                print('Saindo...')
                break
                
            else:
                print('Opção inválida')
            
if __name__== '__main__':
    resultado = criar_conta()
    print(resultado)

    acessar = login()
    print(acessar)
    
#jokenpo

def brincadeira():
    import random
    jokenpo= ['Pedra','Papel','Tesoura']
    for i in jokenpo:
        escolha = input('Escolha (Pedra, Papel ou Tesoura):').lower()

        computador= random.choice(jokenpo)

        print(f'Voce escolheu: {escolha}')
        print(f'Computador escolheu: {computador}')
        
        if escolha == computador:
            return 'Empate!'
        
        elif ((escolha == 'pedra' and computador == 'tesoura') or             
             (escolha == 'tesoura' and computador == 'papel')or
             (escolha == 'papel' and computador =='pedra')):
            
            return 'Você ganhou!'
        else:
            return 'Você perdeu!'
        
if __name__== '__main__':
    brincar= brincadeira()
    print(brincar)

#nivel 9 - exceçoes
    lista= []
def div ():

    
    while True:

        print(f'1-Dividir')
        print(f'2-Ver lista')
        print(f'3-Sair')

        op= int(input('Escolha qual deseja acessar: '))

        match op:
            case 1:
                dividir= divisao()
                print(dividir)
            
            case 2:
                print(lista)

            case 3:
                return 'Saindo do sistema...'
            
            case _:
                print('Operação invalida')
        
def divisao(): #poderia usar 'lista' como parametro
        try:
            n1= int(input('digite um numero:'))
            n2= int(input('digite outro para dividir numero:'))
            resultado = round(n1/n2)      
            lista.append(resultado)      
        
        except ValueError:
            print(f'ocorreu um erro ao ler o valor. Tente novamente.')
        
        except ZeroDivisionError:
            print(f'Não é possivel dividir por 0')
        except:
            print(f'Ocorreu um erro desconhecido...')
        else:
            print(f"{resultado:.0f}") #para numeros sem decimais
        finally:            #bloco associado que sempre sera executado independente de ocorrer ou nao um errou 
                            # o mais correto nesse caso seria usar o 'else:'
            print (f'O resultado é: {resultado}')
    
        for i in lista:
            i = n1
            if n1 > 10:
                print(f'Significante')
            else:
                print('Insignificante')
                print(f'\n calculo finalizado!')

if __name__== '__main__':
    executar = div()
    print(executar)

#nivel 10- lambda,filter,map

def dobradinha():

    lista_amiga= []

    def pares(lista): #o python ja compara o 'lista_amiga = lista, o valor l_a é enviado para o paramero lista'
        lista2=[]
        verificar= lambda x: x%2== 0
        for numero in lista:
            if verificar(numero):
                lista2.append(numero)
        return lista2

    def dobrar(lista):
        verificar2= map(lambda x: x*2, lista)
        return list(verificar2)
    

    for i in range(3):
        numero = int(input(f'Digite o {i+1}º numero: ')) # A variavel não pode ter nome de funçao                                                                                                                                                                                                                                                                                                                                                   
        lista_amiga.append(numero)

    while True:
        print(f'1- Somente numeros pares')
        print(f'2- Somente numeros dobrados')
        print(f'3- Ver lista amiga')
        print(f'4- Ver tudo')
        print(f'5- Sair')

        acessar = int(input('Escolha entre as alterantivas: '))

        match acessar:
            case 1:
                lista2=[]
                for numero in lista_amiga:
                    verificar = lambda x: x %2== 0
                    if verificar(numero):
                        lista2.append(numero)
                        print(lista2)
                    

            case 2:
                lista3=[]
                l=map(lambda lista_amiga: lista_amiga * 2, lista_amiga)
                lista3.append(list(l))
                print(f'Aqui estão os numeros dobrados: {lista3}')
            
            case 3:
                if len(lista_amiga) == 0:
                    print('Ainda não há numeros')

                else:
                    return lista_amiga

            case 4:
                print(f'Aqui está {lista_amiga}, numeros pares{pares(lista_amiga)} e numeros dobrados {dobrar(lista_amiga)}') 

            case 5:
                return 'Saindo..'
        
            case _:
                print('Operação invalida')

        #(return acessar) com isso, encerra a funçao na primeira volta

if __name__ == '__main__':
    ex= dobradinha()
    print(ex) 


def lista_vogais():
    frase= 'Caia sete vezes, levante-se oito." Ensina sobre persistência e resíliência diante das adversidades dá vida.'
    acentuadas =['a', 'e', 'i', 'o', 'u','á','ê','í']

    palavras= []
    vogais= []

    total_frase = 0
    total_vogais = 0
    for i in frase.split():
        total_frase +=1
        palavras.append(i)

        for v in i.lower():
            if v in acentuadas:
                total_vogais +=1
                vogais.append(v)

                
    print(f'A frase possui: {total_frase} palavras')
    print(f'A frase possui: {total_vogais} vogais')
 
    return palavras, vogais

if __name__== '__main__':
    c = lista_vogais()
    print(c)


#lambda + map + filter

def numeros():

    lista= []

    numeros_pares= [] 
    numeros= lambda x: x%2==0
    
    numeros_par3x = []
    multiplicados = lambda y: y*3
    
    for i in range(1,6):
        
        digitados = int(input('Digite 5 numeros aqui: '))
        
        lista.append(digitados)
        
        
        if numeros(digitados):
        
         numeros_pares.append(digitados)
            

        else:
            multiplicados(numeros_par3x)

            numeros_par3x.append(multiplicados(digitados))

    print(f'Lista completa: {lista}')

    #print(f'Números pares: {numeros_pares}')
    print(f'Números pares: {pares}')

    print(f'Os numeros triplicados ficam: {numeros_par3x}')
        
    return lista, numeros_pares
    
if __name__== '__main__':
    lista, numeros_pares = numeros()

#ex02
def numeros():
    digitados=[]

    for i in range(5):

        lista= int(input('Digite 5 numeros aqui: '))
        
        digitados.append(lista)

    numeros_pares= list(filter(lambda x: x%2 == 0, digitados))       
    numeros_triplicados= list(map(lambda k: k*3, digitados))    

    print(f'Os numeros digitados foram: {digitados}')    
    print(f'Os numeros pares são: {numeros_pares}')    
    print(f'Os numeros triplicados foram: {numeros_triplicados}')  

    return digitados, numeros_pares, numeros_triplicados

if __name__=='__main__':
    numeros()  
    



#reduce()
from functools import reduce 

def funçao(x,y):
    return x + y
lista = [2,4,6,8,10]

total =reduce(funçao, lista)
print(f'O resultado é: {total}')
print(f'O maior valor da lista é: {max(lista)}')

                    

#list comprehension
def lista ():

    lis = [1,2,3,4,5,6,7,8,9]

    resultado = [x**2 for x in lis if x % 2 == 0]

    return lis, resultado
if __name__== '__main__':
    lis, resultado = lista()      
    print(lis)
    print(resultado)
        

#POO- praticagem
            
        
        




      

    
        


































    
