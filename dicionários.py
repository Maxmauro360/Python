dicionario = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo':'metais alcalinos',
    'densidade' : 0.534

}
print(f'elemento:  {dicionario['nome']}')
print(f'elemento:  {dicionario['densidade']}')
print(f'elemento:  {dicionario['grupo']}')
dicionario['período'] = 3 # se colocar o nome de uma chave que já existe, ela será trocada, caso ela não existir, será criada.

print(f'O dicionário possui {len(dicionario)} elementos')

#Atualizar uma entrada
# dicionario['grupo'] = 'Alcalinos' 
# print(dicionario)

# #Adicionar entrada
# dicionario['período'] =1
# print(dicionario)
# del dicionario['período'] #deletar entrada
# print(dicionario)

# dicionario.clear() #limpa o dicionário, ainda existe
# print(dicionario)

# del dicionario #apaga totalmente
# print(dicionario)

print(dicionario.items())
for simplifica in dicionario.items(): #retorna uma lista de tuplas, ou seja, imutaveis
    print(simplifica)

print(dicionario.keys())
for simplifica in dicionario.keys(): #atribuidores
    print(simplifica)

print(dicionario.values())
for simplifica in dicionario.values(): #valores atribuidos
    print(simplifica)

for j, k in dicionario.items():
    print(f'{j}: {k}') # mostra cmo se fosse um pequeno relatório
                        # são variaveis de controle