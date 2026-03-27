# coleçoes não ordenadas de valores unicos
#valores não duplicados, mutaveis, não tem como excluir, só adicionar

# planetinha = {'Plutão','Ceres','Eris','Haumea','Makemake'}
# print(len(planetinha))
# print('Ceres'in planetinha)
# print('Lua'in planetinha)
# print('Lua'not in planetinha)

# for astro in planetinha:
#     print(astro.upper())

# astros = ['Lua','Vênus','Lua','Marte','Lua']
# print(astros, end='---')
# astros_set = set(astros) #nos conjuntos não terão valores duplicados
# print(astros_set)

astros1 = {'Lua','Vênus','Lua','Marte','Lua', 'Io'}
astros2 = {'Lua','Vênus','Lua','Marte','Lua','cometa'}
# print(astros1 == astros2)
# print(astros1 | astros2)#uniao
# print(astros1.union(astros2))#uniao

# print(astros1 & astros2)#interseção
# print(astros1.intersection(astros2))#interseção

# print(astros1 ^ astros2)#diferença simetrica
# print(astros1.symmetric_difference(astros2))#diferença simetrica

astros1.add('Urano')
astros1.add('Sol')
astros1.remove('Io')#discard tbm funciona
astros1.pop() #remove de forma aleatória
print(astros1)
astros1.clear()