from math import ceil

area = float(input("Qual a área a ser pintada em m²?\n"))

qtde_litros = area / 3

qtde_latas = ceil(qtde_litros / 18)

preco = qtde_latas * 80

print(f"Compre {qtde_latas} lata(s) por R$ {preco:.2f} para cobrir a área de {area} m².")