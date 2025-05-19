def calcular_valor_prestamo(C0, i, n):
    return C0 * (1 + i) ** n

while True:
    print("\n--- Cálculo del valor de un préstamo con interés compuesto ---")
    capital = float(input("Ingrese el valor inicial del préstamo (C₀): "))
    tasa = float(input("Ingrese la tasa de interés mensual (en porcentaje): "))
    meses = int(input("Ingrese el número de meses (n): "))

    # Convertimos el porcentaje a decimal
    tasa_decimal = tasa / 100

    valor_final = calcular_valor_prestamo(capital, tasa_decimal, meses)
    print(f"\nEl valor total a pagar después de {meses} meses es: ${valor_final:.2f}")
