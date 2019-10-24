x = float(input("Podaj wiek psa w ludzkich latach "))

if x<=2:
    y=x*10.5
    print("Wiek psa w psich latach to {} lata".format(y))
else:
    y=(x-2)*4 + 2*10.5
    print("Wiek psa w psich latach to {} lata".format(y))