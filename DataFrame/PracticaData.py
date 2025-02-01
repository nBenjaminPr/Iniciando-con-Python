import pandas as pd

df = pd.read_csv("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/CODE/Datos parte 2/resumen_resultados_astronautas.csv")


df = df.set_index('nombre') #El método **set_index()** nos permite establecer una columna existente como índice. Al hacerlo, la quita de las columnas del DataFrame.

df = df.reset_index('nombre') #El método **reset_index()** nos permite volver a establecer el índice del DataFrame

df.head() #df.head() = Por defecto se muestran los 5 primeros si quiero ver mas necesito (n=8)


print (df)