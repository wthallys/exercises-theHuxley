metroCubico, custoLitro = input().split()
metroCubico = float(metroCubico)
custoLitro = float(custoLitro)
custoAgua = metroCubico * 1000 * custoLitro
custoEsgoto = 0.8 * custoAgua
print('{:.2f}'.format(custoAgua))
print('{:.2f}'.format(custoEsgoto))
print('{:.2f}'.format(custoAgua + custoEsgoto))