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