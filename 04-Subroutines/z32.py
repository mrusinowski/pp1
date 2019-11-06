def transpozycja(macierz):
    t = []
    for i in range(3):
        t.append([row[i] for row in macierz])
    for w in range(3):
        for k in range(3):
            if k==0 and w>0:
                print(f'\n{t[w][k]}', end=' ')
            else: print(t[w][k], end=' ')

m = [[1, 2, 0],[0, 0, 3],[5, 1, 1]]
print('Macierz:')
for w in range(3):
    for k in range(3):
        if k==0 and w>0:
            print(f'\n{m[w][k]}', end=' ')
        else: print(m[w][k], end=' ')
print('\n\nMacierz transponowana:')
transpozycja(m)