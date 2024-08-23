matriz_A = [[2, -3],
            [-1, 4]]

matriz_inversa = []

for i in range(len(matriz_A)):
    matriz_inversa.append([])
    for j in range(len(matriz_A[0])):
        matriz_inversa[i].append(matriz_A[i][j] * -1)

print(matriz_inversa)
        