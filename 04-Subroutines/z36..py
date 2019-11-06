tab = [7,5,[3,6,[2]],7,[1,[2,3,[4]],9,2],4]
suma,a = 0,0
for q in tab:
    if isinstance(q,list):
        x = q[a]
        for w in q:
            if isinstance(w,list):
                y = w[a]
                for e in w:
                    if isinstance(e,list):
                        z = e[a]
                        for r in e:
                            suma += r
                    else: suma += e
            else: suma += w
    else: suma += q
    
print(suma)