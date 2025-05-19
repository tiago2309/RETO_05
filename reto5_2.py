import math  # Para usar math.pi

def calcular_area_total(r, a, b):
    """
    Calcula el área total de la figura (cuerpo rectangular + 2 circularecirculos).
    """
    area_rectangulo = a * b
    area_circulos = 2 * math.pi * r**2
    return area_rectangulo + area_circulos

def calcular_perimetro_total(r, a, b):
    """
    Calcula el perímetro total de la figura (contorno completo del cuerpo y círculos).
    """
    perimetro = 2 * a + b + 4 * math.pi * r
    return perimetro

# Entrada por teclado
while True:
    r = float(input("Ingrese r (radio de los círculos): "))
    a = float(input("Ingrese a (altura del rectángulo): "))
    b = float(input("Ingrese b (longitud del rectángulo): "))

    # Cálculos
    area = calcular_area_total(r, a, b)
    perimetro = calcular_perimetro_total(r, a, b)

    # Resultados
    print(f"\nÁrea total: {area:.2f} unidades cuadradas")
    print(f"Perímetro total: {perimetro:.2f} unidades")
