kg_maca = int(input("Insira a quantidade em kg de maçãs: "))
kg_morango = int(input("Insira a quantidade em kg de morangos: "))

peso_total = kg_maca + kg_morango

valor_total = 0

if kg_morango > 5:
    valor_morango = 2.20 * kg_morango
    valor_total += valor_morango
else:
    valor_morango = 2.50 * kg_morango
    valor_total += valor_morango

if kg_maca > 5:
    valor_maca = 1.50 * kg_maca
    valor_total += valor_maca
else:
    valor_maca = 1.80 * kg_maca
    valor_total += valor_maca

print(f"Valor total a pagar: R$ {valor_total:.2f}.")
