matriz_A = [[-10, 1, 4, 6],
            [2, 3, 2, 8]]

matriz_B = [[1, 8, 4, -1],
            [0, 6, 3, -3]]

matriz_soma = []

for i in range(len(matriz_A)):
    matriz_soma.append([])
    for j in range(len(matriz_A[0])):
        matriz_soma[i].append(matriz_A[i][j] + matriz_B[i][j])

print(matriz_soma)
