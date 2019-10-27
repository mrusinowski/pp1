p = int(input("Podaj pierwszą liczbę: "))
d = int(input("Podaj drugą liczbę: "))
t = int(input("Podaj trzecią liczbę: "))
liczby = [p, d, t]
liczby.sort()
mediana = liczby[1]
print(f"Mediana wynosi {mediana}")