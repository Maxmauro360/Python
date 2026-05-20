#funções lambda (anônimas) não é definida previamente, voce cria e usa
#sintaxe:
#lambda argumnetos: expressão

quadrado = lambda x: x**2
for k in range(1,11):
    print(quadrado(k))

par = lambda x: x %2 == 0
print(par(10))

f_c = lambda f: (f -32)* 5/9
print(f_c(100))

#função map()- funçoes que aplica funçoes (geralmente usada com outras funçoes lambda)
# é considerada como funçao de ordem superior, pode receber outras funções como argmento ou recerber outras funçoes como resultado
#sintaxe
#map(função,iteravel)

num =[1,2,3,4,5,6,7,8]
dobro = list(map(lambda x:x*2, num))
print(dobro)

palavras = ['Python', 'é', 'uma', 'linguagem', 'de' ,'programação']
maiuscula = list(map(str.upper, palavras))
print(maiuscula)

#Função filter
#sintaxe:
#filter (função, sequencia)

def numeros_pares(n):
    return n % 2 == 0

numeros = [1,2,3,4,5,6,7,8]
num_par = list(filter(numeros_pares, numeros))
print(num_par)

#usando o lambda
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num_impar = list(filter(lambda k: k%2 != 0, numeros))
print (num_impar)

#Função reduce()
#realiza operaçoes acumlativas em sequencia de elementos e retorna um unico valor no final
#sintaxe:
#reduce (função, sequencia, valor_inicial)
from functools import reduce

def mult (x,y):
    return x*y
numeros = [ 1,2,3,4,5,6,7,8]
total = reduce(mult, numeros)
print(total)
 
#soma acumulativa dos quadrados de valores usando a expressao lambda
numeros = [1,2,3,4,5,6]
#((1**2 + 2**2)**2 +3**2)**2 +4**2
total = reduce(lambda x,y: x**2 + y**2, numeros)
print(total)