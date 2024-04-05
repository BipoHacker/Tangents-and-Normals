import numpy as np
import matplotlib.pyplot as plt

def calcular_derivada(funcion_str, x_valor):
    # Calcular la derivada de la función en un punto específico usando diferencias finitas
    h = 1e-5
    derivada = (eval(funcion_str.replace('x', f'({x_valor} + {h})')) - eval(funcion_str.replace('x', f'({x_valor} - {h})'))) / (2 * h)
    return derivada

def graficar_funciones_tangentes_normales():
    funciones = []  # Lista para almacenar las funciones ingresadas por el usuario

    while True:
        # Solicitar una función al usuario
        funcion_str = input("Ingrese una función (use 'x' como variable) o 'n' para detenerse: ")

        if funcion_str.lower() == 'n':
            break  # Salir del bucle si el usuario ingresa 'n'
        
        funciones.append(funcion_str)

    # Solicitar el punto en el que se calcularán las tangentes y normales
    x_punto = float(input("Ingrese el valor de x en el que desea calcular las tangentes y normales: "))

    # Crear el gráfico con todas las funciones ingresadas
    for i, funcion_str in enumerate(funciones, start=1):
        # Cx**rear un rango de valores para x
        x = np.linspace(-10, 10, 1000)

        # Evaluar la función para cada valor de x
        y = eval(funcion_str)

        # Calcular la derivada en el punto dado
        derivada_en_punto = calcular_derivada(funcion_str, x_punto)

        # Calcular la ecuación de la tangente y la normal en el punto dado
        tangente = derivada_en_punto * (x - x_punto) + eval(funcion_str.replace('x', f'{x_punto}'))
        normal = (-1 / derivada_en_punto) * (x - x_punto) + eval(funcion_str.replace('x', f'{x_punto}'))

        # Mostrar la ecuación de la tangente y la normal
        print(f"\nPara la función {i}: {funcion_str}")
        print(f"Tangente en x = {x_punto}: y = {derivada_en_punto:.2f}(x - {x_punto}) + {eval(funcion_str.replace('x', f'{x_punto}')):.2f}")
        print(f"Normal en x = {x_punto}: y = {-1/derivada_en_punto:.2f}(x - {x_punto}) + {eval(funcion_str.replace('x', f'{x_punto}')):.2f}")

        # Graficar la función, la tangente y la normal
        plt.plot(x, y, label=f"Función {i}: {funcion_str}")
        plt.plot(x, tangente, label=f"Tangente {i}")
        plt.plot(x, normal, label=f"Normal {i}")

    plt.title("Gráfico de Funciones, Tangentes y Normales")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.scatter([x_punto], [eval(funcion_str.replace('x', f'{x_punto}'))], color='red', marker='o', label=f'Punto ({x_punto}, f({x_punto}))')
    plt.legend()
    plt.show()

# Llamar a la función principal
graficar_funciones_tangentes_normales()