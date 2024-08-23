numero_1 = [2, 9, 7]
numero_2 = [1, 2, 3, 3, 8, 7]

biggest = numero_1 if len(numero_1) > len(numero_2) else numero_2
smallest = numero_1 if len(numero_1) < len(numero_2) else numero_2

difference = len(biggest) - len(smallest)

for i in range(difference):
    smallest.insert(0, 0)

numero_resultado = [x + y for x, y in zip(biggest, smallest)]

for i in range(len(numero_resultado)):
    if numero_resultado[i] > 10:
        numero_resultado[i] -= 10
        numero_resultado[i - 1] += 1
    
    if numero_resultado[i] > 10 and i == 0:
        numero_resultado[i] -= 10
        numero_resultado.insert(0, 1)

print(numero_resultado)
