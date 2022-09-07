inteiro = int(input())
dias = ['Domingo', 'Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
if 0 < inteiro <= len(dias):
    print(dias[inteiro-1])
else:
    print('Valor invalido')
