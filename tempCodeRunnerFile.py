from functools import reduce

def mult (x,y):
    return x*y
numeros = [ 1,2,3,4,5,6,7,8]
total = reduce(mult, numeros)
print(total)