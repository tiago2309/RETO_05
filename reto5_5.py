import math

# --- Funciones para los diferentes cálculos ---

def calcular_promedio(numeros):
    """Devuelve el promedio de los números en la lista."""
    return sum(numeros) / len(numeros)

def promedio_multiplicativo(numeros):
    """Devuelve el promedio multiplicativo de los números (raíz n-ésima del producto)."""
    producto = 1
    for num in numeros:
        producto *= num
    return producto ** (1 / len(numeros))

def potencia_mayor_menor(numeros):
    """Devuelve el mayor número elevado al menor número."""
    mayor = max(numeros)
    menor = min(numeros)
    return mayor ** menor

def raiz_cubica_menor(numeros):
    """Devuelve la raíz cúbica del menor número (soporta negativos)."""
    menor = min(numeros)
    return math.copysign(abs(menor) ** (1 / 3), menor)

# --- Bucle principal del programa ---

while True:
    # Solicita 5 números reales al usuario
    numeros = []
    for i in range(5):
        num = float(input(f"Número {i + 1}: "))
        numeros.append(num)

    # Llama a las funciones para realizar los cálculos
    prom = calcular_promedio(numeros)
    prom_mult = promedio_multiplicativo(numeros)
    potencia = potencia_mayor_menor(numeros)
    raiz_cubica = raiz_cubica_menor(numeros)

    # Muestra los resultados con 4 cifras decimales
    print(f"\nResultados con los números: {numeros}")
    print(f"Promedio: {prom:.4f}")
    print(f"Promedio multiplicativo: {prom_mult:.4f}")
    print(f"Potencia del mayor elevado al menor: {potencia:.4f}")
    print(f"Raíz cúbica del menor número: {raiz_cubica:.4f}")

    # Pregunta si el usuario quiere repetir
    repetir = input("\n¿Desea ingresar otros valores? (s/n): ").strip().lower()
    if repetir != 's':
        print("Programa finalizado.")
        break
