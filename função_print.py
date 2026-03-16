name = input('type your name:')
msg = 'bonjour,'
msg1 = 'passe une excellente journée'
#print(msg + name, msg1)

k = 'imprime a mensagem e muda de linha'
l = 'imprime a mensagem e permanance na linha.'
m = ' imprime a mensagem e continua '
#print(k,'\n', l, end=''+ m ) # (end ='') faz com que a proxima linha se junte com a que esta escrito

print('imprime a msg e muda de linha')
print('imprime a msg e contiua na msma linha.', end='')
print('imprime a msg e continua')

name = 'max'
age = '22'
msg_formatada = 'his name is {0} and he have {1} years old'.format(name, age)
#print(msg_formatada)

name = 'Anthony'
wheight = 25.7
msg = f'hello, my name is {name} and i wheight {wheight} kilograns'
#print(msg)

a = 10
b = 10
#print(f'the sam of {a} with {b} is {a + b}')

value = 987.654321
#print(f'the value is {value:.2f}') 
#numeros de pontos flutuantes '.2f'exibirá 2 numeros após o ponto

name = 'Max'
age = '22'
print(f'name:{name:}\t age:{age}')
# '\t' caracter de escape, dá espaço