cv, ce, cs, fv, fe, fs = input().split()
pontosC = int(cv) * 3 + int(ce)
pontosF = int(fv) * 3 + int(fe)
if pontosC == pontosF:
    if int(cs) > int(fs):
        print('C')
    elif int(cs) < int(fs):
        print('F')
    else:
        print('=')
elif pontosC > pontosF:
    print('C')
else:
    print('F')
