import statistics

salaries = [21600,4350,3920,5590,3250,4010]
mean = statistics.mean(salaries)
median = statistics.median(salaries)
deviation = statistics.pstdev(salaries)

print(f'''Wynagrodzenia: {salaries}[zł]\n
Średnia arytmetyczna: {mean} zł\n
Mediana: {median} zł\n
Odchylenie standardowe: {deviation} zł
''')