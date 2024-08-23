n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))
n4 = float(input("Insira a quarta nota: "))

soma = (n1 + n2 + n3 + n4)

if soma / 4 > 7:
    print("Aluno aprovado direto.")
else:
    print("Aluno precisa de exame.")
    nota_exame = float(input("Digite a nota do exame: "))
    if (soma + nota_exame) / 5 > 5:
        print("Aluno aprovado em exame.")
    else:
        print("Aluno reprovado.")
