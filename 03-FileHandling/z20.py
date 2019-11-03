liczby = []
with open('numbers.txt', 'r') as file:
    for x in file:
        if int(x)%2==0:
            liczby.append(x)
with open('evennumbers.txt', 'w') as file:
    for n in liczby:
        file.write(n)