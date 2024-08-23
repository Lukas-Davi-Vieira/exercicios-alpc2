soma = 0

for i in range(1, 38):
    numerador = (38 - i) * (37 - (i + 1))
    termo = numerador / i

    soma += termo

print(f"{soma:.2f}")
