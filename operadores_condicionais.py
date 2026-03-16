#simple, composto, encadeado

n1 = n2 = n3 = 0.0
media = 0.0
n1 = (float(input('type the first note: ')))
n2 = (float(input('type the second note: ')))

media = (n1 + n2) / 2

if ( media >= 7):
    print('Result: Aproved! ' , '\n' + 'Congratulations!' )
        # broken line '\n
elif ( media >= 5):
    print('you are in recovery...')
else:
    print(' Result: Reproved' ,'\n' + 'Wasted :(' )
print('your media are:' + str(media))
# print('your media are: {}'.format(media))