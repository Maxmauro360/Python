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

if __name__ =='__main__':
    meu_veiculo= Veiculo("GM", 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('490312-1')
    print(f'Registro: {meu_veiculo.get_num_registro()}')