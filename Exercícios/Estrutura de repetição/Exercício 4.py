limite_tabuada = int(input("Insira até qual tabuada você deseja ver: "))

for i in range(1, limite_tabuada + 1):
    for j in range(0, 11):
        print(f'{j} x {i} = {j * i}')
    print()
