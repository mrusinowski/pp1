def jestImie(imie,imiona):
    print(f'Imiona: {imiona}')
    print(f'Imie: {imie}')
    if imie in imiona:
        print('Rezultat: imię zawarte jest w wykazie imion')
    else:
        print('Rezultat: imię nie jest zawarte w wykazie imion')
        
tab = ['Janek','Ania','Wojtek','Zosia']
jestImie('Wojtek',tab)