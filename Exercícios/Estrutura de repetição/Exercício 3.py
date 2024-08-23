base = int(input("Qual a base?\n"))
expoente = int(input("Qual o expoente?\n"))
resultado = 1

for i in range(expoente):
    resultado *= base

print(f"{base} elevado na {expoente}° potência é igual a {resultado}.")
