from collections import deque
import requests

class Clima():

    def __init__(self):
        self.coletanea= deque()
    respostas = requests.get("")
    Estado = requests.get("Maps")
    Cidade = requests.get("Maps")

    estado.append(Estado)
    cidade.append(Cidade)

    def tempo(self,estado, cidade, clima):
        while True:
            try
                Estado = str(input("Digite o estado:\n "))
                Estado = str(input("Digite a cidade:\n"))
                lista = {
                    "Estado": estado,
                    "Cidade": cidade,
                    "Clima":clima
                }
            except ValueError:
                print(f'Números não são aceitos')
            break

if __name__== '__main__':
    Clima()

