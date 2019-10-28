tab = [32,16,5,8,24,7]
with open('tablica.txt','w') as file:
    for x in tab:
        file.write(f'{str(x)}\n')