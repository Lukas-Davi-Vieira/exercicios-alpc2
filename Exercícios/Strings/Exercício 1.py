nome = input("Digite seu nome: ").strip().upper()
nome_invertido = [x for x in reversed(nome)]

print("".join(nome_invertido))
