def tower_of_hanoi(n, pino_inicial, pino_auxiliar, pino_destino):
    if n == 1:
        print(f"Movendo disco {n} da torre {pino_inicial} para torre {pino_destino}.")
        return
    
    tower_of_hanoi(n - 1, pino_inicial, pino_destino, pino_auxiliar)
    print(f"Movendo disco {n} da torre {pino_inicial} para torre {pino_destino}.")
    tower_of_hanoi(n - 1, pino_auxiliar, pino_inicial, pino_destino)


tower_of_hanoi(3, "A", "B", "C")
