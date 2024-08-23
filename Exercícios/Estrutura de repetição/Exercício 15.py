maior_numero = 0
menor_numero = 0
soma = 0
media = 0
pares = 0
impares = 0
count = 0

while True:
    numero = float(input("Insira qualquer número ou 0 para finalizar: "))
    if numero == 0:
        break
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero
    soma += numero
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    count += 1
    media = soma / count

print(f"""
    Maior número = {maior_numero}
    Menor número = {menor_numero}
    Soma = {soma}
    Média = {media}
    Quantidade de pares = {pares}
    Quantidade de ímpares = {impares}
    Quantidade de números digitados = {count}
""")
