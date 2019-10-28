with open('shoppinglist.txt','w') as file:
    while True:
        produkt = input("Podaj nazwę produktu: ")
        if produkt == '':
            break
        file.write(produkt+"\n")