uni = []
with open('universities.txt','r') as file:
    for n in file:
        uni.append(n)
uni.sort()
with open('universities.txt', 'w') as file:
    for u in uni:
        file.write(u)