def bezpowt(t):
    tab = []
    for x in t:
        if t.count(x) < 2:
            tab.append(x)
        else: pass
    return tab
        
tablica = [0,8,6,0,8,1,2,5,3,1,3,0,8,1,4]
print(bezpowt(tablica))