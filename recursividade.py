#Igual na matematica
#formula do fatorial

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)
    
if __name__== '__main__':
    k = int(input('Digite um numero inteiro:'))
    try:
        res = fatorial(k)
    except RecursionError:
        print(f'numero fornecido é muito grande ou negativo')
    else:
        print(f'o fatorial de {k} é {res}')