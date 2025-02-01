import pandas as pd

df = pd.read_csv("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/CODE/Datos parte 2/resumen_resultados_astronautas.csv")

#Index por Etiqueta con .loc

"""df = df.loc[["Alana Morillo", "Fátima Tafalla", "Sofía Puig"], ["edad", "peso", "altura"]] """

#Podemos utilizar también rangos de etiqueta.
df = df.loc["Alana Morillo":"Regina Cicerón", "edad":"altura"]

print (df)