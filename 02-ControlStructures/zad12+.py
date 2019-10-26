x = int(input("Wprowadź dane: "))
y = int(input("Wprowadź dane: "))

if x<0 and y<0:
    print("Wartość {} i wartość {} są ujemne".format(x,y))
elif x<0 and y>=0:
    print("Wartość {} jest ujemna, a wartość {} nie jest ujemna".format(x,y))
elif x>=0 and y<0:
    print("Wartość {} nie jest ujemna, a wartość {} jest ujemna".format(x,y))
else:
    print("Wartość {} i wartość {} nie są ujemne".format(x,y))