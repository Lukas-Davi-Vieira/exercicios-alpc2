A = float(input("Insira o valor A: "))
B = float(input("Insira o valor B: "))
C = float(input("Insira o valor C: "))
D = float(input("Insira o valor D: "))

# Sem utilizar coleções (listas, tuplas ou sets)

soma_AB = A + B
soma_AC = A + C
soma_AD = A + D
soma_BC = B + C
soma_BD = B + D
soma_CD = C + D

mult_AB = A * B
mult_AC = A * C
mult_AD = A * D
mult_BC = B * C
mult_BD = B * D
mult_CD = C * D

print(f"RESULTADO DA SOMA DISTRIBUTIVA DE {A}, {B}, {C} e {D}:")
print()
print(f"{A} + {B} = {soma_AB}")
print(f"{A} + {C} = {soma_AC}")
print(f"{A} + {D} = {soma_AD}")
print(f"{B} + {C} = {soma_BC}")
print(f"{B} + {D} = {soma_BD}")
print(f"{C} + {D} = {soma_CD}")
print()

print(f"RESULTADO DA MULTIPLICAÇÃO DISTRIBUTIVA DE {A}, {B}, {C} e {D}:")
print()
print(f"{A} x {B} = {mult_AB}")
print(f"{A} x {C} = {mult_AC}")
print(f"{A} x {D} = {mult_AD}")
print(f"{B} x {C} = {mult_BC}")
print(f"{B} x {D} = {mult_BD}")
print(f"{C} x {D} = {mult_CD}")
print()
