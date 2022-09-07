sexo = input()
tempo = int(input())
salario = float(input())

if sexo == 'h' and tempo > 15:
    print(f'{salario + salario * 0.2:.2f}')
elif sexo == 'm' and tempo > 10:
    print(f'{salario + salario * 0.25:.2f}')
else:
    print(f'{salario + 200:.2f}')
