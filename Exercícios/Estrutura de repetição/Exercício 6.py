taxa_juros = 0.005

valor_depositado = float(input("Insira o valor depositado para simular os juros em um ano: "))
valor_com_juros = valor_depositado

for i in range(12):
    valor_com_juros += valor_com_juros * (1 + taxa_juros)

print(f"Após um ano o valor depositado de R$ {valor_depositado} se tornará R$ {valor_com_juros}, rendimento total de R$ {valor_com_juros - valor_depositado}.")
