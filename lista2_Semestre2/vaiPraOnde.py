grana = 300
cidade = {}
while True:
    city = input()
    if city == "0":
        break
    else:
        km = int(input())
        passagem = int(input())
        cidade[city] = [km, passagem]

cidadeNomes = cidade.keys()
print(cidadeNomes)

print(cidade.values())
