from collections import deque
import requests, pprint

class Clima():
    
    def __init__(self):
        self.coletanea= deque()

    def tempo(self):       
        while True:

            try:
                estado = str(input("Digite o estado:\n "))
                cidade = str(input("Digite a cidade:\n"))
                URL = 'https://geocoding-api.open-meteo.com/v1/search'
                URL_2 ='https://api.open-meteo.com/v1/forecast'
                parametros = {
                    "name":f"{cidade}, {estado}",
                    "count": 1,
                    "countryCode": "br"
                }
               
                respostas = requests.get(URL, params=parametros)
                if respostas.status_code == 200:
                    dados_aquisiçao = respostas.json()
                    pprint.pprint(dados_aquisiçao)

                    if dados_aquisiçao.get("results"):
                        latitude = dados_aquisiçao["results"][0]["latitude"]
                        longitude = dados_aquisiçao["results"][0]["longitude"]
                   

                        parametros_2= {
                        "latitude": latitude,
                        "longitude": longitude,
                        "current": "temperature_2m, weather_code",
                        "timezone": "America/Sao_Paulo"
                        }

                        respostas_2 = requests.get(URL_2, params=parametros_2)

                        if respostas_2.status_code == 200:
                            dados_aquisiçao_2 = respostas_2.json()
                            pprint.pprint(dados_aquisiçao_2)
                            temperatura= dados_aquisiçao_2["current"]["temperature_2m"]
                            previsao = dados_aquisiçao_2["current"]["weather_code"]
                        #   pprint.pprint(dados_aquisiçao)
                        # pprint.pprint(dados_aquisiçao_2)


                            registro = {
                            "Cidade": cidade,
                            "Estado": estado,
                            "Temperatura":temperatura,
                            "Previsão": previsao
                            }
                        
                            self.coletanea.append(registro)
                            print(registro)
                            
                    else:
                        print("Cidade não encontrada.")

            except (ValueError, KeyError, IndexError, TypeError) as erro:
                print(f'Não foi possivel acessar:{erro}')
           
            serviço = input(f"Para continuar aperte enter ou digite 's' para sair: \n")

            if serviço.lower() == 's':
                break

if __name__== '__main__':
    programa = Clima()
    programa.tempo()






