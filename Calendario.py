#Considerando el archivo **calendar.csv**:


#- Verifica si existen duplicados luego de eliminar los nulos.


import pandas as pd

df = pd.read_csv("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/CODE/Manipu 1/calendar.csv")
#- elimina las filas que contengan nulos y reinicia el índice del DataFrame.
#Limpiamos eliminando los nulos y reseteamos el indice.
df_sin_nulos = df.dropna().reset_index(drop=True)


print (df_sin_nulos)