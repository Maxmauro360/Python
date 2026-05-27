def lista ():

    lis = [1,2,3,4,5,6,7,8,9]

    resultado = [x**2 for x in lis if x % 2 == 0]

    return lis, resultado
if __name__== '__main__':
    lis, resultado = lista()      
    print(lis)
    print(resultado)
        