grana = 300
city = "SEM DESTINO"
km = 0
while True:
    try:
        city_temp = input()
    except EOFError:
        break
    if city_temp == "FIM":
        break
    elif city_temp == "":
        print("SEM DESTINO")
        break
    else:
        try:
            km_temp = int(input())
        except EOFError:
            break
        passagem = 2 * float(input())
        if passagem <= 300:
            if km_temp > km:
                km = km_temp
                city = city_temp
    
print(city.upper())