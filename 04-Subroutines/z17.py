import random
def rzucKostka():
    return random.randint(1,6)
suma = 0
y = 3
print('Wyrzucone oczka: ',end='')
for x in range(y):
    z = rzucKostka()
    suma += z
    print(z,end=' ')
print(f'\nSuma oczek: {suma}')