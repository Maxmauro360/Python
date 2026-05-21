#Orientação a objetos: Paradigma de Programação
#Classes e objetos

class Veiculo:
    def movimentar(self):
        print(f'Sou um veiculo')

    def __init__(self, fabricante,modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    #Setter--Gravar um dado dentro de um elemnto da classe
    def set_num_registro(self, registro):
        self.__num_registro = registro

    #Getter -- para acessar itens encapsulados
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}. \n')

    def get_num_registro(self):
        return self.__num_registro

class Carro(Veiculo): #a classe carro é um tipo de veiculo
    #método __init__ será herdado
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas')

class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'Corro muito!')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat= categoria
        super().__init__(fabricante, modelo) #super classe -- Classe da qual o aviao herda
                                            #referencia direta da classe init
        
    def get_categoria(self):
        return self.__cat
    
    def movimentar(self):
        print('Eu voo alto!')

if __name__ =='__main__':
    meu_veiculo= Veiculo("GM", 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('490312-1')
    print(f'Registro: {meu_veiculo.get_num_registro()}')

    meu_carro = Carro('Mitsubish','Lancer')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()
    
    seu_carro = Carro('Volkswagen', 'Polo')
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()

    moto = Motocicleta(f'Harley Davidson', 'Nighter Special')
    moto.movimentar()
    moto.get_fabr_modelo()

    meu_aviao = Aviao ('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria: {meu_aviao.get_categoria()}')