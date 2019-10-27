import random
rzut = random.randrange(1,7)
guess = int(input("Podaj, ile oczek kostki wyrzucił komputer: "))
if guess == rzut: x=True
else: x=False
print("Komputer wyrzucił: {}".format(rzut))
print("Zgadłeś: {} ({})".format(guess,x))