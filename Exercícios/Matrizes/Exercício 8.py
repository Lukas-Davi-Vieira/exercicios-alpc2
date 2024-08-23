def rotate90(matriz):
    matriz_resultado = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_resultado[i][j] = matriz[len(matriz[i]) - j - 1][i]

    return matriz_resultado


def rotate180(matriz):
    matriz_resultado = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_resultado[i][j] = matriz[len(matriz) - i - 1][len(matriz[j]) - j - 1]
    
    return matriz_resultado


def rotate270(matriz):
    matriz_resultado = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_resultado[i][j] = matriz[j][len(matriz[i]) - i - 1]
    
    return matriz_resultado


def imprimir(matriz):
    for i in matriz:
        print(i)
    print()

if __name__ == "__main__":
    matriz = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]

imprimir(rotate90(matriz))
imprimir(rotate180(matriz))
imprimir(rotate270(matriz))
