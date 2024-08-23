ordem = int(input("Insira a ordem do triângulo de pascal: "))

triangulo = [[0 for _ in range(ordem)] for _ in range(ordem)]

for i in range(ordem):
    triangulo[i][0] = 1
    triangulo[i][i] = 1

for i in range(1, ordem):
    for j in range(1, ordem):
        triangulo[i][j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]

for i in range(ordem):
    qtde_zeros_linha = triangulo[i].count(0)
    for j in range(qtde_zeros_linha):
        triangulo[i].remove(0)

for i in triangulo:
    print(i)
