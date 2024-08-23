def palavras_iguais(palavra1, palavra2):
    return palavra2.startswith(palavra1) if len(palavra1) < len(palavra2) else False

print(palavras_iguais(input("Primeira palavra: "), input("Segunda palavra: ")))
