print("Preencha abaixo com os valores referentes à sua idade.")

idade_anos = int(input("Anos: "))
idade_meses = int(input("Meses: "))
idade_dias = int(input("Dias: "))

dias_vividos = idade_anos * 365 + idade_meses * 30 + idade_dias

print(f"Você viveu {dias_vividos} dias até hoje!")
