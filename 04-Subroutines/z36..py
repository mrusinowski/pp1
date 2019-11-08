tab = [7,5,[3,6,[2]],7,[1,[2,3,[4]],9,2],4]
suma = 0
for q in tab:
    if isinstance(q,list):
        x = q[0]
        for w in q:
            if isinstance(w,list):
                y = w[0]
                for e in w:
                    if isinstance(e,list):
                        z = e[0]
                        for r in e:
                            suma += r
                    else: suma += e
            else: suma += w
    else: suma += q
    
print(suma)