matriz = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

soma_1 = sum([x for x in matriz[0]])
print(f"Soma da primeira linha =", soma_1)

produto_1 = 1
for i in matriz[0]:
    produto_1 *= i
else:
    print(f"Produto da primeira linha =", produto_1)

soma_matriz = 0
for i in range(len(matriz)):
    soma_matriz += sum([x for x in matriz[i]])
else:
    print("Soma de todos os elementos =", soma_matriz)

produto_matriz = 1
for i in range(len(matriz)):
    produto_matriz *= matriz[i][i]
else:
    print("Produto da diagonal principal =", produto_matriz)
    