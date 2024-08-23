qtde_candidatos = int(input("Quantos candidatos?\n"))
qtde_eleitores = int(input("Quantas pessoas irão votar?\n"))

dict_candidatos = {}

for i in range(qtde_candidatos):
    dict_candidatos.update({i: 0})

for i in range(qtde_eleitores):
    voto = int(input("Compute seu voto: "))
    if voto in dict_candidatos:
        dict_candidatos[voto] += 1

for i, j in dict_candidatos.items():
    print(f"Candidato {1} recebeu {j} votos.")
