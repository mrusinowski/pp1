kwota = int(input("Podaj kwotę w zł: "))
if kwota >= 5:
    p = int(kwota/5)
    d = int((kwota%5)/2)
    if kwota-p*5-d*2>0:
        j = 1
    else: j = 0
elif 5 > kwota >= 2:
    p = 0
    d = int(kwota/2)
    j = kwota%2
else:
    p = 0
    d = 0
    j = kwota
print(f"Kwota {kwota} zł w monetach:")
print(f"5 zł - {p} szt")
print(f"2 zł - {d} szt")
print(f"1 zł - {j} szt")