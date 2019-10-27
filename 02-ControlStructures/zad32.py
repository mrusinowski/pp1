znaki = input("Wprowadź dowolny ciąg znaków: ")
for x in range(0, len(znaki)):
    print(znaki[len(znaki)-x-1], end=" ")
