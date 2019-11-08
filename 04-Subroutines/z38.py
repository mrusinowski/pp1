def wielkielitery(txt):
    t = ''
    for x in txt:
        if x.isupper():
            t += str(x)
        else: pass
    return t

znaki = '#^sdK  NyAP{S.Dj1996 1wNA,..Ostsa'
print(wielkielitery(znaki))