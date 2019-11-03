import re
suma = 0
with open('land.txt', 'r') as file:
    r = re.findall('[0-9]+', file.read())
    for x in r:
        suma += int(x)
print(f'Suma tych cyfr wynosi: {suma}')