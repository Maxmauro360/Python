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