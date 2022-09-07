year = int(input())
period = int(input())

for i in range(3):
    print(year + period, end=" ")
    year += period
