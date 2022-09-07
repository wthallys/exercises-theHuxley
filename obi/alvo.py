xa, ya = input().split()
xa = int(xa)
ya = int(ya)
xb, yb = input().split()
xb = int(xb)
yb = int(yb)
xc, yc = input().split()
xc = int(xc)
yc = int(yc)

distAC = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
distBC = ((xb - xc) ** 2 + (yb - yc) ** 2) ** 0.5

if distAC < distBC:
    print(f'A - {distAC:.2f}')
else:
    print(f'B - {distBC:.2f}')
