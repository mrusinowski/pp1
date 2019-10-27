import random
s = 0
p = 0
c = 0
t = 0
d = 0
j = 0
for x in range(0,101):
    rzut = random.randrange(1,7)
    if rzut == 6:
        s += 1
    elif rzut == 5:
        p += 1
    elif rzut == 4:
        c += 1
    elif rzut == 3:
        t += 1
    elif rzut == 2:
        d += 1
    else:
        j += 1
print(f"Szóstka: {s}")
print(f"Piątka: {p}")
print(f"Czwórka: {c}")
print(f"Trójka: {t}")
print(f"Dwójka: {d}")
print(f"Jedynka: {j}")
    