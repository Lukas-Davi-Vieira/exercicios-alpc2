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

print("Insira abaixo duas cidades para ver o tempo necessário para percorrer a distância entre elas.")
cidade_1 = int(input("Cidade 1 (número correspondente no mapa, eixo y): "))
cidade_2 = int(input("Cidade 1 (número correspondente no mapa, eixo x): "))

print(f"Tempo para ir da cidade {cidade_1} à cidade {cidade_2} é de {tempo[cidade_1][cidade_2]} horas.")
