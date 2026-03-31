#criação de um banco
Valores_depositados = []
banco = 0
while True:
    opçao = input('Aperte "D" para depósito ou "S" para saque:').lower()

    if(opçao =='d'):
        Deposito = int(input('Realize seu depósito aqui:'))
        if (Deposito>0):
          banco+= Deposito
          Valores_depositados.append(Deposito)
        else:
         print('Não foi possivel realizar esta operação!')

    elif(opçao =='s'):
        saque = int(input('Realize aqui seu saque:'))
        if(saque> banco):
            print('Error')
        else:
            banco -= saque
            break
print(f'Seu saldo atual é: {banco}')
print(f'Suas cédulas foram : {Valores_depositados}')

def binario(bin):
   return(x**2 for x in bin)

if __name__ == "__main__":
    valores= [2,3,4,5,6,7,8]
    resultado = binario(valores)
    for k in resultado:
        print(k)

