from random import randint

print("Pense em um número de 1 a 1000")

upper_track = 1000
lower_track = 1
vidas = 10

while vidas > 0:
    numero_aleatório = randint(lower_track, upper_track)

    print(numero_aleatório)

    resposta = input("O valor é este?\n").lower()
    if resposta == "sim" or resposta == "s":
        print("O programa ganhou em {vidas} tentativas!")
        break
    else:
        vidas -= 1
        print("< para menor, > maior")
        track_question = input("O valor gerado é maior ou menor?")
        if track_question == "<":
            lower_track = numero_aleatório
        if track_question == ">":
            upper_track = numero_aleatório
else:
    print("O programa foi derrotado!")
