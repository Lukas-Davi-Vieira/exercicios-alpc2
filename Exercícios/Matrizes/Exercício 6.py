A = [[2, 3, 1],
     [-1, 0, 2]]

B = [[1, -2],
     [0, 5],
     [4, 1]]

if len(A[0]) != len(B):
     raise ValueError("AS dimensões das matrizes não são compatíveis para multiplicação")

# Cria a matriz resultado de acordo com o número de linhas e colunas das matrizes originais
C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

Bt = list(zip(*B))  # Transpondo a segunda matriz para facilitar o cálculo

for i in range(len(A)):
    for j in range(len(B[0])):
        # Matriz C recebe a soma de todos os x * y dos valores x, y gerados pela função zip da matriz original A e da matriz B transposta
        C[i][j] = sum(x * y for x, y in zip(A[i], Bt[j]))

print(f"A x B = {C}")
