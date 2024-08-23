codigo = input("Insira o código de cinco algarismos: ")

if len(codigo) != 5:
    raise ValueError("O código precisa ter cinco algarismos")

codigo = [x for x in map(int, codigo)]

s = 6 * codigo[0] + 5 * codigo[1] + 4 * codigo[2] + 3 * codigo[3] + 2 * codigo[4]

digito_v = s % 7

print(f"O digito verificador é igual a {digito_v}")
