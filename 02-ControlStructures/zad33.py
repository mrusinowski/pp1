nazwy = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
liczba = input("Wprowadź liczbę: ")
l = []
for x in str(liczba):
    l.append(int(x))
print("{} - ".format(liczba), end="")
for y in l:
    print(nazwy[y], end=" ")