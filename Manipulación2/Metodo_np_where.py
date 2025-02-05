#Se utiliza para aplicar una condición a un iterable y devolver valores distintos según se cumpla la condición. Por ejemplo, podemos usar np.where() para marcar valores de un conjunto de datos que son iguales a un valor o están dentro de un conjunto de valores. Si se cumple la condición, np.where() devuelve un valor determinado, y si no se cumple, devuelve otro valor. Observa su uso:

import numpy as np
import pandas as pd

numeros = np.array([-1, 2, 3, -4, 5])
clasificacion = np.where(numeros >= 0, 'positivo', 'negativo')
print (clasificacion)

df = pd.DataFrame (
    {"Nombre": ['Juan', 'María', 'Pedro', 'Laura', 'Ana'],
    'Ingresos': [25000, 45000, 60000, 35000, 80000]}
)
# Definir umbral para clasificar ingresos
umbral = 50000
# Utilizar np.where() para clasificar los ingresos si mayor al umbral alto sino bajo
df['Clasificacion'] = np.where(df['Ingresos'] >= umbral, 'Alto', 'Bajo')

# Imprimir el DataFrame resultante
print (df)