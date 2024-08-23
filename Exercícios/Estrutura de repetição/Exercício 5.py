print("Define abaixo o intervalo que deseja ver a soma dos cubos:")

A = int(input("Insira o limite menor: "))
B = int(input("Insira o limite maior: "))

soma = 0

for i in range(A + 1, B):
    soma += i ** 2

print(f"A soma dos cubos compreendidos entre {A} e {B} é igual a {soma}.")
