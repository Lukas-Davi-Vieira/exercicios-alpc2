v1 = []
v2 = []
counter = 0

for i in range(1, 16):
    v1.append(int(input(f"Insira {i}° valor inteiro para o primeiro vetor: ")))
    v2.append(int(input(f"Insira {i}° valor inteiro para o segundo vetor: ")))

    if v1[i - 1] == v2[i - 1]:
        counter += 1

print(f"Os valores e posições nos vetores foram congruentes {counter} vezes")
