def calkowite():
    import random
    return random.randint(1,50)

p,n=0,0
for x in range(1000):
    l = calkowite()
    if l%2==0: p+=1
    else: n+=1
print('Dla 1000 liczb losowych z przedziału <1,50>:')
print(f'Liczby parzyste: {p/10}%')
print(f'Liczby nieparzyste: {n/10}%')