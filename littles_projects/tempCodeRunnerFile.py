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
            self.clientes_prioritarios(nome)
            self.fila.append(nome)
            print(f'{nome} adicionado a fila prioritária')

    def adicionar_Comum(self,nome):
            self.clientes_comuns(nome)
            self.fila.append(nome)
            print(f'{nome} adicionado à fila comum')

clientes= Clientes()
for i in range(1,7):
    nome = input(f'Digite o nome do {i}º cliente:')
    clientes.adicionar_cliente(nome)

print(f'\n lista dos preferenciais: {clientes.clientes_prioritarios}')
print(f'\n lista dos comuns: {clientes.clientes_comuns}')
print(f'\n lista total: {clientes.fila}')