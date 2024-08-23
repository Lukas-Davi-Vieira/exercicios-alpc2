"""
cont1 = 0
cont2 = 0
brancos = 0
nulos = 0
voto = int(input())
while voto != -1:
    if voto == 1:
        cont1 += 1
    elif voto == 2:
        cont2 += 1
    elif voto == 0:
        brancos += 1
    else:
        nulos += 1
print(cont1)
print(cont2)
print(brancos)
print(nulos)
"""

# O erro no código acima está na declaração da variável "voto" fora do loop while
# Fazendo com que se o usuário digitar um número diferente de -1, o programa entra em um loop infinito.
# Cógido corrigido:

cont1 = 0
cont2 = 0
brancos = 0
nulos = 0

while voto != -1:
    voto = int(input())
    if voto == 1:
        cont1 += 1
    elif voto == 2:
        cont2 += 1
    elif voto == 0:
        brancos += 1
    else:
        nulos += 1

print(cont1)
print(cont2)
print(brancos)
print(nulos)
