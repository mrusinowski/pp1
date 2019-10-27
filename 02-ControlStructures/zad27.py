d = int(input("Podaj największą długość: "))
dlugosc = d
for x in range(d+1):
    print("*"*x)
for y in range(d):
    dlugosc-=1
    print("*"*dlugosc) 