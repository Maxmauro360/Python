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