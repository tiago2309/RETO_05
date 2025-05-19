# RETO_05
Desarrollo de cada uno de los retos 05
## 1. Dada la figura de la imagen, desarrolle:
<img src="https://camo.githubusercontent.com/9a79fe9629fff1ceecb5860dba4054b90da7acda3d4f2c9cd7f62a34799894d2/68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67" alt="Figura del reto" width="400"/>

### - Una función matemática para calcular el volumen y el área superficial.
 **Volúmenes**
  - Esfera:
   ![Fórmula](https://latex.codecogs.com/svg.image?&space;V_{esfera}=\frac{4}{3}\pi&space;r_{1}{^3})
  - Cono:
   ![Fórmula](https://latex.codecogs.com/svg.image?&space;V_{cono}=\frac{1}{3}\pi&space;r_{2}{^2}h)
  - Volumen total:
  ![Fórmula](https://latex.codecogs.com/svg.image?&space;V_{TOTAL}=\frac{4}{3}\pi&space;r_{1}{^3}&plus;\frac{1}{3}\pi&space;r_{2}{^2}h)

**Áreas**
  - Esfera:
    ![Fórmula](https://latex.codecogs.com/svg.image?&space;A_{esfera}=4\pi&space;r_{1}{^2})
  - Generatriz del cono:
    ![Fórmula](https://latex.codecogs.com/svg.image?&space;g=\sqrt{r_{2}{^2}+h^{2})
  - Área del cono:
    ![Fórmula](https://latex.codecogs.com/svg.image?&space;A_{cono}=\pi&space;r_{2}g)
  - Área total:
    ![Fórmula](https://latex.codecogs.com/svg.image?&space;A_{total}=4\pi&space;r_{1}{^2}+\pi&space;r_{2}\sqrt{r_{2}{^2}+h{^2})
   
    
### - Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

```
def calcular_volumen(r1, r2, h):
    """
    Calcula el volumen total del sólido compuesto por una esfera y un cono sin usar el módulo math.
    """
    pi = 3.1416
    volumen_esfera = (4/3) * pi * r1**3
    volumen_cono = (1/3) * pi * r2**2 * h
    volumen_total = volumen_esfera + volumen_cono
    return volumen_total

def calcular_area_superficial(r1, r2, h):
    """
    Calcula el área superficial total del sólido compuesto por una esfera y un cono sin usar el módulo math.
    """
    pi = 3.1416
    area_esfera = 4 * pi * r1**2
    generatriz = (r2**2 + h**2)**0.5  # raíz cuadrada sin usar math.sqrt
    area_cono = pi * r2 * generatriz
    area_total = area_esfera + area_cono
    return area_total

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
```

### - Revise como utilizar el valor de pi usando import math y math.pi
  Usando este comando tendremos más precisión en los resultados
```
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
```
---
## 2. Dado la figura de la imagen, desarrolle:
<img src="https://camo.githubusercontent.com/1e035694c4675debe6703e3771f67ff06d8da330997d02c3806aa2bd5936bc54/68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67" alt="Figura del reto" width="400"/>

### - Una función matemática para calcular el área y el perimetro.
**Áreas:**
- Rectángulo:
  ![Fórmula](https://latex.codecogs.com/svg.image?&space;A_{rec}=b*h)
- Círculos:
  ![Fórmula](https://latex.codecogs.com/svg.image?&space;A_{cir}=\pi&space;r{^2})
- Total:
  ![Fórmula](https://latex.codecogs.com/svg.image?&space;A_{total]=A_{rec}+2A_{cir})
  
**Perímetro:**
- Rectágunlo:
  ![Fórmula](https://latex.codecogs.com/svg.image?&space;P_{rec}=2b+2h)
- Círculos:
  ![Fórmula](https://latex.codecogs.com/svg.image?&space;P_{cir}=2\pi&space;r)
- Total:
  ![Fórmula](https://latex.codecogs.com/svg.image?&space;P_{total}=P_{rec}+2P_{cir})
  
### - Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
```
def calcular_area_total(r, a, b):
    """
    Calcula el área total de la figura (cuerpo rectangular + 2 ruedas circulares)
    sin usar el módulo math.
    """
    pi = 3.1416
    area_rectangulo = a * b
    area_circulos = 2 * pi * r**2
    return area_rectangulo + area_circulos

def calcular_perimetro_total(r, a, b):
    """
    Calcula el perímetro total de la figura (contorno completo del cuerpo y círculos)
    sin usar el módulo math.
    """
    pi = 3.1416
    perimetro = 2 * a + b + 4 * pi * r
    return perimetro

# Entrada por teclado
r = float(input("Ingrese r (radio de los círculos): "))
a = float(input("Ingrese a (altura del rectágunlo): "))
b = float(input("Ingrese b (longitud del rectángulo): "))

# Cálculos
area = calcular_area_total(r, a, b)
perimetro = calcular_perimetro_total(r, a, b)

# Resultados
print(f"\nÁrea total: {area:.2f} unidades cuadradas")
print(f"Perímetro total: {perimetro:.2f} unidades")
```
### - Revise como utilizar el valor de pi usando import math y math.pi
```
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

```
## 3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
Tenemos tres tipos de aves:

- Gallinas, que pesan 6 kilos cada una.
- Gallos, que pesan 7 kilos cada uno.
- Pollitos, que pesan 1 kilo cada uno.

Para calcular el peso total de todas las aves juntas, multiplicamos la cantidad de cada tipo por su peso individual y sumamos los resultados:

Peso total = (N × 6) + (M × 7) + (K × 1)

Donde:
- N es el número de gallinas,
- M es el número de gallos,
- K es el número de pollitos.
```
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

```
## 4. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
Supongamos:

- C1 es el valor inicial del préstamo (capital).
- i es la tasa de interés mensual (en forma decimal: 10% = 0.10).
- n es el número de meses.
- C es el valor final del préstamo que se debe pagar después de aplicar el interés compuesto.

**Fórmula:**  
![Fórmula](https://latex.codecogs.com/svg.image?&space;C=C_{1}*(1+i){^n})

```
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

```
## 5. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

**Paso 1**

  Para que el código sea limpio y reutilizable, se crean funciones separadas para cada operación
- El promedio:
```
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)
```
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos):
```
def promedio_multiplicativo(numeros):
    producto = 1
    for num in numeros:
        producto *= num
    return producto ** (1 / len(numeros))
```
- La potencia del mayor número elevado al menor número:
```
def potencia_mayor_menor(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    return mayor ** menor
```
- La raíz cúbica del menor número:
```
def raiz_cubica_menor(numeros):
    menor = min(numeros)
    return math.copysign(abs(menor) ** (1 / 3), menor)
```
**Paso 2**

Usamos un bucle for para pedir al usuario 5 números reales y guardarlos en una lista numeros.
```
numeros = []
for i in range(5):
    num = float(input(f"Número {i + 1}: "))
    numeros.append(num)
```
**Paso 3**

Se llama a cada función con la lista de números y se imprimen los resultados con 4 decimales.

**Paso 4**

Para repetir el proceso, usamos un bucle while True y al final preguntamos:
```
repetir = input("¿Desea ingresar otros valores? (s/n): ")
if repetir != 's':
    break
```
**Código completo**
```
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
```
## 6. Consultar qué es y cómo funciona pip en python.
pip es el sistema de gestión de paquetes oficial de Python. Su función principal es instalar, actualizar y desinstalar paquetes (también llamados librerías o módulos) que se encuentran en el repositorio PyPI (Python Package Index).

Sirve para:

- Instalar librerías externas, como numpy, pandas, matplotlib, requests, etc.
- Ver qué paquetes tienes instalados.
- Actualizar versiones de paquetes.
- Eliminar paquetes que ya no necesitas.
- 
## 7. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

| Módulo             | Uso principal                                    | Comando de instalación       |
| ------------------ | ------------------------------------------------ | ---------------------------- |
| **numpy**          | Cálculos numéricos y álgebra lineal              | `pip install numpy`          |
| **pandas**         | Manipulación y análisis de datos                 | `pip install pandas`         |
| **matplotlib**     | Visualización y gráficos                         | `pip install matplotlib`     |
| **scikit-learn**   | Machine learning y modelos estadísticos          | `pip install scikit-learn`   |
| **requests**       | Peticiones HTTP sencillas                        | `pip install requests`       |
| **flask**          | Framework para desarrollo web ligero             | `pip install flask`          |
| **django**         | Framework web completo y robusto                 | `pip install django`         |
| **beautifulsoup4** | Análisis y extracción de datos HTML/XML          | `pip install beautifulsoup4` |
| **tensorflow**     | Machine learning y deep learning                 | `pip install tensorflow`     |
| **pytest**         | Testing y pruebas automáticas                    | `pip install pytest`         |
| **opencv-python**  | Procesamiento de imágenes y visión computacional | `pip install opencv-python`  |
| **sqlalchemy**     | ORM para bases de datos                          | `pip install sqlalchemy`     |
| **pygame**         | Desarrollo de videojuegos                        | `pip install pygame`         |
| **sympy**          | Matemáticas simbólicas                           | `pip install sympy`          |
| **jupyter**        | Notebooks interactivos para ciencia de datos     | `pip install jupyter`        |

Para instalarlo solo de debe escribir en la consola: 
```
pip install nombre_del_modulo
```
---
Y listo!! Eso sería todo del reto 5. Gracias por ver :)
