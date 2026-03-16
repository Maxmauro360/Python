age = 21
height = 1.78
result = (age >= 18) and (height >= 1.70)

msg = ('can you attend the event?' + str(result))
print()

#program alarm tigger

door = 'l'
window = 'o'
alarm = (door == 'l') or (window == 'l')
msg1 = ('alarm trigger? '  + str(alarm))
print(msg1)

have_money = False
have_money = not have_money                  #operador que inverte o estado lógico
msg2 = ('have money?' + str(have_money))
print(msg2)