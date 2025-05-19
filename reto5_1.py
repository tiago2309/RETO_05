import math  # Importa el módulo math

def calcular_volumen(r1, r2, h):
    volumen_esfera = (4/3) * math.pi * r1**3
    volumen_cono = (1/3) * math.pi * r2**2 * h
    return volumen_esfera + volumen_cono

def calcular_area_superficial(r1, r2, h):
    area_esfera = 4 * math.pi * r1**2
    generatriz = math.sqrt(r2**2 + h**2)
    area_cono = math.pi * r2 * generatriz
    return area_esfera + area_cono

while True:
    # Entrada por teclado
    r1 = float(input("Ingrese r1 (radio de la esfera): "))
    r2 = float(input("Ingrese r2 (radio de la base del cono): "))
    h = float(input("Ingrese h (altura del cono): "))

    # Cálculos
    volumen = calcular_volumen(r1, r2, h)
    area = calcular_area_superficial(r1, r2, h)

    # Resultados
    print(f"\nVolumen total: {volumen:.2f} unidades cúbicas")
    print(f"Área superficial total: {area:.2f} unidades cuadradas")