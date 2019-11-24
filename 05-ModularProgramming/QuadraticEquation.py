def czytajWspolczynniki():
    a = int(input('Wprowadź a: '))
    b = int(input('Wprowadź b: '))
    c = int(input('Wprowadź c: '))
    return a,b,c
    
def obliczDelte(a,b,c):
    return b**2-(4*a*c)
    
def obliczPierwiastki(a,b,delta):
    if delta > 0:
        x1 = (-b+(delta**0.5))/2*a
        x2 = (-b-(delta**0.5))/2*a
        return x1,x2
    elif delta == 0:
        x1 = -b/2*a
        x2 = None
        return x1, x2
    else: return None,None
    
def wyswietlPierwiastki(x1,x2):
    if x1!=None and x2!=None:
        print(f'Pierwiastki równania: x1={x1}, x2={x2}')
    elif x1!=None and x2==None:
        print(f'Pierwiastek równania: x1={x1}')
    else: print('Brak pierwiastków równania.')