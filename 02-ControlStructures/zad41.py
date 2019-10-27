n = 0
suma = 0
x = -1
while x != 0:
    x = int(input("Podaj liczbę: "))
    n += 1
    suma += x
print("REZULTAT: Liczb={}, Suma={}, Średnia={}".format(n,suma,suma/n))