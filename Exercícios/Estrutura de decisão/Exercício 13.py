litros_vendidos = float(input("Insira a quantidade de litros vendidos: "))
codigo = input("Digite o código do produto (G para gasolina e A para álcool): ").upper()
preco_litro = 0

if codigo == "A":
    preco_litro = 2.90
    if litros_vendidos > 20:
        preco_litro -= preco_litro * 0.05
    else:
        preco_litro -= preco_litro * 0.03
else:
    preco_litro = 3.30
    if litros_vendidos > 20:
        preco_litro -= preco_litro * 0.06
    else:
        preco_litro -= preco_litro * 0.04

print(f"Quantidade de litros vendido: {litros_vendidos} litros. Valor a pagar: R$ {preco_litro * litros_vendidos}.")
