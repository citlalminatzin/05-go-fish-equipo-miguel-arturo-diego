#!/usr/bin/env python

"""
Archivo principal de la práctica.

Este programa utiliza los módulos data.py y models.py para analizar
un dataset de peces. El objetivo es modelar el peso de los peces
a partir de su longitud y comparar distintos modelos.
"""

import numpy as np
import matplotlib.pyplot as plt

from data import read_data
from models import calc_error, modelo_geom, modelo_circ, pearson


def make_plot(l, w_real, w_geom, w_circ):
    """
    Genera una gráfica comparando:

    - Datos reales del dataset
    - Predicciones del modelo geométrico
    - Predicciones del modelo de circunferencia
    """

    idx = np.argsort(l)

    l_sorted = l[idx]
    w_geom_sorted = w_geom[idx]
    w_circ_sorted = w_circ[idx]

    plt.scatter(l, w_real, label="Datos reales")

    plt.plot(l_sorted, w_geom_sorted, label="Modelo geométrico")
    plt.plot(l_sorted, w_circ_sorted, label="Modelo circunferencia")

    plt.xlabel("Longitud del pez")
    plt.ylabel("Peso del pez")

    plt.title("Comparación de modelos de peso de peces")

    plt.legend()
    plt.show()


def plot_data(l, w):
    """Gráfica del ejercicio 1"""
    plt.scatter(l, w)

    plt.xlabel("Longitud del pez")
    plt.ylabel("Peso del pez")

    plt.title("Datos del campeonato de pesca")

    plt.show()


def plot_geom(l, w, w_geom):
    """Gráfica del ejercicio 2"""

    idx = np.argsort(l)

    l_sorted = l[idx]
    w_geom_sorted = w_geom[idx]

    plt.scatter(l, w, label="Datos reales")
    plt.plot(l_sorted, w_geom_sorted, label="Modelo geométrico")

    plt.xlabel("Longitud del pez")
    plt.ylabel("Peso del pez")

    plt.title("Ajuste del modelo W = K l³")

    plt.legend()
    plt.show()


def main():

    # =================================================
    # EJERCICIO 1
    # =================================================

    l, w = read_data("data/pescados.csv")

    print("Longitudes:", l)
    print("Pesos:", w)

    r = pearson(l, w)

    print("\nCoeficiente de Pearson:", r)

    # gráfica de datos
    plot_data(l, w)

    # =================================================
    # EJERCICIO 2
    # =================================================

    # estimación de K
    K = np.sum(w / (l**3)) / len(l)

    print("\nConstante K estimada:", K)

    w_geom = modelo_geom(l, K)

    print("\nPredicciones modelo geométrico:")
    print(w_geom)

    # gráfica modelo geométrico
    plot_geom(l, w, w_geom)

    # =================================================
    # EJERCICIO 3
    # =================================================

    circ = 0.4 * l

    w_circ = modelo_circ(l, circ, K)

    print("\nPredicciones modelo circunferencia:")
    print(w_circ)

    error_geom = calc_error(w_geom, w)
    error_circ = calc_error(w_circ, w)

    print("\nError modelo geométrico:", error_geom)
    print("Error modelo circunferencia:", error_circ)

    if error_geom < error_circ:
        print("\nEl modelo geométrico describe mejor los datos.")
    else:
        print("\nEl modelo basado en circunferencia describe mejor los datos.")

    # gráfica final comparando modelos
    make_plot(l, w, w_geom, w_circ)


if __name__ == "__main__":
    main()