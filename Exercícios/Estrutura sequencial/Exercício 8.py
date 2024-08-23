horas, minutos = input("Qual foi o tempo gasto na viagem? Formato -> HH:MM\n").split(":")
horas, minutos = int(horas), int(minutos)

minutos_real = minutos / 60

tempo_gasto = horas + minutos_real

velocidade_media = float(input("Qual a velocidade média mantida na viagem?\n"))

distancia_percorrida = velocidade_media * tempo_gasto
litros_consumidos = distancia_percorrida / 12  # O veículo consome 1l a cada 12km

print(f"""
          Tempo gasto = {horas} hora(s) e {minutos} minuto(s);
          Velocidade média = {velocidade_media:.2f} km/h;
          Distância percorrida = {distancia_percorrida:.2f} km;
          Litros de combustível consumidos = {litros_consumidos:.2f} litros.
      """)
