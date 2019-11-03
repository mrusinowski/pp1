tab = []
print('Uporządkowane liczby: ',end='')
with open('numbers.txt','r') as file:
    for line in file:
        liczba = int(line)
        tab.append(liczba)
tab.sort()
for x in tab:
    print(x,end=' ')