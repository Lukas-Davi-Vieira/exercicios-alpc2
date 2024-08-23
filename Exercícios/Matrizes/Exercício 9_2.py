tempo = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [1, 0, 2, 11, 6, 15, 11, 1],
    [2, 2, 0, 7, 12, 4, 2, 15],
    [3, 11, 7, 0, 11, 8, 3, 13],
    [4, 6, 12, 11, 0, 10, 2, 1],
    [5, 15, 4, 8, 10, 0, 5, 13],
    [6, 11, 2, 3, 2, 5, 0, 14],
    [7, 1, 15, 13, 1, 13, 14, 0]
]

print("O tempo para percorrer a distância entre duas cidades se dá através da tabela abaixo:")

for i in tempo:
    print(i)

print()

print("Insira abaixo as cidades que deseja visitar, sendo a primeira o ponto de partida.")
print("Para finalizar a rota, digite 0.")

cidades_visitadas = 0
cidade_atual = 0
rota = []
tempo_total = 0
proxima_cidade = ...

while True:
    if proxima_cidade == 0:
        break

    if cidade_atual == 0:
        cidade_atual = int(input("Insira o ponto de partida: "))
        rota.append(cidade_atual)
    else:
        proxima_cidade = int(input("Insira a próxima cidade: "))
        if proxima_cidade == cidade_atual:
            print("Você não pode escolher esta cidade, pois já está nela.")
            continue
        else:
            tempo_total += tempo[cidade_atual][proxima_cidade] if proxima_cidade != 0 else 0
            cidade_atual = proxima_cidade if proxima_cidade != 0 else 0
            rota.append(proxima_cidade if proxima_cidade != 0 else "FIM DE ROTA")

print(f"Sua rota foi: {rota}")
print(f"Tempo para percorrer a rota: {tempo_total} horas.")
