#Considerando el archivo **calendar.csv**:


#- Verifica si existen duplicados luego de eliminar los nulos.
#- La columna price tiene caracteres como el signo "$",  además de puntos y comas, por lo que se lee como un string y no como un número. Límpiala para poder convertirla a tipo de dato float.

import pandas as pd

df = pd.read_csv("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/CODE/Manipu 1/calendar.csv")
#- elimina las filas que contengan nulos y reinicia el índice del DataFrame.
#Limpiamos eliminando los nulos y reseteamos el indice.
df_sin_nulos = df.dropna().reset_index(drop=True)


print (df_sin_nulos)