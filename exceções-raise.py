from math import sqrt

class NumeroNegativoError(Exception):
    def __init__(self):
        pass
if __name__== '__main__':
    try:
        n1= int(input(f'Digite um numero positivo:'))
        if n1 < 0:
            raise NumeroNegativoError
    except NumeroNegativoError:
        print(f'foi fornecido um numero negativo')
    else:
        print(f'A raiz quadrada de {n1} é {sqrt(n1)}')
    finally:
        print(f'fim do calculo!')
