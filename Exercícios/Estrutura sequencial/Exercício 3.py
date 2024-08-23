n1, n2, n3 = input("Insira as três notas\n").split(" ")
n1, n2, n3 = float(n1), float(n2), float(n3)

media = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 3

print("A média ponderada das notas é", media)
