with open('NoEducation.txt','r') as file:
    x = 0
    for line in file:
        x += 1
        print(f'{x} {line}', end='')