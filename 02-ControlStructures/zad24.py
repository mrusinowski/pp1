imiona = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy", "Teofil"]
najdluzsze = imiona[0]
for imie in imiona:
    if len(najdluzsze) < len(imie):
        najdluzsze = imie
print(f"Najdłuższe imię: {najdluzsze}")