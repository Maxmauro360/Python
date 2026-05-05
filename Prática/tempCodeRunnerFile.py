guarda_roupa= []
def armario(qdt):
    for roupas in range(qdt):
        roupas = input('O que tem?:')
        guarda_roupa.append(roupas)

    resultado= []
    roupa_inversa=[]

    for roupas in guarda_roupa:
        vogais=0
        for vogal in roupas:
            if vogal.lower() in 'aeiou':
                vogais += 1
        resultado.append(f'{roupas} tem {vogais} vogais')
        roupa_inversa.append(roupas[::-1])

        return resultado, roupa_inversa
if __name__== '__main__':
    armario(2) 