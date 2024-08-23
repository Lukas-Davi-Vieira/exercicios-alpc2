def mdc(x, y):
    if y == 0:
        return x
    
    return mdc(y, x % y)


print(mdc(int(input("Insira o primeiro valor inteiro: ")), int(input("Insira o segundo valor inteiro: "))))
