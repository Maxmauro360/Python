#Modularização, reúso de código, legibilidade

# def <nome> ([argumento]):
#     <instrução>

# def mensagem():
#     print('Max é foda, lindo gostoso')
#     print('EUEU')

# mensagem()

#função com argumentos
def soma(a, b):
    print(a + b)
soma(20,4)

def mult(x, y):
    return x * y #esta função assim que encontrada, ela encerra a busca

a= 7
b=6
c= mult(a, b)
print(f'produto de {a} e {b} é {c}')
def div(k, j):
    if j != 0:
     return k / j
    else:
       return 'impossivel dividir por zero!'


if __name__ == '__main__': #separa a a´rea do ponto principal do programa de outras áreas
    a = int(input('Digite um numero:'))
    b = int(input('Digite outro numero:'))

r = div(a, b)
print(f'{a} dividido por {b} é igual a {r}')

def quadrado (val):
   return[ x ** 2 for x in val]
   

if __name__ == '__main__':
    valores = [2,4,5,6,7]
    resultados = quadrado(valores)
    for i in resultados:
      print(i)

#parametros opcionais
def contar (num= 7, caractere="+"):
   for k in range(0,num):
      print(caractere)
#se adicionar 'print(num)' ele oscila entre caractere e numero

if __name__ == "__main__":
   contar(caractere=")") # se muda a variavel aqui, ela será modificada enquato execuçao da funçao



def som_animalesco(som):
    if(som== 'auau'):
        return('é um cachorro')
    elif(som == 'miau'):
      return('é um gato')
    elif (som =='quack'):
      return('é um pato')
    
if __name__== '__main__':
   animais = input('Digite o som do animal:').lower()
   res= som_animalesco(animais)
   print(res)



def som_mult_exp(a, b, c):
    if( a== 0):
        return(a+b+c)
    elif(b == 1):
        return(a**c)
    elif(c==1):
     return(a*b*c)

if __name__== '__main__':
   res = som_mult_exp(0,2,3)
   print(res)


def quadrado(val):
    quadrados = []
    for k in val:
        quadrados.append(k** 2)
    return quadrados

if __name__== '__main__':
    valores=[2,3,4,5,6,7,8,9]
    resultado = quadrado(valores)
    for k in resultado:
        print(k)

#funçoes parametros
def contar(num= 11, caractere= '+'):
    for k in range(1,num):
       print (caractere)
if __name__=='__main__':
    contar(caractere= '/') #se eu quiser mudar o parametro, terá de ser feio isso
    #caso a funçao estiver em ordem, colocar o numero e depois outra função ex: (5,'*')

x= 5
y=3
z= 1
def soma_mult(x,y,z):
   if(z== 0):
      return x*z
   else:
      return (x+y+z)
   
if __name__=='__main__':
    res4 = soma_mult(x, y, z) #a declaração da funçao, nao precisa ter as mesmas variaveis, os valores serao copiados
    print(res4)

