salario = float(input())
bonus = salario * 0.75
if bonus < 2000:
    print('ARGENTINA')
elif 2000 <= bonus <= 3000:
    print('ESPANHA')
else:
    print('ALEMANHA')
