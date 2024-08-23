valor = int(input("Digite o valor que deseja verificar se é primo: "))

for i in range(2, valor):
    if valor % i == 0:
        print("O numero não é primo.")
        break
else:
    print("O numero é primo.")
