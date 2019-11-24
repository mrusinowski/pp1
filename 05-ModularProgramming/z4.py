import math

x = 3.7
y = 4

sqrtX = math.sqrt(x)
powXY = math.pow(x,y)
sqrtXY = math.pow(x,1/y)
circfY = math.pi*(y**2)
factY = math.factorial(y)
floorX = math.floor(x)

print(f'''Pierwiastek kwadratowy z {x} wynosi {sqrtX}\n
{x} do potęgi {y} wynosi {powXY}\n
Pierwiastek {y}-tego stopnia z {x} wynosi {sqrtXY}\n
Pole koła o promieniu {y} wynosi {circfY}\n
Silnia {y} wynosi {factY}\n
Największą możliwą liczbą całkowitą, mniejszą bądź równą {x} jest {floorX}
''')