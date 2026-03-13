#!/usr/bin/env python
import numpy as np
import pandas as pd
def read_data(path="data/pescados.csv"):
    """
    Lee los datos de un archivo csv y los devuelve como arrays de numpy.
    y como un DataFrame de pandas.
    
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
    df : pandas.DataFrame
        Tabla con los datos.    
    """
    data = np.genfromtxt(path, delimiter=",", skip_header=1)

    l = data[:,0]
    w = data[:,1]
     # Crear DataFrame para visualizar como tabla
    df = pd.DataFrame({
        "Longitud": l,
        "Peso": w
    })


    return l, w, df

#Probabmos que se impriman los datos al ejecutar el script directamente
if __name__ == "__main__":
    l, w, df = read_data("data/pescados.csv")
    #print("Longitudes:", l)
    #print("Pesos:", w)
    print("\nTabla de datos:\n")
    print(df)
   
