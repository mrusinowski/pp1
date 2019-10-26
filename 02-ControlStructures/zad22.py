tab = [15,8,31,47,2,19]
sumanp = 0
n = 0
for i in tab:
    if i%2==1:
        sumanp += i
        n += 1
print(f"Średnia arytmetyczna wszystkich liczb w tab wynosi {sumanp/n}")