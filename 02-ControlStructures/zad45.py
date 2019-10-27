N = int(input("Podaj ilość początkowych liczb pierwszych: "))
print("Liczby pierwsze:",end=" ")
dzielniki = 0
for x in range(2,N):
    for y in range(1, x+1):
        if x % y == 0:
            dzielniki += 1
    if dzielniki < 3:
        print(x,end=" ")
    dzielniki = 0