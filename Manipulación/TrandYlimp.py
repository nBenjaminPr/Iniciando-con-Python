#La eliminación de datos duplicados implica encontrar filas en una DataFrame que contengan exactamente los mismos valores en todas las columnas o en un subconjunto de columnas, y eliminar todas las filas duplicadas excepto una. Para hacer esto en Python, se puede utilizar la función **drop_duplicates()** de Pandas. Para mostrar su uso, consideremos el siguiente DataFrame

import pandas as pd

df = pd.DataFrame({
    'Nombre': ['Juan', 'Maria', 'Pedro', 'Juan', 'Maria'],
    'Edad': [25, 30, 35, 25, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Madrid', 'Barcelona']
})

#Eliminación de duplicados
df_sin_duplicados = df.drop_duplicates(subset=['Nombre', 'Ciudad'])

#Se utiliza para encontrar filas duplicadas
"""df= df[df.duplicated()]"""

df= df[df.duplicated(subset=["Nombre"])]

print (df)