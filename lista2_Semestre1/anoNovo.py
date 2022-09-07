d1 = int(input())
comida, refri, deco = input().split()
comida = float(comida)
refri = float(refri)
deco = float(deco)

d2 = int(input())
comida2, refri2, breja, deco2 = input().split()
comida2 = float(comida2)
refri2 = float(refri2)
breja = float(breja)
deco2 = float(deco2)

if d1 == 20:
    totalD1 = (comida - comida * 0.12) + (refri - refri * 0.15) + (deco - deco * 0.2)
elif d1 == 21:
    totalD1 = (comida - comida * 0.17) + (refri - refri * 0.22) + (deco - deco * 0.27)
elif d1 == 22:
    totalD1 = (comida - comida * 0.2) + (refri - refri * 0.22) + (deco - deco * 0.3)
elif d1 == 23:
    totalD1 = (comida - comida * 0.25) + (refri - refri * 0.29) + (deco - deco * 0.35)
elif d1 == 24:
    totalD1 = (comida - comida * 0.35) + (refri - refri * 0.35) + (deco - deco * 0.5)
else:
    totalD1 = comida + (refri - refri * 0.1) + (deco - deco * 0.15)

if d2 == 25:
    totalD2 = (comida2 - comida2 * 0.15) + (refri2 - refri2 * 0.13) + (breja - breja * 0) + (deco2 - deco2 * 0.1)
elif d2 == 26:
    totalD2 = (comida2 - comida2 * 0.19) + (refri2 - refri2 * 0.25) + (breja - breja * 0.05) + (deco2 - deco2 * 0.23)
elif d2 == 27:
    totalD2 = (comida2 - comida2 * 0.24) + (refri2 - refri2 * 0.3) + (breja - breja * 0.12) + (deco2 - deco2 * 0.33)
elif d2 == 28:
    totalD2 = (comida2 - comida2 * 0.3) + (refri2 - refri2 * 0.32) + (breja - breja * 0.2) + (deco2 - deco2 * 0.35)
elif d2 == 31:
    totalD2 = (comida2 - comida2 * 0.4) + (refri2 - refri2 * 0.47) + (breja - breja * 0.45) + (deco2 - deco2 * 0.66)
else:
    totalD2 = (comida2 - comida2 * 0.35) + (refri2 - refri2 * 0.4) + (breja - breja * 0.33) + (deco2 - deco2 * 0.42)

print(f'Compras de natal: R$ {totalD1:.2f}.')
print(f'Compras de ano novo: R$ {totalD2:.2f}.')
print(f'Total das compras: R$ {totalD2 + totalD1:.2f}.')
