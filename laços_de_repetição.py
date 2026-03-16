#while

num = 2
#while(num <= 20):
    #print(num)
   # num += 2
#print('lace finished!')

name = None
#while True:
    #print('type your name, or press x to stop')
    #name = input()
    #if name == 'x' or name == 'X':
      #  break
    
    #msg = f"welcome, {name}"
    #print(msg)
#print('See you later!')

#lace 'for' - iteração em estrututras de dados
# executa comandos em itens sequenciais (for 'item' in 'sequencia')

lista = [2,4,6,8,10,12,14]
word = 'max_mauropc'

#for letter in word:
    #print(letter)0

for number in range(1,11):
    print(number)
#the last number never will be allocated

name = input('your name:')
for x in range(10):
    print(f'{x+1} {name}')
    
    #range(valor inicial, valor fianl, incremento{'2 em 2', '3 em 3'})

for x in range (2,20,2):
    n = 'x'
    incr = f'{x} {n}'
    #print(incr)

stones = ('rubi', 'esmeralda', 'quartzo', 'saphira', 'diamond', 'turmalina')
for stone in stones:
    if stone == 'diamond':
     continue
    print(stone)
