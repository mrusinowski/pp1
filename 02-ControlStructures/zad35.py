a = int(input("Wprowadź liczbę: "))
b = int(input("Wprowadź liczbę: "))
c = int(input("Wprowadź liczbę: "))
delta = b**2-4*a*c
if delta>0:
    mz1=(-b-delta**0.5)/(2*a)
    mz2=(-b+delta**0.5)/(2*a)
    print("Ta funkcja posiada dwa miejsca zerowe: {} i {}".format(mz1,mz2))
elif delta==0:
    mz0=-b/(2*a)
    print("Ta funkcja posiada jedno miejsce zerowe: {}".format(mz0))
else:
    print("Ta funkcja nie posiada miejsc zerowych.")