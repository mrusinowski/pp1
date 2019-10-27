pin = "0805"
proby = 0
while True:
    if proby == 3:
        print("Karta płatnicza zostaje zablokowana")
        break
    pin1 = input("Podaj PIN: ")
    if pin1 == pin:
        print("PIN poprawny")
        break
    else:
        print("Kod PIN niepoprawny")
        proby += 1