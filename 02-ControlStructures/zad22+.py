suma = 0
tab = [15, 8, 31, 47, 2, 19]
n = len(tab)
for i in tab:
    if i % 2 != 0:
        suma += i
        n += 1
print(f"średnia arytmetyczna wynosi: {suma/n}")