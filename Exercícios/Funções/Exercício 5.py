def forma_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
        if lado1 == lado2 == lado3:
            print("Com esses segmentos você pode formar um triângulo equilátero!")
        elif lado1 != lado2 != lado3:
            print("Com esses segmentos você pode formar um triângulo escaleno!")
        else:
            print("Com esses segmentos você pode formar um triângulo isósceles!")
    else:
        print("Você não consegue formar um triângulo com os segmentos informados.")


print("Para verificar se três segmentos formam um triângulo, forneça os valores solicitados abaixo:")

lado1 = float(input("Insira o valor do primeiro segmento: "))
lado2 = float(input("Insira o valor do segundo segmento: "))
lado3 = float(input("Insira o valor do terceiro segmento: "))

forma_triangulo(lado1, lado2, lado3)
