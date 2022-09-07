nota1 = float(input('Informe a primeira nota:'))
nota2 = float(input('Informe a segunda nota:'))
nota3 = float(input('Informe a terceira nota:'))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f'Aprovado com media {media:.1f}')
elif 5 <= media < 7:
    print(f'Recuperacao com media {media:.1f}')
else:
    print(f'Reprovado com media {media:.1f}')