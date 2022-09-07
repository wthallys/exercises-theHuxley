numero = int(input())
if numero >= 0:
    print(numero % 10)
else:
    inverte = numero * -1
    print((inverte % 10) * -1)