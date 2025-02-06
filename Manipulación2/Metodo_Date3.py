import pandas as pd
import numpy as np

# Crear un DataFrame de ejemplo
df = pd.DataFrame({'fecha': ['2022-05-02', '2022-05-03', '2022-06-04']})

# Convertir a formato de fecha y hora de Pandas
df['fecha'] = pd.to_datetime(df['fecha'])

df_mayo = df[(df['fecha'] >= '2022-05-01') & (df['fecha'] <= '2022-05-31')]

# Verificar el resultado
print (df_mayo)

#Si tenemos una columna con edades, la podemos separar en categorías como "menores de 18 años", "de 18 a 30 años", "de 31 a 50 años", etc. El método "cut" toma como entrada la columna que deseamos discretizar y los límites de los intervalos que queremos definir

# fijamos la semilla aleatoria de numpy.
np.random.seed(0)

# generamos datos aleatorios.
edades_random = np.random.randint(1, 100, 20)

# creamos un dataframe con los datos aleatorios.
df2 = pd.DataFrame({'edad': edades_random})

intervalos = [0, 18, 30, 50, 100]
etiquetas = ["menores de 18", "de 18 a 30", "de 31 a 50", "mayores de 50"]


df2['edad_categoria']=pd.cut(x = df2['edad'], bins = intervalos, labels = etiquetas)

print (df2)
