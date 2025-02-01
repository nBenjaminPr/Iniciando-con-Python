import pandas as pd

df = pd.read_csv("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/CODE/Datos parte 2/resumen_resultados_astronautas.csv")

df = df.set_index('nombre')

#Lo ordenamos por edad

df = df.sort_values(by='edad', ascending=True)

#Lo ordenamos por Ranking a los valores

df = df['edad'].rank(ascending=False)

print (df)

#Estadistica descriptica

# El método **describe** nos permite obtener varias medidas estadisticas en un solo paso. "" df.describe() ""