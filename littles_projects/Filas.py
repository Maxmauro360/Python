#QUEUES
#ex01- Fila de atendimento(FIFO)
from collections import deque

def Fila():
    fila = deque() #criação de fila vazia 

    for i in range(1,6):
        
        pessoa = input(f'Digite o nome do {i}º cliente (ou "sair" para finalizar): ')

        if pessoa.lower()== 'sair':
            break
            
        fila.append(pessoa)

    print('\n fila atual:' ,list(fila))

    while fila: 
        input(' Pressione ENTER para atender o proximo cliente...') #o input pausa a execução até apertar enter
     
        atendido = fila.popleft()
  
        print(f'Cliente atendido: {atendido}')

        print(f'lista restante:', list(fila))

if __name__ == '__main__':

    Fila()

#ex02 - Fila de impressão

from collections import deque

def Impressao():
    pastas = deque()

    #while True: #for arquivo in pastas: nao vai funcionar pois a lista começa vazia
    #while true: sem for in range: imprime infinitos docuemntos
    for i in range(1,5):

        arquivo = input(f'liste o nome das pastas:')

        if arquivo.lower()== 'sair':
            break
        
        pastas.append(arquivo)

    print(f'Documentos restantes: {list(pastas)}')
    
    while pastas:
        input(f'Imprima os documentos 1 por vez apertando ENTER')

        documento = pastas.popleft()

        print(f'Documento impresso: {documento}')
        print(f'Documentos restantes: {list(pastas)}')

    print(f'Impressão finalizada!')


if __name__ == '__main__':
    Impressao()

#ex03 - fila prioritária manual
from collections import deque

class Clientes():

    def __init__(self):
        self.fila = deque()
        self.clientes_comuns= deque()
        self.clientes_prioritarios= deque()
        self.contador = 0

    def adicionar_cliente(self, nome):
        self.contador += 1

        if self.contador<= 3:
            self.adicionar_Preferencial(nome)
        else:
            self.adicionar_Comum(nome)
         
    def adicionar_Preferencial(self, nome):
            self.clientes_prioritarios.append(nome)
            self.fila.append(nome)
            print(f'{nome} adicionado a fila prioritária')

    def adicionar_Comum(self,nome):
            self.clientes_comuns.append(nome)
            self.fila.append(nome)
            print(f'{nome} adicionado à fila comum')

clientes= Clientes()
for i in range(1,7):
    nome = input(f'Digite o nome do {i}º cliente:')
    clientes.adicionar_cliente(nome)

print(f'\n lista dos preferenciais: {clientes.clientes_prioritarios}')
print(f'\n lista dos comuns: {clientes.clientes_comuns}')
print(f'\n lista total: {clientes.fila}')


#ex04- Simulador de banco

from collections import deque
dados = deque()
gerenciador= Clientes()

def change():
    while True:
        try:
            print(f'1-Criar conta')
            print(f'2-Depositar dinheiro')
            print(f'3-Sacar dinheiro')
            print(f'4-Ver saldo e historico')
            print(f'5-Sair')

            changee= int(input(f'choose one of the options next:'))

            if 1<= changee <= 5:
                return changee

            else:
                print('Digite uma opção de 1 a 5')

        except ValueError: #captura caso o usuaria digite letras ou simbolos
            print(f'Digite uma das opções válidas')
    
class Clientes:

    def __init__(self):
        self.fila = deque()
        self.clientes_comuns = deque()
        self.clientes_prioritarios = deque()
        self.contador = 0

    def chamar_cliente(self, nome):
        self.contador += 1

        if self.contador <= 3:
            self.clientes_prioritarios.append(nome)

        else:
            self.clientes_comuns.append(nome)

    def adicionar_preferencial(self, nome):
        self.clientes_prioritarios.append(nome)

        self.fila.append(nome)

        print(f'^{nome} adicionado com sucesso!')

    def adicionar_comum(self, nome):
        self.clientes_comuns.append(nome)
        
        self.fila.append(nome)

        print(f'{nome} adicionado com sucesso')

class Banco:
    def __init__(self):
        self.__saldo= 0
        self.__historico_bancario = deque()

    def deposito_bancario(self, valor):
        if valor > 0:

            self.__saldo += valor
            self.historico("depósito",valor, self.__saldo)
            print(f'Depósito Realizado!')

    def saque_bancario(self, valor):
        
        if valor > 0 and valor <= self.__saldo: #se o valor que quiser sacar for menor ou igual ao saldo, diminua o saldo
            self.__saldo -= valor

            self.historico("saque",valor,self.__saldo)

            print("Saque realizado!")

        else:
            print("Você não possui esta quantidade para saque")

    def historico(self, tipo_transaçao,valor, saldo):
            self.__historico_bancario.append({
                "Tipo": tipo_transaçao,
                "Quantia": valor,
                "Saldo": saldo

            })
    def carteira_historico(self):
        print(f' Aqui está seu saldo : {self.__saldo:.2f}')

        if not self.__historico_bancario:
            print(f'Não há transações')

        else:
            print(f'\n HISTÓRICO BANCÁRIO ')

            for i in self.__historico_bancario:
                print(
                    f'Tipo:{i["Tipo"]}',
                    f'Valor: {i["Quantia"]:.2f}',
                    f'Saldo após a operação {i["Saldo"]:.2f}'
                )



banco = Banco()
while True:

    escolha = change()
    match escolha:
        case 1:
            if escolha == 1:
                nome= input('Digite seu nome completo: \n')
                cidade= input('Digite sua cidade: \n')
                renda= int(input('Digite sua renda: \n'))

                usuario = {
                    "nome": nome,
                    "cidade": cidade,
                    "renda": renda,
                    "conta": Banco()
                }

                dados.append(usuario)

                print(f'Dados salvos com sucesso! {dados}')

                if renda >= 7000:
                    gerenciador.adicionar_preferencial(usuario)

                else:
                    gerenciador.adicionar_comum(usuario)

#não confundir objeto(gerenciador) com método(.adicionar_preferencial).
#gerenciador: é o objeto criado a partir da classe Clientes. Gerencia as filas de clientes
#.adicionar_preferencial(): é o método responsável por colocar o cliente na fila prioritária. Solicita cadastrar o cliente na fila prioritária
#usuario: é o dicionário que contém nome, cidade e renda. Armazena os dados do cliente

        case 2:
           if escolha == 2:
                deposito = float(input(f'Digite o valor do depósito: R$ \n'))
                banco.deposito_bancario(deposito)


        case 3:
            if escolha == 3:
                saque = float(input(f'Digite o valor do saque: R$ \n'))
                banco.saque_bancario(saque) #aloquei um metódo para um nome de um objeto

        case 4:
            if escolha == 4:
                banco.carteira_historico()

        case 5:
            print('Saindo do sistema...')
            break


import pip

print(dir(random))