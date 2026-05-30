#somente praticas de POO

class  Veiculo:
    
    pass

    def movimentar(self):
        print(f'Sou um carro e me movimento')

    def __init__(self, modelo,ano, cor):
        self.__modelo = modelo
        self.__ano = ano
        self.__cor= cor
        self.__velocidade = 0
        self.__num_regis= None

    def set_num_regis(self, registro):
        self.__num_regis= registro

    def get_num_regis(self):
        return self.__num_regis

    def ligar(self):
    
        print('sou um carro e corro muito!')
    
    def acelerar(self):

        self.__velocidade += 10
        self.__velocidade += 10
        self.__velocidade += 10

    def set_acelerar(self, velocidade):
        return self.__velocidade
    
        print(f'A velocidade do carro é de {self.__velocidade}')

if __name__ == '__main__':
    carro1 = Veiculo('Lancer', 2025, 'Preto fosco')
    print(Veiculo.modelo, Veiculo.ano)
    
#Banco- Operaçoes
class Banco():

    def __init__(self):

        self.__saldo=0  

    def depositar(self, valor):
        
        self.__saldo += valor

        print('Deposito realizado!')

    def sacar(self, valor):

        if valor <= self.__saldo:

            self.__saldo -= valor
            
            print('Saldo realizado!')

        else:
            print('Saldo insufienciente')

    def get_saldo(self):
        print(f'Aqui está seu saldo: {self.__saldo}')
             

            
            
if __name__ == '__main__':
    
    conta = Banco()

    while True:
        
        print('1-Depositar')

        print('2-Sacar')

        print('3-Ver saldo')

        print('4-Sair')
    
        escolhas = int(input('Escolha uma das opçoes: '))    
            
        
        match escolhas:
            case 1:
                    
                valor = int(input('Deposite seu dinheiro aqui: '))

                conta.depositar(valor)
        
            case 2:

                valor = int(input('Digite o valor do saque: '))

                conta.sacar(valor)  

                print('Saque realizado!')

            case 3:
            
                conta.get_saldo()
                    
            case 4:
            
                print('Saindo...')
            
                break

            case _:
            
                print('Opção invalida')


#Rpg
class Personagem():

    def __init__(self, nome):

        self.__nome = nome
        
        self.__vida = 100
   
        
    def dano (self, dano):

        self.__vida -= dano

        
    def vida(self,vida):
       
       print(self.__vida)

class Mago(Personagem):
    
    def bola_de_fogo(self, inimigo):

        dano  = 20

        inimigo.dano(dano)
        
        print('Fireball!')

    def luz_sagrada(self, inimigo):
        
        dano = 25

        inimigo.dano(dano)

        print('Holy light!')

class Paladino(Personagem):    

    def perfuraçao(self, inimigo):
        
        dano = 20

        inimigo.dano(dano)

        print('Perfuração!')

    def espada_arcanjo(self, inimigo):

        dano= 25

        inimigo.dano(dano)

        print('Espada Arcanjo!')

class Druida(Personagem):   

    def vinhas(self, inimigo):
    
        dano = 25

        inimigo.dano(dano)

        print('Vinhas!')
        
    def raizes(self, inimigo):

        dano = 20

        inimigo.dano(dano)

        print('Raizes!')

        
if __name__== '__main__':
    
    Mago= Personagem()
    Druida= Personagem()
    Paladino= Personagem()

    while True:
        def change():
        
            print('1- Druida') 
            print('2- Paladino') 
            print('3- Mago') 
            print('4- Sair do jogo') 

            escolha = int(input('Escolha sua classe: ')) 
        
        match escolha: 

            case 1: 

                druida = Druida('Malfurion') 

                print('Você escolheu Druida') 

            case 2: 
            
                paladino = Paladino('Arthur') 

                print('Você escolheu Paladino') 

            case 3: 
                mago = Mago('Gudan') 

                print('Você escolheu Mago!') 

            case 4:
            
                print('Saindo..') 

                break 

            case _: 

             print('Opçao invalida')





    
    


