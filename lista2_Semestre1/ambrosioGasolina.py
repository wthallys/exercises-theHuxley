d, r, l, p, g = input().split()
d = int(d)
r = int(r)
l = int(l)
p = int(p)
g = int(g)

quantoBotar = (d - (l * 10)) / 10 * g

if l * 10 < d:
    localPosto = d / (p + 1)
    if (l * 10 < localPosto) or (r - quantoBotar < 0):
        print('Nao pode viajar.')
    else:
        print('Pode viajar.')
        print(f'R$: {r - quantoBotar:.0f}')
else:
    print('Pode viajar.')
    print(f'R$: {r}')
