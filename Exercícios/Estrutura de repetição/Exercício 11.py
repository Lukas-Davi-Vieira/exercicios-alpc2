massa = float(input("Insira a massa inicial: "))
count = 50

while massa >= 0.05:
    massa /= 2
    count += 50

print(f"Após {count} segundos, o material terá decaído para uma massa inferior a 0.05g")
