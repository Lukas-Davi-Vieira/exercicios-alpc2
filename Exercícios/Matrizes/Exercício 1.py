matriz = [[], []]

for i in range(2):
    for j in range(4):
        matriz[i].append(int(input(f"Insira o {j + 1}° valor da {i + 1}° coluna: ")))
