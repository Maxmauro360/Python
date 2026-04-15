#Lista: representa uma sequencia de valores 
Listinha = f'[M, a ,x]'
print(f'ordenação: \n{Listinha}')

n1 = [1,2,3,4,5,6]
n2 = [7,8,9,0]

n3 = n1 + n2
print(n3)
print(f'Valor referente a ordem:\n{n3[4]}')
#começa do 0
print(f'Quantidade de valores: \n{len(n3)}') 

print(f'Valores de tras para frente:\n{sorted(n3, reverse= True)}')

print(f'valores somados: \n {sum(n3)}')

print(f'valor minimo: \n {min(n3)}')

print(f'valor máximo: \n {max(n3)}')

n3.append(77)
print(f'valor anexado: \n {n3}')

n3.pop(2)
print(f'valor desanexado: \n {n3}')

n3.insert(5,22)
print(f'valor inserido: \n {n3}')
#position/number
print(12 in n3 ) #verifica se há o numero na lista

# planets = ['Mercurio', 'Venus', 'Terra', 'Marte', 'Jupiter' , 'Saturno', 'urano', 'Netuno']
# for planet in planets:
#    print(planet)

# planets.append(f'Krypto')
# print(planets)

drinks = []
for i in range(5):
   drink = input(f'Type your favorite drink: \n')
   drinks.append(str(drink))

drinks.sort()
print(f'\ndrinks challengers:')
for drink in drinks:
   print(drink)
print(f'cheers!')


