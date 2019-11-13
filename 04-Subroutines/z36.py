def sum(t):
    suma = 0
    for x in t:
        if isinstance(x,list):
            suma += sum(x)
        else:
            suma += x
    return suma

tab = [7,5,[3,6,[2]],7,[1,[2,3,[4]],9,2],4]
print(sum(tab))