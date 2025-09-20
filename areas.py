import math
from scipy.integrate import quad

def area_elipse(a, b):
    """Área de una elipse: π * a * b"""
    return math.pi * a * b

def area_polinomio(x):
    """Ejemplo: área bajo una curva polinómica"""
    # Calcula la integral definida de 0 a 1
    integral, _ = quad(x, 0, 1)
    return integral

def area_parabola(a, b):
    """Área de una parábola y = ax^2 + b desde x=0 hasta x=1"""
    integral, _ = quad(lambda x: a*x**2 + b, 0, 1)
    return integral

def main():
    print("Calculadora de áreas avanzadas")
    print("1. Elipse")
    print("2. Área bajo curva polinómica y = x^n")
    print("3. Área bajo parabola y = ax^2 + b")
    
    opcion = input("Elige la opción: ")

    if opcion == "1":
        a = float(input("Radio mayor a: "))
        b = float(input("Radio menor b: "))
        print("Área de la elipse:", area_elipse(a, b))
    
    elif opcion == "2":
        n = int(input("Introduce el exponente n: "))
        f = lambda x: x**n
        print("Área bajo y=x^{} de 0 a 1:".format(n), area_polinomio(f))
    
    elif opcion == "3":
        a = float(input("Coeficiente a: "))
        b = float(input("Coeficiente b: "))
        print("Área bajo la parábola de x=0 a x=1:", area_parabola(a, b))
    
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
