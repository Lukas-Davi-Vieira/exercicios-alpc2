vetor_original = []

for i in range(20):
    vetor_original.append(int(input(f"Insira o {i + 1}° inteiro do vetor: ")))

print("Vetor original =", vetor_original)

vetor_invertido = []

for i in range(1, 21):
    vetor_invertido.append(vetor_original[-i])

print("Vetor invertido =", vetor_invertido)
