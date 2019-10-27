pesel = input("Podaj PESEL: ")
mezczyzna = [1, 3, 5, 7, 9]
wiek = pesel[0:7]
plec = ""

pmezczyzna = int(pesel[-2])
pwiek = wiek[0:2]
pmiesiac = wiek[2:4]

if pmezczyzna in mezczyzna:
    plec = "mężczyzna"
else:
    plec = "kobieta"
if int(pmiesiac) > 12:
    rok = 2000 + int(pwiek)
else:
    rok = 1900 + int(pwiek)
obecnywiek = 2018-rok
print("Płeć: {}".format(plec))
print("Wiek: {}".format(obecnywiek))