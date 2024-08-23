valor = int(input("Digite qualquer número: "))

str_valor = str(valor)

dict_num = {
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    0: "zero"
}

lista_numeros = [x for x in map(int, str_valor)]

for i, j in enumerate(lista_numeros):
    if i == 0 and len(lista_numeros) != 1:
        print(dict_num[j].capitalize(), end=", ")
    elif i == len(lista_numeros) - 1 and len(lista_numeros) != 1:
        print(dict_num[j])
    elif len(lista_numeros) == 1:
        print(dict_num[j].capitalize())
    else:
        print(dict_num[j], end=", ")
