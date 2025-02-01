import pandas as pd

df = pd.read_csv("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/CODE/Datos parte 2/resumen_resultados_astronautas.csv")

#Podemos seleccionar datos poniendo condiciones, que podemos combinar utilizando los operadores booleanos & (and) y | (or). Notemos que las condiciones deben ponerse entre paréntesis, cuando haya más de una.
"""df = df[(df['edad'] >= 30) & (df['anos_experiencia'] >=5)]"""

#El método llamado **query()** nos permite realizar una indexación booleana más sencilla:

df = df.query("edad <= 21 or anos_experiencia == 0")


print (df)