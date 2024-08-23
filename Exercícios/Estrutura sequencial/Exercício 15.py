salario_bruto = float(input("Insira seu salário bruto: "))

desconto_inss = 0.10
desconto_irpf = 0.05

salario_liquido = salario_bruto - (salario_bruto * desconto_inss)
salario_liquido -= salario_liquido * desconto_irpf

print(f"Seu salário líquido é de R$ {salario_liquido:.2f}")
