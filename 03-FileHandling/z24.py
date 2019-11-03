tab = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
t = 'Imie,Nazwisko,Email\n'
with open('dane.csv', 'w') as file:
    file.write(t)
    for x in tab:
        file.write(x[0]+','+x[1]+','+x[2]+'\n')