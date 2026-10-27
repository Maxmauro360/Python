from collections import deque


def change():
    while True:
        try:
            print(f'1-Criar conta')
            print(f'2-Depositar dinheiro')
            print(f'3-Sacar dinheiro')
            print(f'4-Ver saldo')
            print(f'5-Sair')

            changee= int(input(f'choose one of the options next:'))

            if 1<= changee <= 5:
                return changee

            else:
                print('Digite uma opção de 1 a 5')

        except ValueError: #captura caso o usuaria digite letras ou simbolos
            print(f'Digite uma das opções válidas')
        
            break

    

escolha = change()
dados = deque()

match escolha:
    case 1:
        if escolha == 1:
            nome= input('Digite seu nome completo: \n')
            cidade = input('Digite sua cidade: \n')
            renda= input('Digite sua renda: \n')

            usuario = {
                "nome": nome,
                "cidade": cidade,
                "renda": renda
            }

            dados.append(usuario)

            print(f'Dados salvos com sucesso! {dados}')