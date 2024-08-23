enesimo_termo = int(input("Insira qual o fatorial que deseja ver: "))
resultado = enesimo_termo

for i in range(enesimo_termo, 1, -1):
    resultado *= i - 1
    
print(f"O fatorial de {enesimo_termo} é igual a {resultado}.")
