lista=[]
def matematica():
    num1= int(input('Digite um numero aqui:'))
    num2= int(input('Digite outro numero aqui:'))
    operação = input('Digite a operação aqui (+,-,*,/):')
    
    match operação:
        case '+':
            res = num1 + num2
        case '-':
            res= num1 - num2
        case '*':
            res = num1* num2
        case '/':
            res= num1 / num2
        case _:
            return 'Operação inválida'
    return res
if __name__=='__main__':
    print(matematica())