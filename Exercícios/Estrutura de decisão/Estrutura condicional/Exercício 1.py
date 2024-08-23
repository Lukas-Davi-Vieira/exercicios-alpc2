print("""
    (S) para solteiro
    (C) para casado
    (V) para viúvo
    (Di) para divorciado
    (De) para desquitado
      """)

estado_civil = input("Insira o código do estado cívil que você deseja ver a descrição: ").lower

if estado_civil == "s":
    print("Refere-se a um indivíduo que não mantém um relacionamento sério ou não faz parte de uma união civil.")
elif estado_civil == "c":
    print("É o indivíduo que possui uma união matrimonial através do casamento civil, independente do regime de bens adotado.")
elif estado_civil == "v":
    print("Uma viúva ou viúvo é uma pessoa cujo cônjuge faleceu e geralmente não se casou novamente.")
elif estado_civil == "di":
    print("O divórcio é o rompimento legal e definitivo do vínculo de casamento civil.")
elif estado_civil == "de":
    print("Que se separou da pessoa com a qual mantinha um casamento, através de desquite, ação judicial ou divórcio. ")
else:
    raise ValueError("Código inválido.")
