def dobradinha():
    lista_amiga= []
    for i in range(3):
        dobrar = int(input(f'Digite o {i+1}º numero: '))
        lista_amiga.append(dobrar)

    while True:
        print(f'1- Somente numeros pares')
        print(f'2- Somente numeros dobrados')
        print(f'3- Ver lista amiga')
        print(f'4- Ver tudo')
        print(f'5- Sair')

        acessar = input('Escolha entre as alterantivas: ')

    match acessar:
        case 1:
            lista2=[]
            for numero in lista_amiga:
                if lambda lista_amiga: lista_amiga %2== 0:
                   k= lista2.append(numero)
                print(k)

        case 2:
            lista3=[]
            l=map(lambda lista_amiga: lista_amiga * 2)
            lista3.append(l)
            print(f'Aqui estão os numeros dobrados: {l}')
            
        case 3:
            if (lista_amiga) == None:
                print('Ainda não há numeros')

            else:
                return lista_amiga

        case 4:
            print(f'Aqui está {lista_amiga}, numeros pares{lista2} e numeros dobrados {lista3}') 

        case 5:
            return 'Saindo..'
        
        case _:
            print('Operação invalida')
            
    return acessar

if __name__ == '__main__':
    ex= dobradinha()
    print(ex)