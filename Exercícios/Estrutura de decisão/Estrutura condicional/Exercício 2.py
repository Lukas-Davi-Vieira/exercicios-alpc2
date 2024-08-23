n1 = float(input("Insira o primeiro valor: "))
n2 = float(input("Insira o segundo valor: "))
print()
print("""
    [+] para soma
    [-] para subtração
    [x] para multiplicação
    [/] para divisão
      """)
print()
operacao = input("Insira a operação que deseja realizar: ")
print()

if operacao == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif operacao == "-":
    print(f"{n1} - {n2} = {n1 - n2}")
elif operacao == "x":
    print(f"{n1} x {n2} = {n1 * n2}")
elif operacao == "/":
    print(f"{n1} / {n2} = {n1 / n2}")
else:
    raise ValueError("Operação inválida.")
