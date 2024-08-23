valor_emprestimo = float(input("Digite o valor que você deseja emprestar: "))
qtde_parcelas = int(input("Digite a quantidade de parcelas: "))
salario = float(input("DIgite seu salário: "))

valor_parcelas = valor_emprestimo / qtde_parcelas

if valor_parcelas < salario * 0.3:
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")
    