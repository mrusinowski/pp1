import csv
import statistics

with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    r = list(reader)
    r.pop(0)
    age,y = [],1
    for row in r:
        y += 1
        age.append(int(row[2]))
    mean = statistics.mean(age)
    median = statistics.median(age)
    deviation = statistics.pstdev(age)
    print(f'''Średnia arytmetyczna: {mean}\n
Mediana: {median}\n
Odchylenie standardowe: {deviation}
''')