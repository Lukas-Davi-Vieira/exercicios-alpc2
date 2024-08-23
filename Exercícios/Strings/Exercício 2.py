frase = input("Digite uma frase: ")

dict_vogais = {
    "a": frase.count("a"),
    "e": frase.count("e"),
    "i": frase.count("i"),
    "o": frase.count("o"),
    "u": frase.count("u"),
    "espaçamento": frase.count(" ")
    }

for i in dict_vogais:
    print(f"Ocorrências de {i} = {dict_vogais[i]}")
