pi = 3.14159
raio = float(input())
area = round((pi * raio ** 2) / 10000, 4) # area ja em m2, com arrendondamento
print('Area = {:.4f}'.format(area))
