def peso_total_aves(N, M, K):
    return (N * 6) + (M * 7) + (K * 1)

# Pedir datos al usuario
while True:
    n = int(input("Ingrese el número de gallinas: "))
    m = int(input("Ingrese el número de gallos: "))
    k = int(input("Ingrese el número de pollitos: "))

    # Calcular el peso total
    total = peso_total_aves(n, m, k)

    # Mostrar el resultado
    print(f"El peso total de las aves es: {total} kilos")
