def numeros():

    lista= []

    numeros_pares= [] 
    numeros= lambda x: x%2==0
    
    numeros_par3x = []
    multiplicados = lambda y: y*3
    
    for i in range(1,6):
        
        digitados = int(input('Digite 5 numeros aqui: '))
        
        lista.append(digitados)
        
        for num in lista:
        
            if numeros(num):
        
                numeros_pares.append(num)
        
                print(f'Os numeros pares são: {numeros_pares}')

            elif multiplicados(numeros_par3x):

                numeros_par3x.append(num)

                print(f'Os numeros triplicados ficam: {numeros_par3x}')
        
    return lista, numeros_pares
    
if __name__== '__main__':
    lista, numeros_pares = numeros()
    print(f'Lista completa: {lista}')
    print(f'Números pares: {numeros_pares}')
