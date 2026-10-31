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

        if self.__vida < 0:

            self.__vida = 0
   
    def ver_vida(self):
       
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

        def change():
        
            print('1- Druida') 
            print('2- Paladino') 
            print('3- Mago') 
            print('4- Sair do jogo') 

            return int(input('Escolha sua classe: ')) 
        
        jogador_1 = change()
        jogador_2 = change()
    
        while jogador_1 == jogador_2:

            print('Escolha outro personagem!')

            jogador_2= change()

        
        
        match jogador_1: 

                case 1: 
                    if jogador_1 ==1:


                        personagem1 = Druida('Malfurion') 

                    print('Você escolheu Druida') 

                case 2: 
                    if jogador_1 ==2:

                        personagem1= Paladino('Arthur') 

                    print('Você escolheu Paladino') 

                case 3: 
                    if jogador_1 ==3:
                    
                        personagem1 = Mago('Guldan') 

                    print('Você escolheu Mago!') 

                case 4:
            
                    print('Saindo..') 

                    exit()

                case _: 

                    print('Opçao invalida')

        
        match jogador_2: 

                case 1: 
                    
                    if jogador_2 ==1:
                    
                        personagem2 = Druida('Malfurion') 

                    print('Você escolheu Druida') 

                case 2: 
                    
                    if jogador_2 ==2:

                        personagem2 = Paladino('Arthur') 

                    print('Você escolheu Paladino') 

                case 3: 
                    if jogador_2 ==3:

                        personagem2 = Mago('Guldan') 

                    print('Você escolheu Mago!') 

                case 4:
            
                    print('Saindo..') 

                    exit()

                case _: 

                    print('Opçao invalida')

print('Combate iniciado!')

def personagem1_druida(Druida):

        def poder_druida():

            print('1-Raizes')
            print('2-Vinhas')
            print('3-Desistir')
        
            return int(input("Escolha seu poder: "))
        
        while True:
        
            escolha = poder_druida()

            match escolha:

                case 1:
                    personagem1.raizes(personagem2)

                    personagem2.ver_vida()

                case 2:
                    personagem1.vinhas(personagem2)
                    
                    personagem2.ver_vida()

                case 3:
                    print('Saindo da luta..')
                    print('jogador adversario venceu!')

                    exit()
                case _:
                    print('escolha um poder')

def personagem2_druida(Druida):
        
        def poder_druida():

            print('1-Raizes')
            print('2-Vinhas')
            print('3-Desistir')
        
            return int(input("Escolha seu poder: "))
        
        while True:
        
            escolha = poder_druida()

            match escolha:

                case 1:
                    personagem2.raizes(personagem1)

                case 2:
                    personagem2.vinhas(personagem1)

                case 3:
                    print('Saindo da luta..')
                    print(f'jogador adversario venceu!')
                    
                    exit()

                case _:
                    print('escolha um poder')




def decorator(func):

    def wrapper():
        print('antes')

        func()

        print('depois')

    return wrapper

@decorator
def aprender():
    print('estou aprendendo!')
    
aprender()


class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_barulho(self):
        print(f"{self.nome} fez algum barulho.")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        # Chama o __init__ da classe Animal para configurar o 'nome'
        super().__init__(nome)
        self.raca = raca
        
    def fazer_barulho(self):
        # Chama o método original da classe Animal e depois adiciona algo novo
        super().fazer_barulho()
        print(f"{self.nome} latiu: Au au!")

# Testando
meu_dog = Cachorro("Rex", "Labrador")
meu_dog.fazer_barulho()



def gerador():
    for i in range(2,20,3): 
        print(i)
        
if __name__ == '__main__':
    gerador()




import requests, pprint


api_key = '7d536fc724ec4a0389670626262910'
url = 'http://api.weatherapi.com/v1/current.json'

parametros = {
    "key": api_key,
    "q": "Rio de janeiro",
    "lang": "br"
}

#os parametros são necessarios pegar na documentação do site
# voce só conseguira acessar a api depois que colocar a key e outros parametros obrigatorios



res=requests.get(url, params= parametros)
#res=requests.get(url, params= parametros)
#dados = res.json()                        # tambem poderá ser feito desta forma
#print(dados)
print(res.content)
print(res.status_code)

if res.status_code== 200:   #verifica o status do codigo
    print(res.json())           #acessa os parametros necessarios
    pprint.pprint(res.json())   #acessa os parametros de forma mais clara

    temp = res.json()["current"]["temp_c"]
    print(temp)


    
    


