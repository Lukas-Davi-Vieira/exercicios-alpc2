nome_completo = input("Insira seu nome completo: ").title().split(" ")

nome_completo = [x for x in nome_completo if x not in ["E", "Do", "Da", "Dos", "Das", "De", "Di", "Du"]]

print(nome_completo)

iniciais = []

for i in nome_completo:
    iniciais.append(i[0])

iniciais = "".join(iniciais)

print(iniciais)
