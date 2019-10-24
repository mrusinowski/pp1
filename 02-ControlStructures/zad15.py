l = int(input("Podaj liczbą: "))
c = 0
itersleft = 10
while(itersleft != 0):
    c += 1
    ans = l * c
    itersleft = itersleft - 1
    print(str(l) + "*" + str(c) + " = " + str(ans))