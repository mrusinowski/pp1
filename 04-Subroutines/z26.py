def podatek(dochod):
    if dochod <= 5000:
        return 0.17*dochod
    else:
        return 0.17*5000 + 0.32*(dochod-5000)
    
kwota = int(input('Podaj dochód: '))
print(f'Podatek należny: {int(podatek(kwota))} zł')