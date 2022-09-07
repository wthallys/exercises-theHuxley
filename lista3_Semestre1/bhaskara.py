import re
import math

n = int(input())

for i in range(n):
    texto = input()
    dig = [int(s) for s in re.findall(r'-?\d+\.?\d*', texto)]

    a = dig[0]
    b = dig[2]
    c = dig[3]

    delta = b ** 2 - 4 * a * c

    if delta == 0:
        x = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Test {i+1}", ":", a, "x^2 +", b, "x +", c)
        print(f"X = {x:.2f}")

    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Test {i+1}", ":", a, "x^2 +", b, "x +", c)
        print(f"X1 = {x1:.2f}")
        print(f"X2 = {x2:.2f}")

    else:
        x = 0
        print("SEM RESPOSTA")