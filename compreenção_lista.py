#sintaxe geral
# [expressão for item in lista]
# item = variavel que representa cada elemnto na lista

def dobradinha():
    n =[2,3,4,5,6]
    quadrados = list(map(lambda x: x**2, n))

    return quadrados
if __name__ == '__main__':
    resultado = dobradinha()

    print(resultado) 


def dobradinha():
    num = [2,4,5,6,7]
    quadrado = [x**2 for x in num] #(parametro) para todo numero em 'n'
    print(quadrado)

#criar uma lista de numeros pares de 1 a 10 
def numeros_pares():
    lista = []
    for i in range(3):
        name= int(input('Digite aqui: '))
        pares= lambda x: x%2 == 0
        if pares(name):
                
                lista.append(name)
    return lista

if __name__=='__main__':
    verificar = numeros_pares()
    print(verificar)
 


def compreenssão():
    frase= 'Caia sete vezes, levante-se oito." Ensina sobre persistência e resíliência diante das adversidades dá vida.'
    vogais = ['a','e','i','o','u','á','í','ê']
    listinha =[i for i in frase if i in vogais]
    print(f'A frase possui : {len(listinha)} vogais')

if __name__== '__main__':
    c = compreenssão()
    print(c)

#distributiva entre valores de duas listas
def distributiva():
   dtb = [k * m for k in [2,6,9] for m in [5,7,8]]
   quadrados= [2,5,8,3,6,9]
   qdd= [l**2 for l in quadrados ]
   return dtb, qdd
if __name__== '__main__':
    d = distributiva()
    print(d)

#criar uma lista de numeros pares 
def pares ():
    pares= [num for num in range(1201) if num %2==0]
    return pares
if __name__=='__main__':
    k = pares()
    print(k)