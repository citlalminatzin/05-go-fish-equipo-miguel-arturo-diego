#!/usr/bin/env python

"""
Archivo principal de la práctica.

Aquí se conectan los distintos módulos del proyecto:

- data.py      -> lee el dataset de peces
- models.py    -> contiene los modelos matemáticos y funciones de error

En este archivo se resuelven los tres ejercicios de la práctica:
1. Ajustar el modelo geométrico y calcular su error.
2. Ajustar el modelo basado en circunferencia y calcular su error.
3. Comparar ambos modelos y visualizar los resultados.
"""

import matplotlib.pyplot as plt
from data import read_data
from models import calc_error, modelo_geom, modelo_circ


def make_plot(l, w_real, w_geom, w_circ):
    """
    Genera una gráfica comparando:

    - Datos reales del dataset
    - Predicción del modelo geométrico
    - Predicción del modelo basado en circunferencia

    Parámetros
    ----------
    l : list[float]
        Longitudes de los peces.
    w_real : list[float]
        Pesos reales del dataset.
    w_geom : list[float]
        Pesos predichos por el modelo geométrico.
    w_circ : list[float]
        Pesos predichos por el modelo de circunferencia.
    """

    plt.scatter(l, w_real, label="Datos reales")

    plt.plot(l, w_geom, label="Modelo geométrico")
    plt.plot(l, w_circ, label="Modelo circunferencia")

    plt.xlabel("Longitud del pez")
    plt.ylabel("Peso del pez")

    plt.legend()
    plt.title("Comparación de modelos de peso de peces")

    plt.show()


def main():
    """
    Función principal del programa.

    Ejecuta los tres ejercicios de la práctica:
    - Leer los datos
    - Ajustar los modelos
    - Calcular errores
    - Comparar resultados
    - Graficar
    """

    # -------------------------------------------------
    # EJERCICIO 1
    # Leer los datos del archivo csv
    # -------------------------------------------------

    l, w = read_data("data/pescados.csv")

    print("Longitudes:", l)
    print("Pesos reales:", w)

    # -------------------------------------------------
    # EJERCICIO 2
    # Aplicar los modelos y obtener predicciones
    # -------------------------------------------------

    w_geom = modelo_geom(l)
    w_circ = modelo_circ(l)

    print("\nPredicciones modelo geométrico:")
    print(w_geom)

    print("\nPredicciones modelo circunferencia:")
    print(w_circ)

    # -------------------------------------------------
    # EJERCICIO 3
    # Calcular errores y comparar modelos
    # -------------------------------------------------

    error_geom = calc_error(w_geom, w)
    error_circ = calc_error(w_circ, w)

    print("\nError modelo geométrico:", error_geom)
    print("Error modelo circunferencia:", error_circ)

    if error_geom < error_circ:
        print("\nEl modelo geométrico ajusta mejor los datos.")
    else:
        print("\nEl modelo basado en circunferencia ajusta mejor los datos.")

    # -------------------------------------------------
    # Graficar resultados
    # -------------------------------------------------

    make_plot(l, w, w_geom, w_circ)


if __name__ == "__main__":
    #main()
    pass