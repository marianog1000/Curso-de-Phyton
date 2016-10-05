start_list = [5, 3, 1, 2, 4]
square_list = []

for var in start_list:
    cuadrado = var ** 2
    square_list.append(cuadrado)

square_list.sort()

print square_list
