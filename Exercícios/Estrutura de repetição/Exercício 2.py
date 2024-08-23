limite = int(input("Insira o valor teto para a soma: "))

soma = 0

for i in range(1, limite + 1):
    soma += i

print(f"A soma dos valores de {1} a {limite} é igual a {soma}.")
