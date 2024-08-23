from math import ceil

potencia = float(input("Qual a potência da sua lâmpada em watts?\n"))
area = float(input("Qual a área a ser iluminada em m²?\n"))

eficiencia_m2 = 18

lampadas_necessarias = ceil((area * eficiencia_m2) / potencia)

print(f"Para iluminar um quarto de {area:.2f} m² são necessárias {lampadas_necessarias} "
      f"lâmpada(s) de {potencia:.2f} watts de potência")
