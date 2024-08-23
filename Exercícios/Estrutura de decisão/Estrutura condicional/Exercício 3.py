valor_compra = float(input("Insira o valor da compra: "))
codigo = input("Insira o código identificador (1 para comum, 2 para funcionário, 3 para VIP): ")

coeficiente_desconto = 0.10 if codigo == 2 else 0.05 if codigo == 3 else 0

valor_total = valor_compra * (1 + coeficiente_desconto)

print(f"O valor total a ser pago é de R$ {valor_total}")
