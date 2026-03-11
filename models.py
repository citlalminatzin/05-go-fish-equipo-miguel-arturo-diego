#!/usr/bin/env python
"""
models.py

En este archivo se definen los modelos matemáticos y funciones auxiliares
que se usarán en la práctica para predecir el peso de los peces a partir
de sus dimensiones.
"""

import numpy as np


def modelo_geom(longitudes: list[float], K: float) -> list[float]:
    """
    Predice el peso de un pez usando el modelo de similitud geométrica.

    longitudes: lista con las longitudes de los peces
    K: constante del modelo

    Modelo:
        W = K * l^3
    """

    longitudes = np.array(longitudes)
    return K * longitudes**3


def modelo_circ(longitudes: list[float], circ: list[float], K: float) -> list[float]:
    """
    Predice el peso usando el modelo que incluye la circunferencia máxima.

    longitudes: longitudes de los peces
    circ: circunferencia máxima de cada pez
    K: constante del modelo

    Modelo aproximado:
        W = K * l * C^2
    """

    longitudes = np.array(longitudes)
    circ = np.array(circ)

    return K * longitudes * circ**2

def pearson(x: list[float], y: list[float]):
    """
    Calcula el coeficiente de correlación de Pearson entre dos variables.
    """

    x = np.array(x)
    y = np.array(y)

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    num = np.sum((x - x_mean) * (y - y_mean))
    den = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))

    return num / den

def calc_error(pred: list[float], truth: list[float]):
    """
    Calcula el error cuadrático medio entre las predicciones y los datos reales.
    """

    pred = np.array(pred)
    truth = np.array(truth)

    return np.mean((pred - truth)**2)

def main():
    """Pequeña prueba de las funciones"""

    l = [30, 35, 40]
    w_real = [1.0, 1.3, 1.9]

    K = 0.00002

    w_pred = modelo_geom(l, K)

    print("Predicción:", w_pred)
    print("Error:", calc_error(w_pred, w_real))



if __name__ == "__main__":
    # Si necesitas hacer pruebas de tu función las puedes escribir acá
    main()

