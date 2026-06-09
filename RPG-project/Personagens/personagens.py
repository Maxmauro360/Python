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