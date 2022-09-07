livros = int(input())
alunos = int(input('s'))
conceito = alunos // livros

if conceito <= 8:
    print('A')
elif 9 <= conceito <= 12:
    print('B')
elif 13 <= conceito <= 18:
    print('C')
else:
    print('D')
