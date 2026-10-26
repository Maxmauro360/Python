banco = 0
valores_depositados = []
while True:
    opçao = input('Digite D para depósito ou S para saque:')

    if(opçao== 'd' or opçao== 'D'):
        Deposito = int(input('Realize o deposito:'))
        if(Deposito>0):
            banco += Deposito
            valores_depositados.append(banco)
        else:
            print('[Error] saldo insuficiente')
    
    elif(opçao == 's' or opçao =='S'):
        Saque = int(input('Realize o saque:'))
        if (Saque> banco):
            print('Saldo insuficiente')
        else:
            banco -= Saque
            print('Saque realizado!')
            break
print(f'Seu saldo do banco é: {banco}')
print(f'Quantias depositadas: {valores_depositados}')
print(f'Valor total: {sum(valores_depositados)}')
