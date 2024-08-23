qtde_comprada = int(input("Quantidade de maçãs compradas: "))

preco_maca = 1.30 if qtde_comprada < 12 else 1

print(f"O valor a pagar para {qtde_comprada} maçã(s) é de R$ {preco_maca * qtde_comprada:.2f}.")
