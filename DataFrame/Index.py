import pandas as pd

df = pd.read_csv("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/CODE/Datos parte 2/resumen_resultados_astronautas.csv")

#El primero (2) son las filas y el segundo (1) la columnas
#df = df.iloc[2,1] 

df = df.set_index('nombre')
#Muestra la cantidad de filas y la cantidad de columnas de cada fila o registro
""" df = df.iloc [[0,1,2,3,4,5,6], [0,1,2,3]] """

#Lo utilizamos para marcar un rango 0:5 y 0:4
""" df = df.iloc[0:5 , 0:4] """ 

