from math import sqrt

# Fórmula = -b + ou - raiz de b² - 4ac / 2a

print("Informe os coeficiente da equação de segundo grau que você deseja saber as raízes.")

coeficiente_A = int(input("Coeficiente A: "))
Coeficiente_B = int (input("Coeficiente B: "))
Coeficiente_C = int(input("Coeficiente C: "))

delta = sqrt((Coeficiente_B ** 2) - (4 * coeficiente_A * Coeficiente_C))

if coeficiente_A:
    if delta > 0:
        x1 = (-Coeficiente_B + delta) / (2 * coeficiente_A)
        x2 = (-Coeficiente_B - delta) / (2 * coeficiente_A)
        print(f"x1 = {x1} e x2 = {x2}")
    elif delta == 0:
        x = (-Coeficiente_B + delta) / (2 * coeficiente_A)
        print(f"Esta equação possui apenas uma solução, sendo x = {x}")
    else:
        print("Esta equação de segundo grau não possui soluções reais.")
else:
    raise ValueError("A equação fornecida não é de segundo grau.")
