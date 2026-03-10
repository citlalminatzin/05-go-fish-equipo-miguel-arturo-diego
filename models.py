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



def pearson(x:list[float], y: list[float]):
    """Calcula el coeficiente de pearson"""
    ...

def calc_error(pred:list[float], truth: list[float]):
    """Calcula el error entre una predicción y la verdad del dataset"""

def main():
    ... # Puedes eliminar esta línea

if __name__ == "__main__":
    # Si necesitas hacer pruebas de tu función las puedes escribir acá
    main()

