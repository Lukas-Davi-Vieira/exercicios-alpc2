nome_completo = input("Nome completo: ")
idade = int(input("Idade: "))
grupo_risco = input("Grupo de risco: ").lower()

categoria_seguro = ...

if 17 <= idade <= 70:
    if 17 <= idade <= 20:
        if grupo_risco == "baixo":
            categoria_seguro = 1
        elif grupo_risco == "medio" or grupo_risco == "médio":
            categoria_seguro = 2
        else:
            categoria_seguro = 3
    if 21 <= idade <= 24:
        if grupo_risco == "baixo":
            categoria_seguro = 2
        elif grupo_risco == "medio" or grupo_risco == "médio":
            categoria_seguro = 3
        else:
            categoria_seguro = 4
    if 25 <= idade <= 34:
        if grupo_risco == "baixo":
            categoria_seguro = 3
        elif grupo_risco == "medio" or grupo_risco == "médio":
            categoria_seguro = 4
        else:
            categoria_seguro = 5
    if 35 <= idade <= 64:
        if grupo_risco == "baixo":
            categoria_seguro = 4
        elif grupo_risco == "medio" or grupo_risco == "médio":
            categoria_seguro = 5
        else:
            categoria_seguro = 6
    if 65 <= idade <= 70:
        if grupo_risco == "baixo":
            categoria_seguro = 7
        elif grupo_risco == "medio" or grupo_risco == "médio":
            categoria_seguro = 8
        else:
            categoria_seguro = 9
    print(f"""
        Nome: {nome_completo}
        Idade: {idade}
        Categoria de seguro disponível: {categoria_seguro}
          """)
else:
    print("O pretendente não se enquadra em nenhuma das categorias de seguro disponíveis.")
    