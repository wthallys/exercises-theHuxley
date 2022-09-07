dias = int(input())
km = int(input())
total = dias * 30 + km * 0.01
print('{:.2f}'.format(total - 0.1 * total))