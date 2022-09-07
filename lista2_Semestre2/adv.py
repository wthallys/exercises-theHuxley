nJogos = int(input())

for nJogo in range(nJogos):
    tamSenha = input()
    senha = input()
    while True:
        tentativa = input()
        countExcelente = 0
        countBom = 0
        jaChutadosExcelente = ""
        jaChutadosBons = ""
        if senha == tentativa:
            print("({},0)".format(tamSenha))
            break
        else:
            for j in range(len(tentativa)):
                if tentativa[j] == senha[j]:
                    countExcelente += 1
                    jaChutadosExcelente += senha[j]
                elif (tentativa[j] in senha) and (tentativa[j] not in jaChutadosBons) and (
                        tentativa[j] not in jaChutadosExcelente):
                    countBom += 1
                    jaChutadosBons += tentativa[j]
            if tentativa == "0" * int(tamSenha):
                break
            elif countExcelente == 0 and countBom == 0:
                print("(0,0)")
            else:
                print("({},{})".format(countExcelente, countBom))
