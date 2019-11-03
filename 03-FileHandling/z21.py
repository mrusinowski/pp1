liczby = []
suma = 0
with open('numbersinrows.txt', 'r') as file:
    for x in file:
        for y in x.split(','):
            liczby.append(int(y))
for y in liczby:
    suma += y
print("Ilość liczb: {}\nSuma liczb: {}".format(len(liczby),suma))