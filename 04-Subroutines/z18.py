def silnia(n):
    #0!=1 oraz 1!=1
    if n==0 or n==1:
        return 1
    #n! = n * (n-1)!
    if n > 1:
        return n * silnia(n-1)

n = int(input'Wprowadź liczbę: '))
print( f'n! = {silnia(n)}' )