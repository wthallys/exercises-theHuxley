while True:
    idade = int(input())
    if idade == 0:
        break
    else:
        if idade < 0:
            print("Você ainda não nasceu.")
        elif 1 <= idade <= 11:
            print("Você é uma criança.")
        elif 12 <= idade <= 17:
            print("Você é um adolescente.")
        elif 18 <= idade <= 35:
            print("Você é um jovem.")
        elif 36 <= idade <= 64:
            print("Você é um adulto.")
        else:
            print("Você é um idoso.")
