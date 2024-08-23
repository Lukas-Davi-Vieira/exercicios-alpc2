salario_hora = float(input("Insira o salário-hora: "))
horas_trabalhadas = float(input("Insira a quantidade de horas trabalhadas: "))

horas_normais = 120
horas_extras = horas_trabalhadas - horas_normais

valor_normal = 120 * salario_hora
valor_extra = horas_extras * (1.5 * salario_hora)

salario_mensal = valor_extra + valor_normal

print(f"Salário mensal igual a R$ {salario_mensal}")
