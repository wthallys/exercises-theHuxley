txt = input()
counted = {}
for x in txt:
  if x not in counted:
    frequency = txt.count(x)
    counted[x] = frequency

for value in sorted(counted.keys(), reverse=True):
  print(f"{value} {counted[value]}")
