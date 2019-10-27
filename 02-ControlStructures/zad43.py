p = int(input("Podaj pierwszą liczbę: "))
d = int(input("Podaj drugą liczbę: "))
t = int(input("Podaj trzecią liczbę: "))
tab = [p,d,t]
tab.sort()
print("Liczby w kolejności rosnącej: {}, {}, {}".format(tab[0],tab[1],tab[2]))