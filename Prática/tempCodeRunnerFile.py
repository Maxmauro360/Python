lista =[]
def palavras(qdt):
     for nome in range(qdt):
         nome= input('digite uma palavra: \n')
         lista.append(nome)
     for palavra in lista:
         contador = 0
         for letra in palavra:
             if letra.lower() in 'aeiou':
                contador +=1
         print(f'A palavra "{palavra} tem "{contador}" vogais')
     return lista

if __name__=='__main__':
     print(palavras(1))