import pandas as pd

df = pd.read_csv("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/CODE/Datos parte 2/resumen_resultados_astronautas.csv")

#Podemos exportar fácilmente un DataFrame a un archivo csv (u otro formato, como #xls) mediante el método **to_csv**. Su uso es el siguiente:

df= df.set_index("nombre")

#df = df.loc["Alana Morillo":"Regina Cicerón", "edad":"altura"]

df.query("edad <= 21 or anos_experiencia == 0")

df.query.to_csv("nombre.csv", index = False, sep = ',', header = False, columns = ['edad','evaluacion_adaptativa'])

#los parámetros de este método son:

#  - **nombre.cvs:** corresponde al nombre del archivo que exportaremos (quedará #en la misma carpeta que nuestro archivo de Jupyter o Python.
# - **index:** agrega o no una columna adicional de índice. Por defecto es True, por lo que denbemos especificar si no la queremos.
#  - **sep:** corresponde al separador de datos. En nuestro caso, serán comas.
#  - **header:** similar a index, agrega o no la cabecera.
#  - **columns**: lista de columnas que queremos que se exporten (si no #precisamos, se exportarán todas). Podemos indicar las columnas utilizando sus #etiquetas (como en nuestro ejemplo) o utilizando posiciones. En tal caso #usamos columns=df.columns[[0, 2]]