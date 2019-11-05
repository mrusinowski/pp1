def mediana(tab):
    tab.sort()
    return tab[int(len(tab)/2)]
    
def dominanta(tab):
    return max(set(tab), key=tab.count)

tab = [2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4]
print(f'Tablica: {tab} \nMediana wynosi: {mediana(tab)} \nDominanta wynosi: {dominanta(tab)}')