def soma(n):
    if n == 0:
        return 0
    
    return n + soma(n - 1)


print(soma(int(input("Insira um valor inteiro: "))))
