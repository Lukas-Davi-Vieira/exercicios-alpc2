lista_numeros = []

for i in range(100):
    lista_numeros.append(input("Insira um número: "))

print("Soma dos valores:", sum(lista_numeros))
print("Média dos valores:", sum(lista_numeros)/len(lista_numeros))
print("Maior dos valores:", max(lista_numeros))
print("Menor dos valores:", min(lista_numeros))
