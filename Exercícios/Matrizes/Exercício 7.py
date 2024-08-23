ordem = int(input("Insira a ordem da matriz para gerar sua matriz identidade: "))

matriz_identidade = [[0 for _ in range(ordem)] for _ in range(ordem)]

for i in range(ordem):
    matriz_identidade[i][i] = 1

for i in matriz_identidade:
    print(i)
