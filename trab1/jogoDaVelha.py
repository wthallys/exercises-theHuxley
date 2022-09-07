def tictactoe():  # criação da função do jogo da velha
    print("|=============================================|")
    print("|            JOGO DA VELHA EM PYTHON :D       |")
    print("|=============================================|")
    print("By: João Paulo and Wyddenberg Thallys")
    print()
    print("Para jogar deve-se fornecer a linha e a coluna, por exemplo: caso queira colocar o X na quina \n superior esquerda, informe linha: 0 e coluna: 0 e assim sucessivamente")
    print()
    print("Vamos lá, Diga Seus Nomes!!!")
    print()

    def linha():
        print("___________________________________________")

    a = input("Nome Do Jogador Um:  ")
    b = input("Nome Do Jogador Dois: ")

    print()
    print()
    print(a, "Vs", b, "!!!" " Que vença o MELHOR!!! :D")
    print()
    print()

    casas = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    jogador = False
    jogador2 = False
    vez = True

    jogadas = 0
    m = 0

    print(casas[0][0], "|", casas[0][1], "|", casas[0][2])
    print(casas[1][0], "|", casas[1][1], "|", casas[1][2])
    print(casas[2][0], "|", casas[2][1], "|", casas[2][2])

    while jogadas < 9:  # conta o número de jogadas válidas

        apontador = int(input("Linha:"))
        apontador2 = int(input("Coluna:"))

        print()

        while apontador > 2 or apontador2 > 2 and apontador < 0 or apontador2 < 0:  # verificando se a jogada é válida
            linha()
            print("Um ou mais valores invalidos!!!")
            print("Digite novamente!!!")
            linha()
            apontador = int(input("Linha:"))
            apontador2 = int(input("Coluna:"))

        while casas[apontador][apontador2] != "_":  # verificando se o lugar está ocupado
            print()
            print("Este lugar já esta ocupado!!")
            print()
            apontador = int(input("linha:"))
            apontador2 = int(input("coluna:"))

        if vez:
            casas[apontador][apontador2] = "x"

        elif not vez:
            casas[apontador][apontador2] = "o"

        print(casas[0][0], "|", casas[0][1], "|", casas[0][2])
        print(casas[1][0], "|", casas[1][1], "|", casas[1][2])
        print(casas[2][0], "|", casas[2][1], "|", casas[2][2])

        for i in range(3):

            if casas[m][0] == casas[m][1] and casas[m][2] == casas[m][1]:

                if casas[m][0] == "x":

                    jogador = True

                elif casas[m][0] == "o":

                    jogador2 = True
            m += 1
        m = 0

        for i in range(3):

            if casas[0][m] == casas[1][m] and casas[2][m] == casas[1][m]:

                if casas[0][m] == "x":

                    jogador = True

                elif casas[0][m] == "o":

                    jogador2 = True
            m += 1
        m = 0

        if casas[0][0] == casas[1][1] and casas[1][1] == casas[2][2]:

            if casas[0][0] == "x":

                jogador = True

            elif casas[0][0] == "o":

                jogador2 = True

        elif casas[0][2] == casas[1][1] and casas[1][1] == casas[2][0]:

            if casas[2][0] == "x":

                jogador = True

            elif casas[2][0] == "o":

                jogador2 = True

        jogadas += 1

        if jogadas % 2 == 0:

            print("Vez de", a)
            print()
            vez = True

        elif jogadas % 2 != 0:

            print("Vez de", b)
            print()
            vez = False

        if jogador:

            print("Parabéns", a, "Você Venceu!!!!!!!")
            break

        elif jogador2:
            print("Parabéns", b, "Você Venceu!!!!!!!!")
            break

        if jogadas >= 9:
            print("empate")


tictactoe()
