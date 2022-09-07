def converte(segundos):
    segundos = segundos % (24 * 3600)
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    print(horas,'h',minutos,'m',segundos,'s')

num = int(input())
converte(num)