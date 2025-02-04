#Los datos faltantes o NaN (Not a Number) son valores que faltan o no están disponibles en un DataFrame. **NaN** es un **valor de punto flotante** que puede ser representado por la clase float en Python, pero también se puede acceder a él a través del módulo NumPy como **np.nan**.

"""np.nan, type(np.nan)"""

#¿Por qué los valores NaN son de tipo float?  Esto se hace porque tiene implicaciones en cómo se manejan los datos faltantes en los cálculos. Por ejemplo, cuando se realiza una operación aritmética con NaN, el resultado siempre será NaN. Además, la comparación de valores NaN con cualquier otro valor, incluso con otro valor NaN, siempre devuelve False.

#Algunas de las formas comunes de manejar los datos faltantes son:

#- Obtener un DataFrame indicando True o False si cada celda tiene un valor NaN: **"isna()".**
#- Eliminar filas o columnas con datos faltantes: esto se hace mediante el método **".dropna()"** que elimina todas las filas o columnas que contienen al menos un valor NaN.
#- Reemplazar los valores faltantes con un valor específico: esto se puede hacer utilizando el método **".fillna()"** que reemplaza los valores NaN con un valor específico.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})

#Para obtener un DataFrame indicando True o False si cada celda tiene un valor NaN, se
df = df.isna()

#Le podemos agregar df = df.isna().sum() para obtener la cantidad de nulos

#Para eliminar las filas que contienen al menos un valor NaN df = f.dropna(axis = 0)

#Reemplaza los valores NaN por numeros con df = df.fillna(0)

#Tipos de datos df = df.dtypes

print (df)