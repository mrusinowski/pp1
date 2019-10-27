limit = int(input("Podaj limit prędkości (km/h): "))
predkosc = int(input("Podaj prędkość pojazdu (km/h): "))
if limit < predkosc <= limit+10:
    mandat = 5*(predkosc-limit)
    print(f"Mandat (zł): {mandat}")
elif predkosc > limit+10:
    mandat = 5*10+15*(predkosc-limit-10)
    print(f"Mandat (zł): {mandat}")
else:
    print("Prędkość nie została przekroczona.")

