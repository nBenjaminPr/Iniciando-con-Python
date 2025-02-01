
#Desde una listas
import pandas as pd
import numpy as np

lista = [ [1, 'a', True], [2, 'b', False], [3, 'c', True] ]
columnas = ['columna_1', 'columna_2', 'columna_3']

df2 = pd.DataFrame(lista, columns=columnas)

print (df2)

#Desde un diccionario

datos = {'nombre': ['Juan', 'María', 'Pedro'], 'edad': [25, 30, 40], 'ciudad': ['Bogotá', 'Medellín', 'Cali']}

df3 = pd.DataFrame(datos)
print (df3)

#Desde una lista de diccionarios 

datos = [{'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}, {'nombre': 'María', 'edad': 30, 'ciudad': 'Medellín'}, {'nombre': 'Pedro', 'edad': 40, 'ciudad': 'Cali'}]

df4 = pd.DataFrame(datos)
print (df4)

#Desde un Nympu Array

arr = np.array([[1, 2], [3, 4]])
df5 = pd.DataFrame(arr, columns=['A', 'B'])
print (df5)