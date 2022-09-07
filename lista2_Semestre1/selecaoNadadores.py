idade = int(input())

if 0 <= idade <= 10:
    print('infantil')
elif 11 <= idade <= 14:
    print('junior')
elif 15 <= idade <= 20:
    print('adolescente')
elif 21 <= idade <= 35:
    print('jovem')
else:
    print('master')
