oceny = ["niedostateczny", "mierny", "dostateczny", "dobry", "bardzo dobry", "celujący"]
ocena = int(input("Podaj ocenę: "))
print("Ocena słownie: {}".format(oceny[ocena-1]))