students = []
with open('students.txt', 'r') as file:
    for x in file:
        students.append(x.split(','))
for w in range(1, len(students)):
    if int(students[w][2]) < 30:
        print('{} {} {}'.format(students[w][0], students[w][1], students[w][-1]),end='')