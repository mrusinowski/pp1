import re

komunikat = 'wtorek - 23C, środa - 21C, czwartek 25C '
cyfry = re.findall('\d{2}',komunikat)
srednia = int(cyfry[0])+int(cyfry[1])+int(cyfry[2])/int(len(cyfry))
print(srednia)