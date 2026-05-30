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