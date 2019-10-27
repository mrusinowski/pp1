a = int(input("Wprowadź wysokość prostokąta: "))
b = int(input("Wprowadź długość prostokąta: "))

for x in range(a):
    if x==0:
        print(b*"*")
    elif x==a-1:
        print(b*"*")
    else:
        print("*"+" "*(b-2)+"*")