vetor_A = [1, 3, 5, 7, 9, 11]
vetor_B = [2, 4, 6, 8, 10, 12, 14, 16]

vetor_C = []

if len(vetor_A) == len(vetor_B):
    for i in range(len(vetor_A)):
        vetor_C.append(vetor_A[i])
        vetor_C.append(vetor_B[i])

if len(vetor_A) != len(vetor_B):
    biggest = vetor_A if len(vetor_A) > len(vetor_B) else vetor_B
    smallest = vetor_A if len(vetor_A) < len(vetor_B) else vetor_B
    for i in range(len(biggest)):
        if i <= len(smallest) - 1:
            vetor_C.append(vetor_A[i])
            vetor_C.append(vetor_B[i])
        else:
            vetor_C.append(biggest[i])

print(vetor_C)
