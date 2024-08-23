fib = int(input("Insira o limite para a sequência de Fibonacci: "))
termo_atual = 0
prox_termo = 1


while termo_atual < fib:
    print(termo_atual, end=" ")
    termo_aux = termo_atual
    termo_atual = prox_termo
    prox_termo = termo_atual + termo_aux

print(termo_atual)
