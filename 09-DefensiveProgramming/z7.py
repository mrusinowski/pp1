wzrost = int(input('Wprowadź wartość wyrażona w cm: '))
waga = float(input('Wprowadź wartość wyrażona w kg: '))
assert type(wzrost)==int and 150<=wzrost<=220 and type(waga)==float and 40.0<=waga<=150.0
print(f'BMI wynosi: {waga/(wzrost/100)**2}')