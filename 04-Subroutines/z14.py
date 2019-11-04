def wystepuje(liczba,tablica):
    print(f'Liczba: {liczba}')
    print('Tablica: ',end='')
    for x in tablica:
        print(x,end=' ')
    if liczba in tablica:
        print('\nRezultat: Podana liczba występuje w tablicy')
    else: print('\nRezultat: Podana liczba nie występuje w tablicy')
wystepuje(23,[15,38,7,23,14])