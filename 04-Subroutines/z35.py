def suma_cyfr(n):
    if n > 0:
        return int(n%10 + suma_cyfr(n/10))
    else:
        return 0

l = int(input('Wprowadź liczbę naturalną: '))
print(f'Suma cyfr tej liczby wynosi: {suma_cyfr(l)}')