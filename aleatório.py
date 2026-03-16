import random

#print('generate 5 aleatory numbers between 1 and 50: \n')
#for i in range (1,6):
   # n = random.randint(1, 50)
   # print(f'number generate:\n{n}')

#v = random.random()
#print(f'number generated:\n {round(v * 20, 2)}'
#     )


# v = random.uniform(1,100)
# print(f'valor: \n{round(v, 2)}')

L = [1,2,3,4,5,6,7,8,9,0] 
# n = random.choice(L)
# print(f'Number chalanged: \n{n}')

# n = random.sample(L, 4)
# print(f'Number chalanged: \n{n}')

#embaralhar
print(f'exibir lista orignal: \n{L}'
      )
k = random.shuffle(L)
print(f'embaralhado:\n{L}')


