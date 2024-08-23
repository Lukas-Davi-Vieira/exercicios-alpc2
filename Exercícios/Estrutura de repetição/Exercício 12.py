populacao_a = 80000
populacao_b = 200000

count = 0

while populacao_a < populacao_b:
    populacao_a *= 1.03
    populacao_b *= 1.015   

    count += 1

print(f"Após {count} anos, a população da cidade A será maior ou igual à população da cidade B.")
