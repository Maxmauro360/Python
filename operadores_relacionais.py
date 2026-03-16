x = y = z = 0
n1 = n2 = False

print('type a number:')
n1 = int(input())

n2 = int(input('type other number:'))
x = n1== n2
print('are they the same?', x, '\n')

z = n1 > n2
print( n1, 'is greater than', n2, '?', z,'\n')

y = n1 != n2
print('are differents?' + str(y))
#por ser um operador de concatenação, a ',' não será utilizada
# print('are differents?', + str(y))