resultado = 0

for i in range(1, 51):
    numerador = 1000 - 3 * (i - 1)
    termo = numerador / i
    if i % 2 == 0:
        resultado -= termo
    else:
        resultado += termo

print(f"{resultado:.2f}")
