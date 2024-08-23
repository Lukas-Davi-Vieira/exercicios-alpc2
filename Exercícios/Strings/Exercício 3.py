from random import choice, randrange

palavra_lista = []

lista_palavras = [
    "gato",
    "estado",
    "universidade",
    "carro",
    "saco",
    "motor",
    "olimpiadas",
    "computador",
    "software",
    "menina"
]

palavra_aleatoria = choice(lista_palavras)
palavra_real = palavra_aleatoria

while len(palavra_aleatoria) != 0:
    letra = palavra_aleatoria[randrange(0, len(palavra_aleatoria))]
    palavra_lista.append(letra)
    palavra_aleatoria = list(palavra_aleatoria)
    palavra_aleatoria.remove(letra)
    palavra_aleatoria = "".join(palavra_aleatoria)

palavra_embaralhada = "".join(palavra_lista)
print(palavra_embaralhada)

guess = input("Adivinhe a palavra aleatória!\n")

if guess == palavra_real:
    print("Você ganhou!")
else:
    print("Você perdeu...")
    print(f"A palavra era: {palavra_real}")
