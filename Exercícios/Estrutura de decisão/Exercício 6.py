nome = input("Insira seu nome: ")
valor_venda = float(input("Digite o valor da venda: "))

fator_comissao = 0.12 if valor_venda > 50000 else 0.095 if 50000 >= valor_venda >= 30000 else 0.07

print(f"Valor da comissão para uma venda de R$ {valor_venda} igual a R$ {valor_venda * fator_comissao}.")
