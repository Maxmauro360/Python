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


def change():
    while True:
        try:
            print(f'1-Criar conta')
            print(f'2-Depositar dinheiro')
            print(f'3-Sacar dinheiro')
            print(f'4-Ver saldo')
            print(f'5-Sair')

            changee= int(input(f'choose one of the options next:'))

            if 1<= change <= 5:
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
            informaçao= input('Digite seu nome completo: \n')
            informaçao = input('Digite sua cidade: \n')
            informaçao= input('Digite sua renda: \n')
            informaçao.append(dados)

    case 2:
        if escolha == 2:

            print(Banco())

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

while fila:
    input(f'Digite o nome do usuário ou conta do banco para acessar')


class Banco: