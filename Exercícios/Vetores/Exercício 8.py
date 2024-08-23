vetor_matriculas = []

limite_matriculas = 100

for i in range(limite_matriculas):
    nova_matricula = int(input("Insira um número de matrícula: "))
    if nova_matricula in vetor_matriculas:
        print("Esta matrícula já existe, favor tentar novamente.")
        limite_matriculas += 1
        continue
    else:
        vetor_matriculas.append(nova_matricula)

for i in range(len(0, vetor_matriculas - 1)):
    print(f"{i}° matrícula: {vetor_matriculas[i]}")
