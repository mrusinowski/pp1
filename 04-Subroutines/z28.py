def rysujWykres():
    jezyki = ['Java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android']
    wartosci = [61,47,37,32,26,18,14,14,9,7]
    for x in range(0,len(jezyki)):
        print(f'\n{jezyki[x]}: ',end='')
        for y in range(0,wartosci[x]):
            print('#',end='')
rysujWykres()