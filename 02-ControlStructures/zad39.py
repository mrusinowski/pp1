pierwszy = 0
drugi = 1
suma = 0
for x in range(0,51):
    suma = pierwszy + drugi
    print(pierwszy,end=" ")
    pierwszy = drugi
    drugi = suma