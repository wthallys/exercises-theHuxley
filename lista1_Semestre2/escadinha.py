import sys

num = int(input())

for i in range(num):
    for j in range(i+1):
        print(j + 1, end="")
        # sys.stdout.write(str(j + 1))
    print()