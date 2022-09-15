grana = 300
city = "SEM DESTINO"
km = 0
while True:
    city_temp = input()
    if city_temp == "FIM":
        break
    elif city_temp == "":
        print("SEM DESTINO")
        break
    else:
        km_temp = int(input())
        passagem = 2 * float(input())
        if passagem <= 300:
            if km_temp > km:
                km = km_temp
                city = city_temp

print(city.upper())