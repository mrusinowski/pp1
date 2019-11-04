reduta = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
def samogloski(reduta):
    samo = ['a','A','ą','e','ę','i','I','o','u','y']
    czesto = 0
    for x in reduta:
        if x in samo:
            czesto += 1
    return czesto

print(f'W tym tekście jest {samogloski(reduta)} samogłosek')