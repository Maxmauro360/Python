def criar_conta():
    

    for i in range():
        usuario = input('Crie o usuario aqui: ')
        senha = input ('Crie a senha aqui: ')

        conta = {
            'usuário': usuario,
             'senha': senha,
             'saldo': 0
        }
        contas.append(conta)

        return 'Conta Criada!'
    
    def login():
        usuario= input('Usuário: ')
        senha = input('Senha: ')

        for conta in contas:
            usuario_salvo = conta[0]
            senha_salva = conta[1]

            if usuario == usuario_salvo and senha== senha_salva:
                return 'Login realizado!'
            
                menu_banco(conta)
            else:
                return 'Usuário ou senha incorretos'
            
    def menu_banco(conta):

        usuario = conta[0]
        senha = conta[1]
        saldo = conta[2]

        while true:
            print('1- Depositar')
            print('2- Sacar')
            print('3- Ver saldo')
            print('4- Sair')

            opçao= int(input('Acessar: ')) 

            if opçao == '1':
                valor = float(input('Valor do depósito: '))
                saldo += valor

                print(f'Seu saldo é de: {saldo}')

            elif opçao== '2':
                valor = float(input('Valor do saque: '))

                if valor <= saldo:
                    saldo -= valor

                    print(f'Seu saldo é de: {saldo}')
                else:
                    return 'Saldo insuficente'
                
            elif opçao =='3':
                print(f'Saldo: {saldo}')

            elif opçao== '4':
                return 'Saindo...'
                break
                
            else:
                return 'Opção inválida'
            
if __name__== '___main__':
    resultado = criar_conta()
    print(resultado)