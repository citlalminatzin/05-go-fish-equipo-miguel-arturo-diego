#!/usr/bin/env python
import numpy as np
def read_data(path="data/pescados.csv"):
    """
    Lee los datos de un archivo csv y los devuelve como arrays de numpy.
    
    Parámetro
    ----------
    path : str
        Ruta al archivo csv.

    Regresa
    -------
    l : numpy.array
        Longitudes de los pescados.
    w : numpy.array
        Pesos de los pescados.
    c : numpy.array (opcional)
        Circunferencias máximas si la tabla las contiene.
    """
    data = np.genfromtxt(path, delimiter=",", skip_header=1)

    l = data[:,0]
    w = data[:,1]

    return l, w

#Probabmos que se impriman los datos al ejecutar el script directamente
if __name__ == "__main__":
    l, w = read_data("data/pescados.csv")
    print("Longitudes:", l)
    print("Pesos:", w)
    

