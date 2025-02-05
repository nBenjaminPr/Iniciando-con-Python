#Discretización de datos

#La discretización de datos es un proceso mediante el cual se convierten variables continuas en variables discretas o categóricas. La discretización de datos puede ser útil para crear nuevos atributos, como intervalos o columnas binarias, que se pueden utilizar para agrupar y visualizar los datos.

#Este método se utiliza para discretizar una variable continua en intervalos o categorías. Por defecto, esta función devuelve un objeto de la clase **pd.IntervalIndex,** que representa los intervalos resultantes. Sin embargo, también es posible devolver los valores personalizados en lugar de los intervalos utilizando el parámetro labels. Su sintaxis es la siguiente:

#<center><b>pd.cut(x, bins, labels, include_lowest, right)</b></center>

#- **x:** corresponde al conjunto de datos numéricos.
#- **bins:** es número de intervalos o la secuencia de los límites de los intervalos. También se pueden especificar etiquetas para los intervalos usando una lista de etiquetas.
#- **labels:** es una lista de etiquetas para los intervalos. Si se proporciona, debe tener la misma longitud que bins - 1.
#- **include_lowest:** es un valor booleano que indica si se debe incluir el límite inferior del primer intervalo.
#- **right:** Se utiliza para controlar si los intervalos son cerrados a la derecha o abiertos a la derecha. Cuando se establece en True (valor predeterminado), los intervalos son cerrados a la derecha, lo que significa que el valor límite derecho del intervalo está incluido en el intervalo

import pandas as pd

# Crear un DataFrame de ejemplo
df = pd.DataFrame({'Edad': [20, 25, 30, 35, 40, 45, 50, 55, 60]})

# Discretizar los datos en intervalos
intervalos = [0, 30, 40, 50, 100]  # Definir los intervalos deseados

# Etiquetas para las categorías
etiquetas = ['Joven', 'Adulto joven', 'Adulto', 'Adulto mayor']

# Discretizar y devolver valores en lugar de intervalos
df['GrupoEdad'] = pd.cut(df['Edad'], bins=intervalos, labels=etiquetas)

# Imprimir el DataFrame resultante
print (df)