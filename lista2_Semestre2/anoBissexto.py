anoAtual = 2152

def contarDigito(year):
    if len(year) < 4:
        return False;
    else:
        return True;

def ehBissexto(year):
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True;
    else:
        return False;

def mensagem():
    if contarDigito(ano) == False:
        print("Ano invalido")
    else:
        if ehBissexto(ano) == True:
            if int(ano) < anoAtual:
                print("O ano {} foi bissexto".format(ano))
            elif int(ano) == anoAtual:
                print("O ano {} eh bissexto".format(ano))
            else:
                print("O ano {} serah bissexto".format(ano))
        else:
            print("O ano {} NAO eh bissexto".format(ano))


while True:
    ano = input()
    if ano == "-1":
        break
    else:
        mensagem()