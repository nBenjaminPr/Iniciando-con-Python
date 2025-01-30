#Los argumentos que se pasan a la función son los siguientes:

#- **nombre_astronautas.csv:** este es el nombre del archivo que se #desea cargar.

#- **delimiter:** este argumento indica que el delimitador utilizado #en el archivo es la coma (','). Es decir, cada valor en el archivo #está separado por comas.

#- **dtype:** este argumento indica que se desea cargar los datos como #cadenas de texto (strings).

#- **encoding:** este argumento indica que el archivo está codificado #en UTF-8. UTF-8 es un tipo de codificación de caracteres que permite #representar la mayoría de los caracteres utilizados en el mundo.

#Adiiconalmente, podemos utilizar alguns otros parámetros optativos #que nos serán útiles para la carga de archivos separados por coma, #como los **csv*:

#- **skiprows:** Con este parámetro puedes indicar el número de filas #que quieres saltar al leer el archivo. Esto es útil si el archivo #tiene filas de encabezado que no contienen datos, por ejemplo.

#- **usecols:** Este parámetro te permite seleccionar las columnas que #quieres leer del archivo. Puedes pasarle un número de columna #(empezando por cero) o una lista de números si necesitas leer varias #columnas.

"""
nombres = np.loadtxt("nombre_astronautas.csv", delimiter=',', dtype=str, encoding='utf-8')
"""

import numpy as np

alores = np.array([5,2,7,3,7,4,8,4,2,5,8,4,7,4,7,9,0,5,3,3])

print(np.mean(alores))#Calcula la media de los elementos del array.
print(np.median(alores))#Calcula la mediana de los elementos del array.
print(np.std(alores))#Calcula la desviación estándar de los elementos del array.
print(np.var(alores))#Calcula la varianza de los elementos del array.
print(np.percentile(alores,75))#Calcula el percentil 75 de los elementos del array.

