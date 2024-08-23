primeira_palavra = input("Primeira palavra: ")
segunda_palavra = input("Segunda palavra: ")

for i in primeira_palavra:
    segunda_palavra = segunda_palavra.replace(i, '', 1)

print("São anagramas" if len(segunda_palavra) == 0 and len(primeira_palavra) == len(segunda_palavra) else "Não são anagramas")
