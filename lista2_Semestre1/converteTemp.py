escala = input()
temp = float(input())
if escala == 'C':
    if temp >= -273.0:
        print(f'{(temp * 9 / 5) + 32:.2f} F')
        print(f'{temp + 273.15:.2f} K')
    else:
        print('Valor de temperatura abaixo do minimo')
if escala == 'F':
    if temp >= -459.67:
        print(f'{(temp - 32) * 5 / 9:.2f} C')
        print(f'{(temp - 32) * 5 / 9 + 273.15:.2f} K')
    else:
        print('Valor de temperatura abaixo do minimo')
if escala == 'K':
    if temp >= 0.0:
        print(f'{temp - 273.15:.2f} C')
        print(f'{(temp - 273.15) * 9 / 5 + 32:.2f} F')
    else:
        print('Valor de temperatura abaixo do minimo')
