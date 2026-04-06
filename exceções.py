#objeto que representa um erro que ocorreu ao executar o programa
#blocos try ... except

def div (x, y):
    return round(x /y)

if __name__== '__main__':
    while True:
        try:
            n1= int(input('digite um numero:'))
            n2= int(input('digite outro numero:'))
            break
        except ValueError:
            print(f'ocorreu um erro ao ler o valor. Tente novamente.')
    
    try:
        res = div(n1, n2)
    except ZeroDivisionError:
         print(f'Não é possivel dividir por 0')
    except:
        print(f'Ocorreu um erro desconhecido...')
    else:
        print(f"{res:.0f}") #para numeros sem decimais
    finally:            #bloco associado que sempre sera executado independente de ocorrer ou nao um errou ou 
        print(f'\n calculo finalizado!')                #uma exceção
                       