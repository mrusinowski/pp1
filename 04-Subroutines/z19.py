def suma(N):
    if N != 0:
        return N + suma(N-1)
    else:
        return 0

suma(500)
print(f'Suma liczb wynosi: {suma(500)}')