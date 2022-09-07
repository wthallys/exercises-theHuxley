def verifica(palavra):
    if palavra == "":
        return True
    else:
        for c in range(len(palavra)):
            if palavra[c] in numbers:
                return False


def invert(word):
    invertida = ""
    word = word.lower()
    for i in range(len(word) - 1, -1, -1):
        invertida += word[i]
    return invertida


def leet(invertida):
    global count
    for i in range(len(invertida)):
        if invertida[i] == "a":
            invertida[i] = "@"
            count += 1
        elif invertida[i] == "e":
            invertida[i] = "3"
            count += 1
        elif invertida[i] == "i":
            invertida[i] = "1"
            count += 1
        elif invertida[i] == "o":
            invertida[i] = "0"
            count += 1
        elif invertida[i] == "t":
            invertida[i] = "7"
            count += 1
        elif invertida[i] == "s":
            invertida[i] = "5"
            count += 1
    return invertida


numbers = "0123456789"
palavra = input()
count = 0

if verifica(palavra):
    print("vazio")
    print(0)
elif verifica(palavra) == False:
    print("numeros")
    print(0)
else:
    invertida = invert(palavra)
    tmp = list(invertida)
    tmp = "".join(leet(tmp))
    print(tmp)
    print(count)
