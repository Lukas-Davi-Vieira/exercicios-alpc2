def fib(n):
    if n == 0 or n == 1:
        return 0
    
    if n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


print(fib(int(input("Insira um valor inteiro: "))))
