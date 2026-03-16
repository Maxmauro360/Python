#are immutables, fast for iteration

tuple = (2, 3, 4, 5, 6, 8)
#print(tuple)
#não consegue atribuir depois que ja foi criada
gases_nobres = ['HE','Ne','Ar','Kr','Xr','Rn','Og']
halogenios = ['F', 'Cl', 'Br', 'I' ,'At'] 
tabela = gases_nobres + halogenios
print(tabela)
t1 = (1,2,3,4,4,4,4,5,6,2,4,53,5,434,43,4)
print(tabela[8])
#print(len(halogenios[4])) #função len, serve para ver tamanho
                   # numero usado para ver o elemento
print ('Fe'in tabela)            
#usado para ver se existe na tabela (in)   
print(sum(t1))    

#operação não disponivel em tuplas
#.sort(), .append(), .reverse(), .pop()..
for banana in tabela:
  print(f'elementos:{banana}')

print(sorted(tabela)) #organiza em ordem alfabetica