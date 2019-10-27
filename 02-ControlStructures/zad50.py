from math import floor
l = int(input("Podaj liczbę: "))
x = l
pom = 0
t = ""
print(f"{l}(10)=",end="")
while x != 0:
    b = x % 2
    p = x / 2
    x = floor(p)
    t = str(b) + t
print(f"{t}(2)")