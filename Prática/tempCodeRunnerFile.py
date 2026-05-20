def lista_vogais():
    frase= 'Caia sete vezes, levante-se oito." Ensina sobre persistência e resíliência diante das adversidades dá vida.'
    acentuadas =['a', 'e', 'i', 'o', 'u','á','ê','í']

    palavras= []
    vogais= []

    total_frase = 0
    total_vogais = 0
    for i in frase.split():
        total_frase +=1
        palavras.append(i)

        for v in i.lower():
            if v in acentuadas:
                total_vogais +=1
                vogais.append(v)

                
    print(f'A frase possui: {total_frase} palavras')
    print(f'A frase possui: {total_vogais} vogais')
 
    return palavras, vogais

if __name__== '__main__':
    c = lista_vogais()
    print(c)