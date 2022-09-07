pi = 3.14
altura = float(input())
raio = float(input())
areaBase = pi * raio ** 2
circunferencia = pi * raio * 2
print('{:.2f}'.format(areaBase * altura))
print('{:.2f}'.format(areaBase * 2 + circunferencia * altura))