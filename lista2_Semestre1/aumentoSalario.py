salario = float(input())

if salario <= 280:
    print(salario + 0.2 * salario)
elif 280 < salario <= 700:
    print(salario + 0.15 * salario)
elif 700 < salario <= 1500:
    print(salario + 0.1 * salario)
else:
    print(salario + 0.05 * salario)