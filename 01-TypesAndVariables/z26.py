wzrost = float(input("Podaj wzrost w cm: "))
waga = float(input("Podaj wagę w kg: "))
BMI = waga/((wzrost*0.01)**2)
if BMI>=18.5 and BMI<=24.9:
    x = "waga prawidłowa"
else: x = "waga nieprawidłowa"
print("Wskaźnik BMI: {}({})".format(BMI,x))