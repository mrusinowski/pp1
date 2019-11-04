tablica = [4,3,7,1,3]
def suma(tablica):
    sum = 0
    print('Tablica: ',end='')
    for x in tablica:
        sum += x
        print(x,end=' ')
    print(f'\nSuma wartości: {sum}')
suma(tablica)