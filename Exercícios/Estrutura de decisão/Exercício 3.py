n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digte o segundo número: "))
n3 = float(input("Digte o terceiro número: "))

if n1 > n2:
    if n2 > n3:
        print(f"{n1} > {n2} > {n3}")
    else:
        print(f"{n1} > {n3} > {n2}")
if n2 > n1:
    if n1 > n3:
        print(f"{n2} > {n1} > {n3}")
    else:
        print(f"{n2} > {n3} > {n1}")
if n3 > n2:
    if n2 > n1:
        print(f"{n3} > {n2} > {n1}")
    else:
        print(f"{n3} > {n1} > {n2}")
