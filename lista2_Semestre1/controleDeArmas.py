nacionalidade = input()
ocupacao = input()
armas = int(input())
calibre = int(input())

if nacionalidade == 'B':
    if ((ocupacao == 'T' or 'O') and armas <= 1 and calibre <= 22) or (ocupacao == 'C' and armas <= 2 and calibre <= 38):
        print('Liberado')
    elif ocupacao == 'M' and armas >= 0 and calibre >= 0:
        print('Liberado')
    else:
        print('Barrado')
else:
    if ocupacao == 'T' and armas == 0 and calibre == 0:
        print('Liberado')
    else:
        print('Barrado')
