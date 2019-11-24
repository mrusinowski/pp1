import csv
import statistics

with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    y = 1
    print(f'#\tSURNAME\t\tNAME\t\tAGE\tEMAIL')
    print('='*75)
    r = list(reader)
    r.pop(0)
    age = []
    for row in r:
        print(f'{y}\t{row[0]}\t\t{row[1]}\t\t{row[2]}\t{row[3]}')
        y += 1
        age.append(int(row[2]))
    print(f'Średnia arytmetyczna wieku pracowników wynosi {statistics.mean(age)}')