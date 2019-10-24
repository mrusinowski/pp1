x = int(input("Wprowadź dane "))

if x>0 and x%2!=0:
    print("Liczba {} jest dodatnia i nieparzysta".format(x))
elif x>0 and x%2!=1:
    print("Liczba {} jest dodatnia i nie jest nieparzysta".format(x))
elif x<=0 and x%2!=0:
    print("Liczba {} nie jest dodatnia i jest nieparzysta".format(x))
else:
    print("Liczba {} nie jest dodatnia i nie jest nieparzysta".format(x))