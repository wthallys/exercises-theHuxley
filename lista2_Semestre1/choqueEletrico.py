level = int(input())

if 1 <= level <= 20:
    print('Potencia de :', 20 + level ** 3, 'W')
elif 21 <= level <= 40:
    print('Potencia de :', 8000 + (level - 10) ** 2, 'W')
elif 41 <= level <= 60:
    print('Potencia de :', 9000 + level * 5, 'W')
elif 61 <= level <= 80:
    print('Potencia de :', 9300 + level * 2, 'W')
else:
    print('Potencia de :', 9500 + level, 'W')
