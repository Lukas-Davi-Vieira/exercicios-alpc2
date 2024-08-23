salario = float(input("Digite o salário para ver o reajuste: "))

salario_minimo = 1412

coeficiente_reajuste = 0.5 if salario < (3 * salario_minimo) else 0.2 if salario <= (10 * salario) else 0.15 if salario <= (20 * salario_minimo) else 0.1

salario_reajustado = salario * (1 + coeficiente_reajuste)

print(f"Salário rejustado: R$ {salario_reajustado:.2f}. Percentual de reajuste: {coeficiente_reajuste * 100}%.")
