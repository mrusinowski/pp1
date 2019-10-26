sumap = 0
sumanp = 0
for i in range(0,51):
    if i % 2 == 0:
        sumap += i
    else:
        sumanp += i
print("Suma liczb parzystych w przedziale <0,50> wynosi {}".format(sumap))
print("Suma liczb nieparzystych w przedziale <0,50> wynosi {}".format(sumanp))