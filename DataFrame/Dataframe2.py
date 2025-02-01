import pandas as pd
import numpy as np

#Podemos combinar dos DataFrames en un proceso similar a la operación JOIN, de tablas en SQL.

#Con Python, utilizamos **pd.concat()**, que recibe una lista con DataFrames que deben tener las mismas columnas.

df1 = pd.DataFrame({"mes": "enero", "ventas":np.random.randint(1,100, 2)})

print (df1)

df2 = pd.DataFrame({"mes": "febrero", "ventas":np.random.randint(1,100, 2)})
print (df2)

df3 = pd.DataFrame({"mes": "marzo", "ventas":np.random.randint(1,100, 2)})
print (df3)

df4 = pd.concat([df1,df2,df3])
print (df4)

#Podemos observar que los indices quedaron duplicados y desordenados, por lo que para evitar confusiones se recomienda reiniciar el indice de las filas luego de hacer Uniones de este estilo.

df4 = df4.reset_index(drop=True) #¿Qué ocurre si no ponemos "drop=True" (que es el valor por defecto)?
print (df4)

df5 = pd.DataFrame({"mes": "abril", "ventas": np.random.randint(1,100, 1)})
print (df5)

#Para simplificar, utilizamos el parametro **ignore_index** del método **concat** al realizar la union de DataFrames. De esta manera, el indice se reiniciará automáticamente.

df6 = pd.concat([df4, df5], ignore_index = True)
print (df6)
