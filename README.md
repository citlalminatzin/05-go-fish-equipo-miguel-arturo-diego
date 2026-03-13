
# Práctica 5: Modelos De Similitud Geométrica

## Introducción: 

## Integrantes

1. Domínguez León José Miguel
2. Góngora Ramírez Arturo 
3. Sánchez Ramírez Diego Alberto

## Uso e instalación

Para ejecutar este código correctamente, primero necesitas asegurarte de tener instaladas las librerías de Python: numpy, pandas, matplolib.

La práctica está estructurada en tres archivos distintos para mantener un orden, los cuales son:

- data.py: Se encarga exclusivamente de la lectura y el procesamiento inicial de tu dataset (por ejemplo, cargar la información del archivo CSV y convertirla en estructuras manejables).

- models.py: Aquí viven las definiciones de los modelos predictivos (el geométrico y el basado en circunferencia), así como las herramientas para calcular el error y el coeficiente de correlación.

- main.py: Aquí se definen las funciones para generar las gráficas (plots), se estructura la solución de los ejercicios paso a paso y se importan las herramientas necesarias de los otros dos archivos.

El órden de ejecución es: data, models, main.

## Ejercicio 1

Aunque este ejercicio no tiene una pregunta textual explícita, hacemos una cotejo del comportamiento de los datos con ayuda del coeficiente de Pearson:

La función main() utiliza la función pearson(l, w) para calcular el Coeficiente de Correlación de Pearson entre la longitud y el peso, y pearson(l, c) para la longitud y la circunferencia.

![Gráfica ejercicio 1, Datos del campeonato.](media/Datos_plot.png) 

Los resultados de estas correlaciones son valores positivos cercanos a 1, lo cual indica una correlación lineal directa. Lo cual se intuye con la disposición de los datos en la gráfica. Además esto justifica estadísticamente la idea del campeonato: es posible predecir el peso usando dimensiones fáciles de medir con una cinta métrica.

## Ejercicio 2

(Por favor modifica esta línea, tú puedes yo creo en ti) Puedes darle formato de **negritas**, *itálicas*, incluir texto matemático $x\approx 1, \epsilon > 0$, [enlaces](https://www.markdownguide.org/cheat-sheet/), `código`,

```python
# Esto es un ejemplo, lo puedes quitar
print("Código en bloque")
```

(Si no eliminas esta línea lloro) También puedes incluir citas

> Por favor elimina esta cita

(Si no eliminas esta línea lloro) Puedes incluir notas al pie [^1].

## Ejercicio 3

(Puedes modificar esta línea, su único propósito es existir para ser modificada, cada momento que existe en su forma original llora por no formar parte de la formación de jovenes matemáticas como tú) También se pueden incluir imágenes. Aunque a veces aunque se muestre localmente, no significa que se vaya a mostrar en GitHub. Por ejemplo, adjunto una imagen de una bella rosa:

![Texto alternativo, imagen de la cara de un Mr. Meeseks en fondo azul con la leyenda Existence is Pain por debajo](media/existence_is_pain.jpg)

### También puedes agregar tablas y eliminar este sub encabezado

| Elimíname | Elimíname a mí también |
| -------------- | --------------- |
| $1$ | $54$ |
| $2$ | $1000$ |

(Si no eliminas esta línea lloro) Y luego puedes comentar que con base en la tabla anterior, se ve una explosión en los valores a partir del tiempo $t=2$. 

## Conclusión

(Por favor modifica esta línea bro, es la última que tienes que modificar bro, por favor bro) Es buena práctica concluir tus prácticas. ¿Qué te llevas? ¿Sientes que fue relevante para ti? ¿Se te complicó algún aspecto? ¿Hubo algún resultado que contradijera tu intuición? 

---

[^1]: Sólo soy una nota al pie, elimíname bro, por favor bro.
